import requests # Lib to run requests
import json # Lib to format Json files
import sys # Lib to exit the script gracefully
from flask import Flask, render_template # Lib to show results in template

# Fake API for testing from https://jsonplaceholder.typicode.com/

# Using Flask to
app = Flask(__name__)
@app.route('/')

# Function to execute the request in all methods
def request(endpoint, method, updated_data, headers):    
    api_url = endpoint 
    method = method
    if method == "GET":
        try:
            response = requests.get(api_url)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Access the retrieved data in JSON format and convert it to a Python dictionary
                data = response.json()          
                print("Request successful. Data retrieved:")                             
                if isinstance(data, list):
                    print(f"Fetched {len(data)} items.")
                    for item in data:
                        # Each 'item' is likely a Python dictionary
                        userId = item.get('userId')
                        target_Value = 10
                        if userId == target_Value:
                            print(f"ID: {item.get('id')}, userId: {item.get('userId')}, title: {item.get('title')}")
                        else:
                            print(f"userId: is not {target_Value}, it is {userId}")
                else:
                    print("The response was not a JSON array (list). It might be an object (dictionary).")
                show_data = response.json()
            else:
                # Print an error message if the request was not successful
                print("Error:", response.status_code, response.reason)
                show_data = None
        except requests.exceptions.RequestException as e:
            show_data = None
            print(f"An error occurred: {e}")
            error_message = f"An error occurred: {e}"
            # Pass the data to the HTML template
        return render_template('show_data.html', data=show_data, error=error_message if 'error_message' in locals() else None)
        
    
    elif method == "POST":
        try:
            # Using the 'json' parameter automatically sets the correct Content-Type and serializes the data
            response = requests.post(api_url, json=updated_data, headers=headers)
            # Check the status code for the response
            if response.status_code == 200:
                print("Data created successfully! 200")
                # Print the created resource details formatted with dumps
                print("Updated user data:", json.dumps(response.json(), indent=2))
            elif response.status_code == 201:
                print("Data created successfully! 201")
            else:
                    print(f"Failed to create data. Status code: {response.status_code}")
            print("Response text:", response.text)
        except requests.exceptions.RequestException as e:
            # Handle any potential network or request errors
            print(f"An error occurred: {e}")
        
        
    elif method == "PUT":
        try:
            response = requests.put(api_url, json=updated_data, headers=headers)
            # Check the status code for the response
            if response.status_code == 200:
                print("User full updated successfully!")
                # Print the updated resource details formatted with dumps
                print("Updated user data:", json.dumps(response.json(), indent=2))
            elif response.status_code == 204:
                print("User updated successfully, no content returned.")
            else:
                print(f"Failed to update user. Status code: {response.status_code}")
                print("Response text:", response.text)
        except requests.exceptions.RequestException as e:
            # Handle any potential network or request errors
            print(f"An error occurred: {e}")


    elif method == "PATCH":
        try:
            response = requests.patch(api_url, json=updated_data, headers=headers)
            # Check the status code for the response
            if response.status_code == 200:
                print("Title updated successfully!")
                # Print the updated resource details formatted with dumps
                print("Updated user data:", json.dumps(response.json(), indent=2))
            elif response.status_code == 204:
                print("Title updated successfully, no content returned.")
            else:
                print(f"Failed to update user. Status code: {response.status_code}")
                print("Response text:", response.text)

        except requests.exceptions.RequestException as e:
            # Handle any potential network or request errors
            print(f"An error occurred: {e}")

    elif method == "DELETE":
        try:
            response = requests.delete(api_url, json=updated_data, headers=headers)

            # Check the status code for the response
            if response.status_code == 200:
                print("Data deleted successfully!")
            elif response.status_code == 204:
                print("Data deleted successfully, no content returned.")
            else:
                print(f"Failed to delete data. Status code: {response.status_code}")
                print("Response text:", response.text)

        except requests.exceptions.RequestException as e:
            # Handle any potential network or request errors
            print(f"An error occurred: {e}")
            
        # Keep the code below commented as instruction, use authorization only when required              
        # headers = {
        #     "Content-Type": "application/json; charset=utf-8",
        #     # Add any necessary authorization headers, e.g.,
        #     # "Authorization": "Bearer YOUR_ACCESS_TOKEN"
        # }

# Test Case 1
def testCase1get(endpoint, method, updated_data, headers):
    print("Test Case #1 Get Method")
    request(endpoint, method, updated_data, headers)
   
result = testCase1get("https://jsonplaceholder.typicode.com/posts/1", "GET", "1", headers = {"Content-Type": "application/json; charset=utf-8"})
print(result)

# Test Case 2
def testCase2post(endpoint, method, updated_data, headers):
    print("Test Case #2 POST Method")
    request(endpoint, method, updated_data, headers)
   
result = testCase1get("https://jsonplaceholder.typicode.com/posts", "POST", updated_data = {"id": 12, "userId": 12, "title": "Creating a new tile using POST method", "body": "Here we have the body created using the POST method"}, headers = {"Content-Type": "application/json; charset=utf-8"})
print(result)

# Test Case 3
def testCase3put(endpoint, method, updated_data, headers):
    print("Test Case #3 PUT Method")
    request(endpoint, method, updated_data, headers)
   
result = testCase3put("https://jsonplaceholder.typicode.com/posts/1", "PUT", updated_data = {"id": 12, "userId": 12, "title": "Updating full payload using PUT method", "body": "Here we have the body updated using the PUT method"}, headers = {"Content-Type": "application/json; charset=utf-8"})
print(result)

# Test Case 4
def testCase4patch(endpoint, method, updated_data, headers):
    print("Test Case #4 PATCH Method")
    request(endpoint, method, updated_data, headers)
   
result = testCase4patch("https://jsonplaceholder.typicode.com/posts/1", "PUT", updated_data = {"id": 12, "title": "Updating title only using PATCH method"}, headers = {"Content-Type": "application/json; charset=utf-8"})
print(result)

# Test Case 5
def testCase5delete(endpoint, method, updated_data, headers):
    print("Test Case #5 DELETE Method")
    request(endpoint, method, updated_data, headers)
   
result = testCase5delete("https://jsonplaceholder.typicode.com/posts/1", "DELETE", updated_data={"id": 12}, headers = {"Content-Type": "application/json; charset=utf-8"})
print(result)

sys.exit(0)





    

    
