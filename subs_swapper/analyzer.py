from pysubparser import parser
import textstat
from subs_swapper.subtitle_wrapper import SubtitleWrapper

from datetime import datetime, timedelta, time


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



def set_grading_level(subtitles):
    #text = "Saya suka makan nasi goreng."
    #text = "Contoh kalimat dalam bahasa Indonesia."
    #text = "banyak orang tetap antusias untuk menghadiri acara tersebut di taman kota"
    #text = "Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard."
    #coleman_liau_index = textstat.coleman_liau_index(text)
    #print(f"Coleman-Liau Index: {coleman_liau_index}")
    for subtitle in subtitles:
        subtitle.grade_level = textstat.coleman_liau_index(subtitle.subtitle_line.text)


def are_subtitle_line_approximately_same_time(subtitles1, subtitles2, tolerance=0.8):
    for sub1 in subtitles1:
        for sub2 in subtitles2:
            start_datetime1 = datetime.combine(datetime.min, sub1.subtitle_line.start)
            end_datetime1 = datetime.combine(datetime.min, sub1.subtitle_line.end)

            start_datetime2 = datetime.combine(datetime.min, sub2.subtitle_line.start)
            end_datetime2 = datetime.combine(datetime.min, sub2.subtitle_line.end)

            # Calculate differences in seconds
            start_difference = abs((start_datetime1 - start_datetime2).total_seconds())
            end_difference = abs((end_datetime1 - end_datetime2).total_seconds())

            if (start_difference <= tolerance and end_difference <= tolerance):
                sub1.id_line_external = sub2.subtitle_line.index
                sub2.id_line_external = sub1.subtitle_line.index
                sub1.swap = True
                sub2.swap = True




subtitles1, subtitles2 = read_subs("subs_en.srt", "subs_indo.srt")
set_grading_level(subtitles1)
set_grading_level(subtitles2)

#print(are_subtitle_line_approximately_same_time(subtitles1[273].subtitle_line, subtitles2[303].subtitle_line))
are_subtitle_line_approximately_same_time(subtitles1, subtitles2)

print(subtitles1[273].swap)
print(subtitles1[273].id_line_external)
print(subtitles2[306].swap)
print(subtitles2[306].id_line_external)

#print(subtitles1[-2].subtitle_line.text)
#print(subtitles1[100].subtitle_line.text)
#print(subtitles2[100].subtitle_line.text)