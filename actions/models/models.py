from sqlalchemy import ForeignKey, Column, String, Integer, Date,Boolean
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"
    
    id = Column("id", Integer, primary_key=True, nullable=False)
    project_name = Column("project_name", String, unique=True, nullable=False)
    description = Column("description", String, unique=True, nullable=False)
    start_date = Column("start_date", Date, nullable=False)
    end_date = Column("end_date", Date, nullable=False)

    tasks = relationship("Task", back_populates="project")
    milestones = relationship("Milestone", back_populates="project")


class TeamMembers(Base):
    __tablename__ = "team_members"

    id = Column("id", Integer, primary_key=True, nullable=False)
    name = Column("name", String, unique=True, nullable=False)
    role = Column("role", String, nullable=False)

    tasks = relationship("Task", back_populates="team_member")


class Task(Base):
    __tablename__ = "tasks"

    id = Column("id", Integer, primary_key=True, nullable=False)
    project_id = Column("project_id", Integer, ForeignKey("projects.id"))
    team_member_id = Column("team_member_id", Integer, ForeignKey("team_members.id"),nullable=False)
    description = Column("description",String, unique=True, nullable=False)
    status = Column("status",String, nullable=False)
    due_date = Column("due_date", Date, nullable=False)

    project = relationship("Project", back_populates="tasks")
    team_member = relationship("TeamMembers", back_populates="tasks")



class Milestone(Base):
    __tablename__ = "project_milestones"

    id = Column("id", Integer, primary_key=True, nullable=False)
    project_id = Column("project_id", Integer, ForeignKey("projects.id"), nullable=False)
    milestone = Column("milestone", String, unique=True, nullable=False)
    description = Column("description",String, unique=True, nullable=False)
    due_date = Column("due_date", Date, nullable=False)

    project = relationship("Project",back_populates="milestones")
