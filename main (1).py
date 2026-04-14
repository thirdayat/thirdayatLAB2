def main_menu():
    students = [] 
    
    while True:
        print("\n--- Student Management System ---")
        print("1. Create Student Record")
        print("2. Display All Students")
        print("3. Update Student Skill")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == '1':
            
            name = input("Enter Name: ")
            year = int(input("Enter Year Level: "))
            
            section = ("CPE106L", "A") 
            
            skills = input("Enter skills (comma separated): ").split(",")
            
            student = {
                "name": name,
                "year": year,
                "section": section,
                "skills": [s.strip() for s in skills]
            }
            students.append(student)
            print("Record created successfully!")

        elif choice == '2':
            
            if not students:
                print("No records found.")
            for i, s in enumerate(students):
                print(f"{i+1}. {s['name']} | Year: {s['year']} | Skills: {', '.join(s['skills'])}")

        elif choice == '3':
            
            if students:
                idx = int(input("Enter student number to update: ")) - 1
                new_skill = input("Enter new skill to add: ")
                students[idx]["skills"].append(new_skill)
                print("Skill updated!")
            else:
                print("Nothing to update.")

        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()