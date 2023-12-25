import random
import copy

from subs_swapper.subtitle_wrapper import SubtitleWrapper

def swapa_subtitles(list1, list2, percentage):
    # Copy the first list to avoid modifying the original list
    result_list = [subtitle.__dict__ for subtitle in list1]

    # Filter valid subtitles from both lists
    valid_subtitles_list1 = [subtitle for subtitle in list1 if subtitle.is_valid]
    valid_subtitles_list2 = [subtitle for subtitle in list2 if subtitle.is_valid]

    # Determine the number of subtitles to swap based on the percentage
    num_subtitles_to_swap = int(len(valid_subtitles_list1) * percentage)

    # Randomly select subtitles from both lists to swap
    subtitles_to_swap = random.sample(valid_subtitles_list1, num_subtitles_to_swap)
    subtitles_to_replace = random.sample(valid_subtitles_list2, num_subtitles_to_swap)
    print(subtitles_to_swap)
    # Perform the swapping
    for subtitle_to_swap, subtitle_to_replace in zip(subtitles_to_swap, subtitles_to_replace):
        for i, subtitle_dict in enumerate(result_list):
            if subtitle_dict['index'] == subtitle_to_swap.subtitle_line.index:
                result_list[i]['text'] = subtitle_to_replace.text

    # Convert the dictionary representation back to Subtitle objects
    result_list = [Subtitle(**subtitle) for subtitle in result_list]

    return result_list

def swap_subtitles(list1, list2, percentage):
    # Copy the first list to avoid modifying the original list
#    result_list = [SubtitleWrapper(subtitle_line=subtitle.subtitle_line, id_line_external=subtitle.id_line_external, is_valid=subtitle.is_valid) for subtitle in list1]
    result_list = [subtitle.__dict__ for subtitle in list1]
    result_list = [copy.deepcopy(subtitle.__dict__) for subtitle in list1]


    # Filter valid subtitles from both lists
    valid_subtitles_list1 = [subtitle for subtitle in list1 if subtitle.is_valid]
    valid_subtitles_list2 = [subtitle for subtitle in list2 if subtitle.is_valid]

    # Determine the number of subtitles to swap based on the percentage
    num_subtitles_to_swap = int(len(list1) * percentage)
    random.seed(42)
    # Randomly select subtitles from both lists to swap
    subtitles_to_swap = random.sample(valid_subtitles_list1, num_subtitles_to_swap)
    subtitles_to_replace = valid_subtitles_list2
    # Perform the swapping
#    for subtitle_to_swap, subtitle_to_replace in zip(subtitles_to_swap, subtitles_to_replace):
#        for i, subtitle_wrapper in enumerate(result_list):
#            if subtitle_wrapper.id_line_external == subtitle_to_swap.id_line_external:
#                result_list[i].subtitle_line.text = subtitle_to_replace.subtitle_line.text

    # Perform the swapping
#    for subtitle_to_swap, subtitle_to_replace in zip(subtitles_to_swap, subtitles_to_replace):
#        for i, subtitle_dict in enumerate(result_list):
#            if subtitle_dict['id_line_external'] == subtitle_to_swap['id_line_external']:
#                result_list[i]['subtitle_line']['text'] = subtitle_to_replace['subtitle_line']['text']

# subtitle_to_replace = indo
# subtitle_to_swap = eng

    for subtitle_wrapper_dict, subtitle_to_swap, subtitle_to_replace in zip(result_list, subtitles_to_swap, subtitles_to_replace):
        #print("igonarr max length: " + subtitle_to_swap.subtitle_line.text)
        if subtitle_wrapper_dict['id_line_external'] == subtitle_to_swap.subtitle_line.index:
            print(subtitle_wrapper_dict['subtitle_line'])
            print(subtitle_to_replace.subtitle_line)
            print(subtitle_to_swap.subtitle_line)
            #subtitle_wrapper_dict['subtitle_line']['text'] = subtitle_to_replace.subtitle_line.text
            subtitle_wrapper_dict['subtitle_line'] = {'text': subtitle_to_replace.subtitle_line.text}

            subtitle_wrapper_dict['id_line_external'] = -1
            subtitle_wrapper_dict['grade_level'] = 0
            subtitle_wrapper_dict['is_valid'] = False

            #print(subtitle_wrapper_dict['subtitle_line']['text'])
            #print(subtitle_to_replace.subtitle_line.text)
            #return


    return result_list
