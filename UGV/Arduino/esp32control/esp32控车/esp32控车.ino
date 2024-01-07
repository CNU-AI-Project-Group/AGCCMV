#include <WiFi.h>
#include <WiFiClient.h>
#include <WebServer.h>
#include <ESPmDNS.h>

const char* ssid = "Xiaomi_Polaris";
const char* password = "705537915";

WebServer server(80);

// const int led = 13;
int motor1Pin1 = 2; // 右前进
int motor1Pin2 = 14; // 右后退
int motor1Pin3 = 15; // 左前进 
int motor1Pin4 = 13; // 左后退 //zy
int motorA = 0  ;  //左使能
int motorB = 16 ; //右使能
float pwm = 0.45 ;

void handles() {
  server.send(200, "text/plain", "stop!");
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, HIGH); 
  digitalWrite(motor1Pin3, HIGH);
  digitalWrite(motor1Pin4, HIGH); 
  delay(200);
}

void handlef() {
  server.send(200, "text/plain", "forward!");
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH); 
  digitalWrite(motor1Pin3, LOW);
  digitalWrite(motor1Pin4, HIGH); 
  ledcWrite(0, 65535*pwm); 
  delay(100);
}

void handleb() {
  server.send(200, "text/plain", "back!");
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW); 
  digitalWrite(motor1Pin3, HIGH);
  digitalWrite(motor1Pin4, LOW); 
  ledcWrite(0, 65535*pwm); 
  delay(100);
}

void handlez() {
  server.send(200, "text/plain", "left!");
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, HIGH); 
  digitalWrite(motor1Pin3, LOW);
  digitalWrite(motor1Pin4, HIGH); 
  ledcWrite(0, 65535*pwm); 
  delay(100);
}

void handley() {
  server.send(200, "text/plain", "right!");
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH); 
  digitalWrite(motor1Pin3, HIGH);
  digitalWrite(motor1Pin4, HIGH); 
  ledcWrite(0, 65535*pwm); 
  delay(100);
}



void handleRoot() {
  // digitalWrite(led, 1);
  server.send(200, "text/plain", "hello from esp32!");
  // digitalWrite(led, 0);
}

void handleNotFound() {
  // digitalWrite(led, 1);
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i = 0; i < server.args(); i++) {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
  // digitalWrite(led, 0);
}

void setup(void) {
  // 电机引脚  
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT); 
  pinMode(motor1Pin3, OUTPUT);
  pinMode(motor1Pin4, OUTPUT);
  pinMode(motorA, OUTPUT);
  pinMode(motorB, OUTPUT);
  //pwm
  ledcSetup(0, 500, 16);
  ledcAttachPin(motorA, 0);
  ledcAttachPin(motorB, 0);

  // pinMode(led, OUTPUT);
  // digitalWrite(led, 0);
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  if (MDNS.begin("esp32")) {
    Serial.println("MDNS responder started");
  }

  server.on("/", handleRoot);

  server.on("/inline", []() {
    server.send(200, "text/plain", "this works as well");
  });

  server.onNotFound(handleNotFound);
  server.on("/s",handles);
  server.on("/f",handlef);
  server.on("/b",handleb);
  server.on("/z",handlez);
  server.on("/y",handley);
  
  server.begin();
  Serial.println("HTTP server started");
}

void loop(void) {
  server.handleClient();
  delay(2);//allow the cpu to switch to other tasks
}
