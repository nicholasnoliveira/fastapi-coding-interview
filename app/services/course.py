from app.models.course import Course
from fastapi import HTTPException

def get_valid_course(db, course_id):
    course = db.query(Course).get(course_id)

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return course
