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

int ref = 5000;

long t;
long d;
int h;
int m;
int s;

long llight;
int light;
long ltemp;
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
    "<p><h1>Uptime: $L:$D$D:$D$D:$D$D\n</h1></p>"
    "<p><h3>Brightness: $D\n</h3></p>"
    "<p><h3>Temperature: $D\n</h3></p>"
    "<p><h3>Volume: $D\n</h3></p>"
    "<p><h3>Door: $D\n</h3></p>"
    "<p><h3>Last: $L\n</h3></p>"
    "</body></html>"),
      d, h/10, h%10, m/10, m%10, s/10, s%10, light, temp, sound, door, last);

  return bfill.position();
}

void loop () {
  t = millis() / 1000;
  d = t / 86400;
  h = (t / 3600) % 24;
  m = (t / 60) % 60;
  s = t % 60;
  
  llight = ((1023-analogRead(2))*100)/1023;
  light=llight;
  ltemp = (analogRead(3)*ref)/10230;
  temp=ltemp;
  sound= analogRead(4);
  door = analogRead(5);
  if (door>100)
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
