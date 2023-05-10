import requests
import json


def get_cards():  # functionality to obtains card IDs at time of Updating a Card
    response = requests.get(
        'https://api.trello.com/1/boards/6447398b37323b305e4f4922/cards?key=c0c681b58591a97d3525161f697923d0&token=ATTA3455d6fb27d2a1b0e8ddf49bd045e2027ba6a096ca56e54a947ddc65e305c6dbC14EDB45')
    print(response.text)
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


def get_lists():
    url = "https://api.trello.com/1/boards/6447398b37323b305e4f4922/lists"
    headers = {
        "Accept": "application/json"
    }
    query = {
        'key': 'c0c681b58591a97d3525161f697923d0',
        'token': 'ATTA3455d6fb27d2a1b0e8ddf49bd045e2027ba6a096ca56e54a947ddc65e305c6dbC14EDB45',
    }
    response = requests.request("GET", url, headers=headers, params=query)
    return response.text
    # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


def create_card():
    print(get_lists())
    id_list = input("Please enter the ID of the list that card will belong to : ")
    card_name = input("Please enter the name of the card : ")
    description = input("Please enter the description of the card : ")
    card_position = int(input("Please enter position of the card : "))
    start_date = input("Please enter the start date in mm/dd/yyyy format : ")
    due_date = input("Please enter the due date in mm/dd/yyyy format : ")
    url = "https://api.trello.com/1/cards"
    headers = {"Accept": "application/json"}
    query = {
        'idList': id_list,
        'key': 'c0c681b58591a97d3525161f697923d0',
        'token': 'ATTA3455d6fb27d2a1b0e8ddf49bd045e2027ba6a096ca56e54a947ddc65e305c6dbC14EDB45',
        'name': card_name,
        'desc': description,
        'pos': card_position,
        'start': start_date,
        'due': due_date

    }
    response = requests.request("POST", url, headers=headers, params=query)
    print(response.text)
    print(
        'New card with the name ' + card_name + ' has been created successfully in list ' + id_list + ' on the Trello Board!')
    # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


def update_card():
    print(get_cards())
    url = "https://api.trello.com/1/cards/"
    headers = {"Accept": "application/json"}
    card_id = input("Please enter the ID of the card : ")
    url += card_id
    card_name = input("Please enter the updated name of the card : ")
    description = input("Please enter the updated description of the card : ")
    start_date = input("Please enter the updated start date in mm/dd/yyyy format : ")
    due_date = input("Please enter the updated due date in mm/dd/yyyy format : ")
    query = {
        'key': 'c0c681b58591a97d3525161f697923d0',
        'token': 'ATTA3455d6fb27d2a1b0e8ddf49bd045e2027ba6a096ca56e54a947ddc65e305c6dbC14EDB45',
        'name': card_name,
        'desc': description,
        'start': start_date,
        'due': due_date
    }
    response = requests.request("PUT", url, headers=headers, params=query)
    print(response.text)
    print('Card ' + card_name + ' has been updated successfully on the Trello Board!')
    # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


def main():
    print("Options: \n 1.Create a new Card \n 2.Update an existing Card")
    option = int(input("Please enter the operation to be performed : "))
    if option == 1:
        create_card()
    elif option == 2:
        update_card()


if __name__ == '__main__':
    main()
