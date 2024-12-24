# Real-Time EV Fleet Monitoring and Predictive Analytics Solution 

## Project Overview  
This project aims to develop a comprehensive **Real-Time Electric Vehicle (EV) Fleet Monitoring and Predictive Analytics Solution**. The system integrates various features to enhance the efficiency, reliability, and sustainability of EV fleet management by leveraging advanced technologies.This model predicts critical parameters such as battery health and driver behavior, and provides actionable insights to improve fleet performance, reduce costs, and ensure operational safety.

---

## Features  
### Admin Interface
1. **User Management**: Manage user accounts and roles.
2. **Fleet Management**: Register and manage vehicle details.
3. **System Settings**: Configure system-wide settings and preferences.

### User Interface
1. **Vehicle Registration**: Register new EVs and manage their details.
2. **Real-Time Monitoring**: Monitor vehicle data such as location, battery health, and operational status.
3. **Driver Behavior Analysis**: Analyze driving patterns and identify unsafe behaviors.
4. **Battery Health Monitoring**: Track battery performance and generate alerts for potential issues.

### Predictive Analytics Modules
1. **Route Optimization**: Suggest energy-efficient routes.
2. **Maintenance Alerts**: Predict maintenance requirements to prevent downtime.
3. **Cost and Energy Consumption Analysis**: Track operational costs and energy usage for fleet-wide optimization.

### Report Generation
- Generate detailed reports on vehicle performance, driver behavior, and fleet operations.
- Provide data visualizations for actionable insights.

---

## Technologies Used  
### **Frontend**  
- HTML, CSS, JavaScript  
- Chart.js for data visualization  

### **Backend**  
- Flask for server-side development  

### **Database**  
- SQLite (or any chosen relational database)

### **APIs**  
- Integration with third-party APIs for real-time data (e.g., location, weather, route optimization)

---

## Setup Instructions  
### Prerequisites  
1. Python 3.x installed on your system.  
2. Required Python packages (install via `pip`).  

### Installation Steps  
1. Clone the repository:  
   ```bash
   https://github.com/prabhuleti/Real-Time-EV-Fleet-Monitoring-and-Predictive-Analytics-Solution.git
   cd Real-Time-EV-Fleet-Monitoring-and-Predictive-Analytics-Solution
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:  
   ```bash
   python app.py
   ```
4. Open your browser and navigate to:  
   ```text
   http://127.0.0.1:5000/
   ```

---

## Usage

1. **Admin Panel**:
   - Log in as an administrator to manage users, vehicles, and system settings.

2. **Register Vehicles**:
   - Use the Vehicle Registration module to add new EVs to the system.

3. **Monitor Fleet**:
   - Track vehicle locations and operational metrics in real-time.

4. **Analyze Performance**:
   - Access predictive analytics for route optimization, battery health, and driver behavior.

5. **Generate Reports**:
   - Generate and download reports for performance reviews and decision-making.

---
---

## Project Structure  
```
project/
│
├── static/
│   └── styles.css
│
├── templates/
│   ├── Battery_Health_Status_Section.html
│   ├── Cost_and_Energy_Consumption.html
│   ├── cost_and_energy_trends.html
│   ├── Display_Behavior_Analysis_and_Alerts.html
│   ├── Driver_Behavior_and_Maintenance_Alerts.html
│   ├── forgot_password.html
│   ├── histogram.html
│   ├── index.html
│   ├── login.html
│   ├── optimize_route.html
│   ├── register.html
│   ├── Report_Generation.html
│   └── vehicle_registration.html
│
├── app.py
├── battery_health_model.pkl
├── battery_status_model.py
├── create_db.py
├── insert_data.py
├── LICENSE
├── README.md
├── retrieve_data.py
├── Tamilnadu_EV_Stations.pkl
├── test_app.py
└── vehicle_data.db

```

---

## Future Enhancements

1. **Integration with Cloud Platforms**:
   - Host data and analytics on cloud services like AWS or Azure for scalability.

2. **Enhanced Machine Learning Models**:
   - Improve predictive analytics for more accurate maintenance alerts and battery health predictions.

3. **Mobile Application**:
   - Develop a mobile app for fleet monitoring on the go.

---

## Contribution  
Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests.  

---

## License  
This project is licensed under the [MIT License](LICENSE).  

---

## Contact
For any queries or support, please contact:
- **Name:** Prabhuleti Venkata Ananth
- **Email:** ananthprabhuleti@gmail.com

---
