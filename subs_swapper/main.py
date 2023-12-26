import argparse

from subs_swapper.subtitle_wrapper import SubtitleWrapper
import subs_swapper.swapper as swapper
import subs_swapper.writer as writer
import subs_swapper.analyzer as analyzer

def main():
    parser = argparse.ArgumentParser(description='Your trustful sub swapper, improve this descript TODO.')

    parser.add_argument('-p', type=int, help='Specify a number for percentage')
    parser.add_argument('-g', type=int, help='Specify a number for grade-level')
    parser.add_argument('-i', nargs=2, help='Specify two strings for input subtitles')

    args = parser.parse_args()

    p_value = args.p
    g_value = args.g
    i_values = args.i

    if  i_values is None:
        parser.error('Missing required arguments for -i. Use -h for help.')
    if p_value is None:
        p_value = 5
    if  g_value is None:
        g_value = 5

    print(f"arg -p: {p_value}")
    print(f"arg -g: {g_value}")
    print(f"arg -i: {i_values[0]}, {i_values[1]}")

    path = './helo.srt'
    subtitles1, subtitles2 = analyzer.read_subs("subs_en.srt", "subs_indo.srt")
    analyzer.set_grading_level(subtitles1)
    analyzer.set_grading_level(subtitles2)
    analyzer.validate_subtitles(subtitles1, subtitles2)
    swapped_subs = swapper.swap_subtitles(subtitles1, subtitles2, 0.5)
    writer.write_srt(swapped_subs, path)


if __name__ == '__main__':
    main()


