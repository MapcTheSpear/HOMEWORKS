import sqlite3

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)


connection = create_connection('hw8.db')

cursor = connection.cursor()
if connection:
    cicle = True
    while cicle:
        print('\nYou can print list of employees by city id. Type 0 to exit')
        print("List of id's and cities: \n1.Krasnodar \n2.Pekin \n3.Tokyo \n4.Moscow \n5.Hangzhou"
              "\n6.Hiroshima \n7.St.Petersburg")
        try:
            choice = int(input('\nEnter id of city: '))
        except ValueError:
            print('Enter number only!')
            continue
        cursor.execute('''
            SELECT employees.first_name, employees.last_name, countries.title, cities.title, cities.area
            FROM employees
            INNER JOIN cities ON employees.city_id = cities.id
            INNER JOIN countries ON cities.country_id = countries.id
            WHERE cities.id = ?
        ''', (choice,))
        results = cursor.fetchall()
        if results:
            print("|Имя\tФамилия\tСтрана\tГород проживания\tПлощадь города|\n")
            for row in results:
                first_name, last_name, country, city, area = row
                print(f"|{first_name}\t{last_name}\t{country}\t{city}\t{area}|")
        elif choice == 0:
            print('Exiting...')
            cicle = False
        else:
            print("Нет сотрудников, проживающих в выбранном городе.\n")
    connection.commit()
    connection.close()



