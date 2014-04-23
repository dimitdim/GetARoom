#include <EtherCard.h>
static byte mymac[] = { 0x74,0x69,0x69,0x2D,0x33,0x35 };
static byte myip[] = { 10,27,65,99  };
static byte gwip[] = { 10,27,65,1 };
static byte dnsip[] = { 10,1,15,56 };
static byte mask[] = { 255,255,255,0 };

byte Ethernet::buffer[500];
BufferFiller bfill;

void setup () {
  Serial.begin(57600);
  Serial.println("GetARoom");
  
  if (ether.begin(sizeof Ethernet::buffer, mymac) == 0)
    Serial.println( "Failed to access Ethernet controller");
  ether.staticSetup(myip, gwip, dnsip, mask);
  
  ether.printIp("IP:   ", ether.myip);
  ether.printIp("GW:   ", ether.gwip);
  ether.printIp("DNS:  ", ether.dnsip);
  ether.printIp("MAC:  ", ether.mymac);
  ether.printIp("Mask: ", ether.netmask);
  ether.printIp("Bdcs: ", ether.broadcastip);
  ether.printIp("DHCP: ", ether.dhcpip);
  
  pinMode(9, OUTPUT);
}

void(* resetFunc )(void)=0;

static word homePage() {
  long t = millis() / 1000;
  word h = t / 3600;
  byte m = (t / 60) % 60;
  byte s = t % 60;
  
  long ldata = (1023-analogRead(2));
  ldata = ldata*100;
  ldata = ldata/1023;
  int data = ldata;
  /**int data =100*analogRead(2)/1023;**/
  long ref=5000;
  long ltemp = analogRead(3)*ref;
  ltemp = ltemp/10230;
  int temp = ltemp;
  int sound= analogRead(4);
  
  bfill = ether.tcpOffset();
  bfill.emit_p(PSTR(
    "HTTP/1.0 200 OK\r\n"
    "Content-Type: text/html\r\n"
    "Pragma: no-cache\r\n"
    "\r\n"
    "<html><head><title>GetARoom</title></head><body>"
    "<p><h1>Uptime: $D$D:$D$D:$D$D\n</h1></p>"
    "<p><h3>Brightness: $D\n</h3></p>"
    "<p><h3>Temperature: $D\n</h3></p>"
    "<p><h3>Volume: $D\n</h3></p>"
    "</body></html>"),
      h/10, h%10, m/10, m%10, s/10, s%10, data, temp, sound);

  return bfill.position();
}

void loop () {
  if (ether.packetLoop(ether.packetReceive()))
    ether.httpServerReply(homePage());
  if ((millis()%1000)>499)
    digitalWrite(9, HIGH);
  else
    digitalWrite(9, LOW);
/**  if (millis()>3600000)
    resetFunc(); **/
}
