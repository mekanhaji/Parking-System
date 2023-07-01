# Project Overview
> This project aims to develop a comprehensive parking management system using Flask, SQLite, and Bootstrap. The system provides an efficient and user-friendly solution for managing parking spaces, vehicle records, and payments. By leveraging the power of Flask's web framework, the flexibility of SQLite as a lightweight database, and the responsive design capabilities of Bootstrap, It will create a seamless parking experience for both administrators and users.

# Technology Stack
- `Flask`: A Python-based web framework for building the server-side logic and RESTful APIs.
- `SQLite`: A lightweight and self-contained relational database management system for storing and retrieving data efficiently.
- `Bootstrap`: A popular HTML, CSS, and JavaScript framework for creating responsive and visually appealing user interfaces.

# Key Features
### User Registration and Authentication: 
The system allows users to create accounts and log in securely. This feature ensures that only authorized individuals can access the parking system and perform relevant actions.

### Parking Space Management
Administrators have the ability to manage parking spaces dynamically. They can add new parking slots, update availability status, and assign slots to specific users or vehicles. This functionality ensures efficient utilization of parking resources.

### Vehicle Registration and Records
Users are able to register their vehicles by providing necessary details such as vehicle type, license plate number, and owner information. The system will maintain a comprehensive record of all registered vehicles, facilitating seamless monitoring and identification.

### Parking Reservation `(Underdevelpment)`
Users can reserve parking spaces in advance, specifying the desired date and duration. This feature helps users plan their parking needs and guarantees a space upon arrival.

### Real-Time Parking Availability `(Underdevelpment)`
The system will display real-time information about available parking spaces. Users can check the availability status before arriving, saving time and reducing frustration.

### Payment Integration
The parking system will incorporate a secure payment gateway, enabling users to pay for their parking sessions online. Users will have options to choose from various payment methods, ensuring a hassle-free payment experience.

### Reporting and Analytics
Administrators will have access to comprehensive reports and analytics, including parking usage statistics, revenue generation, and historical data. These insights will help make informed decisions and optimize parking management strategies.

Flask App

```bash
pip install Flask Flask-SQLAlchemy Flask-WTF flask-login email_validator
```

```bash
pip install Flask
```
```bash
pip install -U Flask-SQLAlchemy
```
```bash
pip install -U Flask-WTF
```
```bash
pip install flask-login
```
```bash
pip install email_validator
```
