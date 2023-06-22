from django.shortcuts import render, redirect
from pyresparser import ResumeParser
from .models import Resume
from django.contrib import messages
from django.conf import settings
from django.db import IntegrityError
from rest_framework.decorators import api_view
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(["POST"])
def homepage_api(request):
    file = request.FILES.get("file", False)
    try:
        # saving the file
        resume = Resume(resume=file)
        resume.save()

        # extracting resume entities
        parser = ResumeParser(os.path.join(settings.MEDIA_ROOT, resume.resume.name))
        data = parser.get_extracted_data()

        data["resume_path"] = os.path.abspath(
            os.path.join(settings.MEDIA_URL, resume.resume.name)
        )

        resume.name = data.get("name")
        resume.email = data.get("email")
        resume.mobile_number = data.get("mobile_number")

        if data.get("degree") is not None:
            resume.education = ", ".join(data.get("degree"))
        else:
            resume.education = None

        resume.company_names = data.get("company_names")
        resume.college_name = data.get("college_name")
        resume.designation = data.get("designation")
        resume.total_experience = data.get("total_experience")
        if data.get("skills") is not None:
            resume.skills = ", ".join(data.get("skills"))
        else:
            resume.skills = None
        if data.get("experience") is not None:
            resume.experience = ", ".join(data.get("experience"))
        else:
            resume.experience = None

        resume.save()

        print(resume)

        response_data = {
            "message": "Resume uploaded successfully.",
            "resume_data": {
                "name": resume.name,
                "email": resume.email,
                "mobile_number": resume.mobile_number,
                "education": resume.education,
                "skills": resume.skills,
                "company_name": resume.company_name,
                "college_name": resume.college_name,
                "designation": resume.designation,
                "experience": resume.experience,
                "total_experience": resume.total_experience,
                "resume_path": data.get("resume_path"),
            },
        }

        return JsonResponse(response_data)
    except IntegrityError:
        return JsonResponse({"error": "Duplicate resume found."})
