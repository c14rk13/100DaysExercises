from datetime import datetime, timezone
import requests
import os


CREATE_NEW_ACCT = False
CREATE_GRAPH = False
ADD_PIXEL = False
UPDATE_PIXEL = False
DELETE_PIXEL = False
USERNAME = "estonuevo"
TOKEN = os.environ.get("PIXELA_TOKEN")
pixela_endpoint = "https://pixe.la/v1/users"


def create_pixela_acct():

    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=pixela_endpoint, json=user_params)
    # user_data = response.json()
    print(response.text)    # https://pixe.la/@estonuevo


def create_graph(graph_params):
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    graph_headers = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_headers)
    print(response.text)


def create_graph_pixel(gid, graph_params):
    graph_pixel_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{gid}"
    graph_headers = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.post(url=graph_pixel_endpoint, json=graph_params, headers=graph_headers)
    print(response.text)


def update_graph_pixel(gid, pixel_date, graph_params):
    graph_pixel_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{gid}/{pixel_date}"
    graph_headers = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.put(url=graph_pixel_endpoint, json=graph_params, headers=graph_headers)
    print(response.text)


def delete_graph_pixel(gid, pixel_date):
    graph_pixel_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{gid}/{pixel_date}"
    graph_headers = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.delete(url=graph_pixel_endpoint, headers=graph_headers)
    print(response.text)


if CREATE_NEW_ACCT:
    create_pixela_acct()

if CREATE_GRAPH:
    graph_params = {
            "id": "graph001",
            "name": "Reading Graph",
            "unit": "pages",
            "type": "int",
            "color": "ajisai"
        }
    create_graph(graph_params)
    # To check the created graph online: https://pixe.la/v1/users/estonuevo/graphs/graph001.html

today = datetime.now(timezone.utc).strftime("%Y%m%d")

if ADD_PIXEL:
    graph_params = {
        "date": today,
        "quantity": "10",
        "optionalData":"{\"ISBN\": \"978-1-492-04345-4\"}"
    }
    create_graph_pixel("graph001", graph_params)

# Update pixel
if UPDATE_PIXEL:
    update_pixel_params = {
        "quantity": "5"
    }
    update_graph_pixel("graph001", today, update_pixel_params)

# Delete pixel
if DELETE_PIXEL:
    delete_graph_pixel("graph001", today)

