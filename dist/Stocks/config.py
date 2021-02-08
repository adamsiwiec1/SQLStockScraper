import pyodbc

sqlConnection = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-FMRK48D\SQLSERVER2019;'
                      'Database=stock_db;'
                      'Trusted_Connection=yes;')
