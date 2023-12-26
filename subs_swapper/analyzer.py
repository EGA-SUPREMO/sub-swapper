import textstat

from pysubparser import parser
from datetime import datetime, timedelta, time

from subs_swapper.subtitle_wrapper import SubtitleWrapper
import subs_swapper.swapper as swapper

def read_subs(input_1: str, input_2: str):
    subtitle1 = list(parser.parse(input_1))
    subtitle2 = list(parser.parse(input_2))
    subtitle_wrappers1 = []
    subtitle_wrappers2 = []

    for subtitle in subtitle1:
        subtitle_wrapper = SubtitleWrapper(subtitle, 0, False)
        subtitle_wrappers1.append(subtitle_wrapper)
    for subtitle in subtitle2:
        subtitle_wrapper = SubtitleWrapper(subtitle, 0, False)
        subtitle_wrappers2.append(subtitle_wrapper)

    return subtitle_wrappers1, subtitle_wrappers2

def set_grading_level(subtitles):
    for subtitle in subtitles:
        subtitle.grade_level = textstat.coleman_liau_index(subtitle.subtitle_line.text)

def validate_subtitles(subtitles1, subtitles2, tolerance=0.8):
    for sub1 in subtitles1:
        for sub2 in subtitles2:
            start_datetime1 = datetime.combine(datetime.min, sub1.subtitle_line.start)
            end_datetime1 = datetime.combine(datetime.min, sub1.subtitle_line.end)

            start_datetime2 = datetime.combine(datetime.min, sub2.subtitle_line.start)
            end_datetime2 = datetime.combine(datetime.min, sub2.subtitle_line.end)

            start_difference = abs((start_datetime1 - start_datetime2).total_seconds())
            end_difference = abs((end_datetime1 - end_datetime2).total_seconds())

            if (start_difference <= tolerance and end_difference <= tolerance):
                sub1.id_line_external = sub2.subtitle_line.index
                sub2.id_line_external = sub1.subtitle_line.index
                sub1.is_valid = True
                sub2.is_valid = True

                #if (subtitles1[58].subtitle_line.index==sub1.subtitle_line.index):
                #    print(subtitles1[58].subtitle_line.text)
                #    print(subtitles1[58].id_line_external)


subtitles1, subtitles2 = read_subs("subs_en.srt", "subs_indo.srt")
set_grading_level(subtitles1)
set_grading_level(subtitles2)

validate_subtitles(subtitles1, subtitles2)

new_subs = swapper.swap_subtitles(subtitles1, subtitles2, 0.5)
#for subtitle in new_subs:
#    print(subtitle)


print("-----")
print(subtitles1[273].is_valid)
print(subtitles1[273].id_line_external)
print(subtitles2[306].is_valid)
print(subtitles2[306].id_line_external)
