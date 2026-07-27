country_code={'India' : '0091',
              'Australia' : '0025',
              'Nepal': '00977',
              'Usa' : '001',
              'Japan' : '0081',
              'china' : '0086',
              'Uk' : '0044',
              'Denmark' : '0045',
              'sweeden' : '0046',
              'finland' : '00358'}

print("Country codde for India -")
print(country_code.get('India', 'Not Found'))

print("Country code for Russia -")
print(country_code.get('Russia', 'Not Found'))