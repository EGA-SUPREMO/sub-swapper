from pysubparser import parser

def read_subs(input_1: str, input_2: str):
    return list(parser.parse(input_1)), list(parser.parse(input_2))

subtitles1, subtitles2 = read_subs("subs_en.srt", "subs_indo.srt")

print(subtitles1[0])
print(subtitles2[0])