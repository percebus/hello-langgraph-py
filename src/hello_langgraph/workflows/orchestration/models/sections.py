from pydantic import BaseModel, Field


# Schema for structured output to use in planning
class Section(BaseModel):
    name: str = Field(
        description="Name for this section of the report.",
    )
    description: str = Field(
        description="Brief overview of the main topics and concepts to be covered in this section.",
    )


class SectionCollection(BaseModel):
    items: list[Section] = Field(
        description="Sections of the report.",
    )
