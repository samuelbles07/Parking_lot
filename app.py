# import others
import datetime
import time

# import module
from peripherals import Peripherals
from db import Database

# import component library
import RPi.GPIO as GPIO

BUTTONA = 17
BUTTONB = 18

LED_GREEN = 22
LED_RED = 23

BUZZER = 27

class App():
    def __init__(self):
        self.peripheral = Peripherals()
        self.db = Database()
        #TODO: GUI

        # Setup IO
        GPIO.setmode(GPIO.BCM)

        # Setup output IO
        GPIO.setup(LED_GREEN, GPIO.OUT)
        GPIO.setup(LED_RED, GPIO.OUT)

        # Setup PWM
        GPIO.setup(BUZZER, GPIO.OUT)
        self.pwm = GPIO.PWM(BUZZER, 100)    # Created a PWM object

        # Setup Input IO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BUTTONA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(BUTTONB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # Just initialize variable
        self.in_home = True
        self.data_valid = False
        self.order_number = ""
        self.barcode = ""
        self.enter_time = ""
        self.exit_time = ""
        self.parking_time = 0
        self.total_payment = 0

    def do_buzzer(self, fading, times):
        print("buzz")
        if fading:
            self.pwm.start(0)                    # Started PWM at 0% duty cycle
            for i in range(times):
                for x in range(100):    # This Loop will run 100 times
                    self.pwm.ChangeDutyCycle(x) # Change duty cycle
                    time.sleep(0.01)         # Delay of 10mS

            self.pwm.stop()

        else:
            self.pwm.start(0)
            for i in range(times):
                self.pwm.ChangeDutyCycle(100)
                time.sleep(0.7)
                self.pwm.ChangeDutyCycle(0)
                time.sleep(0.7)
            self.pwm.stop()

        print("done")

    def scanner_callback(self, data):
        self.in_home = False
        print("Scanned barcode: %s" % str(data))
        resp = self.db.select_enter(data)
        if resp != "":
            self.order_number = resp[0]
            self.barcode = resp[1]
            self.enter_time = resp[2]

            resp = self.db.select_exit(self.order_number)
            if resp != "":
                #TODO : go to validation page, display variables, POP UP "data tidak sesuai"
                print("Invalid, vehicle already exit!")
                self.do_buzzer(False, 3)
                GPIO.output(LED_RED, GPIO.HIGH)

            else:
                GPIO.output(LED_GREEN, GPIO.HIGH)
                print("Okay valid, now waiting for payment")
                #Date stuff
                dt = datetime.datetime.now()
                self.exit_time = dt.strftime("%Y-%m-%d %H:%M:%S")
                
                # Getting time differences
                t_exit = datetime.datetime.strptime(self.exit_time, "%Y-%m-%d %H:%M:%S")
                t_enter = datetime.datetime.strptime(str(self.enter_time), "%Y-%m-%d %H:%M:%S")
                tdelta = t_exit - t_enter

                self.parking_time = (tdelta.seconds//60) % 60 # Rounding the value to minute
                self.total_payment = 3000 * (int(self.parking_time / 60) + 1) # per hour 3k rupiah then times how many hour

                self.data_valid = True

                print("Parking time: %s" % self.parking_time)
                print("Total Payment: %s" % self.total_payment)
                print("Exit Time: %s" % self.exit_time)
                # TODO: Display variables to GUI, change to validation page

                self.do_buzzer(False, 2)


        else:
            #TODO : go to validation page, display variables, POP UP "data tidak sesuai"
            print("Not valid, barcode never registered!")
            self.do_buzzer(False, 3)
            GPIO.output(LED_RED, GPIO.HIGH)

    def do_payment(self):
        if self.data_valid is True:
            self.db.insert_exit([self.order_number, self.enter_time, self.parking_time, self.total_payment])

            # TODO: send open gate to PLC
            print("Payment done! Opening Gate")
            #TODO: POP up selamat jalan

            time.sleep(5) # NOTE: Simulate vehicle already out of gate

            # TODO: send open close to PLC

            GPIO.output(LED_GREEN, GPIO.LOW)

        # If data not valid, trigger by button to go back home
        else:
            # NOTE: Exit from validation page. Do pop up or something
            print("Exit from validation page")
            GPIO.output(LED_RED, GPIO.LOW)
            time.sleep(1.5) # To avoid button bounce
        
        # Reset all variables
        self.in_home = True
        self.data_valid = False
        self.order_number = ""
        self.barcode = ""
        self.enter_time = ""
        self.exit_time = ""
        self.parking_time = 0
        self.total_payment = 0
        self.peripheral.start_scanner(self.scanner_callback)

        #TODO: go back to home page


    def do_enter(self):
        GPIO.output(LED_GREEN, GPIO.HIGH)
        
        #Date stuff
        dt = datetime.datetime.now()
        dt_now = dt.strftime("%Y-%m-%d %H:%M:%S")
        unixt    = int(time.mktime(dt.timetuple()) - time.timezone) # Got time in unix time
        print("Unix time " + str(unixt))

        # append 0 to order number
        id = str(self.db.lastid_enter).zfill(4)
        print("new id is " + id)

        # Join order number and datetime to make barcodes id
        barcodes = id + str(unixt)
        print(barcodes)

        # Print receipt
        self.peripheral.start_print(dt_now, id, barcodes)

        # Save to database
        self.db.insert_enter([barcodes, dt_now])

        #TODO: Send command to PLC to open gate
        
        self.do_buzzer(False, 1)
        time.sleep(5)               # You can adjust this to simulate vehicle already through gate

        #TODO: Send command to PLC to close gate

        
        GPIO.output(LED_GREEN, GPIO.LOW)


    def start(self):
        print("App start!")
        self.peripheral.start_scanner(self.scanner_callback)

        while True:
            if GPIO.input(BUTTONA):
                print("Button A hit")
                if self.in_home is True:
                    self.do_enter()

                else:
                    self.do_payment()

            if GPIO.input(BUTTONB):
                print("Button B hit")
                self.do_buzzer(True, 5)

            time.sleep(0.05)


if __name__ == "__main__":
    myapp = App()
    myapp.start()
