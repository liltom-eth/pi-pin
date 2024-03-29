# Pi Pin - Open-source AI Wearable based on Raspberry Pi

![IMG_3746_s](https://i.imgur.com/IynuFz8.jpeg)

- Pi Pin is an AI Pin you can wear all day 24 hours which records the conversation you have and uses Generative AI to summarize and take notes for you.

- Pi Pin is fully open-source and affordable, it is built on a $15 Raspberry Pi Zero 2 W with a microphone and battery.

- It is fully hackable and you can write your own application on it.


## Contents

- [The Design](#the-design)
- [Hardware](#hardware)
  - [Hardware List](#hardware-list)
  - [The Assembly](#the-assembly)
    - [Wiring Checklist](#wiring-checklist)
    - [Step by Step Assembly](#step-by-step-assembly)
- [Env Setup](#env-setup)
  - [Install Raspbian on an SD Card](#install-raspbian-on-an-sd-card)
  - [Install Mic Dependencies](#install-mic-dependencies)
  - [Test Mic Recording](#test-mic-recording)
  - [Add Capture Volume Control and Device Name](#add-capture-volume-control-and-device-name)
  - [Install Python Dependencies](#install-python-dependencies)
- [Usage](#usage)
  - [Start Recording](#start-recording)
  - [Auto Start Recording when Boot Pi](#auto-start-recording-when-boot-pi)
  - [Use GenAI to Summarize Conversation](#use-genai-to-summarize-conversation)


## The Design

The enclosure of Pi Pin is designed around the Raspberry Pi Zero, Microphone, and battery to ensure (relatively) compact physical dimensions.

![IMG_3719](https://i.imgur.com/PUDzEZm.png)
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

   The power module also provides a USB-C port for you to charge the battery.

   | ![img](https://i.imgur.com/Sv59xWT.png) | ![IMG_2598_s](https://i.imgur.com/zFBTA5c.jpeg) |
   | --------------------------------------- | ----------------------------------------------- |

   We also add a switch [Panel Slide Switch](https://www.amazon.com/dp/B08SLPWDR9?ref=ppx_yo2ov_dt_b_product_details&th=1) between power module 5V `+` and Pi 5V header, which helps turn on / turn off the whole pin system. 

2. Microphone:

   We are using [Adafruit I2S MEMS Microphone](https://www.adafruit.com/product/3421) as the microphone module, and the graph below shows how you wire the mic to a Raspberry Pi. The graph shows the mic wiring with a big Raspberry Pi but the GPIO header is the same as the Raspberry Pi Zero we used in Pi Pin.

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



## Env Setup

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

![yKBsvF4_s](https://i.imgur.com/UZED1Ce.png)

The Pi model should be automatically detected.

If you want the I2S mic module support to be loaded at boot, select Yes here. Otherwise, you'll have to manually install the module each time you want to use it.

**You need to reboot for the settings to take effect.**

```bash
sudo reboot
```

### Test Mic Recording

Use the following command to list the available input devices:

```bash
arecord -l
```

You should see a card entry with information similar to this:

![sensors_Screenshot_from_2020-04-21_13-29-52.png](https://cdn-learn.adafruit.com/assets/assets/000/090/555/medium800/sensors_Screenshot_from_2020-04-21_13-29-52.png?1587501002)

Note the card number. In the screen shot above it is `0`. You can record a 6 seconds wav file in mono with this command (change the `-plughw` parameter to match the card number from above):

```bash
arecord -D dmic_sv -c2 -r 44100 -f S32_LE -t wav -V mono -v file.wav --duration=6
```

If you have speakers hooked up to the Pi, you can play the file back directly on the device:

```none
aplay file.wav
```

Or, you can copy it over to your computer for playback.

###  Add Capture Volume Control and Device Name

You can add volume control to your mic via **alsamixer** and alsa config.

```bash
sudo apt-get install vim
vim ~/.asoundrc
```

and put the following in:

```bash
#This section makes a reference to your I2S hardware, adjust the card name
# to what is shown in arecord -l after card x: before the name in []
#You may have to adjust channel count also but stick with default first
pcm.dmic_hw {
	type hw
	card sndrpii2scard
	channels 2
	format S32_LE
}

#This is the software volume control, it links to the hardware above and after
# saving the .asoundrc file you can type alsamixer, press F6 to select
# your I2S mic then F4 to set the recording volume and arrow up and down
# to adjust the volume
# After adjusting the volume - go for 50 percent at first, you can do
# something like 
# arecord -D dmic_sv -c2 -r 48000 -f S32_LE -t wav -V mono -v myfile.wav
pcm.dmic_sv {
	type softvol
	slave.pcm dmic_hw
	control {
		name "Boost Capture Volume"
		card sndrpii2scard
	}
	min_dB -3.0
	max_dB 30.0
}
```

Now before you can change the volume you need to use the device once (this is an alsa thing)

Run:

```bash
arecord -D dmic_sv -c1 -r 48000 -f S32_LE -t wav -V mono -v file1.wav --duration=6
```

**Now** you can run **alsamixer** - press **F6** and select the I2S sound card

![sensors_Screenshot_from_2020-04-21_13-58-32.png](https://cdn-learn.adafruit.com/assets/assets/000/090/559/medium800/sensors_Screenshot_from_2020-04-21_13-58-32.png?1587502991)

It will complain there are no playback controls (because its for recording only).

Press **F4** to switch to **Capture** mode and you should be able to adjust the volume with up/down arrow keys.

![sensors_Screenshot_from_2020-04-21_14-04-35.png](https://cdn-learn.adafruit.com/assets/assets/000/090/560/medium800/sensors_Screenshot_from_2020-04-21_14-04-35.png?1587503088)

Sometimes `~/.asoundrc` [disappears](https://forums.raspberrypi.com/viewtopic.php?t=295008) after reboot, you need to setup `raspi-config` to boot to the console rather than boot to the desktop.

```bash
sudo raspi-config
```

![Screenshot 2024-03-29 at 12.52.56 AM](https://i.imgur.com/B6yAOvy.png)

![Screenshot 2024-03-29 at 12.54.37 AM](https://i.imgur.com/q6LSEs5.png)

### Install Python Dependencies

To record the audio through python scripts, you need install these dependencies:

```bash
sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
sudo pip install pyaudio
```

## Usage

### Start Recording

```bash
python record_on_boot.py --output_folder ./recording
```



### Auto Start Recording when Boot Pi

We will be running the Pi Zero as a wearable with a battery power supply, so we need a way of starting the Python script when the Zero powers on.

Create a service file in `/lib/systemd/system/`, e.g. `pipin.service` with the following content:

```bash
sudo vim /lib/systemd/system/pipin.service
```

and put the following in:

```bash
Description=Record on Boot
After=sound.target alsa-state.service

[Service]
User=tom
Type=simple
ExecStart=/usr/bin/python /home/tom/projects/pi-pin/record_on_boot.py --output_folder /home/tom/projects/pi-pin/recording/
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

change `User` and `ExecStart` to your own name and script path.

Change the file permission and enable the service to be started when boot.

```bash
sudo chmod 644 /lib/systemd/system/pipin.service
sudo systemctl start pipin.service
sudo systemctl enable pipin.service
```

For debugging, you can use `sudo systemctl status pipin.service` to check the status and use `journalctl -u pipin.service` to check the output log.

To manually stop the service, use `sudo systemctl stop pipin.service` .

### Use GenAI to Summarize Conversation

Before using the script, you might need to install some OpenAI client dependencies on the device which you want to get the summary. I am using my laptop to call these AI endpoints.

```bash
pip install -r requirements.txt
```

`summarize.ipynb` shows you an example using `OpenAI` `whisper` for speech2text and then use `OpenAI` `gpt4` to summarize the transcription of your conversation.

This is a summary I got when I wore the Pi-Pin listenning to a tech news (the audio recording can be found `./recording/wav_2024_03_20-065147_PM.wav`). 

```text
The report discusses the significant comeback of tech conferences in the Bay Area, focusing on a particularly large event in downtown San Jose centered around artificial intelligence. Tens of thousands of attendees created a scene reminiscent of a major concert outside the SAP Center, highlighting the immense interest and investment in AI. NVIDIA's GTC convention is spotlighted as a major contributor to this momentum, drawing a crowd of around 20,000 people and significantly benefiting local businesses. NVIDIA CEO Jensen Wang spoke on the transformative impact of AI across various industries, emphasizing the computer as a crucial societal tool. The event has led to a notable economic boost for the area, with restaurants and venues experiencing high demand. This resurgence of tech conferences is likened to the phenomenon of "revenge travel" post-COVID lockdowns, indicating a strong desire within the tech community to reconnect, explore new technologies, and invest in the industry's future.
```

The transcription and summary can also be found at `./recording/` folder.