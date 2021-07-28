#Assignment 1 for One Month Pyhon
#tip calculator


print("\n")

print(               ' XYZ Restaurant')
print('----------------------------------------------------------------------------------- .\n')
name = input('Hello!, may I get your name please!. \n')
print(f'hello, {name}!. \n')
bill = float(input('Enter Your Sub-Total in $. \n').strip('$'))

answer = input('If you enjoyed our services, you may tip off the service staff. Enter "yes" to proceed for tip and "no" to exit.\n')
yes_responses = ['yes', 'y']
no_responses = ['no', 'n']
if answer.lower() in yes_responses:
 tip_selection = int(input(f'Thank you {name}. The subtotal for your meal is ${bill:.2f}.\n'
 'Please enter your tip percentage (15, 18, 20): \n'
 '15 - average service\n'
 '18 - good service\n'
 '20 - fantastic service\n'))
 total = bill + (bill * tip_selection / 100)
 print(f'Thanks\'s for the tip! {name}. \n Your Grand Total(including tip) in $ ={total:.2f}. \n')
 print('------------------------------------------------------------------------------------')
 print(f'We hope {name}, you enjoyed your meal at Rajwada Heritage Restaurant.')
 print(                              'THANK\'S FOR VISITING'                 )
elif answer.lower() in no_responses:
	print('------------------------------------------------------------------------------------')
	print(f'We hope {name}, you enjoyed your meal at XYZ Restaurant.')
	print(                              'THANK\'S FOR VISITING'                 )
else:
    print('I don\'t understand.')





