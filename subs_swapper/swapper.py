import random

def swap_subtitles(list1, list2, percentage):
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

    # Perform the swapping
    for subtitle_to_swap, subtitle_to_replace in zip(subtitles_to_swap, subtitles_to_replace):
        for i, subtitle_dict in enumerate(result_list):
            if subtitle_dict['id'] == subtitle_to_swap.id:
                result_list[i]['text'] = subtitle_to_replace.text

    # Convert the dictionary representation back to Subtitle objects
    result_list = [Subtitle(**subtitle) for subtitle in result_list]

    return result_list

new_list = swap_subtitles(list1, list2, 0.5)

for subtitle in new_list:
    print(subtitle.text)
