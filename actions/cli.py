from commands import (
    exit_program,
    project_list,
    find_project_by_id,
    create_new_project,
    update_existing_project,
    delete_project,
    team_members_list,
    find_team_member_by_id,
    add_new_team_member,
    update_team_member,
    delete_team_member,
    tasks_list,
    find_tasks_by_project_id,
    find_tasks_by_team_member_id,
    create_new_task,
    update_existing_task,
    delete_task,
    milestone_list,
    find_milestone_by_project_id
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            project_list()
        elif choice == "2":
            find_project_by_id()
        elif choice == "3":
            create_new_project()
        elif choice == "4":
            update_existing_project()
        elif choice == "5":
            delete_project()
        elif choice == "6":
            team_members_list()
        elif choice == "7":
            find_team_member_by_id()
        elif choice == "8":
            add_new_team_member()
        elif choice == "9":
            update_team_member()
        elif choice == "10":
            delete_team_member()
        elif choice == "11":
            tasks_list()
        elif choice == "12":
            find_tasks_by_project_id()
        elif choice == "13":
            find_tasks_by_team_member_id()
        elif choice == "14":
            create_new_task()
        elif choice == "15":
            update_existing_task()
        elif choice == "16":
            delete_task()
        elif choice == "17":
            milestone_list()
        elif choice == "18":
            find_milestone_by_project_id()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all projects")
    print("2. Find project by id")
    print("3. Create project")
    print("4. Update project")
    print("5. Delete project")
    print("6. List all team members")
    print("7. Find team member by id")
    print("8. Create team member")
    print("9. Update team member")
    print("10. Delete team member")
    print("11. List all tasks")
    print("12. List all tasks for a specific project")
    print("13. List all tasks assigned to a team member")
    print("14. Create Task")
    print("15. Update Task")
    print("16. Delete Task")
    print("17. List all project milestones")
    print("18. List all milestones for a specific project")
    


if __name__ == "__main__":
    main()