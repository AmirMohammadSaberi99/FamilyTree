from family_tree import FamilyTree

def main():
    family_tree = FamilyTree()

    while True:
        print("\nFamily Tree Creator")
        print("1. Add Member")
        print("2. Add Relationship")
        print("3. Display Member")
        print("4. Display All Members")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name: ").strip()
            gender = input("Enter the gender (M/F): ").strip()
            birth_year = input("Enter the birth year: ").strip()
            family_tree.add_member(name, gender, birth_year)
        elif choice == '2':
            parent_name = input("Enter the parent's name: ").strip()
            child_name = input("Enter the child's name: ").strip()
            family_tree.add_relationship(parent_name, child_name)
        elif choice == '3':
            name = input("Enter the name of the member to display: ").strip()
            family_tree.display_member(name)
        elif choice == '4':
            family_tree.display_all_members()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
