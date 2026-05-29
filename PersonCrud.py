import pymysql

def connect_db():
    try:
        connection = pymysql.connect(user = 'root', password = 'route', port=3306, database='rakshitha', charset='utf8', host= 'localhost')
        print('DB connected')
        return connection
    except:
        print('DB connection failed')

def disconnect_db(connection):
    try:
        connection.close()
        print('DB disconnected')
    except:
        print('DB connection failed')


def create_table():
    query = 'create table IF NOT EXITS people(id int primary key auto_increment, name varchar(64) not null, gender bool not null, age int default(0) ,location varchar(32));'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)

        if count == 0:
            print('Table created')

        else:
            print('Table creation failed')
        cursor.close()
        disconnect_db(connection)

    except:
        print('Table creation error')

def create_database(connection):
    query = 'create table people(id int primary key auto_increment, name varchar(64) not null, gender bool not null, age int default(0) ,location varchar(32));'

    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)

        if count == 0:
            print('Table created')

        else:
            print('Table creation failed')
        cursor.close()
        disconnect_db(connection)

    except:
        print('Table creation error')

    create_table()

def read_person():
    name = input("Enter person name:")
    age = int(input("Enter person age:"))
    gender = input("Enter person gender (m/f):")
    location = input("Enter person location:")
    if gender.lower() == 'f' : 
        gender = True
    else:
        gender = False
    return (name, gender, age, location)

def create_person():
    query = 'insert into people(name, gender, location, age) values(%s, %s, %s, %s);'
    try:
        person = read_person
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query, person)

        if count == 1:
            print('Person created')

        else:
            print('Person creation failed')
        connection.commit()
        cursor.close()
        disconnect_db(connection)

    except:
        print('Person creation error')

    def create_person_demo():
     query = 'insert into people(name, gender, location, age) values("rakshitha", true, "bengaluru", 18);'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        print(f"count=", {count})
        if count == 0:
            print('Person created')

        else:
            print('Person creation failed')
        cursor.close()
        disconnect_db(connection)

    except Exception as e:
        print('Person creation error')

def search_person():
    pass

def delete_person():
    pass

def list_people():
    query = 'select * from people;'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)

        if count >= 1:
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            

        else:
            print('No person was found')
        connection.commit()
        cursor.close()
        disconnect_db(connection)

    except:
        print('Listing the people failed')

list_people()
