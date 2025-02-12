weight = float(input('enter your weight: '))
index_value = input('enter wether your weight is in kgs or lbs: ')
if index_value.lower() == 'k' or index_value == 'K':
    x = weight * 2.205
    print('your weight in lbs is: ' + str(x) + ' lbs')
elif index_value == 'l' or index_value == 'L':
    x = weight / 2.205
    print('your weight in kgs is: ' + str(x)+' kgs')
else:
    print('please enter either "k" or "kgs" for weight or either "l" or "lbs"')
