#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  delay(500);
  Serial.println("BOOT_OK fw=0.1.0 chip=ESP32");
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd == "PING") {
      Serial.println("PONG");
    } else if (cmd.length() > 0) {
      Serial.println("ERR unknown_command");
    }
  }
}