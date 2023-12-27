[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
# Sub Swapper
Learn languages the easy way.

---
Sub Swapper is a Python script designed to swap a specified percentage of subtitles between two subtitle files. It also takes into account a specified grade level to intelligently guess whether the viewer would likely understand each sentence.

The script is designed to enhance language learning by making it easier and more enjoyable to practice new languages. The recommended usage is to watch TV series or films dubbed in the target language you want to learn, with subtitles comprising 80% in your native language and 20% in the language of the dub.

## Features
* Swap a percentage of subtitles between two subtitle files.
* Set a specific grade reading level to ensure you will understand the subtitles.
* Specify input and output paths for subtitle files.

## Usage
### Command-line Arguments
* `-p`: Specify the percentage of subtitles to be swapped.
* `-o`: Specify the output path for the swapped subtitles.
* `-g`: Specify the grade level for reading comprehension.
* `-i`: Specify two paths for input subtitle files.
### Example
```sh
python3 -m subs_swapper.main -i 'subs_english.srt' 'subs_espanish.srt' -p 20 -g 3 -o output.srt
```

This command will swap 20% of subtitles between `subs_english.srt` and `subs_spanish.srt`, considering a grade level of 3, and save the result in `output.srt`.
### Running Tests
To run the tests, use the following command:

```sh
python3 -m tests.test_compare_subs
```
### Limitations
* Both subtitles need to be synchronized
* Remember that expressions and idioms might affect understanding, even though they may appear to has a low grading level

## How to Contribute
We welcome contributions! Feel free to open issues, submit pull requests, or share your ideas.

## License
This project is licensed under the [GNU General Public License (GPL) version 3](LICENSE)
