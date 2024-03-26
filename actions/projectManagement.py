from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, Project, TeamMembers, Task, Milestone
from datetime import date


class ProjectManagement:

    def __init__(self, db_name):
        self.engine = create_engine(f'sqlite:///{db_name}')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_project(self,project_name,description,start_date,end_date):
        try:
            project = Project(project_name=project_name,description=description,start_date=start_date,end_date=end_date)

            self.session.add(project)
            self.session.commit()
            # print("project added successfully")
            return project
        except Exception as e:
            self.session.rollback()
            print(f'Error adding project: {e}')

    def add_team_member(self,name,role):
        try:
            team_member = TeamMembers(name=name,role=role)

            self.session.add(team_member)
            self.session.commit()
            # print("team_member added successfully")
            return team_member
        except Exception as e:
            self.session.rollback()
            print(f'Error adding team member: {e}')


    def add_task(self,project_id,team_member_id,description,status,due_date):
        try:
            task = Task(project_id=project_id, team_member_id=team_member_id,description=description,status=status,due_date=due_date)

            self.session.add(task)
            self.session.commit()
            # print("task added successfully")
            return task
        except Exception as e:
            self.session.rollback()
            print(f'Error adding task: {e}')


    def add_project_milestone(self,project_id,milestone,description,due_date):
        try:
            milestone = Milestone(project_id=project_id,milestone=milestone, description=description,due_date=due_date)

            self.session.add(milestone)
            self.session.commit()
            # print("milestone added successfully")
        except Exception as e:
            self.session.rollback()
            print(f'Error adding project milestone: {e}')


    # getall()
    def get_all_projects(self):
        return self.session.query(Project).all()
    
    def get_all_team_members(self):
        return self.session.query(TeamMembers).all()
    
    def get_all_tasks(self):
        return self.session.query(Task).all()
    
    def get_all_milestones(self):
        return self.session.query(Milestone).all()
    
    # get by id
    def get_project_by_id(self,project_id):
        project = self.session.query(Project).filter_by(id=project_id).first()
        # print(f"Project name: {project.project_name}, Description: {project.description}, Start date: {project.start_date}, End date: {project.end_date}")
        return project
    
    def get_member_by_id(self,team_member_id):
        member = self.session.query(TeamMembers).filter_by(id = team_member_id).first()
        # print(f"Name: {member.name}, Role: {member.role}")
        return member
    
    def get_task_by_id(self,task_id):
        task = self.session.query(Task).filter_by(id=task_id).first()
        # print(f"Project id: {task.project_id},Team member id: {task.team_member_id}, Task: {task.description}, Status: {task.status}, Due date: {task.due_date}")
        return task

    def get_tasks_by_project_id(self,project_id):
        tasks = self.session.query(Task).filter_by(project_id = project_id).all()
        # print([task.description for task in tasks])
        return tasks
    
    def get_tasks_by_member_id(self,team_member_id):
        member_task = self.session.query(Task).filter_by(team_member_id= team_member_id).all()
        # print([task.description for task in member_task])
        return member_task
    
    def get_milestone_by_project_id(self,project_id):
        milestones = self.session.query(Milestone).filter_by(project_id = project_id).all()
        # print([miles.milestone for miles in milestones])
        return milestones
        
    # update
    def update_project(self, id, project_name, description,start_date,end_date):
        try:
            project = self.session.query(Project).filter_by(id=id).first()

            project.project_name = project_name
            project.description = description
            project.start_date = start_date
            project.end_date = end_date
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f'Error updating project : {e}')

    def update_team_members(self, id, name, role):
        try:
            member = self.session.query(TeamMembers).filter_by(id=id).first()

            member.name = name
            member.role = role
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f'Error updating team member : {e}')

    def update_milestone(self, milestone_id, milestone, description, due_date):
        try:
            miles = self.session.query(Milestone).filter_by(id=milestone_id).first()

            miles.milestone = milestone
            miles.description = description
            miles.due_date = due_date
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f'Error updating project milestone : {e}')

    # Delete
    def delete_project(self,id):
        try: 
            project = self.session.query(Project).filter_by(id=id).first()

            self.session.delete(project)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f'Error deleting project : {e}')