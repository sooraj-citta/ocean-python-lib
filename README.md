# Ocean-Python-Lib
Python library(under development) for the ocean protocol that process the data &amp; give various parameters to the end users. 
By getting to know the various parameters the users can gauge the quality of the data and then decide if they want to use if for their tasks.

## Dependencies
```
pip install PrettyTable
pip install easygui
```
## Example
```
from citta import check
import easygui

location = easygui.fileopenbox()
table=check.summary(location)
```
