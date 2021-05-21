import pandas as pd
import pyodbc

# Read the flat file and create a Dataframe.
data = pd.read_csv (r'C:\Users\Bhavesh\Desktop\Test\Customer.csv',sep = '|')   
df = pd.DataFrame(data, columns= ['Name','Cust_I','Open_Dt','Consul_Dt','VAC_ID','DR_name','State','County','DOB','FLAG'])

# Connect to SQL Server. These details will depending on the Database server.
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=Bhavesh\SQLEXPRESS;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO TestDB.dbo.customer (Name,Cust_I,Open_Dt,Consul_Dt,VAC_ID,DR_name,State,County,DOB,FLAG)
                VALUES (?,?,?,?,?,?,?,?,?,?)
                ''',
                row.Name,
                row.Cust_I,
                row.Open_Dt,
                row.Consul_Dt,
                row.VAC_ID,
                row.DR_name,
                row.State,
                row.County,
                row.DOB,
                row.FLAG
                )
conn.commit()
