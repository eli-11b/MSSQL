#connect
import pymssql  
conn = pymssql.connect(server='yourserver.database.windows.net', user='yourusername@yourserver', password='yourpassword', database='AdventureWorks')  
cursor = conn.cursor() 


#execute query
import pymssql  
conn = pymssql.connect(server='yourserver.database.windows.net', user='yourusername@yourserver', password='yourpassword', database='AdventureWorks')  
cursor = conn.cursor()  
cursor.execute('SELECT c.CustomerID, c.CompanyName,COUNT(soh.SalesOrderID) AS OrderCount FROM SalesLT.Customer AS c LEFT OUTER JOIN SalesLT.SalesOrderHeader AS soh ON c.CustomerID = soh.CustomerID GROUP BY c.CustomerID, c.CompanyName ORDER BY OrderCount DESC;')  
row = cursor.fetchone()  
while row:  
    print str(row[0]) + " " + str(row[1]) + " " + str(row[2])     
    row = cursor.fetchone()  

    
#insert a row
import pymssql  
conn = pymssql.connect(server='yourserver.database.windows.net', user='yourusername@yourserver', password='yourpassword', database='AdventureWorks')  
cursor = conn.cursor()  
cursor.execute("INSERT SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) OUTPUT INSERTED.ProductID VALUES ('SQL Server Express', 'SQLEXPRESS', 0, 0, CURRENT_TIMESTAMP)")  
row = cursor.fetchone()  
while row:  
    print "Inserted Product ID : " +str(row[0])  
    row = cursor.fetchone()  
conn.commit()
conn.close()

#rollback a transaction
import pymssql  
conn = pymssql.connect(server='yourserver.database.windows.net', user='yourusername@yourserver', password='yourpassword', database='AdventureWorks')  
cursor = conn.cursor()  
cursor.execute("BEGIN TRANSACTION")  
cursor.execute("INSERT SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) OUTPUT INSERTED.ProductID VALUES ('SQL Server Express New', 'SQLEXPRESS New', 0, 0, CURRENT_TIMESTAMP)")  
conn.rollback()  
conn.close()

    
