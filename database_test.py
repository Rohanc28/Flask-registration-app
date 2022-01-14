
import db
menu_prompt = """\n\n--- Sports Tournament ---

Welcome to Sports Tournament, please register if you have not!

1) Register
2) Find registrant(s) detail by name
3) Find registrant(s) for specific sport
4) See all registrant(s)
5) Deregister User
6) Exit

your selection = """
sports = ["Cricket", "Football", "Basketball", "Tennis"]


def menu():
    connection = db.connect()
    db.create_table(connection)

    while (user_input := input(menu_prompt)) != "6":
        print(user_input)
        if user_input == "1":  # register
            first_name = input("Enter First name\n")
            while(first_name.isdigit()):
                print("Invalid name\n")
                first_name = input("Enter First name\n")
            last_name = input("Enter last name\n")
            while(last_name.isdigit()):
                print("Invalid name\n")
                last_name = input("Enter last name\n")
            email = input("Enter email\n")
            print("Select sport: \n")
            print(sports)
            select_sport = input()
            while(select_sport not in sports):
                print("Invalid sport\n")
                print("Select sport: \n")
                print(sports)
                select_sport = input()
            db.add_user(connection, first_name, last_name, email, select_sport)

            print("You have successfully registered!\n\n")

        elif user_input == "2":  # Find registrant detail by name
            first_name = input("Enter first name\n")
            last_name = input("Enter last name\n")
            u = db.get_user_name(connection, first_name, last_name)
            for _ in u:
                print(f"\t{_[1]} {_[2]}\t \t- \t{_[3]}\t,\t {_[4]}")

        elif user_input == "3":  # Find registratns for specific sport
            print("Select sport: \n")
            print(sports)
            sport = input("")
            u = db.sport_list(connection, sport)
            for _ in u:
                print(f"\t{_[1]} {_[2]}\t \t- \t{_[3]}\t,\t {_[4]}")

        elif user_input == "4":  # See all registrants
            u = db.get_all(connection)
            for _ in u:
                print(f"\t{_[1]} {_[2]}\t \t- \t{_[3]}\t,\t {_[4]}")

        elif user_input == "5":  # Deregister user by name
            first_name = input("Enter first name of user to deregister\n")
            while first_name == "":
                print("Invalid Name\n")
                first_name = input("Enter first name of user to deregister\n")
            last_name = input("Enter last name of user to deregister\n")
            while last_name == "":
                print("Invalid Name\n")
                last_name = input("Enter last name of user to deregister\n")
            db.drop_user_name(connection, first_name, last_name)
            print("User DELETED\n")

        else:
            print("Invalid Input\n")


menu()
