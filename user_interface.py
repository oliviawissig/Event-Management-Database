"""
This is the user interface where the program interacts with the user.
USAGE: 1. Go to sqlconfig.conf file and change the username and password
          values to the ones from you are using in your mysql instance
       2. Open a terminal windows and run the following command:
       python3 user_interface.py
NOTE: Only option 3 and 4 from the menu is implemented so students can
      understand the flow of the program as a base to
      implement the rest of the options
"""
import mysql.connector
import hashlib

global user_type

def show_menu():
    """
    Prints in console the main menu
    :return: VOID
    """
    print("\nUser Menu \n"
          "1. Create Account \n" #done
          "2. Login \n" #done
          "3. Search \n" #implemented already
          "4. Insert \n" #implemented already
          "5. Update \n" #done
          "6. Delete \n" #done
          "7. Exit \n") #implemented already


def show_table_names(tables):
    """
    Show all the tables names
    :param tables: a list with the tables names.
                   You can get it by calling the method
                   get_table_names() from DB object
    :return: VOID
    """
    index = 1
    print("\nTables:")
    for table in tables:
        print(table[0])  # print tables names
        index += 1

def show_column_names(db_object, table):
    cols = db_object.get_column_names(table)
    print()
    index = 0
    for c in cols:
        print(cols[index][0])
        index+=1
    print()

def show_entire_table(db_object, table):
    elements = db_object.select("""SELECT * FROM {}""".format(table))
    cols = db_object.get_column_names(table)

    print()
    index = 0
    for c in cols:
        print(cols[index][0], end='\t\t')
        index+=1
    print()

    index = 0
    index2 = 0
    for e in elements:
        print(end='\t')
        for e in elements[0]:
            print(elements[index][index2], end='\t\t\t')
            index2+=1
        print()
        index+=1
        index2 = 0
    print()

def option1(db_object, tables):
    """
    Create Account option
    """
    print("\nWhich type of account would you like to create?\n"
          "1. Attendee\n"
          "2. Event Organizer\n"
          "3. Employee\n"
          "4. Venue Organizer\n"
          "5. Exit\n")
    try:
        acc_type = input("Select an account: ")

        username = input("Enter a username: ")
        password = input("Enter your password: ")
        name = input("Enter your first and last name: ")
        email = input("Enter your email: ")

        #gets user_id values from largest to smallest
        query = """SELECT {} FROM {} ORDER BY {} DESC""".format("user_id", "user", "user_id")
        results = db_object.select(query=query, values=None)

        user_id = results[0][0]
        user_id += 1

        user_id = str(user_id)

        columns = db_object.get_column_names("user")  # get columns names for the table selected
        values = [user_id, name, email]

        attributes = []
        index = 0
        for c in columns:
            attributes.append(columns[index][0])
            index += 1

        if db_object.insert(table="user", attributes=attributes, values=values):
            db_object.write_insert_transaction(table="user", attributes=attributes, values=values, file="transactions.sql")
            print("User successfully added!")

        #gets user_id values from largest to smallest
        query = """SELECT {} FROM {} ORDER BY {} DESC""".format("account_id", "account", "account_id")
        results = db_object.select(query=query, values=None)

        account_id = results[0][0]
        account_id += 1
        account_id = str(account_id)

        columns = db_object.get_column_names("account")  # get columns names for the table selected
        values = [account_id, username, password, acc_type, user_id]

        attributes = []
        index = 0
        for c in columns:
            attributes.append(columns[index][0])
            index += 1

        if db_object.insert(table="account", attributes=attributes, values=values):
            db_object.write_insert_transaction(table="account", attributes=attributes, values=values, file="transactions.sql")
            print("Account successfully created!")
        
    except (mysql.connector.Error, Exception) as e:
        print("Error when creating account!")
        print(e)

def option2(db_object, tables):
    """
    Login option
    """
    try:
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            acc = db_object.getAcc(username)

            acc_password = acc[0][0]
            acc_user = acc[0][1]

            #encrypt input password to match db password
            password = hashlib.md5(password.encode())

            if acc_password != password.hexdigest():
                print("Wrong username or password.")
                break
            else:
                user = db_object.getUser(acc_user)
                name = user[0][0]
                print(user)
                print("\nYou are logged in as {}!".format(name))

                #acc = self.select(query="""SELECT password, user FROM account WHERE username = %s""", values=username)
                user_type_results = db_object.select(query="""SELECT type FROM account WHERE username = %s""", values=username)
                user_type = user_type_results[0][0]
                break
    except (mysql.connector.Error, Exception) as e:
        print("Error while logging in!")
        print(e)

"""
One thing you may implement to solve the permissions issue is to create a table (permissions) 
in your database model with the following attributes table_name, role.
Then you insert manually in your inserts.sql file something like this:
INSERT INTO permissions (table_name, role) VALUES (“maintenance”, “admin”);
INSERT INTO permissions (table_name, role) VALUES (“blocks”, “general_user”);
So you insert all the permissions and then when you run the program and the user creates an account 
and login, you just execute a select to show only the tables for which that user role has permissions
"""

def option3(db_object, tables):
    """
    Search option
    :param db_object: database object
    :param tables: the name of the tables in the database
    :return: VOID
    """
    try:
        # shows that tables names in menu
        show_table_names(tables)

        # get user input
        table_selected = input("\nSelect a table to search: ")
        attribute_selected = input("Search by attribute (i.e name): ")
        value_selected = input("Enter the value: ")

        columns = db_object.get_column_names(table_selected)  # get columns names for the table selected

        # build queries with the user input
        query = """SELECT * FROM {} WHERE {} = %s""".format(table_selected, attribute_selected)

        if table_selected == "track":  # only if the table selected is track because we want to join
            query = """SELECT album.title as AlbumTitle, artist.name, track.id, track.length, track.title FROM track 
                           JOIN album ON album.id = track.album_id
                           JOIN Artist ON artist.id = track.artist_id
                           WHERE track.{} = %s""".format(attribute_selected)
        value = value_selected

        # get the results from the above query
        results = db_object.select(query=query, values=value)
        column_index = 0

        # print results
        print("\n")
        print("Results from: " + table_selected)
        for column in columns:
            values = []
            for result in results:
                values.append(result[column_index])
            print("{}: {}".format(column[0], values) ) # print attribute: value
            column_index+= 1
        print("\n")

    except (mysql.connector.Error, Exception) as err:  # handle error
        print("The data requested couldn't be found\n")



# option 4 when user selects insert
def option4(db_object, tables):
    try:
        # show tables names
        show_table_names(tables)

        # get user input for insert
        table = input("\nEnter a table to insert data: ")
        show_column_names(db_object, table)
        attributes_str = input("Enter the name attribute/s separated by comma? ")
        values_str = input("Enter the values separated by comma: ")

        # from string to list of attributes and values
        if "," in attributes_str:  # multiple attributes
            attributes = attributes_str.split(",")
            values = values_str.split(",")
        else:  # one attribute
            attributes = [attributes_str]
            values = [values_str]

        if db_object.insert(table=table, attributes=attributes, values=values):
            db_object.write_insert_transaction(table, attributes, values, "transactions.sql")
            print("Data successfully inserted into {} \n".format(table))

    except (mysql.connector.Error, Exception) as e: # data was not inserted, then handle error
        print("Error:", values_str, "failed to be inserted in ", table, "\n")
        print(e)

def option5(db_object, tables):
    """
    Update option
    """
    try:
        show_table_names(tables)

        # get user input for insert
        table = input("\nEnter a table to update data: ")

        show_column_names(db_object, table)
        show_entire_table(db_object, table)

        attribute = input("Enter the attribute to update: ")

        temp = db_object.get_column_names(table)
        table_id = temp[0][0]

        selected_id = input("For which {}?: ".format(table_id))
        value = input("Enter the new value: ")

        #UPDATE user SET user_id = 4 WHERE name = 'Olivia';
        query = """UPDATE {} SET {} = %s WHERE {} = {}""".format(table, attribute, table_id, selected_id)

        if db_object.update(query, values=value):
            db_object.write_transaction(query, value, "transactions.sql")
            print("Data successfully updated for {} \n".format(table))

    except (mysql.connector.Error, Exception) as e:
        print("Error while updating data!")
        print(e) 


def option6(db_object, tables):
    """
    Delete option
    """
    try:
        show_table_names(tables)

        # get user input for insert
        table = input("\nEnter a table to delete data from: ")
        
        show_entire_table(db_object, table)

        attribute = input("Enter the attribute of the data you wish to delete: ")

        #temp = db_object.get_column_names(table)
        #table_id = temp[0][0]

        value = input("Enter the value of the row you wish to delete: ")

        #DELETE FROM user WHERE email = 'ahart@mail.sfsu.edu';
        query = """DELETE FROM {} WHERE {} = %s""".format(table, attribute)

        if db_object.delete(query, value):
            db_object.write_transaction(query, value, "transactions.sql")
            print("Data successfully deleted from {} \n".format(table))
    except (mysql.connector.Error, Exception) as e:
        print("Error while deleting data!")
        print(e)


##### Driver execution.....
from database import DB

print("Setting up the database......\n")

# DB API object
db = DB(config_file="sqlconfig.conf")

# create a database (must be the same as the one is in your config file)
database = "EventManagementDB"
if db.create_database(database=database, drop_database_first=True):
    print("Created database {}".format(database))
else:
    print("An error occurred while creating database {} ".format(database))

# create all the tables from databasemodel.sql
db.run_sql_file("EventManagementDB.sql")

# insert sample data from insert.sql
db.run_sql_file("insert.sql")

db.encrypt_passwords()

if int(db._transactions) == 1:
    db.run_sql_file("transactions.sql")
    print("\nSet up process finished with queries from transactions.sql")
else:
    print("\nSet up process finished")


tables = db.get_table_names()
show_menu()
option = int(input("Select one option from the menu: "))
while option != 7:
    if option == 1:
        option1(db, tables)  # create account
    elif option == 2:
        option2(db, tables)  # login
    elif option == 3:
        option3(db, tables)
    elif option == 4:
        option4(db, tables)
    elif option == 5:
        option5(db, tables) #update
    elif option == 6:
        option6(db, tables) #delete
    show_menu()
    option = int(input("Select one option from the menu: "))
