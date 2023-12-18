from pysubparser import parser
 

import argparse

def main():
    parser = argparse.ArgumentParser(description='Your script description here.')

    # Add command-line arguments
    parser.add_argument('-p', type=int, help='Specify a number for option p')
    parser.add_argument('-g', type=int, help='Specify a number for option g')
    parser.add_argument('-i', nargs=2, help='Specify two strings for option i')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the parsed arguments
    p_value = args.p
    g_value = args.g
    i_values = args.i

    # Check if required arguments are provided
    if p_value is None or g_value is None or i_values is None:
        parser.error('Missing required arguments. Use -h for help.')

    # Your script logic goes here
    print(f"Option -p: {p_value}")
    print(f"Option -g: {g_value}")
    print(f"Option -i: {i_values[0]}, {i_values[1]}")

#subtitles = parser.parse('./output_subtitles.srt')
#print(subtitles)
#for subtitle in subtitles:
#    print(subtitle.text)

if __name__ == '__main__':
    main()


