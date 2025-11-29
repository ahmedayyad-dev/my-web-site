"""
In-memory database for portfolio data.
For production, replace with SQLAlchemy + PostgreSQL/MySQL
"""

from typing import List
from app.models import (
    ProfileData, SocialLink, Skill, AboutSection, ContactInfo
)
from app.utils import calculate_age_from_date, calculate_experience_years


class Database:
    def __init__(self):
        self.profile = ProfileData()
        self.social_links = [
            SocialLink(name="email", url="mailto:ahmedyad200@gmail.com", icon="email", order=1),
            SocialLink(name="github", url="https://github.com/ahmedayyad-dev", icon="github", order=2),
            SocialLink(name="linkedin", url="https://www.linkedin.com/in/ahmedayyad2/", icon="linkedin", order=3),
            SocialLink(name="phone", url="tel:+201068159910", icon="phone", order=4),
            SocialLink(name="whatsapp", url="https://wa.me/201068159910", icon="whatsapp", order=5),
            SocialLink(name="telegram", url="https://t.me/ayyad", icon="telegram", order=6),
            SocialLink(name="facebook", url="https://www.facebook.com/ahmedyad200", icon="facebook", order=7),
            SocialLink(name="rapidapi", url="https://rapidapi.com/user/ahmedyad200", icon="rapidapi", order=8),
        ]

        self.skills = [
            Skill(name_ar="بايثون", name_en="Python", order=1),
            Skill(name_ar="FastAPI", name_en="FastAPI", order=2),
            Skill(name_ar="REST APIs", name_en="REST APIs", order=3),
            Skill(name_ar="ديبيان (لينكس)", name_en="Debian (Linux)", order=4),
            Skill(name_ar="ريديس", name_en="Redis", order=5),
            Skill(name_ar="البرمجة غير المتزامنة", name_en="Async Programming", order=6),
            Skill(name_ar="أدوات الذكاء الاصطناعي", name_en="AI Tools", order=7),
            Skill(name_ar="الأتمتة", name_en="Automation", order=8),
            Skill(name_ar="Telethon", name_en="Telethon", order=9),
            Skill(name_ar="Py-TgCalls", name_en="Py-TgCalls", order=10),
            Skill(name_ar="yt-dlp", name_en="yt-dlp", order=11),
            Skill(name_ar="Playwright", name_en="Playwright", order=12),
        ]

        self.about_sections = [
            AboutSection(
                title_ar="🌟 من أنا؟",
                title_en="🌟 Who Am I?",
                content_ar="أنا أحمد عياد، مطور برمجيات مستقل وشغوف بحلول الـ Backend المعتمدة على Python. تخصصي يكمن في بناء أنظمة الأتمتة المعقدة، وأركز حالياً بشكل كبير على تطوير بوتات Telegram عالية الكفاءة؛ وتحديداً بوتات التحميل من YouTube وبوتات تشغيل الوسائط، بالإضافة إلى التعامل الاحترافي مع دمج الـ APIs المتنوعة.",
                content_en="I'm Ahmed Ayyad, a freelance software developer passionate about Python-based Backend solutions. My specialty lies in building complex automation systems, currently focusing heavily on developing high-performance Telegram bots; specifically YouTube download bots and media playback bots, in addition to professional handling of various API integrations.",
                order=1
            ),
            AboutSection(
                title_ar="🐧 فلسفتي التقنية",
                title_en="🐧 My Technical Philosophy",
                content_ar="أنا ملتزم تمامًا بالاعتماد على الأنظمة مفتوحة المصدر والبيئات التقنية المستقلة. Linux أولاً وأخيراً: أنا مستخدم عميق ومتعصب لنظام Linux (Debian)، وهذا الالتزام نابع من قناعتي بالاستقلالية التقنية والكفاءة العالية.",
                content_en="I am fully committed to relying on open-source systems and independent technical environments. Linux First and Last: I am a deep and devoted Linux (Debian) user, and this commitment stems from my conviction in technical independence and high efficiency.",
                order=2
            ),
            AboutSection(
                title_ar="🏡 نمط الحياة",
                title_en="🏡 Lifestyle & Focus",
                content_ar="أعمل وأعيش بشكل مستقل، مما يمنحني الانضباط والقدرة على التركيز العميق الذي ينعكس مباشرة على جودة الكود والأداء النهائي للخدمات التي أقدمها. أبحث عن البيئات السمعية التي تساعد على الإبداع؛ ولذلك لا أستمع إلى الأغاني الشعبية وأفضل الموسيقى التي تعزز الهدوء والتركيز أثناء العمل.",
                content_en="I work and live independently, which gives me the discipline and ability to focus deeply, directly reflected in code quality and final service performance. I seek audio environments that aid creativity; therefore I don't listen to popular music and prefer music that enhances calm and focus while working.",
                order=3
            ),
        ]

        self.contact = ContactInfo(
            email="ahmedyad200@gmail.com",
            phone="+201068159910",
            github="https://github.com/ahmedayyad-dev",
            telegram="https://t.me/ayyad",
            linkedin="https://www.linkedin.com/in/ahmedayyad2/",
            facebook="https://www.facebook.com/ahmedyad200",
            whatsapp="https://wa.me/201068159910",
            rapidapi="https://rapidapi.com/user/ahmedyad200"
        )

    def calculate_age(self) -> int:
        """Use utility function for age calculation"""
        return calculate_age_from_date(self.profile.birth_date)

    def calculate_experience(self) -> int:
        """Use utility function for experience calculation"""
        return calculate_experience_years(self.profile.experience_start_date)


# Singleton instance
db = Database()
