import pandas as pd
from scipy.stats import gmean, hmean
import numpy as np

income_Data = [14.9,106.0,104.6,148.9,55.9,80.2,21.0,71.4,15.1,71.1,63.1,15.0]
Rating_Data = [283,483,514,681,357,569,259,512,266,491,589,138]
Age_Data =   [34,82,71,36,68,77,37,87,66,41,30,64]
Education_Data = [11,15,11,11,16,10,12,9,13,19,14,16]



income = pd.Series(income_Data)
Rating = pd.Series(Rating_Data)
Age = pd.Series(Age_Data)
Education = pd.Series(Education_Data)


sample_sizei = income.count()
meani = income.mean()
mediani = income.median()
modei = income.mode().tolist()
minimumi = income.min()
maximumi= income.max()
range_vali = maximumi - minimumi
first_quartilei = income.quantile(0.25)
second_quartilei = income.quantile(0.50) 
third_quartilei = income.quantile(0.75)
iqri = third_quartilei - first_quartilei
variancei = income.var()
std_devi = income.std()
geometric_meani = gmean(income)
harmonic_meani = hmean(income)
cv_percenti = (std_devi / meani) * 100 if meani != 0 else 0

sample_sizer = Rating.count()
meanr = Rating.mean()
medianr = Rating.median()
moder = Rating.mode().tolist()
minimumr = Rating.min()
maximumr = Rating.max()
range_valr = maximumr - minimumr
first_quartiler = Rating.quantile(0.25)
second_quartiler = Rating.quantile(0.50) 
third_quartiler = Rating.quantile(0.75)
iqrr = third_quartiler - first_quartiler
variancer = Rating.var()
std_devr = Rating.std()
geometric_meanr = gmean(Rating)
harmonic_meanr = hmean(Rating)
cv_percentr = (std_devr / meanr) * 100 if meanr != 0 else 0

sample_sizea = Age.count()
meana = Age.mean()
mediana= Age.median()
modea = Age.mode().tolist()
minimuma= Age.min()
maximuma = Age.max()
range_vala = maximuma - minimuma
first_quartilea = Age.quantile(0.25)
second_quartilea = Age.quantile(0.50) 
third_quartilea = Age.quantile(0.75)
iqra = third_quartilea - first_quartilea
variancea = Age.var()
std_deva = Age.std()
geometric_meana = gmean(Age)
harmonic_meana = hmean(Age)
cv_percenta = (std_deva / meana) * 100 if meana != 0 else 0

sample_sizee = Education.count()
meane = Education.mean()
mediane = Education.median()
modee = Education.mode().tolist()
minimume = Education.min()
maximume = Education.max()
range_vale = maximume - minimume
first_quartilee = Education.quantile(0.25)
second_quartilee = Education.quantile(0.50) 
third_quartilee = Education.quantile(0.75)
iqre = third_quartilee - first_quartilee
variancee = Education.var()
std_deve = Education.std()
geometric_meane = gmean(Education)
harmonic_meane = hmean(Education)
cv_percente = (std_deve / meane) * 100 if meane != 0 else 0


stats_dicti = {
    "Sample size (n)": sample_sizei,
    "Mean": meani,
    "Median": mediani,
    "Mode": 'No Mode',
    "Geometric Mean": geometric_meani,
    "Harmonic Mean": harmonic_meani,
    "Minimum": minimumi,
    "Maximum": maximumi,
    "Range": range_vali,
    "First Quartile": first_quartilei,
    "Second Quartile": second_quartilei,
    "Third Quartile": third_quartilei,
    "Inter-Quartile Range": iqri,
    "Variance": variancei,
    "Standard Deviation": std_devi,
    "CV %": cv_percenti
}
stats_dictr = {
    "Sample size (n)": sample_sizer,
    "Mean": meanr,
    "Median": medianr,
    "Mode": 'No Mode',
    "Geometric Mean": geometric_meanr,
    "Harmonic Mean": harmonic_meanr,
    "Minimum": minimumr,
    "Maximum": maximumr,
    "Range": range_valr,
    "First Quartile": first_quartiler,
    "Second Quartile": second_quartiler,
    "Third Quartile": third_quartiler,
    "Inter-Quartile Range": iqrr,
    "Variance": variancer,
    "Standard Deviation": std_devr,
    "CV %": cv_percentr
}
stats_dicta = {
    "Sample size (n)": sample_sizea,
    "Mean": meana,
    "Median": mediana,
    "Mode": 'No Mode',
    "Geometric Mean": geometric_meana,
    "Harmonic Mean": harmonic_meana,
    "Minimum": minimuma,
    "Maximum": maximuma,
    "Range": range_vala,
    "First Quartile": first_quartilea,
    "Second Quartile": second_quartilea,
    "Third Quartile": third_quartilea,
    "Inter-Quartile Range": iqra,
    "Variance": variancea,
    "Standard Deviation": std_deva,
    "CV %": cv_percenta
}
stats_dicte = {
    "Sample size (n)": sample_sizee,
    "Mean": meane,
    "Median": mediane,
    "Mode": modee,
    "Geometric Mean": geometric_meane,
    "Harmonic Mean": harmonic_meane,
    "Minimum": minimume,
    "Maximum": maximume,
    "Range": range_vale,
    "First Quartile": first_quartilee,
    "Second Quartile": second_quartilee,
    "Third Quartile": third_quartilee,
    "Inter-Quartile Range": iqre,
    "Variance": variancee,
    "Standard Deviation": std_deve,
    "CV %": cv_percente
}
print('------------------------------------------------------------------------------------------------')
print("Descriptive Statistics for Income Data:")
for stat, value in stats_dicti.items():
    if isinstance(value, list):
        print(f"{stat}: {', '.join(map(str, value))}")
    else:
        print(f"{stat}: {value:.2f}" if isinstance(value, (float, np.float64)) else f"{stat}: {value}")

print('------------------------------------------------------------------------------------------------')
print("Descriptive Statistics for Rating Data:")

for stat, value in stats_dictr.items():
    if isinstance(value, list):
        print(f"{stat}: {', '.join(map(str, value))}")
    else:
        print(f"{stat}: {value:.2f}" if isinstance(value, (float, np.float64)) else f"{stat}: {value}")

print('------------------------------------------------------------------------------------------------')
print("Descriptive Statistics for Age Data:")

for stat, value in stats_dicta.items():
    if isinstance(value, list):
        print(f"{stat}: {', '.join(map(str, value))}")
    else:
        print(f"{stat}: {value:.2f}" if isinstance(value, (float, np.float64)) else f"{stat}: {value}")

print('------------------------------------------------------------------------------------------------')
print("Descriptive Statistics for Education Data:")
for stat, value in stats_dicte.items():
    if isinstance(value, list):
        print(f"{stat}: {', '.join(map(str, value))}")
    else:
        print(f"{stat}: {value:.2f}" if isinstance(value, (float, np.float64)) else f"{stat}: {value}")

print('------------------------------------------------------------------------------------------------')

Corr = np.corrcoef(income_Data, Education_Data)[0, 1]
print(f"Correlation between Income and Education: {Corr:.2f}")
print('------------------------------------------------------------------------------------------------')
x = Education_Data
y = income_Data
slope, intercept = np.polyfit(x, y, 1)
print(f"Slope of the regression line: {slope:.2f}")
print(f"Intercept of the regression line: {intercept:.2f}")
print('------------------------------------------------------------------------------------------------')