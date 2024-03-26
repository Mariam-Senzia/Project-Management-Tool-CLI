from projectManagement import ProjectManagement
from datetime import date


if __name__ == '__main__':

    technical_project_management = ProjectManagement("projects.db")

   
    # Add projects 
    technical_project_management.add_project("Shopify Project","Project to develop an e-commerce website",date(2024, 3,18),date(2024, 3,25))
    technical_project_management.add_project("Safety Project","Project to develop a women's safety app",date(2024, 3,1),date(2024, 3, 7))
    technical_project_management.add_project("Fitness Project","Project to develop a fitness tracking app",date(2024, 3,8),date(2024, 3,16))

    # Add team members
    technical_project_management.add_team_member("Frank Miller","Frontend Developer")
    technical_project_management.add_team_member("Grace Lee","Designer")
    technical_project_management.add_team_member("Harry Davis","Tester")
    technical_project_management.add_team_member("Teyanna Taylor","Backend Developer")
    technical_project_management.add_team_member("Alice Smith","Analyst")

    # Add tasks
    technical_project_management.add_task(1, 1,"Implement functional UI components and client side logic","In progress",date(2024,3,25)) 
    technical_project_management.add_task(1, 2,"Design the user interface and user experience of the app ","Done",date(2024,3,30)) 
    technical_project_management.add_task(2, 4,"Develop backend infrastructure and server side logic","In progress",date(2024,4,1)) 
    technical_project_management.add_task(2, 4,"Managing the application's database","Done",date(2024,4,1)) 
    technical_project_management.add_task(3, 3,"Conduct thorough testing and proceed with deployement to production","In progress",date(2024,3,25)) 
    technical_project_management.add_task(3, 5,"Analyze market trends and user feedback","In progress",date(2024,3,30)) 

    # Add milestones
    technical_project_management.add_project_milestone(1,"Design","Design and create visually appealing app",date(2024, 4,10))
    technical_project_management.add_project_milestone(2,"Development","Develop backend logic and functionality of the app",date(2024, 4,15))
    technical_project_management.add_project_milestone(3,"Testing and Deployment","Conduct thorough testing and deploy the app",date(2024, 4,15))

    # Get projects list
    # projects = technical_project_management.get_all_projects()
    #  print("****** projects ******")
    # for project in projects:
        # print(project.project_name)

    # team_members = technical_project_management.get_all_team_members()
    # # print("****** team members ******")
    # for member in team_members:
    #     print(member.name)

    # tasks = technical_project_management.get_all_tasks()
    # print("****** tasks ******")
    # for task in tasks:
    #     print(task.description)

    # milestones = technical_project_management.get_all_milestones()
    # print("****** milestones ******")
    # for milestone in milestones:
    #     print(f"{milestone.milestone}, description:{milestone.description}")

    # Get by id
    # print(technical_project_management.get_project_by_id(3))

    # print(technical_project_management.get_member_by_id(4))

    # print(technical_project_management.get_tasks_by_project_id(1))

    # print(technical_project_management.get_tasks_by_member_id(4))

    # print(technical_project_management.get_milestone_by_project_id(1))

    # Update
    # technical_project_management.update_milestone(1,"Design","Design and create visually appealing app",date(2024, 3,6)) date

    # technical_project_management.update_project(2,"Safety Project","Project to develop a safety app",date(2024, 3,1),date(2024, 3, 7))

    # technical_project_management.update_team_members(5,"Breana Smith","Analyst")

    #delete
    # technical_project_management.delete_project(3)