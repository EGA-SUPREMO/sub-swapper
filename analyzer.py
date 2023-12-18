from pysubparser import parser

def read_subs(input_1: str, input_2: str):
    return parser.parse(input_1), parser.parse(input_2)
    

subtitles1, subtitles2 = read_subs("subs_en.srt", "subs_indo.srt")
for subtitle in subtitles1:
    print(subtitle.text)
print(subtitles1)
print(subtitles2)