from fastapi import APIRouter
from fastapi import HTTPException, Query


from models.todos import Student
from config.database import collection_name

from schema.schemas import list_serial
from bson import ObjectId



router = APIRouter()


# API endpoint to create a new student
@router.post("/students/")
async def create_student(student: Student):
    result = collection_name.students.insert_one(student.dict())
    return {"id": str(result.inserted_id)}

# API endpoint to read a student by ID
@router.get("/students/{id}")
async def read_student(id: str):
    student_obj_id = ObjectId(id)
    student = collection_name.students.find_one({"_id": student_obj_id})
    
    if student:
        # Convert ObjectId to string for JSON serialization
        student["_id"] = str(student["_id"])
        return student
    else:
        raise HTTPException(status_code=404, detail="Student not found")

# API endpoint to update a student by ID
@router.patch("/students/{id}")
async def update_student(id: str, student_patch: Student):
    student_obj_id = ObjectId(id)
    update_fields = student_patch.dict(exclude_unset=True)  # Exclude fields with None values
    if not update_fields:
        raise HTTPException(status_code=400, detail="No fields provided for update")
    
    result = collection_name.students.update_one({"_id": student_obj_id}, {"$set": update_fields})
    if result.modified_count == 1:
        return
    else:
        raise HTTPException(status_code=404, detail="Student not found")

# API endpoint to delete a student by ID
@router.delete("/students/{id}")
async def delete_student(id: str):
    student_obj_id = ObjectId(id)
    result = collection_name.students.delete_one({"_id": student_obj_id})
    if result.deleted_count == 1:
        return
    else:
        raise HTTPException(status_code=404, detail="Student not found")

# API endpoint to get all students with optional filters
@router.get("/students/")
async def get_all_students(country: str = Query(None), age: int = Query(None)):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}
    
    students = collection_name.students.find(query)
    students = [student for student in students]
    for student in students:
        student["_id"] = str(student["_id"]) # Convert ObjectId to string for JSON serialization
    return {"data": students}





































# # retrieve #GET REQUEST METHOD
# @router.get("/")
# async def get_todos():
#     todos = list_serial(collection_name.find())
#     return todos


# # post #POST REQUEST METHOD
# @router.post("/")
# async def create_todo(todo: Todo):
#     collection_name.insert_one(dict(todo))
#     # _id = collection_name.insert_one(dict(todo))
#     # return todos_serializer(collection_name.find({"_id": _id.inserted_id}))


# # update #PUT REQUEST METHOD
# @router.patch("/{id}")
# async def patch_todo(id: str, todo: Todo):
#     collection_name.find_one_and_update({"_id": ObjectId(id)}, {
#         "$set": dict(todo)
#     })
#     # return todos_serializer(collection_name.find({"_id": ObjectId(id)}))


# # delete #DELETE REQUEST METHOD
# @router.delete("/{id}")
# async def delete_todo(id: str):
#     collection_name.find_one_and_delete({"_id": ObjectId(id)})
#     # return {"status": "ok"}