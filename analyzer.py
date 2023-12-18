from pysubparser import parser

print(subtitles)
for subtitle in subtitles:
    print(subtitle.text)

def read_subs(input_1: str, input_2: str):
    subtitles1 = parser.parse(input_1)
    subtitles2 = parser.parse(input_2)
    