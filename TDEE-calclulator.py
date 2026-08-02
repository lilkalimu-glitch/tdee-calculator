#explaing what tdee is and asking for a name

print('Hello stranger, this script helps you to calculate your daily TDEE depending on your goal.\n' 
    'TDEE stands for Total Daily Energy Expenditure, which is the total number of calories your body burns in a day during rest and physical activity.\n'
    'Before we start asking you a few questions to calculate your TDEE, we need to know your Name!')
bmr_explain = 'BMR is the calories your body burns if he would only lay down the whole day! So the minimum you need to survive.'
user_name = input('Please enter a name.\n>')
user_name = user_name.strip().title()
print(f"Let's get started {user_name}!")

#helper function for user informations like weight etc...

def user_information():
    print('Please enter your weight in kg!')
    while True:    
        try:
            user_weight = float(input('>').strip())
            if not 0 <= user_weight <= 150:
                print(f'Please enter a realistic value! We do no think that you weight {user_weight}kg :)')
                continue
            break
        except ValueError:
            print('Please enter only a value between 0 and 150.')
            continue
    print('Please enter your height in cm!')
    while True:
        try:
            user_height = float(input('>').strip())
            if not 0 <= user_height <= 250:
                print(f'Please enter a realistic value! We do not think that you are {user_height}cm tall :)')
                continue
            break
        except ValueError:
            print('Please enter only a value between 0 and 250.')
            continue
    print('Please enter your age in years!')
    while True:
        try:
            user_age = int(input('>'))
            
            if not 0 <= user_age <= 99:
                print(f'Please enter a realistic value! We do not think that you are {user_age} years old :)')
                continue
            break
        except ValueError:
            print('Please enter only a value between 0 and 99.')
            continue
    return user_weight, user_height, user_age       



#helper function for user gender male and bmr calculation
def user_gender_malef():#IMPORTANT: i created another helper function for user genders, since it is more practical to call the function instead of writing for both man and female
    user_weight, user_height, user_age = user_information()
    # print('Please enter your weight in kg!')
    # #asking fot user weight and checking for conditions
    # while True:
    #     try:
    #         weight_men = input('>')
    #         weight_men = float(weight_men)
    #         if weight_men <= 0 or weight_men >= 150:
    #             print('Damn bro, you gotta be kidding with that weight. At this point just give up!\nEnter your weight again.')
    #             continue
    #         break
    #     except ValueError:
    #         print(f'{name} enter only fkn numbers!')
    #         continue
    # print('Please enter your height in cm!') 
            
    #    #asking for user height and checking conditions
    # while True:
    #     try:
    #         height_men = input('>')                             
    #         height_men = float(height_men)       
    #         if height_men <= 0 or height_men >= 200:
    #             print(f'BRO YOU ARE NOT {height_men}cm tall!\nfunny guy')
    #             continue
    #         break
    #     except ValueError:
    #             #if user enters invalid value
    #             print('how many times do i have to tell you to enter only numbers? Enter only numbers')
    #             continue
    #     #asking for age 
    # print('Please enter your age in years!')
    # while True:
    #     try:
    #         age_men = input('>')
    #         age_men = int(age_men)
    #         if age_men not in range(0,100):
    #             print(f'dude you are NOT {age_men}!')
    #             continue           
    #         break
    #         #if user enters invalid value                 
    #     except ValueError:
    #         print('Please enter only numbers...')
    #         continue

    bmr_calculator_men = int(66 + (13.7 * user_weight) + (5 * user_height) - (6.8 * user_age))
    return bmr_calculator_men

#if user gender female
def user_gender_femalef():
    user_weight, user_height, user_age = user_information()
    bmr_calculator_female =  int(655 + (9.6 * user_weight) + (1.8 * user_height) - (4.7 * user_age))
    return bmr_calculator_female

#helper function for TDEE calculation
def activity_level():
    print('Please enter your weekly activity level!\n'
          '1. Sedentary\n'
          '2. Lightly active\n'
          '3. Moderately active\n'
          '4. Very active\n'
          '5. Extra active')
    while True:      
        try:
            user_activity_level = int(input('>'))
            if user_activity_level in range(1,6):
                activity_factor = {1:1.25, 2:1.375, 3:1.55, 4:1.725, 5:1.9}#convert user choice to the activity factor
                user_activity_level = activity_factor[user_activity_level]
                break
            else:
                print('Please enter only 1-5')
                continue
        except ValueError:
            print('Please enter only a number between 1-5')
            continue
    return user_activity_level

#main function to calculate TDEE and asking for user gender
def TDEE_calculator(name):
    print(f'Please enter your gender {name}!\nM for male\nF for female')

    while True:
        user_gender_input = input('>')
        user_gender_input = user_gender_input.lower().strip()
        if user_gender_input not in ['m', 'f']:    
            print('Please enter either only m or f!')
            continue       
        break
    if user_gender_input == 'm':#after user entered male as his gender it will call the helper function 
        user_bmr_info = user_gender_malef()
        print(f"Your daily BMR is {user_bmr_info}kcal!")
        print(bmr_explain)
    elif user_gender_input == 'f':
        user_bmr_info = user_gender_femalef()
        print(f'Your daily BMR is {user_bmr_info}kcal!')
        print(bmr_explain)
        #after bmr calculation, the tdee(main part) will executet after asking for his activity levels!
    user_activity_info = activity_level()
    user_tdee_info = int(user_bmr_info * user_activity_info)
    print(f"Your TDEE is {user_tdee_info}kcal!")

TDEE_calculator(user_name)
         
