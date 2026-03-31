from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.models.course import Course
from app.schemas.courses import CourseRead, CourseCreate, CourseUpdate
from app.services.course import get_valid_course

router = APIRouter(prefix="/courses", tags=["courses"])

@router.get("/", response_model=list[CourseRead])
def get_all(
    db: Session = Depends(get_db),
) -> list[CourseRead]:
    return db.query(Course).all()


@router.post("/", response_model=CourseRead)
def create(
    payload: CourseCreate,
    db: Session = Depends(get_db),
) -> CourseRead:
    course = Course(
        title=payload.title,
        description=payload.description,
    )

    db.add(course)
    db.commit()
    db.refresh(course)

    return course


@router.get("/{id}", response_model=CourseRead)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
) -> CourseRead:
    return get_valid_course(db, id)


@router.patch("/{id}", response_model=CourseRead)
def update(
    id: int,
    payload: CourseUpdate,
    db: Session = Depends(get_db),
) -> CourseRead:
    course = get_valid_course(db, id)

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(course, field, value)

    db.commit()
    db.refresh(course)

    return course


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
) -> dict:
    course = get_valid_course(db, id)

    db.delete(course)
    db.commit()

    return {"detail": "Course deleted"}
