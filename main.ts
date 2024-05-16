input.onButtonPressed(Button.A, function () {
    password_enter = "" + password_enter + "."
    serial.writeString(password_enter)
    serial.writeLine("")
    I2C_LCD1602.ShowString(password_enter, 0, 1)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    for (let index = 0; index < 1; index++) {
        I2C_LCD1602.clear()
    }
    I2C_LCD1602.ShowString("close the door", 0, 0)
    pins.servoWritePin(AnalogPin.P8, 0)
    basic.pause(1000)
    password_enter = ""
    for (let index = 0; index < 1; index++) {
        I2C_LCD1602.clear()
    }
    I2C_LCD1602.ShowString("Enter password", 0, 0)
    strip.clear()
    strip.clear()
})
function WINDOW () {
    A = pins.digitalReadPin(DigitalPin.P9)
    if (A >= 300) {
        pins.servoWritePin(AnalogPin.P9, 0)
    } else {
        pins.servoWritePin(AnalogPin.P9, 180)
    }
}
input.onButtonPressed(Button.AB, function () {
    I2C_LCD1602.clear()
    if (password_enter == password) {
        basic.showIcon(IconNames.Heart)
        I2C_LCD1602.ShowString("successful", 0, 0)
        I2C_LCD1602.ShowString("open the door", 0, 1)
        pins.servoWritePin(AnalogPin.P8, 180)
        strip.showColor(neopixel.colors(NeoPixelColors.Purple))
        strip.show()
    } else {
        I2C_LCD1602.ShowString("enter again", 0, 0)
        I2C_LCD1602.ShowString("error", 0, 1)
        password_enter = ""
        basic.pause(100)
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowString("enter password", 0, 0)
    }
})
input.onButtonPressed(Button.B, function () {
    password_enter = "" + password_enter + "-"
    serial.writeString(password_enter)
    serial.writeLine("")
    I2C_LCD1602.ShowString(password_enter, 0, 1)
})
function LED () {
    if (pins.digitalReadPin(DigitalPin.P15) == 1) {
        pins.digitalWritePin(DigitalPin.P16, 1)
    } else {
        pins.digitalWritePin(DigitalPin.P16, 0)
    }
}
function TEMP () {
    TEMP1 = input.temperature()
    serial.writeValue("temperature(C)", dht11_dht22.readData(dataType.temperature))
    serial.writeValue("humidity(%RH)", dht11_dht22.readData(dataType.humidity))
}
function Automode () {
    TEMP()
    WINDOW()
    LED()
}
let TEMP1 = 0
let A = 0
let strip: neopixel.Strip = null
let password_enter = ""
let password = ""
serial.redirectToUSB()
basic.showIcon(IconNames.Square)
pins.servoWritePin(AnalogPin.P9, 100)
music.play(music.stringPlayable("B A G A B B B - ", 120), music.PlaybackMode.UntilDone)
I2C_LCD1602.LcdInit(39)
I2C_LCD1602.clear()
basic.pause(100)
I2C_LCD1602.ShowString("Enter password", 0, 0)
pins.digitalWritePin(DigitalPin.P16, 0)
password = "..--"
password_enter = ""
strip = neopixel.create(DigitalPin.P14, 4, NeoPixelMode.RGB)
strip.clear()
strip.show()
basic.forever(function () {
    Automode()
})
