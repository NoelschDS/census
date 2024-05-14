# -*- coding: utf-8 -*-
"""Project_data_collection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cG-xCj68l8tkmkHSz_QNFPWy3-CWz5x5
"""

import requests
import json


def make_call(year, mon, vars, key="&key=3a9f008a5485a325fc9a459873d07294a071e184"):
  #https://api.census.gov/data/2024/cps/basic/jan?get=PEMLR,PWSSWGT,PEMARITL&for=state:01&PEEDUCA=39
  url = "https://api.census.gov/data/"
  year = f"{year}"
  mon = f"{mon}"
  dataset = "/cps/basic/"
  get = "?get="
  vars = f"{vars}"
  predicate = "&for="
  geog =  "state"

  return url + year + dataset + mon + get + vars + predicate + geog + key

#Variable list
#STATE - FIPS STATE Code
#GTCBASZ - Metropolitan Statistical Area Size
#GTMETSTA - Metropolitan Status
#PRTAGE - Demographics - age topcoded at 85, 90 or 80 (see full description)
#PEDISDRS - Disability - Difficulty dressing or bathing
#PEDISEAR - Disability - Deaf or serious difficulty hearing
#PEDISEYE - Disability - Blind or difficulty seeing even with glasses
#PEDISOUT - Disability - Difficulty doing errands
#PEDISPHY - Disability - Difficulty walking or climbing stairs
#PEDISREM - Disability - Difficulty remembering or making decisions
#HEHOUSUT - Household-type of living quarters
#HETENURE - Household-own/rent living quarters
#HRNUMHOU - Household-total # of members
#HRHTYPE - Household-type of family/single individual
#CBSA - #HRHTYPE - Household-type of family/single individual
vars = "CBSA,GTMETSTA,GTCBSASZ,PRTAGE,PEDISDRS,PEDISEAR,PEDISEYE,PEDISOUT,PEDISPHY,PEDISREM,HEHOUSUT,HETENURE,HRNUMHOU,HRHTYPE"
var_list = vars.split(",")

dat = requests.get(make_call(2024, "mar", vars)).text

#Investigate list of results
results = json.loads(dat)

import pandas as pd

df=pd.DataFrame(results[1:], columns=results[0])

#Get Dictionary for vars
def retrieve_dictionaries(year, mon, vars, key="&key=3a9f008a5485a325fc9a459873d07294a071e184"):
  #https://api.census.gov/data/2024/cps/basic/mar/variables/CBSA.json
  url = "https://api.census.gov/data/"
  year = f"{year}"
  dataset = "/cps/basic/"
  mon = f"{mon}"
  variables = "/variables/"
  vars = f"{vars}"
  end = ".json"

  return url + year + dataset + mon + variables + vars + end

def list_dictionaries(year, mon, var_list):
  var_map = {}
  for var in var_list:
    var_map[var] = var
    try:
      if "range" in json.loads(requests.get(retrieve_dictionaries(year, mon, var)).text)['values'].keys():
        var_map[var] = json.loads(requests.get(retrieve_dictionaries(year, mon, var)).text)['values']['range']
      else:
        var_map[var] = json.loads(requests.get(retrieve_dictionaries(year, mon, var)).text)['values']['item']
    except:
      var_map[var] = "Dictionary Not Found"
  return var_map

ref = list_dictionaries(2024, "mar", var_list)

#Map values from df to dictionary values
df_values = df.copy()
for col in df.columns:
  try:
    df_values[col] = df[col].map(ref[col])
  except:
    pass

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

for year in years:
  locals()[f'dat{year}'] = requests.get(make_call(year, "mar", vars)).text

results2010 = json.loads(dat2010)

results2011 = json.loads(dat2011)
results2012 = json.loads(dat2012)
results2013 = json.loads(dat2013)
results2014 = json.loads(dat2014)
results2015 = json.loads(dat2015)
results2016 = json.loads(dat2016)
results2017 = json.loads(dat2017)
results2018 = json.loads(dat2018)
results2019 = json.loads(dat2019)
results2020 = json.loads(dat2020)
results2021 = json.loads(dat2021)
results2022 = json.loads(dat2022)
results2023 = json.loads(dat2023)

results2010[0]

df2010 = pd.DataFrame(results2010[1:], columns=results2010[0])

df2011 = pd.DataFrame(results2011[1:], columns=results2011[0])
df2012 = pd.DataFrame(results2012[1:], columns=results2012[0])
df2013 = pd.DataFrame(results2013[1:], columns=results2013[0])
df2014 = pd.DataFrame(results2014[1:], columns=results2014[0])
df2015 = pd.DataFrame(results2015[1:], columns=results2015[0])
df2016 = pd.DataFrame(results2016[1:], columns=results2016[0])
df2017 = pd.DataFrame(results2017[1:], columns=results2017[0])
df2018 = pd.DataFrame(results2018[1:], columns=results2018[0])
df2019 = pd.DataFrame(results2019[1:], columns=results2019[0])
df2020 = pd.DataFrame(results2020[1:], columns=results2020[0])
df2021 = pd.DataFrame(results2021[1:], columns=results2021[0])
df2022 = pd.DataFrame(results2022[1:], columns=results2022[0])
df2023 = pd.DataFrame(results2023[1:], columns=results2023[0])

ref2010 = list_dictionaries(2010, "mar", var_list)

ref2011 = list_dictionaries(2011, "mar", var_list)
ref2012 = list_dictionaries(2012, "mar", var_list)
ref2013 = list_dictionaries(2013, "mar", var_list)
ref2014 = list_dictionaries(2014, "mar", var_list)
ref2015 = list_dictionaries(2015, "mar", var_list)
ref2016 = list_dictionaries(2016, "mar", var_list)
ref2017 = list_dictionaries(2017, "mar", var_list)
ref2018 = list_dictionaries(2018, "mar", var_list)
ref2019 = list_dictionaries(2019, "mar", var_list)
ref2020 = list_dictionaries(2020, "mar", var_list)
ref2021 = list_dictionaries(2021, "mar", var_list)
ref2022 = list_dictionaries(2022, "mar", var_list)
ref2023 = list_dictionaries(2023, "mar", var_list)

df_values2010 = df2010.copy()
for col in df2010.columns:
  try:
    df_values2010[col] = df2010[col].map(ref2010[col])
  except:
    pass

df_values2011 = df2011.copy()
for col in df2011.columns:
  try:
    df_values2011[col] = df2011[col].map(ref2011[col])
  except:
    pass
df_values2012 = df2012.copy()
for col in df2012.columns:
  try:
    df_values2012[col] = df2012[col].map(ref2012[col])
  except:
    pass
df_values2013 = df2013.copy()
for col in df2013.columns:
  try:
    df_values2013[col] = df2013[col].map(ref2013[col])
  except:
    pass
df_values2014 = df2014.copy()
for col in df2014.columns:
  try:
    df_values2014[col] = df2014[col].map(ref2014[col])
  except:
    pass
df_values2015 = df2015.copy()
for col in df2015.columns:
  try:
    df_values2015[col] = df2015[col].map(ref2015[col])
  except:
    pass
df_values2016 = df2016.copy()
for col in df2016.columns:
  try:
    df_values2016[col] = df2016[col].map(ref2016[col])
  except:
    pass
df_values2017 = df2017.copy()
for col in df2017.columns:
  try:
    df_values2017[col] = df2017[col].map(ref2017[col])
  except:
    pass
df_values2018 = df2018.copy()
for col in df2018.columns:
  try:
    df_values2018[col] = df2018[col].map(ref2018[col])
  except:
    pass
df_values2019 = df2019.copy()
for col in df2019.columns:
  try:
    df_values2019[col] = df2019[col].map(ref2019[col])
  except:
    pass
df_values2020 = df2020.copy()
for col in df2020.columns:
  try:
    df_values2020[col] = df2020[col].map(ref2020[col])
  except:
    pass
df_values2021 = df2021.copy()
for col in df2021.columns:
  try:
    df_values2021[col] = df2021[col].map(ref2021[col])
  except:
    pass
df_values2022 = df2022.copy()
for col in df2022.columns:
  try:
    df_values2022[col] = df2022[col].map(ref2022[col])
  except:
    pass
df_values2023 = df2023.copy()
for col in df2023.columns:
  try:
    df_values2023[col] = df2023[col].map(ref2023[col])
  except:
    pass

df_values2010["year"]=2010
df_values2011["year"]=2011
df_values2012["year"]=2012
df_values2013["year"]=2013
df_values2014["year"]=2014
df_values2015["year"]=2015
df_values2016["year"]=2016
df_values2017["year"]=2017
df_values2018["year"]=2018
df_values2019["year"]=2019
df_values2020["year"]=2020
df_values2021["year"]=2021
df_values2022["year"]=2022
df_values2023["year"]=2023

frames=[df_values2010, df_values2011, df_values2012, df_values2013, df_values2014, df_values2015, df_values2016, df_values2017, df_values2018, df_values2019, df_values2020, df_values2021, df_values2022, df_values2023]

df_from_2010_to_2023 = pd.concat(frames)

df_from_2010_to_2023.to_csv("df_from_2010_to_2023.csv")

df_values.to_csv("df_2024.csv")