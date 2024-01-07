// #include <ESP8266WiFi.h>
#include <ESP8266WiFi.h>
#include <ESPAsyncTCP.h>




#include <ESPAsyncWebServer.h>

// WiFi网络参数
const char* ssid = "Xiaomi_430F_ROS";
const char* password = "12345678";


// const char* ssid = "your_SSID_here";
// const char* password = "your_PASSWORD_here";

AsyncWebServer server(80);

void setup() {
  Serial.begin(115200);
  delay(100);

  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  server.on("/data", HTTP_POST, [](AsyncWebServerRequest *request){
    if(request->hasParam("data", true)){
      String data = request->getParam("data", true)->value();
      Serial.print("Received data: ");
      Serial.println(data);
      request->send(200, "text/plain", "Data received");
    } else {
      request->send(400, "text/plain", "Missing data parameter");
    }
  });

  server.begin();
}

void loop() {

}



// WiFiServer server(80);

// void setup() {
//   Serial.begin(115200);
//   delay(10);

//   // 连接WiFi网络
//   Serial.println();
//   Serial.println();
//   Serial.print("Connecting to ");
//   Serial.println(ssid);

//   WiFi.begin(ssid, password);

//   while (WiFi.status() != WL_CONNECTED) {
//     delay(500);
//     Serial.print(".");
//   }

//   Serial.println("");
//   Serial.println("WiFi connected");

//   // 开启服务器
//   server.begin();
//   Serial.println("Server started");
// }

// void loop() {
//   // 等待客户端连接
//   WiFiClient client = server.available();
//   if (!client) {
//     return;
//   }

//   // 等待客户端发送数据
//   while(!client.available()){
//     delay(1);
//   }

//   // 读取客户端发送的数据
//   String request = client.readStringUntil('\r');
//   Serial.println(request);

//   // 判断客户端发送的数据并做出相应操作
//   while(request !="q"){
//     client.println("recived");
//     String request = client.readStringUntil('\r');
//     if (request.indexOf("forward") != -1) {
//     // 小车前进
//     Serial.println("Car forward");
//   } else if (request.indexOf("backward") != -1) {
//     // 小车后退
//     Serial.println("Car backward");
//   } else if (request.indexOf("left") != -1) {
//     // 小车向左转
//     Serial.println("Car left");
//   } else if (request.indexOf("right") != -1) {
//     // 小车向右转
//     Serial.println("Car right");
//   } else {
//     // 未知操作
//     Serial.println("Unknown command");
//   }
//   }
//   client.stop();
  
// }
