# Lab Activity 2: Strings, Lists, Tuples, and Dictionaries
**Course:** CPE106L-4 - Software Design Laboratory  
**Student Name:** Norberto Ayat III 
**Professor:** Dr. John De Guzman Tarampi  

## Description
This laboratory activity focuses on developing a **menu-driven Python program** to manage structured student data. The program demonstrates the practical application of core Python data types:
- **Strings:** Used for user input and data display.
- **Lists:** Used to store multiple student records.
- **Tuples:** Used for immutable data (e.g., Course Code and Section).
- **Dictionaries:** Used to structure individual student profiles.

## Program Features (CRUD Operations)
- **Create:** Allows the user to input new student details.
- **Read/Display:** Lists all students currently stored in the system.
- **Update:** Specifically allows adding new skills to a selected student's record.

## Project Structure
- `src/`: Contains `main.py` (the menu-driven logic).
- `tests/`: Contains screenshots of the three required test runs (Create, Read, Update).
- `README.md`: Documentation and execution instructions.

## How to Run the Activity
1. This activity was developed using **OneCompiler**.
2. Copy the code from `src/main.py`.
3. In OneCompiler, you **must** use the **STDIN** box to provide inputs before clicking 'Run'.
   - *Example STDIN input:*
     ```
     1 (to Create)
     Name
     Year
     Skills
     2 (to Display)
     4 (to Exit)
     ```
4. View the output in the console to verify the CRUD operations.

## Test Case Summary
1. **Test 1:** Successful creation of a single student record.
2. **Test 2:** Displaying multiple records to verify list storage.
3. **Test 3:** Updating a student's skills to verify dictionary modification.
