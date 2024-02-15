weight = int(input('what is your weight ' ))
Unit = input('in KG or LB? ')

if Unit.upper == 'KG':
 print('Weight in Lbs = ' + str(weight / 0.45))
else:
 print('weight in Kgs = ' + str(weight * 0.45) )

