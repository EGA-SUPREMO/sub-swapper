import textstat

from pysubparser.cleaners import brackets, formatting
from pysubparser import parser
from datetime import datetime, timedelta, time

from subs_swapper.subtitle_wrapper import SubtitleWrapper

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
    subtitles_cleaned = []
    for subtitle in subtitles:
        subtitles_cleaned.append(list(
            formatting.clean(
                [subtitle.subtitle_line]
            )
        )[0])
    for index, subtitle in enumerate(subtitles_cleaned):
        subtitles[index].grade_level = textstat.coleman_liau_index(subtitle.text)

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
