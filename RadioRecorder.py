import sys
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


if __name__ == '__main__':
    # defaults are for Lagos de Moreno and the name of file for Ficciones de la palabra
    radio_url = "http://lagosdemoreno.radioudg.okhosting.com:8000/"
    name_part = datetime.date.today()
    ext = '.mp3'
    file_name = f"FiccionesDeLaPalabra-{name_part}{ext}"
    record(radio_url, file_name, 2*60)




