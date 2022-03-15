"""
This module aggregates the most frequently used data
pre-processing functions and provides methods for running them
automatically.
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns
import scipy
from scipy import stats
from statistics import mean
#Main method for calling dataset structural check functions
def structureCheck(df):
    print("Please see below the structural parameters of the dataset.")
    print()
    print("Missing rows\n")
    print(rowMissing(df))
    print()
    print("Missing values\n")
    print(misCount(df))
    print()
    print("Data types\n")
    print(dataTypes(df))

#Missing row identification

def rowMissing (df):
    #Total rows
    missing_rows = []
    count = 0
    length = len(df.columns)
    for i in df.index:
        for e in df.columns:
            #print(type(df[e][i]))
            if pd.isnull(df[e][i]):
                count +=1
        if count == length:
            missing_rows.append(i)
        count = 0
    if len(missing_rows)>0:
        print("Attention, missing rows with following indexes have been detected:")
        for i in missing_rows:
            print(i)
    return missing_rows

def misCount(dataset):
    return dataset.isnull().sum()

def dataTypes(dataset):
    return dataset.dtypes

#---------------Input error checks------------------

#Outlier detection
def outlDet(dframe, field):
    zsc = np.abs(scipy.stats.zscore(dframe[f"{field}"]))#Z-scores for each value.
    count = 0
    for i in zsc:
        if i >= 3:
            count += 1
    print(f"{field}:{count}")
#Outlier removal
def outlRem(dframe, field):
    zsc = np.abs(scipy.stats.zscore(dframe[f"{field}"]))#Z-scores for each value.
    filt_lst = []# Will hold the filtered values.
    index = 0 #Index to help reference the zsc list.
    for i in dframe[f"{field}"]:
        if zsc[index] <3: #If the corresponding z-score is less than 3, the value (i) is appended to the filtered list.
            filt_lst.append(i)
        index +=1
    return filt_lst
#Main method for input error detection
def contentCheck(dataFr, unique =[], repeating =[]):
    """
    This function identifies input errors in a dataset
    by checking the outliers and categorical value distribution.
    """
    classes = ["<class 'numpy.float64'>", "<class 'numpy.int64'>", "<class 'numpy.integer'>","<class 'numpy.unsigned integer'>"]

    print("-----Outlier count-----\n")
    for column in dataFr:
        if str(type(dataFr[column][1])) in classes:
            if all(x not in column for x in ['id', 'ID', 'Id', 'iD']):
                outlDet(dataFr, column)
                fig=mpl.pyplot.figure()
                #sns.boxplot(x=dataFr[column],ax=fig.add_axes([0, 0, 1.5, 1]))

    if len(unique)!=0:
        print("\n-----Categorical value check-----\n||Unique value columns\n")
        for column in unique:
            fig=mpl.pyplot.figure()
            print(f"\nColumn:{column}\nValue distribution:\n", mean(dataFr[column].value_counts()))

    if len(repeating)!=0:
        print("\n-----Categorical value check-----\n||Repeating values\n")
        for column in repeating:
            print(dataFr[column].value_counts(),"\n")
