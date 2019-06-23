# Parking Lot

#### Parking lot system based on Raspberry PI. Just like a similar parking scenario in mall or other parking system

**Hardware used**

- Raspberry pi 
- Aibecy MP2600 Scanner
- Taffware POS-5890K USB Thermal Printer
- HDMI Display
- PLCs

**Generate .ui to .py**

```
$ pyuic5 home.ui -o home.py
$ pyuic5 payment.ui -o payment.py
```

**Connections**

|Component|Interface|Pin/others|
|-----|----|----|
|Scanner|USB|-|
|Printer|USB|-|
|PLC|Modbus|TCP|
|BUTTONA|GPIO|17|
|BUTTONB|GPIO|18|
|LED_GREEN|GPIO|22|
|LED_RED|GPIO|23|
|BUZZER|GPIO|27|

**Install requirements**

```
pip3 install -r requirements.txt
```

TODO :

- Add camera?
- TODO's in code