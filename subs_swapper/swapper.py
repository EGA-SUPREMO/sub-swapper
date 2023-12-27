import random
import copy

from pysubparser.classes.subtitle import Subtitle

from subs_swapper.subtitle_wrapper import SubtitleWrapper

def swap_subtitles(list1, list2, percentage, reading_level):
    result_list = [copy.deepcopy(subtitle.__dict__) for subtitle in list1]

    valid_subtitles_list1 = [subtitle for subtitle in list1 if subtitle.is_valid and subtitle.grade_level < reading_level]
    valid_subtitles_list2 = [subtitle for subtitle in list2 if subtitle.is_valid]

    num_subtitles_to_swap = int(len(list1) * percentage)
    if num_subtitles_to_swap > len(valid_subtitles_list1):
        num_subtitles_to_swap = len(valid_subtitles_list1)
        print(f"Warning: You requested {percentage * 100:.0f}%, but only {num_subtitles_to_swap / len(list1) * 100:.2f}% of subtitles have a grading level below {reading_level}. Setting to the maximum available, which is {num_subtitles_to_swap / len(list1)*100:.2f}%.")


    subtitles_to_swap = random.sample(valid_subtitles_list1, num_subtitles_to_swap)
    subtitles_to_replace = valid_subtitles_list2

    for subtitle_to_swap in subtitles_to_swap:
        result_list[subtitle_to_swap.subtitle_line.index]['subtitle_line'] = Subtitle(
                index=result_list[subtitle_to_swap.subtitle_line.index]['subtitle_line'].index,
                start=result_list[subtitle_to_swap.subtitle_line.index]['subtitle_line'].start,
                end=result_list[subtitle_to_swap.subtitle_line.index]['subtitle_line'].end,
                lines=list2[subtitle_to_swap.id_line_external].subtitle_line.lines)

    return result_list
