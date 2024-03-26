# Project Management System with CLI and ORM

## Description
This project is a Command-Line Interface (CLI) and Object-Relational Mapping (ORM) based project management system developed in Python. It serves as a tool for managing projects, tasks, milestones, and team members efficiently.

## Features
- **CLI Application**: Provides a user-friendly command-line interface for managing projects, tasks, milestones, and team members.
- **ORM with SQLAlchemy**: Utilizes SQLAlchemy ORM to create and manage a relational database with tables representing projects, tasks, milestones, and team members.
- **Project Management Capabilities**: Allows users to create, update, and delete projects, tasks, milestones, and team members.
- **Virtual Environment Management**: Maintains a well-organized virtual environment using Pipenv for dependency management.
- **Proper Package Structure**: Follows a structured package layout to ensure modularity and maintainability of the application.
- **Utilization of Python Data Structures**: Uses lists, dictionaries, and tuples effectively throughout the application.

## Major Learning Goals
- Develop a project management system that provides essential functionalities for managing projects and tasks effectively.
- Implement and manipulate a relational database using SQLAlchemy ORM to store project-related data.
- Demonstrate proficiency in virtual environment management using Pipenv.
- Establish a proper package structure to ensure scalability and maintainability of the application.
- Utilize Python data structures such as lists, dictionaries, and tuples to manage and manipulate project data efficiently.

## Relationships
The application's ORM includes the following relationships:
- One-to-Many Relationship: Between projects and tasks, where each project can have multiple tasks.
- One-to-Many Relationship: Between projects and milestones, where each project can have multiple milestones.
- Many-to-One Relationship: Between tasks and team members, where many tasks can be assigned to one team member.

## Usage
To run the project management system, follow these steps:
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install dependencies using Pipenv: `pipenv install`.
4. Activate the virtual environment: `pipenv shell`.
5. Run the CLI application: `python cli.py`.