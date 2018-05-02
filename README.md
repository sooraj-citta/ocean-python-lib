# Ocean-Python-Lib
**citta** - Python library (under progress) for the [ocean protocol](https://oceanprotocol.com/) that process the data &amp; give various parameters to the end users. 
By getting to know the various parameters the users can gauge the quality of the data and then decide if they want to use it for their tasks. The citta library contains a file conversion module which currently has a **_csv to json_** & **_json to csv_** convertor module. The output so created will be stored in the source location itself with the same name as the source file.
```
citta
    └── file_convert
        ├── csv2json
        ├── csv_to_json
        └── json2csv
```
## Dependencies
Includes PrettyTable, easygui, numpy & pandas which are automatically installed while building or installing the library. The library is based on python 3.5.

## Installation
#### Via building library
* Clone the folder using git clone or download.
* Within the folder run the following command `python setup.py sdist`.
* Open the **dist** folder and run pip install from there. This will install the library locally. 
* You can also directly `pip install citta-1.1.tar.gz` file in the home folder if you want to avoid building from scratch.
#### Via testPypi
* ~~Use this command to install the library from testPypi directly `pip install --index-url https://test.pypi.org/simple/  citta`~~
## Contents
The **_csv to json_** modules take an input csv file and creates json file of required format depending on the function used. 
* csv2json output :
```
[{
  "Id": "100",
  "number": "1",
  "Date": "2018/01/01"
  },
  {
   "Id": "101",
   "number": "2",
   "Date": "2018/02/02"
  }]
```
* csv_to_json output :
```
{
  "Id": {"100", "101", "103", "104"},
   "number": {"1", "2","3", "4"},
   "Date": {"2018/01/01", "2018/02/02"}
}
```
The **_json to csv_** module can handle 3 different types of json as input. 
```
Simple json                          Json with multiple values
-----------                          -------------------------
{                                    {
 "last_name" : "Shark",                "first_name" : ["Sammy","dammy"],
 "location" : "Ocean"                  "last_name" : "Shark",
}                                      "online" : true,
                                       "followers" : [987,1000,259,25687,741] 
                                      }
Multiple arrays
---------------
[{"HR": "100","Time": "2017/01/01"},
 {"HR": "100","Time": "2017/01/02"}]  
```

## Example
```
from citta import file_convert
import easygui

location = easygui.fileopenbox()
file_convert.json2csv(location)
file_convert.csv2json(location)
file_convert.csv_to_json(location)
```
## Maintainers
This repo is updated and maintained by [Hisham](https://github.com/Hisham-PM) and [Deepika](https://github.com/17Deepika). Our company [website](https://www.citta.ai/).
