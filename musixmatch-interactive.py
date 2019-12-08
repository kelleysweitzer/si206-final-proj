import requests
import json 
from lyrics_api import * 

while True: 
    print()
    print("Welcome to MusixMatch API")
    print()
    print("MENU OPTIONS")
    print("1- Call one of the API methods with parameters and see JSON")
    print("2- EXAMPLE Search for the lyrics of a song")
    print("0- Exit")
    print()
    choice = input("> ")
    print()

    if choice == "0":
        break 
    # see the parameters for an API method 
    if choice == "1":
        print("API METHODS")
        for index, api_method in enumerate(api_methods, start = 0): 
            print(str(index) + ": " + api_method)
        print()
        print("Your choice (0-15)")
        method_choice = input("> ")
        print()
        #index of the array we want to pull out 
        #method user chose chose
        user_choice = api_methods[int(method_choice)]
        parameter_list = get_parameters (user_choice)

        print("PARAMATERS")
        for index, parameter in enumerate(parameter_list, start = 0):
            print(str(index) + ": " + parameter)
        print()
        #start building the API call 

        api_call = base_url + user_choice + format_url 

        while True: 
            print("API call so far: " + api_call)
            print()
            print("Which parameter would you like to add a value for? (0-n) (type x to make the call)")
            paramater_choice = input(" >")
            print()
            # add the API key and make the call 
            if paramater_choice == "x": 
                api_call = api_call + api_key 
                request = requests.get(api_call)
                data = request.json()
                print("FINAL API CALL: " + api_call)
                print()
                print("JSON DATA")
                print(json.dumps(data, sort_keys = True, indent=2))
                break
            else: 
                paramater_choice_string = parameter_list[int(paramater_choice)]
                value = input(paramater_choice_string)
                api_call  = api_call + paramater_choice_string + value
                print()


 
    #example 
    if choice == "2":
        print("What is the name of the artist?")
        artist_name = input(">")
        print("What is the name of the track?")
        track_name = input(">")
        print()
        #Finding the lyrics of a song: base url + api method + different parameters + the input that the user put in + API key 
        api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
        
        #call the API 
        request = requests.get(api_call)
        data = request.json()
        #data is equivalent to whatever is down at this level of message and body 
        data = data["message"]["body"]
        print("API Call: " + api_call)
        print()
        print(data["lyrics"]["lyrics_body"])