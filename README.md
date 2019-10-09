# Credit application

## About program
This program is about creating loan application. It is a simulation with simple algorithm of granting/rejecting 
application of loan.

## Running the program
When you run the program you can see the menu with a few points to choose:
1. Create a loan application
2. Show history
3. Search customer
4. Check customer
5. Quit

Entering one of the above points you can get the following information:
1. Start a full credit application and at the end get the decision of bank if your loan application was accepted or rejected
2. You can show all loans applications and choose one to learn more about it
3. You can find some specific client by putting down their pesel number
4. You can check the client by putting down their pesel number if he or she is in the red or blacklisted
5. Quit the program

## Database
In the database folder you can find 2 sql files. One of them is empty schema script with code to create empty tables 
and stored procedures to easier fill in the tables from the SQL Server level, if it is needed.
The another sql file is with a few example records which I introduced creating a loan application. 
You can use them to check how the program works or create your own loan applications

## Connector python with database
To connect Python with database this program uses module pyodbc.
Click the link below to see the pyodbc documentation:
https://github.com/mkleehammer/pyodbc/wiki