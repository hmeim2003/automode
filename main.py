def on_button_pressed_a():
    global password_enter
    password_enter = "" + password_enter + "."
    serial.write_string(password_enter)
    serial.write_line("")
    I2C_LCD1602.show_string(password_enter, 0, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_pressed():
    global password_enter
    for index in range(1):
        I2C_LCD1602.clear()
    I2C_LCD1602.show_string("close the door", 0, 0)
    pins.servo_write_pin(AnalogPin.P8, 0)
    basic.pause(1000)
    password_enter = ""
    for index2 in range(1):
        I2C_LCD1602.clear()
    I2C_LCD1602.show_string("Enter password", 0, 0)
    strip.clear()
    strip.clear()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def WINDOW():
    global A
    A = pins.digital_read_pin(DigitalPin.P9)
    if A >= 300:
        pins.servo_write_pin(AnalogPin.P9, 0)
    else:
        pins.servo_write_pin(AnalogPin.P9, 180)

def on_button_pressed_ab():
    global password_enter
    I2C_LCD1602.clear()
    if password_enter == password:
        basic.show_icon(IconNames.HEART)
        I2C_LCD1602.show_string("successful", 0, 0)
        I2C_LCD1602.show_string("open the door", 0, 1)
        pins.servo_write_pin(AnalogPin.P8, 180)
        strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
        strip.show()
    else:
        I2C_LCD1602.show_string("enter again", 0, 0)
        I2C_LCD1602.show_string("error", 0, 1)
        password_enter = ""
        basic.pause(100)
        I2C_LCD1602.clear()
        I2C_LCD1602.show_string("enter password", 0, 0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global password_enter
    password_enter = "" + password_enter + "-"
    serial.write_string(password_enter)
    serial.write_line("")
    I2C_LCD1602.show_string(password_enter, 0, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def LED():
    if pins.digital_read_pin(DigitalPin.P15) == 1:
        pins.digital_write_pin(DigitalPin.P16, 1)
    else:
        pins.digital_write_pin(DigitalPin.P16, 0)
def TEMP():
    global TEMP1
    TEMP1 = input.temperature()
    serial.write_value("temperature(C)",
        dht11_dht22.read_data(dataType.TEMPERATURE))
    serial.write_value("humidity(%RH)", dht11_dht22.read_data(dataType.HUMIDITY))
def Automode():
    TEMP()
    WINDOW()
    LED()
TEMP1 = 0
A = 0
strip: neopixel.Strip = None
password_enter = ""
password = ""
serial.redirect_to_usb()
basic.show_icon(IconNames.SQUARE)
pins.servo_write_pin(AnalogPin.P9, 100)
music.play(music.string_playable("B A G A B B B - ", 120),
    music.PlaybackMode.UNTIL_DONE)
I2C_LCD1602.lcd_init(39)
I2C_LCD1602.clear()
basic.pause(100)
I2C_LCD1602.show_string("Enter password", 0, 0)
pins.digital_write_pin(DigitalPin.P16, 0)
password = "..--"
password_enter = ""
strip = neopixel.create(DigitalPin.P14, 4, NeoPixelMode.RGB)
strip.clear()
strip.show()

def on_forever():
    Automode()
basic.forever(on_forever)
