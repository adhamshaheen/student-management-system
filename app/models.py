from pydantic import BaseModel, Field


# Class to represent a student for creation
class StudentCreate(BaseModel):
    name: str
    age: int = Field(gt=0)
    major: str


# Class to represent a student for response
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    major: str