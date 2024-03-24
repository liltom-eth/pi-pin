import os
import argparse
from datetime import datetime

import pyaudio
import wave


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--mic_name", help="Microphone device name", type=str, default="dmic_sv"
    )

    parser.add_argument(
        "--output_folder",
        help="Absolute path to recorded audio.",
        default="/home/tom/projects/ai-pin/recording/",
    )

    args = parser.parse_args()

    FORM_1 = pyaudio.paInt16  # 16-bit resolution
    SAMPLE_RATE = 16000
    CHANNEL = 1
    CHUNK = 256

    audio = pyaudio.PyAudio()

    device_list = [
        audio.get_device_info_by_index(i) for i in range(audio.get_device_count())
    ]
    # print(device_list)
    devicename_to_index_dict = {
        device["name"]: device["index"] for device in device_list
    }
    # print(devicename_to_index_dict)

    # check if device found
    DEVICE_NAME = args.mic_name
    if DEVICE_NAME in devicename_to_index_dict:
        DEVICE_INDEX = devicename_to_index_dict.get(DEVICE_NAME)
    else:
        raise Exception("Can not find microphone device name: " + DEVICE_NAME)

    date = datetime.now().strftime("%Y_%m_%d-%I%M%S_%p")
    wav_output_filename = "wav_" + date + ".wav"  # unique filename with date and time
    print(wav_output_filename)

    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    wav_output_path = os.path.join(args.output_folder, wav_output_filename)

    wavefile = wave.open(wav_output_path, "wb")
    wavefile.setnchannels(CHANNEL)
    wavefile.setsampwidth(audio.get_sample_size(FORM_1))
    wavefile.setframerate(SAMPLE_RATE)

    stream = audio.open(
        format=FORM_1,
        rate=SAMPLE_RATE,
        channels=CHANNEL,
        input_device_index=DEVICE_INDEX,
        input=True,
        # output = True,
        frames_per_buffer=CHUNK,
    )

    try:

        print("Listening...")
        while True:
            data = stream.read(
                CHUNK, exception_on_overflow=False
            )  # added per stackoverflow
            if wavefile is not None:
                wavefile.writeframes(data)

    except:
        print("Stopping ...")
    finally:
        print("finish recording")
        stream.stop_stream()
        stream.close()
        audio.terminate()
        wavefile.close()


if __name__ == "__main__":
    main()
