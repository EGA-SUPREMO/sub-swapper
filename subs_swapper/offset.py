import re
from datetime import datetime, timedelta

import argparse

def main():
    parser = argparse.ArgumentParser(description='Temp script to offset subs.')
    parser.add_argument('-o', type=str, help='Specify a output path for offset subtitle')
    parser.add_argument('-s', type=float, help='Specify a time to offset')
    parser.add_argument('-i', type=str, help='Specify a string for input subtitle file')

    args = parser.parse_args()

    if args.i is None:
        parser.error('Missing required arguments for -i. Use -h for help.')

    offset_srt(args.i, args.o, args.s)
    print(f"Subtitles offset by {args.s} seconds and saved to {args.o}.")

def convert_to_seconds(time_str):
    time_obj = datetime.strptime(time_str, "%H:%M:%S,%f")
    return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second + time_obj.microsecond / 1e6

def format_time(seconds):
    time_obj = timedelta(seconds=seconds)
    formatted_time = "{:02}:{:02}:{:06.3f}".format(
        int(time_obj.total_seconds() // 3600),
        int((time_obj.total_seconds() % 3600) // 60),
        time_obj.total_seconds() % 60
    )
    formatted_time = formatted_time.replace('.', ',')
    
    return formatted_time

def offset_subtitle(subtitle, offset):
    start_time, end_time = subtitle.group(1, 2)
    start_time = convert_to_seconds(start_time) + offset
    end_time = convert_to_seconds(end_time) + offset
    return f"{format_time(start_time)} --> {format_time(end_time)}"

def offset_srt(input_file, output_file, offset):
    with open(input_file, 'r', encoding='utf-8') as f:
        srt_content = f.read()

    # Use regex to find and offset subtitles
    pattern = re.compile(r'(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)')
    srt_content = re.sub(pattern, lambda match: offset_subtitle(match, offset), srt_content)

    # Write the new content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(srt_content)

if __name__ == "__main__":
    main()
