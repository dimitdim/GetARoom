#include <EtherCard.h>
static byte mymac[] = { 0x74,0x69,0x69,0x2D,0x24,0x24 };
static byte myip[] = { 10,25,9,90  };
static byte gwip[] = { 10,25,9,1 };
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

long time;
int light;
int temp;
int sound;
int door;
long last;

void(* resetFunc )(void)=0;

static word homePage() {
  bfill = ether.tcpOffset();
  bfill.emit_p(PSTR(
    "HTTP/1.0 200 OK\r\n"
    "Content-Type: text/html\r\n"
    "Pragma: no-cache\r\n"
    "\r\n"
    "<html><head><title>GetARoom</title></head><body>"
    "<p>{'uptime':$L,'brightness':$D,'temperature':$D,'volume':$D,'door':$D,'last':$L}</p>"
    "</body></html>"),
      time, light, temp, sound, door, last);
  return bfill.position();
}

void loop () {
  time = millis();
  light = 1023-analogRead(2);
  temp = analogRead(3);
  sound= analogRead(4);
  door = analogRead(5);
  if (door>550)
    last = millis();
  
  if ((millis()%1000)>499)
    digitalWrite(9, HIGH);
  else
    digitalWrite(9, LOW);
  
  if (ether.packetLoop(ether.packetReceive()))
    ether.httpServerReply(homePage());
  /**if (millis()>3600000)
    resetFunc();**/
}
