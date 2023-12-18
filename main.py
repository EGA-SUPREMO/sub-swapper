from pysubparser import parser
 

import argparse

def main():
    parser = argparse.ArgumentParser(description='Your trustful sub swapper, improve this descript TODO.')

    # Add command-line arguments
    parser.add_argument('-p', type=int, help='Specify a number for percentage')
    parser.add_argument('-g', type=int, help='Specify a number for grade-level')
    parser.add_argument('-i', nargs=2, help='Specify two strings for input subtitles')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the parsed arguments
    p_value = args.p
    g_value = args.g
    i_values = args.i

    # Check if required arguments are provided
    if  i_values is None:
        parser.error('Missing required arguments for -i. Use -h for help.')
    if p_value is None:
        p_value = 5
    if  g_value is None:
        g_value = 5

    # Your script logic goes here
    print(f"arg -p: {p_value}")
    print(f"arg -g: {g_value}")
    print(f"arg -i: {i_values[0]}, {i_values[1]}")

#subtitles = parser.parse('./output_subtitles.srt')
#print(subtitles)
#for subtitle in subtitles:
#    print(subtitle.text)

if __name__ == '__main__':
    main()


