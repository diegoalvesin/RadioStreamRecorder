#!/usr/bin/env python3

import argparse
import vlc
import time
import datetime


def record(radio_url, file_name, program_time):
    i = vlc.Instance()
    p = i.media_player_new()
    cmd1 = f"sout=#duplicate{{dst=std{{access=file,mux=raw,dst='./{file_name}'}},dst=nodisplay}}"
    cmd2 = f"stop-time={program_time}"
    med = i.media_new(radio_url, cmd1, cmd2)
    med.get_mrl()
    p.set_media(med)
    p.play()
    time.sleep(program_time + 5)


def read_arguments():
    parser = argparse.ArgumentParser(description="Parse arguments for stream URL, filename, and duration")
    parser.add_argument("-u", "--url", help="URL for the stream to be recorded (defaults to radio udg lagos)",
                        default="http://lagosdemoreno.radioudg.okhosting.com:8000/", dest="stream_url")
    parser.add_argument("-f", "--filename", help="prefix for the filename, will apend date and mp3 extension",
                        default="FiccionesDeLaPalabra", dest="name_prefix")
    parser.add_argument("-d", "--duration", type=int, help="Duration of program in minutes (defaults to 70 mins)",
                        default=70, dest="duration")
    return parser.parse_args()


if __name__ == '__main__':
    args = read_arguments()
    name_part = datetime.date.today()
    ext = '.mp3'
    out_filename = f"{args.name_prefix}-{name_part}{ext}"
    record(args.stream_url, out_filename, args.duration * 60)




