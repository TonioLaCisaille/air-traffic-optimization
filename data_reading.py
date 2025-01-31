import pandas as pd

Flights_march_2019 = pd.read_csv('C:/Users/anton/OneDrive - ISAE-SUPAERO/Documents/MES DOC/SUPAERO/4A/Domaine - ETE/projet ETE aviation/Flights_20190301_20190331.csv')
# Flights_20190601_20190630 = pd.read_csv('C:/Users/anton/OneDrive - ISAE-SUPAERO/Documents/MES DOC/SUPAERO/4A/Domaine - ETE/projet ETE aviation/Flights_20190601_20190630.csv')
# Flights_20190901_20190930 = pd.read_csv('C:/Users/anton/OneDrive - ISAE-SUPAERO/Documents/MES DOC/SUPAERO/4A/Domaine - ETE/projet ETE aviation/Flights_20190901_20190930.csv')
# Flights_20191201_20191231 = pd.read_csv('C:/Users/anton/OneDrive - ISAE-SUPAERO/Documents/MES DOC/SUPAERO/4A/Domaine - ETE/projet ETE aviation/Flights_20191201_20191231.csv')
# Flights_20201201_20201231 = pd.read_csv('C:/Users/anton/OneDrive - ISAE-SUPAERO/Documents/MES DOC/SUPAERO/4A/Domaine - ETE/projet ETE aviation/Flights_20201201_20201231.csv')

print(Flights_march_2019.head())

# Getting all ORY-PMO fligts
flights_ORY_PMO = Flights_march_2019[(Flights_march_2019['ADEP'] == 'LFPO') & (Flights_march_2019['ADES'] == 'LICJ')]

# Afficher les résultats
print(flights_ORY_PMO)

# Lire et afficher les coefficients de consommation/émission
fuel_consumption_data = pd.read_csv('C:/Users/anton/OneDrive - ISAE-SUPAERO/Documents/MES DOC/SUPAERO/4A/Domaine - ETE/projet ETE aviation/ac_model_coefficients.csv')
aircraft_fuel_consumption_data = fuel_consumption_data[(fuel_consumption_data['ac_code_icao'] == "A320")]
fuel_consumpiton_coeff1 = aircraft_fuel_consumption_data.iloc[0,4]
fuel_consumpiton_coeff2 = aircraft_fuel_consumption_data.iloc[0,5]
fuel_consumpiton_coeff3 = aircraft_fuel_consumption_data.iloc[0,6]
print("Coefficient n°1\n",fuel_consumpiton_coeff1)
print("Coefficient n°2\n",fuel_consumpiton_coeff2)
print("Coefficient n°3\n",fuel_consumpiton_coeff3)

