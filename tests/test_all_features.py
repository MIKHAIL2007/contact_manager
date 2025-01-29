import requests

BASE_URL = "http://localhost:8080"

def test_home_page():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200, "Home page did not return status code 200"

def test_guest_page():
    response = requests.get(f"{BASE_URL}/Guest")
    assert response.status_code == 200, "Guest page did not return status code 200"

def test_contacts_page():
    response = requests.get(f"{BASE_URL}/contacts")
    assert response.status_code == 200, "Contacts page did not return status code 200"

def test_add_contact_page():
    response = requests.get(f"{BASE_URL}/contacts/add")
    assert response.status_code == 200, "Add contact page did not return status code 200"

def test_edit_contact_page():
    response = requests.get(f"{BASE_URL}/contacts/edit/1")
    assert response.status_code in [200, 404], "Edit contact page returned an unexpected status code"