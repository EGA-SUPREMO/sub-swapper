import subprocess

def extract_subs_ffmpeg(input_file, output_file):
    # Run ffmpeg command to extract subtitles
    cmd = [
        'ffmpeg',
        '-i', input_file,
        '-c', 'copy',
        output_file
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"Subtitles extracted successfully to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error extracting subtitles: {e}")
        print(e.stderr)


# Example usage
input_file = 'scot.mkv'
output_file = 'output_subtitles.ass'  # You can change the extension based on the subtitle format you want

extract_subs_ffmpeg(input_file, output_file)
 
