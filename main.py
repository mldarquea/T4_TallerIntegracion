from pandas.core.frame import DataFrame
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe

##########################################
#############API -> xml -> DF#############

############Uruguay URY###################
url = 'http://tarea-4.2021-1.tallerdeintegracion.cl/gho_URY.xml'
response = requests.get(url)
string_xml = response.content
tree = ET.fromstring(string_xml)
i=0
gho=[]
dict_atributos = {}
for elem in tree: #####DATA
    if list(elem):#####FACT
        dict_mijo = {}
        for mijo in list(elem):
            if mijo.tag in ['GHO','SEX','COUNTRY','YEAR','GHECAUSES','AGEGROUP','Display','Numeric','Low','High']:
                dict_mijo[mijo.tag] = mijo.text
            dict_atributos[i] = dict_mijo
    i+=1
df_uruguay = pd.DataFrame.from_dict(dict_atributos, orient='index')
gho_deseados = ['Number of deaths','Number of infant deaths','Number of under-five deaths','Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)','Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)','Estimates of number of homicides','Crude suicide rates (per 100 000 population)','Mortality rate attributed to unintentional poisoning (per 100 000 population)','Number of deaths attributed to non-communicable diseases, by type of disease and sex',\
'Estimated road traffic death rate (per 100 000 population)','Estimated number of road traffic deaths','Mean BMI (kg/m&#xb2;) (crude estimate)','Mean BMI (kg/m&#xb2;) (age-standardized estimate)','Prevalence of obesity among adults, BMI &GreaterEqual; 30 (age-standardized estimate) (%)', 'Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)', 'Prevalence of overweight among adults, BMI &GreaterEqual; 25 (age-standardized estimate) (%)',\
'Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)', 'Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)', 'Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)', 'Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)', 'Estimate of daily cigarette smoking prevalence (%)',\
'Estimate of daily tobacco smoking prevalence (%)', 'Estimate of current cigarette smoking prevalence (%)', 'Estimate of current tobacco smoking prevalence (%)', 'Mean systolic blood pressure (crude estimate)', 'Mean fasting blood glucose (mmol/l) (crude estimate)', 'Mean Total Cholesterol (crude estimate)']
df_uruguay_deseados = df_uruguay.loc[df_uruguay['GHO'].isin(gho_deseados)]
print(df_uruguay_deseados)
#comprobar_categorias = df_uruguay_deseados.groupby('GHO').count()
#print(comprobar_categorias, "Comprobar n° de categorías#############")
#print(gho)

############Alemania DEU##################
url = 'http://tarea-4.2021-1.tallerdeintegracion.cl/gho_DEU.xml'
response = requests.get(url)
string_xml = response.content
tree = ET.fromstring(string_xml)
i=0
gho=[]
dict_atributos = {}
for elem in tree: #####DATA
    if list(elem):#####FACT
        dict_mijo = {}
        for mijo in list(elem):
            if mijo.tag in ['GHO','SEX','COUNTRY','YEAR','GHECAUSES','AGEGROUP','Display','Numeric','Low','High']:
                dict_mijo[mijo.tag] = mijo.text
            dict_atributos[i] = dict_mijo
    i+=1
df_alemania = pd.DataFrame.from_dict(dict_atributos, orient='index')
gho_deseados = ['Number of deaths','Number of infant deaths','Number of under-five deaths','Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)','Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)','Estimates of number of homicides','Crude suicide rates (per 100 000 population)','Mortality rate attributed to unintentional poisoning (per 100 000 population)','Number of deaths attributed to non-communicable diseases, by type of disease and sex',\
'Estimated road traffic death rate (per 100 000 population)','Estimated number of road traffic deaths','Mean BMI (kg/m&#xb2;) (crude estimate)','Mean BMI (kg/m&#xb2;) (age-standardized estimate)','Prevalence of obesity among adults, BMI &GreaterEqual; 30 (age-standardized estimate) (%)', 'Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)', 'Prevalence of overweight among adults, BMI &GreaterEqual; 25 (age-standardized estimate) (%)',\
'Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)', 'Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)', 'Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)', 'Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)', 'Estimate of daily cigarette smoking prevalence (%)',\
'Estimate of daily tobacco smoking prevalence (%)', 'Estimate of current cigarette smoking prevalence (%)', 'Estimate of current tobacco smoking prevalence (%)', 'Mean systolic blood pressure (crude estimate)', 'Mean fasting blood glucose (mmol/l) (crude estimate)', 'Mean Total Cholesterol (crude estimate)']
df_alemania_deseados = df_alemania.loc[df_alemania['GHO'].isin(gho_deseados)]
#print(df_alemania_deseados)
#comprobar_categorias = df_alemania_deseados.groupby('GHO').count()
#print(comprobar_categorias, "Comprobar n° de categorías#############")

############Reino Unido GBR##################
url = 'http://tarea-4.2021-1.tallerdeintegracion.cl/gho_GBR.xml'
response = requests.get(url)
string_xml = response.content
tree = ET.fromstring(string_xml)
i=0
dict_atributos = {}
for elem in tree: #####DATA
    if list(elem):#####FACT
        dict_mijo = {}
        for mijo in list(elem):
            if mijo.tag in ['GHO','SEX','COUNTRY','YEAR','GHECAUSES','AGEGROUP','Display','Numeric','Low','High']:
                dict_mijo[mijo.tag] = mijo.text
            dict_atributos[i] = dict_mijo
    i+=1
df_gran_bre = pd.DataFrame.from_dict(dict_atributos, orient='index')
gho_deseados = ['Number of deaths','Number of infant deaths','Number of under-five deaths','Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)','Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)','Estimates of number of homicides','Crude suicide rates (per 100 000 population)','Mortality rate attributed to unintentional poisoning (per 100 000 population)','Number of deaths attributed to non-communicable diseases, by type of disease and sex',\
'Estimated road traffic death rate (per 100 000 population)','Estimated number of road traffic deaths','Mean BMI (kg/m&#xb2;) (crude estimate)','Mean BMI (kg/m&#xb2;) (age-standardized estimate)','Prevalence of obesity among adults, BMI &GreaterEqual; 30 (age-standardized estimate) (%)', 'Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)', 'Prevalence of overweight among adults, BMI &GreaterEqual; 25 (age-standardized estimate) (%)',\
'Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)', 'Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)', 'Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)', 'Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)', 'Estimate of daily cigarette smoking prevalence (%)',\
'Estimate of daily tobacco smoking prevalence (%)', 'Estimate of current cigarette smoking prevalence (%)', 'Estimate of current tobacco smoking prevalence (%)', 'Mean systolic blood pressure (crude estimate)', 'Mean fasting blood glucose (mmol/l) (crude estimate)', 'Mean Total Cholesterol (crude estimate)']
df_gran_bre_deseados = df_gran_bre.loc[df_gran_bre['GHO'].isin(gho_deseados)]
#print(df_gran_bre_deseados)
#comprobar_categorias = df_gran_bre_deseados.groupby('GHO').count()
#print(comprobar_categorias, "Comprobar n° de categorías#############")

############Ucrania UKR##################
url = 'http://tarea-4.2021-1.tallerdeintegracion.cl/gho_UKR.xml'
response = requests.get(url)
string_xml = response.content
tree = ET.fromstring(string_xml)
i=0
dict_atributos = {}
for elem in tree: #####DATA
    if list(elem):#####FACT
        dict_mijo = {}
        for mijo in list(elem):
            if mijo.tag in ['GHO','SEX','COUNTRY','YEAR','GHECAUSES','AGEGROUP','Display','Numeric','Low','High']:
                dict_mijo[mijo.tag] = mijo.text
            dict_atributos[i] = dict_mijo
    i+=1
df_ucrania = pd.DataFrame.from_dict(dict_atributos, orient='index')
gho_deseados = ['Number of deaths','Number of infant deaths','Number of under-five deaths','Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)','Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)','Estimates of number of homicides','Crude suicide rates (per 100 000 population)','Mortality rate attributed to unintentional poisoning (per 100 000 population)','Number of deaths attributed to non-communicable diseases, by type of disease and sex',\
'Estimated road traffic death rate (per 100 000 population)','Estimated number of road traffic deaths','Mean BMI (kg/m&#xb2;) (crude estimate)','Mean BMI (kg/m&#xb2;) (age-standardized estimate)','Prevalence of obesity among adults, BMI &GreaterEqual; 30 (age-standardized estimate) (%)', 'Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)', 'Prevalence of overweight among adults, BMI &GreaterEqual; 25 (age-standardized estimate) (%)',\
'Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)', 'Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)', 'Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)', 'Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)', 'Estimate of daily cigarette smoking prevalence (%)',\
'Estimate of daily tobacco smoking prevalence (%)', 'Estimate of current cigarette smoking prevalence (%)', 'Estimate of current tobacco smoking prevalence (%)', 'Mean systolic blood pressure (crude estimate)', 'Mean fasting blood glucose (mmol/l) (crude estimate)', 'Mean Total Cholesterol (crude estimate)']
df_ucrania_deseados = df_ucrania.loc[df_ucrania['GHO'].isin(gho_deseados)]
#print(df_ucrania_deseados)
#comprobar_categorias = df_ucrania_deseados.groupby('GHO').count()
#print(comprobar_categorias, "Comprobar n° de categorías#############")

############Suiza CHE##################
url = 'http://tarea-4.2021-1.tallerdeintegracion.cl/gho_CHE.xml'
response = requests.get(url)
string_xml = response.content
tree = ET.fromstring(string_xml)
i=0
dict_atributos = {}
for elem in tree: #####DATA
    if list(elem):#####FACT
        dict_mijo = {}
        for mijo in list(elem):
            if mijo.tag in ['GHO','SEX','COUNTRY','YEAR','GHECAUSES','AGEGROUP','Display','Numeric','Low','High']:
                dict_mijo[mijo.tag] = mijo.text
            dict_atributos[i] = dict_mijo
    i+=1
df_suiza = pd.DataFrame.from_dict(dict_atributos, orient='index')
gho_deseados = ['Number of deaths','Number of infant deaths','Number of under-five deaths','Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)','Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)','Estimates of number of homicides','Crude suicide rates (per 100 000 population)','Mortality rate attributed to unintentional poisoning (per 100 000 population)','Number of deaths attributed to non-communicable diseases, by type of disease and sex',\
'Estimated road traffic death rate (per 100 000 population)','Estimated number of road traffic deaths','Mean BMI (kg/m&#xb2;) (crude estimate)','Mean BMI (kg/m&#xb2;) (age-standardized estimate)','Prevalence of obesity among adults, BMI &GreaterEqual; 30 (age-standardized estimate) (%)', 'Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)', 'Prevalence of overweight among adults, BMI &GreaterEqual; 25 (age-standardized estimate) (%)',\
'Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)', 'Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)', 'Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)', 'Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)', 'Estimate of daily cigarette smoking prevalence (%)',\
'Estimate of daily tobacco smoking prevalence (%)', 'Estimate of current cigarette smoking prevalence (%)', 'Estimate of current tobacco smoking prevalence (%)', 'Mean systolic blood pressure (crude estimate)', 'Mean fasting blood glucose (mmol/l) (crude estimate)', 'Mean Total Cholesterol (crude estimate)']
df_suiza_deseados = df_suiza.loc[df_suiza['GHO'].isin(gho_deseados)]
#print(df_suiza_deseados)

############China CHN##################
url = 'http://tarea-4.2021-1.tallerdeintegracion.cl/gho_CHN.xml'
response = requests.get(url)
string_xml = response.content
tree = ET.fromstring(string_xml)
i=0
dict_atributos = {}
for elem in tree: #####DATA
    if list(elem):#####FACT
        dict_mijo = {}
        for mijo in list(elem):
            if mijo.tag in ['GHO','SEX','COUNTRY','YEAR','GHECAUSES','AGEGROUP','Display','Numeric','Low','High']:
                dict_mijo[mijo.tag] = mijo.text
            dict_atributos[i] = dict_mijo
    i+=1
df_china = pd.DataFrame.from_dict(dict_atributos, orient='index')
gho_deseados = ['Number of deaths','Number of infant deaths','Number of under-five deaths','Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)','Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)','Estimates of number of homicides','Crude suicide rates (per 100 000 population)','Mortality rate attributed to unintentional poisoning (per 100 000 population)','Number of deaths attributed to non-communicable diseases, by type of disease and sex',\
'Estimated road traffic death rate (per 100 000 population)','Estimated number of road traffic deaths','Mean BMI (kg/m&#xb2;) (crude estimate)','Mean BMI (kg/m&#xb2;) (age-standardized estimate)','Prevalence of obesity among adults, BMI &GreaterEqual; 30 (age-standardized estimate) (%)', 'Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)', 'Prevalence of overweight among adults, BMI &GreaterEqual; 25 (age-standardized estimate) (%)',\
'Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)', 'Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)', 'Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)', 'Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)', 'Estimate of daily cigarette smoking prevalence (%)',\
'Estimate of daily tobacco smoking prevalence (%)', 'Estimate of current cigarette smoking prevalence (%)', 'Estimate of current tobacco smoking prevalence (%)', 'Mean systolic blood pressure (crude estimate)', 'Mean fasting blood glucose (mmol/l) (crude estimate)', 'Mean Total Cholesterol (crude estimate)']
df_china_deseados = df_china.loc[df_china['GHO'].isin(gho_deseados)]
print(df_china_deseados)

gc = gspread.service_account(filename='###')
sh = gc.open_by_key('###')

# ########## Primera hoja ~ df de todos los países juntos
# df_paises_juntos = pd.concat([df_uruguay_deseados,df_alemania_deseados,df_gran_bre_deseados,df_ucrania_deseados,df_suiza_deseados, df_china_deseados])
# worksheet_juntos = sh.get_worksheet(0)
# set_with_dataframe(worksheet_juntos,df_paises_juntos)