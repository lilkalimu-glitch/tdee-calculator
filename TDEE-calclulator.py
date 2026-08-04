import json



# Explaing what tdee is and asking for a name

bmr_explain = 'BMR is the calories your body burns if he would only lay down the whole day! So the minimum you need to survive.'
tdee_explanaiton = ('Hello stranger, this script helps you to calculate your daily TDEE.\n' 
                    'TDEE stands for Total Daily Energy Expenditure, which is the total number of calories your body burns in a day during rest and physical activity.\n'
                    'Before we start asking you a few questions to calculate your TDEE, we need to know your Name!')

# Helper function for username

def user_namef():
    user_name = input('Please enter a name.\n>')
    user_name = user_name.strip().title()
    return user_name


# Helper function to load user data

def load_user_data():
    try:
        with open("user_data.json", "rt") as file:
            user_data = json.load(file)
            if user_data != None:
                return user_data
            else:
                return None
    except FileNotFoundError:
        return None
        

# Helper function for user informations like weight etc...

def user_information():
    print('Please enter your weight in kg!')
    while True:    
        try:
            user_weight = float(input('>').strip())
            if not 0 < user_weight:
                print('Please enter a positive value!\n '
                      f'We do not think that you weight {user_weight}kg :)')
                continue
            break
        except ValueError:
            print('Please enter only a value between 0 and 150.')
            continue
    print('Please enter your height in cm!')
    while True:
        try:
            user_height = float(input('>').strip())
            if not 0 < user_height:
                print('Please enter a positive value!\n'
                      f'We do not think that you are {user_height}cm tall :)')
                continue
            break
        except ValueError:
            print('Please enter only a value between 0 and 250.')
            continue
    print('Please enter your age in years!')
    while True:
        try:
            user_age = int(input('>'))
            
            if not 0 < user_age < 99:
                print(f'Please enter a positive value! We do not think that you are {user_age} years old :)')
                continue
            break
        except ValueError:
            print('Please enter only a value between 0 and 99.')
            continue
    return user_weight, user_height, user_age       


# Helper function for user gender male and bmr calculation

def user_genderf():
    user_weight, user_height, user_age = user_information()
    print('Please enter gender male/female')
    bmr = int((10 * user_weight) + (6.25 * user_height) - (5 * user_age))
    while True:
        user_gender = input('>').lower().strip()
        if user_gender in ['m', 'male']:
            bmr = int(bmr + 5)
            break
        elif user_gender in ['f', 'female']:
            bmr = int(bmr - 161)
            break
        else:
            print('Please enter either only m or f')
    return bmr


# Helper function for TDEE calculation

def activity_level():
    # Ask the user for his activity level and converet it to factor
    print('Please enter your weekly activity level!\n'
          '1. Sedentary\n'
          '2. Lightly active\n'
          '3. Moderately active\n'
          '4. Very active\n'
          '5. Extra active')

    # Keep asking until user enters a value between 1-5
    while True:      
        try:
            user_activity_level = int(input('>'))
            if user_activity_level in range(1,6):
                activity_factor = {1: 1.25, 
                                   2: 1.375, 
                                   3: 1.55, 
                                   4: 1.725, 
                                   5: 1.9
                                   }  
                user_activity_level = activity_factor[user_activity_level]
                break
            else:
                print('Please enter only 1-5')
                continue
        except ValueError:
            print('Please enter only a number between 1-5')
            continue
    return user_activity_level          
       

# Main function to calculate TDEE and asking for user gender

def run_tdee_script(): 
    user_data = load_user_data()
    if user_data is None:
         user_name = user_namef()
         user_bmr_info = user_genderf()
                
        # After bmr calculation, the tdee(main part) will executet after asking for his activity levels!
        
         user_activity_info = activity_level()
         user_tdee_info = int(user_bmr_info * user_activity_info)
         print(f"Your TDEE is {user_tdee_info}kcal!\nThank you for choosing us {user_name}!")
         user_data = {
            "user_name": user_name,
            "user_bmr_info": user_bmr_info,
            "user_activity_info": user_activity_info,
            "user_tdee_info": user_tdee_info
            }
         with open("user_data.json", "wt") as file:
            json.dump(user_data, file)
         return user_data, user_name
    elif user_data != None:
        print(f'Welcome back {user_data["user_name"]}!\n'
            'Your data has been saved from last time, if you wanna know what your values are,\n' 
            'please enter yes, if not please enter no.')    
        while True:
            user_ask_for_values = input('>')
            if user_ask_for_values not in ['yes', 'no']:
                print('Please enter either yes or no.')
                continue
            break
        if user_ask_for_values in ['yes', "y"]:
            print(f'Your stats:\nBMR: {user_data["user_bmr_info"]}kcal\n'
                f'Activity Info: {user_data["user_activity_info"]}\n'
                f'TDEE: {user_data["user_tdee_info"]}kcal')
        elif user_ask_for_values in ['no', 'n']:
            print('Alright, if you want you can log your calories now!')
            print('IMPORTANT: We are currently working on this part :) It will be available soon!')
            #So now the next step would be to work on a calorie tracker, a helper function to track the user's calories.

    
run_tdee_script()



         
