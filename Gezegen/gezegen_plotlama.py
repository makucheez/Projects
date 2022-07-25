import pandas as pd
import math

data = pd.read_csv('gezegen.txt', sep=',')

density = [0,0,0,0,0,0,0,0,0]

data['density'] = density

data["density"] = data["mass"]/(data["diameter"] * data["diameter"] * data["diameter"] * math.pi * (4/3))
print("a)")
print(data)

data_sort_dia = data.sort_values(by="diameter")
print("\nb)")
print(data_sort_dia)

data_mass_greater_earth = data[data.mass>1]
data_mass_greater_earth = data_mass_greater_earth.sort_values(by="mass")
print("\nc)")
print(data_mass_greater_earth)


data_greatermass_lessgrav = data_mass_greater_earth[data_mass_greater_earth.gravity<1]
print("\nd)")
print(data_greatermass_lessgrav)

plot = data.plot.bar(y="density",x="planet")