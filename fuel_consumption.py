import pandas as pd
import numpy as np

EARTH_RADIUS_KM = 6371

def fuel_consumption(aircraft_type,ADEP_latitude_degree,ADEP_longitude,ADES_latitude_degree,ADES_longitude):
    fuel_consumption_data = pd.read_csv('C:/Users/anton/OneDrive - ISAE-SUPAERO/Documents/MES DOC/SUPAERO/4A/Domaine - ETE/projet ETE aviation/ac_model_coefficients.csv')
    aircraft_fuel_consumption_data = fuel_consumption_data[(fuel_consumption_data['ac_code_icao'] == aircraft_type)]
    ADEP_latitude_radian =  ADEP_latitude_degree*np.pi/180
    ADES_latitude_radian =  ADES_latitude_degree*np.pi/180
    delta_latitude_radian = (ADES_latitude_degree - ADEP_latitude_degree)*np.pi/180
    delta_longitude_radian = (ADES_longitude - ADEP_longitude)*np.pi/180
    distance_km = 2*EARTH_RADIUS_KM*np.arcsin(np.sqrt(np.sin(delta_latitude_radian/2)**2 + np.cos(ADEP_latitude_radian)*np.cos(ADES_latitude_radian)*np.sin(delta_longitude_radian/2)**2))
    fuel_consumption_coeff1 = aircraft_fuel_consumption_data.iloc[0,4]
    fuel_consumption_coeff2 = aircraft_fuel_consumption_data.iloc[0,5]
    fuel_consumption_coeff3 = aircraft_fuel_consumption_data.iloc[0,6]
    fuel_consumption_kg = fuel_consumption_coeff1*distance_km**2 + fuel_consumption_coeff2*distance_km + fuel_consumption_coeff3
    return fuel_consumption_kg