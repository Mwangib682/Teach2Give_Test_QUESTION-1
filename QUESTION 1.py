"""
QUESTION 1: Write a query that will display the results below (Note: some columns might be renamed 
but use the column names above). It should only show 2020 data and order by driver 
points.
"""



import sqlite3

# Connecting to the SQLite database
conn = sqlite3.connect('Race_Results_database.db')
cursor = conn.cursor()

# SQL query to fetch results for the year 2020 and order by points (SQL Query)
query = """
SELECT 
    circuits.circuit_location, 
    results.grid, 
    results.position, 
    results.fastest_lap, 
    results.points, 
    drivers.driver_name, 
    races.race_name, 
    results.race_time, 
    races.race_year, 
    constructors.team_name, 
    races.race_date
FROM 
    results
JOIN 
    drivers ON results.driver_number = drivers.driver_number
JOIN 
    races ON results.race_year = races.race_year
JOIN 
    circuits ON races.circuit_id = circuits.circuit_id
JOIN 
    constructors ON results.team_id = constructors.constructor_id
WHERE 
    races.race_year = 2020
ORDER BY 
    results.points DESC;
"""

# Executing the query
cursor.execute(query)

# Fetching all results
results = cursor.fetchall()

# Displaying the results
for row in results:
    print(row)

# Closing the connection
conn.close()