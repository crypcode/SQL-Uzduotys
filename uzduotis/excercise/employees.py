import sqlite3


def open_connection():
    connection = sqlite3.connect("exercise.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection, cursor):
    cursor.close()
    connection.close()

# Metodas queriams rasyti sutrumpintas
def query_database(query, params = None):
    try:
        connection, cursor = open_connection()
        if params:
            cursor.execute(query)
            connection.commit()
        else:
            for row in cursor.execute(query):
                print(row)
    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        close_connection(connection, cursor)


def get_employes_filter1():
    query = """SELECT first_name, last_name, salary, job_id  FROM employees 
    WHERE salary < 10000 or salary < 15000 """
    query_database(query)

# get_employes_filter1()

def get_employes_filter2():
    query = """SELECT first_name, last_name, department_id  FROM employees
    WHERE department_id = 30 or department_id = 100
    ORDER BY department_id ASC """
    query_database(query)

# get_employes_filter2()

def get_employes_filter3():
    query = """SELECT first_name, last_name, department_id, salary  FROM employees
    WHERE (department_id = 30 or department_id = 100) AND (salary <10000 or salary > 15000)   """
    query_database(query)

# get_employes_filter3()

def get_employes_filter4():
    query = """SELECT first_name  FROM employees
    WHERE (first_name LIKE "%b%") AND (first_name LIKE "%c%")  """
    query_database(query)

# get_employes_filter4()

def get_employes_filter5():
    query = """SELECT last_name, job_id, salary  FROM employees
    WHERE (job_id = "IT_PROG" OR job_id = "SH_CLERK" ) AND (NOT salary =  4500 or 10000 or 15000)  """
    query_database(query)

# get_employes_filter5()

def get_employes_filter6():
    query = """SELECT last_name FROM employees
    WHERE LENGTH(last_name) = 6  """
    query_database(query)

# get_employes_filter6()


def get_employes_filter7():
    query = """SELECT last_name FROM employees
    WHERE last_name LIKE "___e%"  """
    query_database(query)

# get_employes_filter7()


#  Sekanti uzduociu dalis

def get_employes_filter8():
    query = """SELECT DISTINCT job_id FROM employees
    ORDER BY job_id ASC  """
    query_database(query)

# get_employes_filter8()

def get_employes_filter9():
    query = """SELECT SUM(salary) AS total_salary FROM employees"""
    query_database(query)

# get_employes_filter9()

def get_employes_filter10():
    query = """SELECT MIN(salary) AS min_salary FROM employees"""
    query_database(query)

# get_employes_filter10()

def get_employes_filter11():
    query = """SELECT MAX(salary) AS max_salary FROM employees"""
    query_database(query)

# get_employes_filter11()


def get_employes_filter12():
    query = """SELECT AVG(salary), COUNT(employee_id), department_id FROM employees
    WHERE department_id = 90"""
    query_database(query)

# get_employes_filter12()


def get_employes_filter13():
    query = """SELECT MIN(salary), MAX(salary), AVG(salary), SUM(salary) FROM employees"""
    query_database(query)

# get_employes_filter13()

def get_employes_filter14():
    query = """SELECT job_id, count(*) as samejob FROM employees GROUP BY job_id"""
    query_database(query)

# get_employes_filter14()

def get_employes_filter15():
    query = """SELECT MAX(salary) - MIN(salary) as difference FROM employees"""
    query_database(query)

# get_employes_filter15()

def get_employes_filter16():
    query = """SELECT department_id, SUM(salary) FROM employees
    GROUP BY department_id """
    query_database(query)

# get_employes_filter16()

def get_employes_filter17():
    query = """SELECT job_id, AVG(salary) FROM employees
    WHERE job_id NOT IN (SELECT job_id FROM employees WHERE job_id ="IT_PROG")
    GROUP BY job_id """
    query_database(query)

# get_employes_filter17()


def get_employes_filter18():
    query = """SELECT manager_id, employee_id, MIN(salary) FROM employees
    GROUP BY manager_id"""
    query_database(query)

# get_employes_filter18()


# Part 3

def create_view():
    query = """CREATE VIEW IF NOT EXISTS names
            as
            SELECT
                first_name,
                last_name
            FROM employees"""
    query_database(query)
    query_database("SELECT * FROM names")


create_view()

def get_all():
    query = "SELECT * FROM employees"
    querry_database(query)


def get_3_1():
    query = """SELECT first_name, last_name, salary  FROM employees
    WHERE salary > (SELECT salary FROM employees WHERE last_name="Bull")"""
    querry_database(query)


def get_3_2():
    query = """SELECT first_name, last_name, job_id, manager_id  FROM employees
    WHERE employee_id IN (SELECT manager_id FROM employees)"""
    querry_database(query)


def get_3_3():
    query = """SELECT first_name, last_name, salary FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees)"""
    querry_database(query)


def get_3_4():
    query = """SELECT first_name, last_name, salary FROM employees
        WHERE salary IN (SELECT MIN(salary) FROM employees)"""
    querry_database(query)


def get_3_5():
    query = """SELECT first_name, last_name, salary, job_id FROM employees
        WHERE salary > (SELECT AVG(salary) FROM employees WHERE manager_id IN (SELECT department_id from employees))"""
    querry_database(query)


# get_3_2()
# get_all()
# get_3_1()
# get_3_3()
# get_3_4()
# get_3_5()