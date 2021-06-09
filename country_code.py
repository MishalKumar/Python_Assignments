# Problem statement
'''
Given a Phone number in the format +91-0431-2503333 split them and store in a tuple and
identify the country.

'''


def countrycode(phone_number):

    tuplelist = tuple(phone_number.split('-'))
    print(tuplelist)

    for k, v in country_n_codes.items():

        if v in tuplelist:
            print(f'country: {k} and code: {v}')
            

if __name__== '__main__':

    country_n_codes = {'India': '+91', 'Pakistan': '+92', 'China': '+86', 'Nepal': '+977', 'Bhutan': '+975', 'Myanmar': '      +95', 'Bangladesh': '+880', 'Srilanka': '+94'}
    
    phonenumber = input('enter phone number: \n')
    
    countrycode(phonenumber)