#Import the requests library into the script to access the API related information
import requests
#Import json to make the response prettier for learning purposes - can be replaced with standard print or stored in a variable for later.
import json

#Create the function for pulling the space data
def GetAPOD():
    #URL and parameters you may need to pull from *NTOTE* Demo_Key is JUST a demo - replace this with your own key 
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    #Get the response code of the website (we want 200)
    response = requests.get(url)
    #Check if the response code is 200, if so continue on if not - return the error
    if response.status_code == 200:
            #Pull the JSON from the response paramter and pretty up the json (response.json is our raw response, use json dumps to convert the response into json formatting.)
            apod = json.dumps(response.json(), indent=4)
            # Return the APOD data as end result.
            return apod
    else:
          # Error if 200 is not found.
          return "Response code was not 200."

#Run the function and store the return result as "APOD"
apod = GetAPOD()
#Finally, if you want to print the results, run print :) 
print(apod)