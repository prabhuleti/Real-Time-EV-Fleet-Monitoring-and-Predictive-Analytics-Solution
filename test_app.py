import requests

base_url = "http://127.0.0.1:5001"

def test_index():
    url = f"{base_url}/"
    data = requests.get(url)
    assert data.status_code == 200
    
def test_histogram():
    url = f"{base_url}/histogram.html"
    data = requests.get(url)
    assert data.status_code == 200
    
def test_login():
    url = f"{base_url}/login.html"
    data = requests.get(url)
    assert data.status_code == 200
    
def test_register():
    url = f"{base_url}/register.html"
    data = requests.get(url)
    assert data.status_code == 200
    
def test_forgot_password():
    url = f"{base_url}/forgot_password.html"
    data = requests.get(url)
    assert data.status_code == 200
    
def test_Battery_Health_Status_Section():
    url = f"{base_url}/Battery Health Status Section.html"
    data = requests.get(url)
    assert data.status_code == 200
    
def test_Cost_and_Energy_Consumption():
    url = f"{base_url}/Cost and Energy Consumption.html"
    data = requests.get(url)
    assert data.status_code == 200
    
def test_Display_Behavior_Analysis_and_Alerts():
    url = f"{base_url}/Display Behavior Analysis and Alerts.html"
    data = requests.get(url)
    assert data.status_code == 200
    
def test_Driver_Behavior_and_Maintenance_Alerts():
    url = f"{base_url}/Driver Behavior and Maintenance Alerts.html"
    data = requests.get(url)
    assert data.status_code == 200
    
def test_Report_Generation():
    url = f"{base_url}/Report Generation.html"
    data = requests.get(url)
    assert data.status_code == 200
    
def test_vehicle_registration():
    url = f"{base_url}/vehicle_Registration.html"
    data = requests.get(url)
    assert data.status_code == 200