from sqlalchemy import DateTime, String, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base

class Enrollments(Base):
    __tablename__ = "enrollments"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        primary_key=True
    )

    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id"),
        primary_key=True
    )
    
