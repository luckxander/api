import requests # Lib to run requests
import json # Lib to format Json files

# Fake API for testing from https://jsonplaceholder.typicode.com/

def api(endpoint, method, updated_data, headers):    
    api_url = endpoint 
    method = method
    if method == "GET":
        try:
            response = requests.get(api_url)
            data = response.json()
            if response.status_code == 200:       
                print("Request successful. Data retrieved:")                             
                if isinstance(data, list):
                    print(f"Fetched {len(data)} items.")
                    for item in data:
                        userId = item.get('userId')
                        target_Value = 10
                        if userId == target_Value:
                            print(f"ID: {item.get('id')}, userId: {item.get('userId')}, title: {item.get('title')}")      
                        else:
                            print(f"userId: is not {target_Value}, it is {userId}")                         
                else:
                    print("The response was not a JSON array (list). It might be an object (dictionary).")      
                    print(f"Formatted data: {json.dumps(data, indent=2)}")  
            else:
                print("Error:", response.status_code, response.reason)             
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")     
    elif method == "POST":
        try:
            response = requests.post(api_url, json=updated_data, headers=headers)
            if response.status_code == 200:
                print("Data created successfully! 200")
                print("Created user data:", json.dumps(response.json(), indent=2))
            elif response.status_code == 201:
                print("Data created successfully! 201")
                print("Created user data:", json.dumps(response.json(), indent=2))
            else:
                print(f"Failed to create data. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")              
    elif method == "PUT":
        try:
            response = requests.put(api_url, json=updated_data, headers=headers)
            if response.status_code == 200:
                print("User full updated successfully!")
                print("User data:", json.dumps(response.json(), indent=2))
            elif response.status_code == 204:
                print("User updated successfully, no content returned.")
            else:
                print(f"Failed to update user. Status code: {response.status_code}")
                print("Response text:", response.text)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
    elif method == "PATCH":
        try:
            response = requests.patch(api_url, json=updated_data, headers=headers)
            if response.status_code == 200:
                print("Title updated successfully!")
                print("User data:", json.dumps(response.json(), indent=2))
            elif response.status_code == 204:
                print("Title updated successfully, no content returned.")
            else:
                print(f"Failed to update user. Status code: {response.status_code}")
                print("Response text:", response.text)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
    elif method == "DELETE":
        try:
            response = requests.delete(api_url, json=updated_data, headers=headers)
            if response.status_code == 200:
                print("Data deleted successfully!")
            elif response.status_code == 204:
                print("Data deleted successfully, no content returned.")
            else:
                print(f"Failed to delete data. Status code: {response.status_code}")
                print("Response text:", response.text)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")            
        # Keep the code below commented as instruction, use authorization only when required              
        # headers = {
        #     "Content-Type": "application/json; charset=utf-8",
        #     # Add any necessary authorization headers, e.g.,
        #     # "Authorization": "Bearer YOUR_ACCESS_TOKEN"
        # }

# Test Case 1 
def testCase1getHappy(endpoint, method, updated_data, headers):
    print("Test Case #1 Get Method")
    api(endpoint=endpoint, method=method, updated_data=updated_data, headers=headers)

endpoint = "https://jsonplaceholder.typicode.com/posts/1"
method = "GET"
updated_data = "1"
headers = {"Content-Type": "application/json; charset=utf-8"}
result = testCase1getHappy(endpoint, method, updated_data, headers)

# Test Case 2
def testCase2post(endpoint, method, updated_data, headers):
    print("Test Case #2 POST Method")
    api(endpoint=endpoint, method=method, updated_data=updated_data, headers=headers)

endpoint = "https://jsonplaceholder.typicode.com/posts"
method = "POST"
updated_data = {"id": 12, "userId": 12, "title": "Creating a new tile using POST method", "body": "Here we have the body created using the POST method"}
headers = {"Content-Type": "application/json; charset=utf-8"}   
result = testCase2post(endpoint, method, updated_data, headers)

# Test Case 3
def testCase3put(endpoint, method, updated_data, headers):
    print("Test Case #3 PUT Method")
    api(endpoint=endpoint, method=method, updated_data=updated_data, headers=headers)

endpoint = "https://jsonplaceholder.typicode.com/posts/1"
method = "PUT"
updated_data = {"id": 12, "userId": 12, "title": "Updating full payload using PUT method", "body": "Here we have the body updated using the PUT method"}
headers = {"Content-Type": "application/json; charset=utf-8"}   
result = testCase3put(endpoint, method, updated_data, headers)

# Test Case 4
def testCase4patch(endpoint, method, updated_data, headers):
    print("Test Case #4 PATCH Method")
    api(endpoint=endpoint, method=method, updated_data=updated_data, headers=headers)

endpoint = "https://jsonplaceholder.typicode.com/posts/1"
method = "PATCH"
updated_data = {"id": 12, "title": "Updating title only using PATCH method"}
headers = {"Content-Type": "application/json; charset=utf-8"}     
result = testCase4patch(endpoint, method, updated_data, headers)

# Test Case 5
def testCase5delete(endpoint, method, updated_data, headers):
    print("Test Case #5 DELETE Method")
    api(endpoint=endpoint, method=method, updated_data=updated_data, headers=headers)

endpoint = "https://jsonplaceholder.typicode.com/posts/1"
method = "DELETE"
updated_data = {"id": 12}
headers = {"Content-Type": "application/json; charset=utf-8"}     
result = testCase5delete(endpoint, method, updated_data, headers)