[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
# Sub Swapper
Learn languages the easy way.

---
Sub Swapper is a Python script designed to swap a specified percentage of subtitles between two subtitle files while considering a specified grade level to try to guess whenever the viewer would understand that sentence

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
`python3 -m subs_swapper.main -i 'subs_english.srt' 'subs_espanish.srt' -p 20 -g 3 -o output.srt`
This command will swap 20% of subtitles between `subs_english.srt` and `subs_spanish.srt`, considering a grade level of 3, and save the result in `output.srt`.
### Running Tests
To run the tests, use the following command:
`python3 -m tests.test_compare_subs`

### Notes
Remember that expressions and idioms might affect understanding, even though they may appear to has a low grading level

### Limitations
* Both subtitles need to be synchronized

## How to Contribute
We welcome contributions! Feel free to open issues, submit pull requests, or share your ideas.

## License
This project is licensed under the [GNU General Public License (GPL) version 3](LICENSE)


* poner pequenas lineas de texto donde uso el espanol como desmostracion de lo que seria usarlo en las pelis y asi, tratar de que aunque la persona no entienda, no importe, porque son lineas de relleno(como las lineas de spiderman, o el gato con botas)
