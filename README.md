# Ocean-Python-Lib
Python library (under progress by [citta](https://www.citta.ai/)) for the [ocean protocol](https://oceanprotocol.com/) that process the data &amp; give various parameters to the end users. 
By getting to know the various parameters the users can gauge the quality of the data and then decide if they want to use if for their tasks.

## Dependencies
These include PrettyTable, easygui & setuptools which is automatically installed while building or installing the library.

## Installation

After installing the dependacies, clone the repository and run the setup file using the following command.
```
python setup.py install
```
Now the package is ready to be used in any python program.
## Example
```
from citta import check
import easygui

location = easygui.fileopenbox()
table=check.summary(location)
```
## Maintainers

This repo is updated and maintained by [Hisham](https://github.com/Hisham-PM) and [Deepika](https://github.com/17Deepika).
