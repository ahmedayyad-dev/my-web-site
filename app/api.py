from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.database import db
from app.models import PortfolioResponse
from app.utils import (
    calculate_detailed_age,
    calculate_detailed_experience,
    calculate_productivity_stats,
    format_date_ar,
    format_date_en
)

router = APIRouter(prefix="/api/v1", tags=["API"])


@router.get("/portfolio", response_model=PortfolioResponse)
async def get_portfolio():
    """
    Get complete portfolio data including profile, skills, social links, and about sections.
    """
    return PortfolioResponse(
        profile=db.profile,
        social_links=sorted(db.social_links, key=lambda x: x.order),
        skills=sorted(db.skills, key=lambda x: x.order),
        about_sections=sorted(db.about_sections, key=lambda x: x.order),
        contact=db.contact,
        age=db.calculate_age(),
        experience_years=db.calculate_experience()
    )


@router.get("/profile")
async def get_profile():
    """Get profile data only"""
    return {
        **db.profile.dict(),
        "age": db.calculate_age(),
        "experience_years": db.calculate_experience()
    }


@router.get("/profile/detailed")
async def get_detailed_profile():
    """Get detailed profile with advanced calculations"""
    age_details = calculate_detailed_age(db.profile.birth_date)
    exp_details = calculate_detailed_experience(db.profile.experience_start_date)
    productivity = calculate_productivity_stats(db.profile.experience_start_date)

    return {
        **db.profile.dict(),
        "age": {
            "simple": db.calculate_age(),
            "detailed": age_details,
            "birth_date_ar": format_date_ar(db.profile.birth_date),
            "birth_date_en": format_date_en(db.profile.birth_date)
        },
        "experience": {
            "simple": db.calculate_experience(),
            "detailed": exp_details,
            "start_date_ar": format_date_ar(db.profile.experience_start_date),
            "start_date_en": format_date_en(db.profile.experience_start_date),
            "productivity": productivity
        }
    }


@router.get("/skills")
async def get_skills():
    """Get all skills"""
    return sorted(db.skills, key=lambda x: x.order)


@router.get("/social-links")
async def get_social_links():
    """Get all social media links"""
    return sorted(db.social_links, key=lambda x: x.order)


@router.get("/about")
async def get_about():
    """Get about sections"""
    return sorted(db.about_sections, key=lambda x: x.order)


@router.get("/contact")
async def get_contact():
    """Get contact information"""
    return db.contact


@router.get("/stats")
async def get_stats():
    """Get statistics with heavy calculations"""
    age_details = calculate_detailed_age(db.profile.birth_date)
    exp_details = calculate_detailed_experience(db.profile.experience_start_date)
    productivity = calculate_productivity_stats(db.profile.experience_start_date)

    return {
        "basic": {
            "age": db.calculate_age(),
            "experience_years": db.calculate_experience(),
            "skills_count": len(db.skills),
            "social_links_count": len(db.social_links),
            "about_sections_count": len(db.about_sections)
        },
        "age_breakdown": {
            "years": age_details["years"],
            "months": age_details["months"],
            "days": age_details["days"],
            "total_days": age_details["total_days"]
        },
        "experience_breakdown": {
            "years": exp_details["years"],
            "months": exp_details["months"],
            "days": exp_details["days"],
            "total_days": exp_details["total_days"]
        },
        "productivity": {
            "working_days": productivity["working_days_estimate"],
            "working_hours": productivity["working_hours_estimate"],
            "weeks": productivity["weeks"]
        }
    }


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Ahmed Ayyad Portfolio API"}
