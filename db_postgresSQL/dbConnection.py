#importing libraries
import psycopg2
  
# a function to connect to
# the database.
def connect():
  
    # connecting to the database called test
    # using the connect function
    try:
  
        conn = psycopg2.connect(database ="test", 
                            user = "postgres", 
                            password = "!QAZxsw2", 
                            host = "localhost", 
                            port = "5432")
  
        # creating the cursor object
        cur = conn.cursor()
      
    except (Exception, psycopg2.DatabaseError) as error:
          
        print ("Error while creating PostgreSQL table", error)
      
  
    # returning the conn and cur
    # objects to be used later
    return conn, cur
  
  
# a function to create the 
# emp table.
def create_table():
  
    # connect to the database.
    conn, cur = connect()
  
    try:
        # the test database contains a table called emp  
        # the schema : (id INTEGER PRIMARY KEY,  
        # name VARCHAR(10), salary INT, dept INT) 
        # create the emp table 
  
        cur.execute('CREATE TABLE emp (id INT PRIMARY KEY, name VARCHAR(10), salary INT, dept INT)')
  
        # the commit function permanently
        # saves the changes made to the database
        # the rollback() function can be used if
        # there are any undesirable changes and
        # it simply undoes the changes of the
        # previous query
      
    except:
  
        print('error')
  
    conn.commit() 
  
   
# a function to insert data
# into the emp table
def insert_data(id = 1, name = '', salary = 1000, dept = 1):
  
    conn, cur = connect()
  
    try:
        # inserting values into the emp table
        cur.execute('INSERT INTO emp VALUES(%s, %s, %s, %s)',
                                    (id, name, salary, dept))
      
    except Exception as e:
  
        print('error', e)
    # committing the transaction.
    conn.commit()
  
  
# a function to fetch the data 
# from the table
def fetch_data():
  
    conn, cur = connect()
  
    # select all the rows from emp
    try:
        cur.execute('SELECT * FROM emp')
      
    except:
        print('error !')
  
    # store the result in data
    data = cur.fetchall()
  
    # return the result
    return data
  
# a function to print the data
def print_data(data):
  
    print('Query result: ')
    print()
  
    # iterating over all the 
    # rows in the table
    for row in data:
  
        # printing the columns
        print('id: ', row[0])
        print('name: ', row[1])
        print('salary: ', row[2])
        print('dept: ', row[3])
        print('----------------------------------')
  
# function to delete the table
def delete_table():
  
    conn, cur = connect()
  
    # delete the table
    try:
  
        cur.execute('DROP TABLE emp')
  
    except Exception as e:
        print('error', e)
  
    conn.commit()
  
  
# driver function
if __name__ == '__main__':
  
    # create the table
  
    create_table()
  
    # inserting some values
    insert_data(1, 'adith', 1000, 2)
    insert_data(2, 'tyrion', 100000, 2)
    insert_data(3, 'jon', 100, 3)
    insert_data(4, 'daenerys', 10000, 4)
  
    # getting all the rows
    data = fetch_data()
  
    # printing the rows
    print_data(data)
  
    # deleting the table
    # once we are done with
    # the program
    #delete_table()
