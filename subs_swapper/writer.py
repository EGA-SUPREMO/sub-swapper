from pysubparser.writers import srt

def write_srt(new_subs, path):
    write_subs = []
    for subtitle in new_subs:
        write_subs.append(subtitle['subtitle_line'])
    srt.write(write_subs, path)
