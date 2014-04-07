// This is a demo of the RBBB running as webserver with the Ether Card
// 2010-05-28 <jc@wippler.nl> http://opensource.org/licenses/mit-license.php
 
#include <EtherCard.h>
 
// ethernet interface mac address, must be unique on the LAN
static byte mymac[] = { 0x74,0x69,0x69,0x2D,0x30,0x30 };
static byte myip[] = { 10,26,26,26 };
static byte gwip[] = { 10,26,26,1 };
static byte dnsip[] = { 10,1,15,56 };

byte Ethernet::buffer[500];  
BufferFiller bfill;

#define STATIC 0
 
void setup () {
  Serial.begin(57600);
  Serial.println("\n[backSoon]");
  pinMode(2,INPUT);
  
  if (ether.begin(sizeof Ethernet::buffer, mymac) == 0) 
    Serial.println( "Failed to access Ethernet controller");
#if STATIC
  ether.staticSetup(myip, gwip);
#else
  if (!ether.dhcpSetup())
    Serial.println("DHCP failed");
#endif

  ether.printIp("IP:  ", ether.myip);
  ether.printIp("GW:  ", ether.gwip);  
  ether.printIp("DNS: ", ether.dnsip); 
  ether.printIp("MAC: ", ether.mymac);
  ether.printIp("Mask:", ether.netmask);
  ether.printIp("Bdcs:", ether.broadcastip);
  ether.printIp("DHCP:", ether.dhcpip);
}

void(* resetFunc )(void)=0;
 
static word homePage() {
  long t = millis() / 1000;
  word h = t / 3600;
  byte m = (t / 60) % 60;
  byte s = t % 60;
  int d = analogRead(2);
  int temp = analogRead(3);
  bfill = ether.tcpOffset();
  bfill.emit_p(PSTR(
    "HTTP/1.0 200 OK\r\n"
    "Content-Type: text/html\r\n"
    "Pragma: no-cache\r\n"
    "\r\n"

    "<meta http-equiv='refresh' content='1'/>"
    "<title>RBBB server</title>"
    "<h1>$D$D:$D$D:$D$D\n</h1>"
    "<h2>Pot Value:$D\n</h2>"
    "<h2>Temperature:$D\n</h2>"),
      h/10, h%10, m/10, m%10, s/10, s%10, d, temp);
  if (m>1) //software reset every minute.
    resetFunc();
  return bfill.position();
}
 
void loop () {
  word len = ether.packetReceive();
  word pos = ether.packetLoop(len);
 
  if (pos)  // check if valid tcp data is received
    ether.httpServerReply(homePage()); // send web page data
}