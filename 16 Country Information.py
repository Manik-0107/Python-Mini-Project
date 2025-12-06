from countryinfo import CountryInfo

try:
    country_name = input("Enter your country: ").strip().title()
    country = CountryInfo(country_name)

    print("Capital is:", country.capital())
    print("Currencies are:", country.currencies())
    print("Languages are:", country.languages())
    print("Borders are:", country.borders())
    print("Other names:", country.alt_spellings())

except KeyError:
    print("❌ Country not found! Please check the spelling.")

except Exception as e:
    print("⚠️ Something went wrong:", e)



"""
Enter your country: India
Capital is: New Delhi
Currencies are: ['INR']
Languages are: ['hi', 'en']
Borders are: ['AFG', 'BGD', 'BTN', 'MMR', 'CHN', 'NPL', 'PAK', 'LKA']
Other names: ['IN', 'Bhārat', 'Republic of India', 'Bharat Ganrajya']

"""
