import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
GRAPH_ID = os.getenv("GRAPH_ID")


# CREATING THE USER
# to customise, check out - https://docs.pixe.la/entry/post-user

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# run and check status of request
"""
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)  
"""


# CREATING THE GRAPH
# to customise your graph, check out - https://docs.pixe.la/entry/post-graph

graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {"X-USER-TOKEN": PIXELA_TOKEN}

# run and check status of request
"""
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
"""


# find your graph at - https://pixe.la/v1/users/<pixela username>/graphs/<graph id>


# POSTING A PIXEL IN THE GRAPH
# to customise, check out - https://docs.pixe.la/entry/post-pixel

post_pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

# to add a pixel to a different date, use (for example) -
# today = datetime(year=2021, month=8, day=3)

post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}

# run and check status of request
"""
response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
print(response.text)
"""


# UPDATING A PIXEL
# to customise, check out - https://docs.pixe.la/entry/put-pixel

update_pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/20210803"

update_pixel_params = {
    "quantity": "10",
}

# run and check status of request
"""
response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
print(response.text)
"""


# DELETE A PIXEL
# check out - https://docs.pixe.la/entry/delete-pixel

delete_pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/20210803"

# run and check status of request
"""
response = requests.delete(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
print(response.text)
"""
