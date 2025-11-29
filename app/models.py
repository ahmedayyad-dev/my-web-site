from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr


class ProfileData(BaseModel):
    name_ar: str = "أحمد عياد"
    name_en: str = "Ahmed Ayyad"
    bio_ar: str = "لا يمكنك أن تكون مثلي"
    bio_en: str = "You can't be like me"
    job_title_ar: str = "مطور سوفت وير"
    job_title_en: str = "Software Developer"
    birth_date: str = "2005-05-21"
    experience_start_date: str = "2021-02-05"
    profile_image: str = "profile.jpg"


class SocialLink(BaseModel):
    name: str
    url: str
    icon: str
    order: int


class Skill(BaseModel):
    name_ar: str
    name_en: str
    order: int


class AboutSection(BaseModel):
    title_ar: str
    title_en: str
    content_ar: str
    content_en: str
    order: int


class ContactInfo(BaseModel):
    email: EmailStr
    phone: str
    github: str
    telegram: str
    linkedin: str
    facebook: str
    whatsapp: str
    rapidapi: str


class PortfolioResponse(BaseModel):
    profile: ProfileData
    social_links: List[SocialLink]
    skills: List[Skill]
    about_sections: List[AboutSection]
    contact: ContactInfo
    age: int
    experience_years: int
