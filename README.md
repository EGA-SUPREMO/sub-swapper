# Sub Swapper
Sub Swapper is a Python script designed to swap a specified percentage of subtitles between two subtitle files while considering a specified grade level for readability.

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

### Notes
Remember that expressions and idioms might affect understanding, even though they may appear to has a low grading level

### Limitations
* Both subtitles need to be synchronized

## How to Contribute
We welcome contributions! Feel free to open issues, submit pull requests, or share your ideas.

## License
This project is licensed under the [GNU General Public License (GPL) version 3](LICENSE)

Rememeber to put the program that I painfully made to mesauere the grade level reading, to try to guess whenever the viewer would understand that sentence

* poner pequenas lineas de texto donde uso el espanol como desmostracion de lo que seria usarlo en las pelis y asi, tratar de que aunque la persona no entienda, no importe, porque son lineas de relleno(como las lineas de spiderman, o el gato con botas)

contras
las expreciosnes pueden hace que uno no entineda a pesar ed que parezca que si, talvez anadir una opcion donde analiza los dialogos con los del mazo Neri, y agregarle un checkbox, si quiere swap con los subs en dialogos donde se cree que pueden ser expreciones
* dar de advertencia que los dos subs deben estar sincronizados, y que si necesita, que use cierto comando del pograma para hacerlo(bukan terbuat oleh aku, tapi jangan bilang itu di video)

Objetivo secundario
* dar instruciones de como ejecutar los tests(kalaupun tests tidak berhasil)
* anadir soporte para extenciones, ej language reactor, donde se agrega subtitulo ya cambiado para los que usan neftflix con esa extension, y la gente que no lo hacen con contenido descargado o para youtube