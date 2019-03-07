#!/usr/bin/env python3
"""Cleans and processes the data ready for model fitting"""
__appname__ = "DataWrang.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Feb-2019"

## imports ##
import os
import scipy as sp
import pandas as pd
import re

## Functions ##

def Distance(origin, destination):
    """Distance - Get the distance in kilometers between two coordinates.

    :param origin: tuple of origin lat and long
    :param destination: tuple of destination lat and long
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = sp.radians(lat2 - lat1)
    dlon = sp.radians(lon2 - lon1)
    a = sp.sin(dlat / 2) * sp.sin(dlat / 2) + sp.cos(sp.radians(lat1)) \
        * sp.cos(sp.radians(lat2)) * sp.sin(dlon / 2) * sp.sin(dlon / 2)
    c = 2 * sp.arctan2(sp.sqrt(a), sp.sqrt(1 - a))
    d = radius * c

    return d

def CombineCsvData():
    """CombineCsvData - Import the data from seperate files into a single
    pandas dataframe"""
    # use a regular expression to get the two input files from Data directory
    regex = r"(ROT2.csv).+?(ZSL2.csv)"
    csv_files = list(re.findall(regex, " ".join(os.listdir("../Data")))[0])
    # read the csv files into pandas dataframes
    csv_data = [pd.read_csv("../Data/{}".format(x)) for x in csv_files]
    # combine the two data frames into a single dataframe
    data = pd.concat(csv_data)
    return data

def FormatDataframe(data):
    """FormatDataframe - Convert columns to the correct format

    :param data: dataframe to clean up.
    """
    # remane columns headings and set data types
    data.rename(columns={"X" : "Destination_Latitude",
                         "Y" : "Destination_Longitude"},
                         inplace = True)
    data.Destination_Latitude.astype("float64")
    data.Destination_Longitude.astype("float64")
    data.Date = pd.to_datetime(data.Date, format = "%d/%m/%Y")

    return data

def CalculateDistance(data):
    """CalculateDistance - Gets the distance in KM between data coordinates

    :param data: the dataframe with coordinates in.
    """
    # extract the hive coordinates from the metadata file and put them in the
    # dataframe
    hive_coord = pd.read_csv("../Data/HiveMetaData.csv")
    data["Hive_Latitude"] = sp.where(data.Location == "ZSL",
            hive_coord.Latitude[hive_coord.Hive == "ZSL"],
            hive_coord.Latitude[hive_coord.Hive == "ROT"])
    data["Hive_Longitude"] = sp.where(data.Location == "ZSL",
            hive_coord.Longitude[hive_coord.Hive == "ZSL"],
            hive_coord.Longitude[hive_coord.Hive == "ROT"])
    # Calculate the distance in Km using the coordinates in the dataframe.
    data["Distance_Km"] = Distance((data.Hive_Latitude,
                                    data.Hive_Longitude),
                                   (data.Destination_Latitude,
                                    data.Destination_Longitude))
    return data

def CreateMetaData(data):
    """CreateMetaData - Creates a meta data file for the given dataframe.

    :param data: the dataframe given
    """
    metadata = pd.DataFrame(columns = ["ColumnName", "Description", "DataType"])
    descriptions = ["Location of the source Hive",
                    "The date the observations were made",
                    "Longitude coordinate of foraging destination",
                    "Latitude coordinate of formaging destination",
                    "Latitude coordinate of hive location",
                    "Longitude coordinate of hive location",
                    "Ecludian distance in Kilometers between hive and destination"]
    datatype = ["String", "DateTime object", "float64", "float64", "float64",
            "float64", "float64"]
    metadata.ColumnName = list(data)
    metadata.Description = descriptions
    metadata.DataType = datatype

    return metadata


def main():
    """main - The program main function"""
    # load the data into a single pandas dataframe
    data = CombineCsvData()
    # clean up the data
    data = FormatDataframe(data)
    # calculate the foraging distance in Km
    data = CalculateDistance(data)
    # save the output to a csv file
    data.to_csv("../Data/Distances.csv", index = False)
    # create the metadata file
    metadata = CreateMetaData(data)
    # save the metadata output to csv
    metadata.to_csv("../Data/Distances_MetaData.csv", index = False)


if __name__ == "__main__":
    main()
