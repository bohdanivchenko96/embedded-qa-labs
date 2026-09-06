embedded-qa-labs

Hands-on labs for hardware test automation with pytest — built while switching from web/mobile QA into Embedded / HIL QA.

Each lab is a small, self-contained exercise: a concept to learn, a board to touch (or a virtual port to fake one), and a pytest suite that proves the concept works — not just a script that prints output, but an automated pass/fail check.

Hardware used
Component	Role
ESP32 DevKit V1	Main test target — custom UART command-protocol firmware
STM32 "Blue Pill" (STM32F103C8T6)	Secondary test target — flashed via SWD
ST-Link V2 (mini)	SWD programmer/debugger for the Blue Pill
CP2102 USB-UART adapter	External UART bridge
OLED SSD1306 (I2C, 128x64)	I2C peripheral under test
Breadboard + jumper wires	Shared bus — everything sits on one breadboard

Environment
Windows 11 + WSL2 (Ubuntu 24.04); boards are passed through to Linux with usbipd-win
Firmware: PlatformIO, Arduino framework
Tests: Python 3, pytest, pyserial

Prepare env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt