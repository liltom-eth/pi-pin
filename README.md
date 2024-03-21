# Pi Pin

## Hardware 

### Hardware List

- Raspberry Pi Zero 2 W
- Battery Charging Board
  - DWEII Type-C USB 5V 2A Boost Converter Step-Up Power Module Lithium Battery Charging Protection Board
  - [Amazon](https://www.amazon.com/dp/B09YD5C9QC?ref=ppx_yo2ov_dt_b_product_details&th=1)
  - Size unknown
- Battery
  - 3.7V 600mAh 702030 Lithium Polymer
  - Temu discontinued
  - Size unknown
- Switch
  - SS12F15 Panel Slide Switch 
  - [Amazon](https://www.amazon.com/dp/B08SLPWDR9?ref=ppx_yo2ov_dt_b_product_details&th=1)
  - Size unknown
- Audio
  - Adafruit I2S MEMS Microphone Breakout - SPH0645LM4H
  - [Adafruit](https://www.adafruit.com/product/3421)
  - 16.7mm x 12.7mm x 1.8mm

## Software

### Installation

Install Raspbian on an SD Card

You'll need to start with Raspbian or Raspbian Lite. Get the latest version from the [Raspberry Pi Download page](https://www.raspberrypi.org/downloads/raspbian/) and follow [these instructions to install the OS image to the SD card](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).

Update the Pi

```bash
sudo apt-get -y update
sudo apt-get -y upgrade
```

Install Microphone Packages

```bash
sudo pip install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2smic.py
sudo python i2smic.py
```

Once you run the script, you will be presented with options for configuration.

<img src="https://i.imgur.com/yKBsvF4.png" alt="sensors_i2smic_python_install_autoload.png" style="zoom:67%;" />

The Pi model should be automatically detected.

If you want the I2S mic module support to be loaded at boot, select Yes here. Otherwise, you'll have to manually install the module each time you want to use it.

**You need to reboot for the settings to take effect.**

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

