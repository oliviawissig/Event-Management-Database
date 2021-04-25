### Event-Management-Database

One of the projects I completed as a senior at San Francisco State University. This code is old and it hasn't been managed since I graduated college.

To run this program, you'll have to change the password in the configuration file to your SQL password. Then run ```python3 user_interface.py``` in the same directory as these files. I use Python 3 to implement this program.

The two libraries used are
* mysql
* pymysql

From the user menu, these are your options:

#### Creating an account:

When selected, this prompts the user which account they are creating which is stored as an account_type when creating the user account. It this gathers user input for a username, password, name, and email and then inserts the new user into the database.

#### Logging in:

If this option is selected, it finds the user with the same username in the database, and verifies the password entered matches the one in the database. Then it shows the name that belongs to the username and password and displays the menu again.

#### Searching:

This displays a list of tables that the user can search in, then gathers user input for the name of the table they want to search, the attribute they want to search, and the value they are looking for in the attribute. If there is a result in the database, the results will show all the values and all the attributes for that specific search. If there is not data, the values with be empty (blank)

#### Inserting:

This displays a list of tables that the user can insert into, then gathers user input the table, attributes, and values they would like to insert. In order for the insert to be successful, it needs to match the database requirements (if 'Not Null', must not be left blank). If all the requirements are fulfilled, the data will be inserted and the user will be notified. If the insert fails, the user will be shown the error for the insert (e.g. which field was left blank, etc.).

#### Updating & Deleting:

Options 5 and 6 allow the user to update and delete objects in the database. If there is an error updating or deleting data, the user will be shown the SQL error. The user is shown the information in the database so they know exactly what they are updating/deleting. This was the most effective implementation I could think of since the user would not know what to delete otherwise. (Sorry if the formatting is ugly in these options...)

This program runs until it the user quits using option 7 (exit).
