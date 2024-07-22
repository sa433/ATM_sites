
# ATM Sites Management using Django and Python

This project involves developing a Django application to manage ATM site data, allowing users to upload and manage site data via an Excel file and interface. The application includes models for ATMSite, State, and City, with fields for site name, site ID, address, and JSON-encoded contact details. Users can view detailed site information on web pages. The tech stack used is Python, Django, and MySQL.


## Getting Started

**Dependencies**

To run the project, ensure you have the following packages installed:

Django: for web framework functionality
pymysql: for MySQL database connectivity
openpyxl: for Excel file handling
## Execution Instructions

1. Input File Format: Prepare an Excel file containing the following fields for each ATM site entry:

Branch ID
Branch Name
Branch Address
Branch City
Branch State
Manager Details (in JSON format) including:
Branch Manager Name
Branch Manager Phone
Branch Manager Email

2. Running the Django Project:

Open your terminal and navigate to the project directory.
Execute the command: 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
This command starts the Django development server, allowing you to interact with the ATM site management application through API endpoints.
## Endpoints Overview:

Create ATM Site: Allows users to add new ATM sites to the database.
Read ATM Site: Retrieves information about existing ATM sites.
Update ATM Site: Modifies details of an existing ATM site.
Delete ATM Site: Removes an ATM site from the database.
## Note

Ensure that your Excel input file follows the specified format to seamlessly integrate new ATM sites into the system.
