from escpos.printer import Usb
from evdev import InputDevice, categorize, ecodes
from thread import BaseThread

NOT_RECOGNIZED_KEY = u'X'

class Peripherals:
    def __init__(self):
        self.printer = Usb(0x0416,0x5011, profile="POS-5890")
        self.scanner = InputDevice('/dev/input/event0') # Replace with your device

        self.scancodes = {
            11:	u'0',
            2:	u'1',
            3:	u'2',
            4:	u'3',
            5:	u'4',
            6:	u'5',
            7:	u'6',
            8:	u'7',
            9:	u'8',
            10:	u'9'
        }

    def start_scanner(self, cbfunc):
        print("Starting scanner thread!")
        self.scanner_thr = BaseThread(
            name='scanner_thr',
            target=self.scanner_func,
            callback=cbfunc
        )
        self.scanner_thr.start()

    def scanner_func(self):
        barcode = ''
        # Make a thread
        for event in self.scanner.read_loop():
            if event.type == ecodes.EV_KEY:
                eventdata = categorize(event)
                # Keydown
                if eventdata.keystate == 1:
                    scancode = eventdata.scancode
                    # Enter
                    if scancode == 28:
                        # get the barcode (barcode)
                        return barcode
                    else:
                        key = self.scancodes.get(scancode, NOT_RECOGNIZED_KEY)
                        barcode = barcode + key
                        if key == NOT_RECOGNIZED_KEY:
                            print('unknown key, scancode=' + str(scancode))

    def start_print(self, time, order_number, barcodes):
        self.printer.set(align='left')
        self.printer.text("Time : %s \n" % time)
        self.printer.text("No Order : %s \n" % order_number)
        self.printer.text("Gate : 1")
        self.printer.text('\n')
        self.printer.soft_barcode('code128', barcodes, module_height=8, module_width=0.18)
        self.printer.text('\n')
        
        print("Done printing!")

# def cobalah_callback(data):
#     print("callback!")
#     print(data)

if __name__ == "__main__":
    print("Start")
    myPer = Peripherals()

    # myPer.start_print()
    myPer.start_scanner(cobalah_callback)