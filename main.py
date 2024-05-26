from database import PollDatabase
from poll import Poll
from authentication.authentication import Authentication
from report.report import ReportGenerator
from user.user import User
def main():
    db = PollDatabase(server='DESKTOP-VIKK52P', database='PollingSystem_New')
    auth = Authentication(db)
    user_handler = User(db)
    
    logged_in = False
    user_id = None 

    while True:

        if not logged_in:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                try:
                    auth.register(username, password)
                    print("Registration successful.")
                except ValueError as e:
                    print(e)

            elif choice == "2":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if auth.login(username, password):
                    print("Login successful.")
                    logged_in = True
                else:
                    print("Invalid username or password.")

            elif choice == "3":
                break


            else:
                print("Invalid choice. Please try again.")

        else:
            print("\n4. Create a new poll")
            print("5. Update a poll question")
            print("6. Delete a poll")
            print("7. Vote in a poll")
            print("8. Show poll results")
            print("9. Show all polls")
            print("10. Generate report")
            print("11. View who voted for each option in a poll")
            print("12. Logout")
            print("13. Exit")
            choice = input("Enter your choice: ")

        

            if choice == "4":
                question = input("Enter the poll question: ")
                poll = Poll(db)
                poll.create(question)
                print(f"Poll created with ID: {poll.poll_id}")

                # Add exactly 3 options initially
                options = []
                for i in range(3):
                    option_text = input(f"Enter option {i+1} text: ")
                    options.append(option_text)
                poll.add_options(options)
                print("Three options added.")

            elif choice == "5":
                poll_id = int(input("Enter the poll ID: "))
                new_question = input("Enter the new poll question: ")
                poll = Poll(db, poll_id=poll_id)
                poll.update(new_question)

            elif choice == "6":
                poll_id = int(input("Enter the poll ID: "))
                poll = Poll(db, poll_id=poll_id)
                poll.delete()

            elif choice == "7":
                    poll_id = int(input("Enter the poll ID: "))
                    poll = Poll(db, poll_id=poll_id)
                    options = poll.choose()
                    print("Options:")
                    for option_id, option_text in options:
                        print(f"{option_id}. {option_text}")
                    option_id = int(input("Enter the option ID you want to vote for: "))
                    poll.vote(option_id)
                    print("Vote recorded successfully.")
                    db.commit()  # Commit the transaction after voting


            elif choice == "8":
                poll_id = int(input("Enter the poll ID: "))
                poll = Poll(db, poll_id=poll_id)
                poll.show_results()

            elif choice == "9":
                polls = Poll.show_all(db)
                for poll in polls:
                    print(f"{poll[0]}. {poll[1]}")
            
            elif choice == "10":
                # Generate report
                poll_id = int(input("Enter the poll ID: "))
                poll = Poll(db, poll_id=poll_id)
                report = ReportGenerator.generate_poll_results(poll)
                print(report)
            
            elif choice == "11":
                # View who voted for each option in a poll
                poll_id = int(input("Enter the poll ID: "))
                votes = user_handler.get_votes_for_poll(poll_id)
                print("Votes for each option:")
                for username, option_text in votes:
                    print(f"{username} voted for {option_text}")
            
            elif choice == "12":
                    logged_in = False
                    print("Logged out.")

            elif choice == "13":
                break

            else:
                print("Invalid choice. Please try again.")

    db.close()

if __name__ == "__main__":
    main()
