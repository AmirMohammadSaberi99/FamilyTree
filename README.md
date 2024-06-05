# Family Tree Creator

A Python script to create and manage a family tree. Add family members, define parent-child relationships, and display family member details.

## Features

- Add family members
- Define parent-child relationships
- Display member details
- Display all members

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/family-tree-creator.git
    cd family-tree-creator
    ```

2. (Optional) Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

## Usage

1. Run the script:
    ```bash
    python main.py
    ```

2. Follow the on-screen instructions to interact with the family tree.

## Example

```plaintext
Family Tree Creator
1. Add Member
2. Add Relationship
3. Display Member
4. Display All Members
5. Exit
Enter your choice: 1
Enter the name: John Doe
Enter the gender (M/F): M
Enter the birth year: 1980
Added John Doe (M, 1980)

Family Tree Creator
1. Add Member
2. Add Relationship
3. Display Member
4. Display All Members
5. Exit
Enter your choice: 4
Name: John Doe
Gender: M
Birth Year: 1980
Parents: None
Children: None
--------------------
