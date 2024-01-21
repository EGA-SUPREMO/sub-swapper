for i in {1,2,3,4,5,6,7,8,9,10,11,12}; do python3 -m subs_swapper.main -i "$i.srt" "$i.ass" -p 25 -g 5 -o out_$i.srt; done; 
