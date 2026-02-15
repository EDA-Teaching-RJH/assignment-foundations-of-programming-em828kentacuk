name = ["Spock", "Picard", "Riker", "Data", "Worf"]
rank = ["Captain", "Captain", "Commander", "Lt. Commander", "Lieutenant"]
division = ["Command", "Command", "Command", "Operations", "Security"]
id = [1, 2, 3, 4, 5]
id = [1, 2, 3, 4, 5]
salary = [1100, 1000, 800, 700, 600]


active = True

def main():

    while True:

        print("\n--- MENU ---")
        print("1. Display Roster")        
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Update Rank")
        print("5. Search Crew")
        print("6. Filter by Division")
        print("7. Calculate Payroll")
        print("8. Count officers by Commander or Captain ranks")
        option = input("Select option: ")

        if option == "1":

            for i in range(len(name)):
                print(" ")
                print(str(id[i]) + " - " + name[i] + " - " + rank[i] + " - " + division[i])  

        
        elif option == "2": 

            new_name = input("Enter crew member's name: ")
            new_rank = input("Enter crew member's rank: ")
            new_division = input("Enter crew member's division: ")
            new_id = int(input("Enter crew member's ID: "))


            name.append(new_name)

            if new_rank != "Captain" and new_rank != "Commander" and new_rank != "Lt. Commander" and new_rank != "Lieutenant":
                print("Invalid rank. Please enter a valid rank.")
                continue
            rank.append(new_rank)
            if new_division != "Command" and new_division != "Operations" and new_division != "Security":
                print("Invalid division. Please enter a valid division.")
                continue
            division.append(new_division)
            if new_id in id:
                print("ID already exists. Please enter a unique ID.")
                continue
            id.append(new_id)
            print("Crew member added.")

        elif option == "3":
            remove_id = int(input("Enter crew member's ID to remove: "))
            if remove_id not in id:
                print("ID not found. Please enter a valid ID.")
                continue
            index = id.index(int(remove_id))
            name.pop(index)
            rank.pop(index)
            division.pop(index)
            id.pop(index)
            print("Removed.")   

        elif option == "4":
            update_id = int(input("Enter Crew member's ID to update: "))
            if update_id not in id:
                print("ID not found. Please enter a valid ID.")
                continue
            print("Update rank to:")
            print("1 - Captain")
            print("2 - Commander")
            print("3 - Lt. Commander")
            print("4 - Liutenant")

            def update_from_user(id, rank):

                new_rank = input("Select new rank: ")
                if update_id == "1":
                    update_rank = rank.index(update_id)
                    rank[update_rank] = "Captain"
                
                elif update_id == "2":
                    update_rank = rank.index(update_id)
                    rank[update_rank] = "Captain"
                    
                
                elif update_id == "3":
                    update_rank = rank.index(update_id)
                    rank[update_rank] = "Lt. Commander"
            

                elif update_id == "4":
                    update_rank = rank.index(update_id)
                    rank[update_rank] = "Liutenant"
                     
            
            update_from_user(id, rank)
            print("Updated") 

        elif option == "5":
            search_crew_member = input("Enter crew member name: ")
            if search_crew_member in name:
                print (search_crew_member)
            elif search_crew_member not in name:
                print("Not found")    

        elif option == "6":
            
            print("Choose from:", ", ".join(division))
            filter_by_division = input("Enter division: ")

            match filter_by_division:
                    case "Command":
                        filter_by_division = "Picard", "Riker", "Spock"
                    case "Operations":
                        filter_by_division = "Data"
                    case "Security":
                        filter_by_division = "Worf"
            print(f"Output: {filter_by_division}")

        elif option == "7":

            total = sum(salary)
            print(f"Total crew cost: ${total}")

        elif option == "8":

            value = ("Captain")
            value_2 = ("Commander")
            count = rank.count(value)
            count2 = rank.count(value_2)
            total = count + count2

            print(f"Captain and Commanders appears {total} times in the list")
        
main()