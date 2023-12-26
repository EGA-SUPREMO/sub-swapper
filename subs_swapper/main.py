import argparse

from subs_swapper.subtitle_wrapper import SubtitleWrapper
import subs_swapper.swapper as swapper
import subs_swapper.writer as writer
import subs_swapper.analyzer as analyzer

def main():
    parser = argparse.ArgumentParser(description='Your trustful sub swapper, improve this descript TODO.')

    parser.add_argument('-p', type=int, help='Specify a number for percentage')
    parser.add_argument('-o', type=str, help='Specify a path for output file')
    parser.add_argument('-g', type=int, help='Specify a number for grade-level')
    parser.add_argument('-i', nargs=2, help='Specify two strings for input subtitles')

    args = parser.parse_args()

    percentage_arg = args.p
    grade_reading_arg = args.g
    input_path_arg_subs = args.i
    path_arg = args.o

    if input_path_arg_subs is None:
        parser.error('Missing required arguments for -i. Use -h for help.')
    if percentage_arg is None:
        percentage_arg = 5
    if grade_reading_arg is None:
        grade_reading_arg = 5
    if path_arg is None:
        path_arg = './output.srt'

    print(f"arg -p: {percentage_arg}")
    print(f"arg -g: {grade_reading_arg}")
    print(f"arg -o: {path_arg}")
    print(f"arg -i: {input_path_arg_subs[0]}, {input_path_arg_subs[1]}")

    percentage = percentage_arg/100

    subtitles1, subtitles2 = analyzer.read_subs(input_path_arg_subs[0], input_path_arg_subs[1])
    analyzer.set_grading_level(subtitles1)
    analyzer.set_grading_level(subtitles2)
    analyzer.validate_subtitles(subtitles1, subtitles2)
    swapped_subs = swapper.swap_subtitles(subtitles1, subtitles2, percentage)
    writer.write_srt(swapped_subs, path_arg)


if __name__ == '__main__':
    main()


