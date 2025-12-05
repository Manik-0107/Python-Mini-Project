from countryinfo import CountryInfo

count = input("Enter your country: ")
country = CountryInfo(count)

print("Capital is: ", country.capital())
print("Currencies are: ", country.currencies())
print("Languages are: ", country.languages())
print("Borders are: ", country.borders())
print("Other names: ", country.alt_spellings())



"""
Enter your country: Canada
Capital is:  Ottawa
Currencies are:  ['CAD']
Languages are:  ['en', 'fr']
Borders are:  ['USA']
Other names:  ['CA']

"""
