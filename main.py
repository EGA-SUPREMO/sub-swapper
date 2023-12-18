from pysubparser import parser
 

subtitles = parser.parse('./output_subtitles.srt')
#print(subtitles)
for subtitle in subtitles:
    print(subtitle.text)