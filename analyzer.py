from pysubparser import parser
import textstat
from subtitle_wrapper import SubtitleWrapper


def read_subs(input_1: str, input_2: str):
    subtitle1 = list(parser.parse(input_1))
    subtitle2 = list(parser.parse(input_2))
    subtitle_wrappers1 = []
    subtitle_wrappers2 = []

    for subtitle in subtitle1:
        subtitle_wrapper = SubtitleWrapper(subtitle, 0, 0, False)
        subtitle_wrappers1.append(subtitle_wrapper)
    for subtitle in subtitle2:
        subtitle_wrapper = SubtitleWrapper(subtitle, 0, 0, False)
        subtitle_wrappers2.append(subtitle_wrapper)

    return subtitle_wrappers1, subtitle_wrappers2



def get_grading_level():
    pass

text = "Saya suka makan nasi goreng."
#text = "Contoh kalimat dalam bahasa Indonesia."
#text = "banyak orang tetap antusias untuk menghadiri acara tersebut di taman kota"
#text = "Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard."




coleman_liau_index = textstat.coleman_liau_index(text)

print(f"Coleman-Liau Index: {coleman_liau_index}")


subtitles1, subtitles2 = read_subs("subs_en.srt", "subs_indo.srt")

print(subtitles1[100].subtitle_line.text)
print(subtitles2[100].subtitle_line.text)