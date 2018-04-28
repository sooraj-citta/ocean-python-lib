#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: uvionics
Module name : File conversion

This module performs filetype conversion. This can facilite the user to convert
the file into the desired type either before or after the data analysis. 
As of now json->csv & csv->json are implemented.
"""

import csv
import json
import pandas as pd
import numpy as np

"""
The standard libraries that are needed to handle the file inputs are imported.
The global variable are also declared before the function declaration. 
"""
copy=[]
list_positions=[] 

"""
The name module is used to make function file callable.  
"""
def name(self):
    """Returns the file name."""
    return self.__name

def csv_to_json(filepath):
    """
    This function converts the csvfile into a json file . 
    Arguments:
         csv_file : The input csv file to be converted to json
    Returns:
         The function returns the json file in the location specified
    Example:
        csv_file = '/home/Desktop/asd.csv'
        save_path = '/home/Desktop/asd.json'
        csv_to_json(csv_file,save_path)
    Output File:
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
     
    """
    if(filepath.find('csv')!=-1):     
        try:
            old_name=filepath.split('/')[-1]
            new_name=old_name.replace('csv','json')
            save_path=filepath.replace(old_name,new_name)
        except:
            old_name=filepath.split("'\'")[-1]
            new_name=old_name.replace('csv','json')
            save_path=filepath.replace(old_name,new_name)
        with open(filepath, 'r') as f: # Open the csv file as readable
             # The csv file is read and mapped into dict
             d_reader = csv.DictReader(f) 
             data = [r for r in d_reader] 
             # The keys or the fieldnames are extracted
             # headers = d_reader.fieldnames
        with open(save_path,'w') as f1:
             json.dump(data, f1,indent = 4,separators=(',', ': '))
             f1.writelines('\n')
        print("Csv to json conversion successful !")
    else:
        print("Please input valid .csv files !")

def csv2json(filepath):
    """
    This function converts the csvfile into a json file.
    Arguments:
        csv_file : The input csv file to be converted to json.
        save_path : The output file to which the json is to be written
    Returns:
        The function returns the json file in the location specified
    Example:
        csv_file = '/home/Desktop/asd.csv'
        save_path = '/home/Desktop/dsa.json'
        csv_to_json(csv_file,save_path)
    Output File:
        {
          "Id": {"100", "101", "103", "104"},
           "number": {"1", "2","3", "4"},
           "Date": {"2018/01/01", "2018/02/02", "2018/03/03", "2018/04/04"}
        }
    
    """
    if(filepath.find('csv')!=-1): 
       #Read the csv file
        csvdata = pd.read_csv(filepath, sep = ",", header = 0, 
                              index_col = False)
        #   converting the csvfile into
        #   Dataframe
        csvfile = pd.DataFrame(csvdata)
        #   Converting the dataframe object into a matrix
        #   and take the transpose of the matrix
        df_tomat = csvfile.as_matrix()
        dftran = df_tomat.transpose()
        #   Converting the matrix back into a dataframe object
        df_again = pd.DataFrame(dftran)
        #   Convert the dataframe into json 
        #   Write the json file into the file location specified
        try:
            old_name=filepath.split('/')[-1]
            new_name=old_name.replace('csv','json')
            save_path=filepath.replace(old_name,new_name)
        except:
            old_name=filepath.split("'\'")[-1]
            new_name=old_name.replace('csv','json')
            save_path=filepath.replace(old_name,new_name)
        df_again.to_json(save_path, orient = "columns", date_format = "epoch", 
                         double_precision = 10, force_ascii = True, 
                         date_unit = "ms", default_handler = None)
        csvfile.to_json(save_path, orient = "columns", date_format = "epoch", 
                        double_precision = 10, force_ascii = True, 
                        date_unit = "ms", default_handler = None)
        print("Csv to json conversion successful !")
    else:
        print("Please input valid .csv files !")
        
def json2csv(filepath):
    """
    In the json2csv module, the required json file is opened & read using the 
    standard json load. The file can be selected using the another python 
    module "easygui" which provides the user with the gui to search & select
    the file.from json the key value pairs are extracted. The key form the 
    column names and the values forms the column values for the csv. The output
    will be saved in the position where the source file is residing. 
    Empty array "a" is declared for data storage during the json->csv 
    conversion.  
    """
    if(filepath.find('json')!=-1):
        a=[]
        try:
            with open(filepath,"r") as f:
                x=json.load(f)
                """
                The if module handles json formats like :
                 [{"HR": "100","Time": "2017/01/01"},
                 {"HR": "100","Time": "2017/01/02"}]
                
        
                The elif module is to handles json formats like :           
                   {"first_name" : ["Sammy","dammy"],
                     "last_name" : "Shark",
                      "online" : true,
                      "followers" : [987,1000,259,25687,741]     
                   }
                   
                Finally the else module to handle simple json formats like :
                    {
                    "last_name" : "Shark",
                    "location" : "Ocean"
                    }
                """
                if(type(x)==list):                
                    a.append(list(x[0].keys()))  
                    for i in range(1,len(x)):
                        a.append(list(x[i].values()))
        
                elif(any(isinstance(item,list)for item in list(x.values()))==True): 
                    copy=dict(x)
                    for key,value in list(x.items()):
                        if type(value)==list:
                            list_positions.append(key)
                            x[key]=np.array(value)
                            del x[key]
                            
                    out=dict((k, copy[k]) for k in list_positions)
                    df=pd.DataFrame.from_dict(out,orient='index')
                    df1=pd.DataFrame.from_dict(x,orient='index')
                    df1=df1.append(df)
                    a=df1.transpose()
                    
                else:
                    a.append(x.keys())          
                    a.append(x.values())
                    print("Json to csv conversion successful !")
            """
            The last block is used to create output filename and output path. 
            The output path will be same as that of the input location and 
            filename same as the input with the extension changed to .csv
            
            """ 
            try:
                old_name=filepath.split('/')[-1]
                new_name=old_name.replace('json','csv')
                save_path=filepath.replace(old_name,new_name)
            except:
                old_name=filepath.split("'\'")[-1]
                new_name=old_name.replace('json','csv')
                save_path=filepath.replace(old_name,new_name)
            
            if(type(a)==list):
                with open(save_path,"w") as f1:
                    writer = csv.writer(f1)
                    writer.writerows(a)
            else:
                a.to_csv(save_path,index=False)
        except:
            print("Input file json format is invalid !")
    else:
        print("Please input valid .json files !")

        
    
            