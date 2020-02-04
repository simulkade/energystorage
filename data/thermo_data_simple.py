# a simple module that reads the physical data of a limited number
# of pure components


import pandas as pd
import numpy as np
import os, sys
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

thermo_data = pd.read_csv(os.path.join(dir_path, 'thermo_data.csv'))
available_property = list(thermo_data)[1:]

def data_file():
    return thermo_data

def get_data_by_formula(formula):
    return thermo_data.loc[thermo_data['formula'].isin(formula)]

def get_data_by_name(comp_names):
    return thermo_data.loc[thermo_data['name'].isin(comp_names)]

def get_h_form(comp_name):
    return float(thermo_data.loc[(thermo_data['name']==comp_name) | (thermo_data['formula']==comp_name)]['dh_form'])

def get_property(comp_name, prop_name):
    return float(thermo_data.loc[(thermo_data['name']==comp_name) | (thermo_data['formula']==comp_name)][prop_name])

def print_available_property():
    print(available_property)