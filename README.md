# Pi Pin - Open-source AI Wearable based on Raspberry Pi

![IMG_3746_s](https://i.imgur.com/IynuFz8.jpeg)

- Pi Pin is an AI Pin you can wear all day 24 hours which records the conversation you have and uses Generative AI to summarize and take notes for you.

- Pi Pin is fully open-source and affordable, it is built on a $15 Raspberry Pi Zero 2 W with a microphone and battery.

- It is fully hackable and you can write your own application on it.



## The Design

The enclosure of Pi Pin is designed around the Raspberry Pi Zero, Microphone and battery to ensure (relatively) compact physical dimensions.

![IMG_3720](https://i.imgur.com/NZmAXCN.jpeg)

Electronics are intentionally kept minimal (Pi, Microphone, Battery, Battery Charging Module) and most of the parts are either 3D printable or available as off-the-shelf products.

| ![](https://i.imgur.com/WRYmsXQ.jpeg)         | ![](https://i.imgur.com/nugJUNO.jpeg)         |
| --------------------------------------------- | --------------------------------------------- |
| ![IMG_3743](https://i.imgur.com/sTFf5gc.jpeg) | ![IMG_3741](https://i.imgur.com/kWaQIV9.jpeg) |
| ![](https://i.imgur.com/dsYf3rd.jpeg)         | ![IMG_3725](https://i.imgur.com/O7UJOI4.jpeg) |

## Hardware

### Hardware List

- Case
  - 3D printed parts ([STEP files](https://github.com/liltom-eth/pi-pin/blob/main/step))
  - M1x7mm screws x 4
- [Raspberry Pi Zero 2 W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)
  - 65mm × 30mm
- Battery Charging Board
  - DWEII Type-C USB 5V 2A Boost Converter Step-Up Power Module Lithium Battery Charging Protection Board
  - [Amazon](https://www.amazon.com/dp/B09YD5C9QC?ref=ppx_yo2ov_dt_b_product_details&th=1)
  - Size unknown
- Battery
  - 3.7V 600mAh 702030 Lithium Polymer
  - Temu discontinued, [Aliexpress](https://www.aliexpress.us/item/3256806102198497.html?src=google&src=google&albch=shopping&acnt=708-803-3821&slnk=&plac=&mtctp=&albbt=Google_7_shopping&albagn=888888&isSmbAutoCall=false&needSmbHouyi=false&albcp=20123152476&albag=&trgt=&crea=en3256806102198497&netw=x&device=c&albpg=&albpd=en3256806102198497&gad_source=1&gclid=CjwKCAjwte-vBhBFEiwAQSv_xRsccW7pTkCGBeYwrlAua_-4K2JR1EvW3KQWdi5Rkl47-qrVKlCvzhoCUtwQAvD_BwE&gclsrc=aw.ds&aff_fcid=e504ff0d30804237976584ac28861318-1711069940562-07127-UneMJZVf&aff_fsk=UneMJZVf&aff_platform=aaf&sk=UneMJZVf&aff_trace_key=e504ff0d30804237976584ac28861318-1711069940562-07127-UneMJZVf&terminal_id=aa26aeb9b4294a0aace4b0a9f4391832&afSmartRedirect=y&gatewayAdapt=glo2usa)
  - 20mm x 30mm x 7mm
- Switch
  - SS12F15 Panel Slide Switch 
  - [Amazon](https://www.amazon.com/dp/B08SLPWDR9?ref=ppx_yo2ov_dt_b_product_details&th=1)
  - Size unknown
- Microphone
  - Adafruit I2S MEMS Microphone Breakout - SPH0645LM4H
  - [Adafruit](https://www.adafruit.com/product/3421)
  - 16.7mm x 12.7mm x 1.8mm

### The Assembly

The graph below shows all wiring you need for Pi Pin.

![IMG_3720](https://i.imgur.com/NZmAXCN.jpeg)

#### Wiring Checklist

| **From**                | **To**             |
| ----------------------- | ------------------ |
| Slide Switch right pin  | Pi 5V (pin 2)      |
| Slide Switch middle pin | Power Module 5V +  |
| Power Module 5V -       | Pi GND (pin 6)     |
| Power Module 3.7V +     | Battery +          |
| Power Module 3.7V -     | Battery -          |
| Mic GND                 | Pi GND (pin 6)     |
| Mic 3V                  | Pi 3.3V (pin 1)    |
| Mic BCLK                | Pi PCM 18 (pin 12) |
| Mic LRCL                | Pi PCM 19 (pin 35) |
| Mic DOUT                | Pi PCM 20 (pin 38) |

#### Step by Step Assembly

1. Battery: 

   We use a [3.7V 600mAh 702030 Lithium](https://www.aliexpress.us/item/3256806102198497.html?src=google&src=google&albch=shopping&acnt=708-803-3821&slnk=&plac=&mtctp=&albbt=Google_7_shopping&albagn=888888&isSmbAutoCall=false&needSmbHouyi=false&albcp=20123152476&albag=&trgt=&crea=en3256806102198497&netw=x&device=c&albpg=&albpd=en3256806102198497&gad_source=1&gclid=CjwKCAjwte-vBhBFEiwAQSv_xRsccW7pTkCGBeYwrlAua_-4K2JR1EvW3KQWdi5Rkl47-qrVKlCvzhoCUtwQAvD_BwE&gclsrc=aw.ds&aff_fcid=e504ff0d30804237976584ac28861318-1711069940562-07127-UneMJZVf&aff_fsk=UneMJZVf&aff_platform=aaf&sk=UneMJZVf&aff_trace_key=e504ff0d30804237976584ac28861318-1711069940562-07127-UneMJZVf&terminal_id=aa26aeb9b4294a0aace4b0a9f4391832&afSmartRedirect=y&gatewayAdapt=glo2usa) battery with a [Power Module](https://www.amazon.com/dp/B09YD5C9QC?ref=ppx_yo2ov_dt_b_product_details&th=1) as the battery solution. The power module works like a battery charge controller and a DC/DC converter in one. 

   Normally the wire connection would like the left below graph. You can connect the 3.7V Lithium battery `+` to power module battery `+` and 3.7V Lithium battery `-` to power module battery `-` (Just like below right graph).

   After that, you’ll have constant 5V output at the power module 5V `+` and `-` .

   The power module also provides a USB-C port for you to charging the battery.

   | ![img](https://i.imgur.com/Sv59xWT.png) | ![IMG_2598_s](https://i.imgur.com/zFBTA5c.jpeg) |
   | --------------------------------------- | ----------------------------------------------- |

   We also add a switch [Panel Slide Switch](https://www.amazon.com/dp/B08SLPWDR9?ref=ppx_yo2ov_dt_b_product_details&th=1) between power module 5V `+` and Pi 5V header, which helps turn on / turn off the whole pin system. 

2. Microphone:

   We are using [Adafruit I2S MEMS Microphone](https://www.adafruit.com/product/3421) as the microphone module, and the graph below shows how you wire the mic to a Raspberry Pi. The graph shows the mic wiring with a big Raspberry Pi but the GPIO header is same as the Raspberry Pi Zero we used in Pi Pin.

   ![sensors_pi_i2s_bb.png](https://i.imgur.com/BRpojfD.png)

3. Case Assembly:

   You can find 3D printed parts here ([STEP files](https://github.com/liltom-eth/pi-pin/blob/main/step)). The top part is designed around the Raspberry Pi Zero, and the bottom part is designed containing microphone, battery, power module and switch. All modules should be fitting perfectly inside the case, and you can also use tape or glue to stable them.

   The graph left below shows the modules (no wiring) fitting in the case.

   The graph left below shows the modules (wiring) fitting in the case.

| ![IMG_7143](https://i.imgur.com/UIYWVhd.jpeg) | ![IMG_3725](https://i.imgur.com/O7UJOI4.jpeg) |
| --------------------------------------------- | --------------------------------------------- |

Then you can combine two parts and use four M1x7mm screws to fasten them.

| ![IMG_3741](https://i.imgur.com/kWaQIV9.jpeg) | ![IMG_3743](https://i.imgur.com/sTFf5gc.jpeg) |
| --------------------------------------------- | --------------------------------------------- |



## Software

### Install Raspbian on an SD Card

You'll need to start with Raspbian or Raspbian Lite. Get the latest version from the [Raspberry Pi Download page](https://www.raspberrypi.org/downloads/raspbian/) and follow [these instructions to install the OS image to the SD card](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).

Update the Pi

```bash
sudo apt-get -y update
sudo apt-get -y upgrade
```

### Install Mic Dependencies

```bash
sudo pip install --upgrade adafruit-python-shell
git clone https://github.com/liltom-eth/pi-pin.git
cd pi-pin/scripts
sudo python i2smic.py
```

Once you run the script, you will be presented with options for configuration.

<img src="https://i.imgur.com/yKBsvF4.png" alt="sensors_i2smic_python_install_autoload.png" style="zoom:67%;" />

The Pi model should be automatically detected.

If you want the I2S mic module support to be loaded at boot, select Yes here. Otherwise, you'll have to manually install the module each time you want to use it.

**You need to reboot for the settings to take effect.**

```
sudo reboot
```

### Test Mic Recording



```
arecord -l
```



```
arecord -D plughw:0 -c1 -r 48000 -f S32_LE -t wav -V mono -v file1.wav --duration=6
arecord -D dmic_sv -c1 -r 48000 -f S32_LE -t wav -V mono -v file1.wav --duration=6
```



```
sudo apt-get install vim
vim ~/.asoundrc
```



```
arecord -D dmic_sv -c2 -r 44100 -f S32_LE -t wav -V mono -v file2.wav --duration=6
```



```
sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev

sudo pip install pyaudio
```







vad

```
cobra_demo_mic --access_key 'ygrj9sIlLrxhY802Vgq7RWMjuFxh+xo47dmSehxHBYBgvvpfWUOyTA==' --output_path ./test.wav --audio_device_index 0

cobra_demo_file --access_key 'ygrj9sIlLrxhY802Vgq7RWMjuFxh+xo47dmSehxHBYBgvvpfWUOyTA==' --input_wav_path ./wav_2024_03_20-020352_AM.wav
```





We will be running the Pi Zero as a wearable with a USB power supply (and not with a keyboard, mouse or monitor attached), so we need a way of starting the Python script when the Zero powers on.

```
sudo vim ~/.config/lxsession/LXDE-pi/autostart

```

A file will open up, add this line at the bottom of the file to automatically start your time-lapse file using Python 3:

```bash
sudo /usr/bin/python /home/tom/projects/ai-pin/record_on_boot.py & > /home/tom/projects/ai-pin/log.txt 2>&1
```



crontab

```
sudo crontab -e
```



```
@reboot /bin/sleep 10; /usr/bin/python /home/tom/projects/ai-pin/record_on_boot.py >> /home/tom/projects/ai-pin/log.txt 2>&1
```



systemd

```
sudo vim /lib/systemd/system/aipin.service
```

```
Description=RecordDescription=Record on Boot
After=sound.target alsa-state.service

[Service]
User=tom
Type=simple
ExecStart=/usr/bin/python /home/tom/projects/ai-pin/record_on_boot.py
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```
sudo chmod 644 /lib/systemd/system/aipin.service
sudo systemctl start aipin.service
sudo systemctl enable aipin.service

sudo systemctl stop aipin.service

journalctl -u aipin.service

```

