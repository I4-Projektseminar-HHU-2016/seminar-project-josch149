# Weatherdata and weatherrules analysis with Python

My project-code will be able to analyze weather data, to proof if weather rules are true or false, for the vicinity of Duesseldorf.

## Features ##

- [x] read-in-function for weather datas form CSV-files, provided by the DWD ("Deutscher Wetterdienst", weatherservice of germany)
- [x] generate-function for specific date intervals for each weatherrule
- [x] draw-faction for additive charts, to visualize each parts result of a weather rule
- [x] rating-function to rate the meaningfulness of each weather rule
- [x] draw-function for pie charts, to visualize the meaningfulness of each weather rule

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisities

- This Python-code was written and tested with Python 2.7.11 - Anaconda 4.0.0 (64-bit).
  You can get this form https://www.continuum.io/downloads .
  
Optional:
- Editor like "Geany",
  you can get "Geany" from https://www.geany.org/ .

### Installing

You need a Python 2.7 distribution, preferably Anaconda 4.0.0, to run this script.

If you have it installed, you can continue as followed:

At first you have to download the "wetter.py" file, and the "CSVs" folder.

Now open the command line (CMD) and navigate to the folder, where the "wetter.py" and the "CSVs" folder are.

To navigate use "cd ..." as command.

`cd Downloads` will navigate to the folder "Downloads" in the current folder.

Since you have navigated to the folder with the "wetter.py" and the "CSVs" folder, you can run the script as follows:

`python wetter.py`

Finally the different charts should be shown successively.

Optional:

You can optional open the "wetter.py" file with an editor and run the Python-script (in "Geany" just press the "F5" button).


## Author

* **Joh. Christian Schade** - [I4-Projektseminar-HHU-2016/seminar-project-josch149](https://github.com/I4-Projektseminar-HHU-2016/seminar-project-josch149/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/I4-Projektseminar-HHU-2016/seminar-project-josch149/blob/master/LICENSE.md) file for details.

## Acknowledgments

* Weatherdata by Deutscher Wetterdienst (DWD)



*template inspired by [https://gist.github.com/PurpleBooth/109311bb0361f32d87a2](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)*
