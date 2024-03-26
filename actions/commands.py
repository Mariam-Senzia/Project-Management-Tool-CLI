from projectManagement import ProjectManagement
project_management = ProjectManagement("projects.db")
from datetime import datetime

def exit_program():
    print("Goodbye!")
    exit()
    
#projects
def project_list():
    projects = project_management.get_all_projects()
    for project in projects:
        print(f"Project name: {project.project_name}, Description: {project.description}")

def find_project_by_id(): 
    id = input("Enter the project's id : ")

    project = project_management.get_project_by_id(id)
    if project:
        print(f"Project name: {project.project_name}, Description: {project.description}, Start date: {project.start_date}, End date: {project.end_date}")
        # print(project)
    else: 
        print(f"Project {id} not found")

def create_new_project():
    project_name = input("Enter project's name : ")
    description = input("Enter project's description : ")
    project_start_date = input("Enter project's start date  : ")
    project_end_date = input("Enter project's end date : ")
    try:
        project_start_date = datetime.strptime(project_start_date, "%Y-%m-%d").date()
        project_end_date = datetime.strptime(project_end_date, "%Y-%m-%d").date()

        project = project_management.add_project(project_name,description,project_start_date,project_end_date)
        print("Success: Project created.")
        print(f"Project name: {project.project_name}, Description: {project.description}, Start date: {project.start_date}, End date: {project.end_date}")

    except Exception as exc:
        print("Error creating project: ", exc)

def update_existing_project():
    id = input("Enter projects's id : ")
    if project  := project_management.get_project_by_id(id):
        try:
            project_name = input("Enter project's name : ")
            project.project_name = project_name

            description = input("Enter project's description : ")
            project.description = description

            project_start_date = input("Enter project's start date  : ")
            project_start_date = datetime.strptime(project_start_date, "%Y-%m-%d").date()
            # project.start_date = project_start_date

            project_end_date = input("Enter project's end date : ")
            project_end_date = datetime.strptime(project_end_date, "%Y-%m-%d").date()
            # project_end_date = project_end_date

            project_management.session.commit()
            print("Success: Project updated.")
            print(f"Project name: {project.project_name}, Description: {project.description}, Start date: {project.start_date}, End date: {project.end_date}")

        except Exception as exc:
            print("Error updating the project: ", exc)
    else:
        print(f"Project {id} not found")   

def delete_project():
    id = input("Enter the project's id : ")  
    if project := project_management.get_project_by_id(id):
        project_management.session.delete(project)
        print(f"Project {id} deleted")
    else:
        print(f"Project {id} not found")     

#team members
def team_members_list():
    members = project_management.get_all_team_members()
    for member in members:
        print(f"Name: {member.name}, Role: {member.role}")

def find_team_member_by_id(): 
    id = input("Enter the team member's id : ")

    member = project_management.get_member_by_id(id)
    if member:
        print(f"Name: {member.name}, Role: {member.role}")
    else: 
        print(f"Team member {id} not found")

def add_new_team_member():
    name = input("Enter team member's name : ")
    role = input("Enter team member's role : ")
    
    try:
        member = project_management.add_team_member(name,role)
        print("Success: Team member added.")
        print(f"Name: {member.name}, Role: {member.role}")

    except Exception as exc:
        print("Error adding new team member: ", exc)

def update_team_member():
    id = input("Enter team member's id : ")
    if member  := project_management.get_member_by_id(id):
        try:
            name = input("Enter team member's name : ")
            member.name = name

            role = input("Enter team member's role : ")
            member.role = role

            project_management.session.commit()
            print("Success: team member updated.")
            print(f"Name: {member.name}, Role: {member.role}")

        except Exception as exc:
            print("Error updating team member: ", exc)
    else:
        print(f"Team member {id} not found")  

def delete_team_member():
    id = input("Enter the team member's id : ")  
    if member := project_management.get_member_by_id(id):
        project_management.session.delete(member)
        print(f"Team member {id} deleted")
    else:
        print(f"Team member {id} not found")   


# Tasks  
def tasks_list():
    tasks = project_management.get_all_tasks()
    for task in tasks:
        print(f"Task: {task.description}, Due date: {task.due_date}, Status: {task.status}")

def find_tasks_by_project_id(): 
    id = input("Enter the project's id : ")

    tasks = project_management.get_tasks_by_project_id(id)
    if tasks:
        for task in tasks:
            print(f"Project id: {task.project_id},Team member id: {task.team_member_id}, Task: {task.description}, Status: {task.status}, Due date: {task.due_date}")
        
    else: 
        print(f"Tasks for project id {id} not found")

def find_tasks_by_team_member_id(): 
    id = input("Enter the team member's id : ")

    tasks = project_management.get_tasks_by_member_id(id)
    if tasks:
        for task in tasks:
            print(f"Project id: {task.project_id},Team member id: {task.team_member_id}, Task: {task.description}, Status: {task.status}, Due date: {task.due_date}")
        
    else: 
        print(f"Tasks for member id {id} not found")

def create_new_task():
    project_id= input("Enter project's id : ")
    team_member_id = input("Enter team member id : ")
    description = input("Enter task  : ")
    status = input("Enter status(In progress or Done) : ")
    due_date = input("Enter due date : ")
    
    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()

        task = project_management.add_task(project_id,team_member_id,description,status,due_date)
        print("Success: Task created.")
        print(f"Project id: {task.project_id},Team member id: {task.team_member_id}, Task: {task.description}, Status: {task.status}, Due date: {task.due_date}")

    except Exception as exc:
        print("Error creating task: ", exc)

def update_existing_task():
    id = input("Enter task's id : ")
    if task  := project_management.get_task_by_id(id):
        try:
            project_id = input("Enter project's id : ")
            task.project_id = project_id

            team_member_id = input("Enter team member's id : ")
            task.team_member_id = team_member_id

            task_description = input("Enter task's description : ")
            task.description = task_description

            status = input("Enter satus(In progress or Done)  : ")
            task.status = status

            due_date = input("Enter project's due date : ")
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()

            project_management.session.commit()
            print("Success: Task updated.")
            print(f"Project id: {task.project_id},Team member id: {task.team_member_id}, Task: {task.description}, Status: {task.status}, Due date: {task.due_date}")

        except Exception as exc:
            print("Error updating the task: ", exc)
    else:
        print(f"Task {id} not found")   

def delete_task():
    id = input("Enter the task's id : ")  
    if task := project_management.get_task_by_id(id):
        project_management.session.delete(task)
        print(f"Task {id} deleted")
    else:
        print(f"Task {id} not found")     

#milestones
def milestone_list():
    milestones = project_management.get_all_milestones()
    for milestone in milestones:
        print(f"Milestone: {milestone.milestone} ,Description: {milestone.description}, Due date: {milestone.due_date}")

def find_milestone_by_project_id(): 
    id = input("Enter the project's id : ")

    milestones = project_management.get_milestone_by_project_id(id)
    if milestones:
        for miles in milestones:
            print(f"Milestone: {miles.milestone} ,Description: {miles.description}, Due date: {miles.due_date}")
        
    else: 
        print(f"Milestone for project id {id} not found")
