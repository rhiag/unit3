"""Queries for Part 2 and 3"""

import sqlite3

# Connecting to the database
conn = sqlite3.connect("./northwind_small.sqlite3")
curs = conn.cursor()

# Executing queries
"""Part2 - The Nothwind Database"""

curs.execute("""SELECT *
                FROM Product
                ORDER BY UnitPrice DESC
                LIMIT 10;
            """)
expensive_items = curs.fetchall()

curs.execute("""SELECT AVG(hd - bd) AS avg_hire_age
                FROM
                ( SELECT BirthDate AS bd , HireDate AS hd FROM Employee);
            """)
avg_hire_age = curs.fetchall()

curs.execute("""SELECT City, AVG(hd - bd) AS avg_hire_age
                FROM (select BirthDate AS bd ,HireDate AS hd ,City
                FROM Employee)
                GROUP BY City;
            """)
avg_age_by_city = curs.fetchall()

"""Part 3 - Sailing the Northwind Seas"""

curs.execute("""SELECT p.ProductName, p.UnitPrice, s.CompanyName
                FROM Product AS p
                JOIN Supplier AS s
                ON p.SupplierId = s.Id
                ORDER BY p.UnitPrice DESC
                LIMIT 10;
            """)
ten_most_expensive = curs.fetchall()


curs.execute("""SELECT c.CategoryName,
                       COUNT(DISTINCT(p.ProductName)) AS unique_products
                FROM Product as p
                JOIN Category as c
                ON p.CategoryId = c.Id
                GROUP BY c.CategoryName
                ORDER BY unique_products DESC
                LIMIT 1;""")
largest_category = curs.fetchall()

curs.execute("""SELECT e.Id,
                       e.FirstName,
                       e.LastName,
                       count(et.TerritoryId) AS territory_count
                FROM Employee AS e
                JOIN EmployeeTerritory AS et
                ON e.Id = et.EmployeeId
                GROUP BY e.Id
                ORDER BY territory_count DESC
                LIMIT 1;
            """)
most_territories = curs.fetchall()
curs.close()

# Printing Results
print("The 10 most expensive items are: ", expensive_items)
print("Average hire age is : ", avg_hire_age)
print("Average hire age by city :", avg_age_by_city)
print("--------------------------------------------------")
print("The 10 most expensive products and its Suppliers: ", ten_most_expensive)
print("the Largest Category is :", largest_category)
print("Employee with the most territories: ", most_territories)
