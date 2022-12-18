#!-- Import necessary modules
import sys
import json
import subprocess

#!-- Get the JSON data from the command-line argument
if len(sys.argv) > 1:
    json_data = sys.argv[1]
    print("\033c")
else:
    print("\033c")
    print("\33[31mError, you need to input the json string from the MH+ browser extension.\33[37m")
    sys.exit()

#!-- Parse the JSON data
data = json.loads(json_data)

#!-- Get the values and set them to variables
minehut_Token = data['minehutToken']
minehut_session = data['minehutSession']
slg_user_token = data['slgUserToken']

#!-- Run mh-watch commands
subprocess.run(['mh-watch', f'--setsession={minehut_session}'])
subprocess.run(['mh-watch', f'--setauth={minehut_Token}'])
subprocess.run(['mh-watch', f'--setprofiletoken={slg_user_token}'])
print("\33[32mSuccessfuly inputted the api keys into mh-watch.\33[37m")
