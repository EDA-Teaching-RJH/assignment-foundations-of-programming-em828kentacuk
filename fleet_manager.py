name = ["Picard", "Riker", "Data", "Worf"]
rank = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
division = ["Command", "Command", "Operations", "Security"]
id = [1, 2, 3, 4]

def main():


    while True:

        print("Please select an option: ")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Update Rank")
        print("5. View Crew")
        print("6. Display Roster")
        print("7. Search Crew")
        print("8. Filter by Division")
        print("9. Calculate Payroll")
        print("10 Count officers by Rank")
        option = input("Select option: ")

        if option == "2": 

            new_name = input("Enter crew member's name: ")
            new_rank = input("Enter crew member's rank: ")
            new_division = input("Enter crew member's division: ")
            new_id = int(input("Enter crew member's ID: "))
            name.append(new_name)
            if rank != "Captain" and rank != "Commander" and rank != "Lt. Commander" and rank != "Lieutenant":
                print("Invalid rank. Please enter a valid rank.")
                continue
            rank.append(new_rank)
            if division != "Command" and division != "Operations" and division != "Security":
                print("Invalid division. Please enter a valid division.")
                continue
            division.append(new_division)
            if new_id in id:
                print("ID already exists. Please enter a unique ID.")
                continue
            id.append(new_id)
            print("Crew member added.")

        elif option == "3":




main()
