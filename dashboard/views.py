from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import openai
import re
from resume import models
openai.api_key = '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'

class chatgptapi:
    def __init__(self):
        self.responsepattern = r'\[(.*?)\]'
    def gen_response(self,inp):
        messages = [{"role":"user","content":inp}]
        chat = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo", messages=messages
                )
        reply = chat.choices[0].message.content
        return reply
    def parse_gpt_response(self,response):
        out = re.findall(self.responsepattern,response)
        return out #dtype = list, list of all values within square braces

@login_required
def main_board(request):
    user_resume = models.Resume.objects.filter(user=request.user).first()

    # Check if the user's resume exists
    if user_resume:
        
        # Check if job roles exist in the database for this user's resume
        existing_roles = user_resume.job_roles.all()

        if existing_roles:
            roles = [role.role for role in existing_roles]  # Extract job roles from the database entries
        else:
            # If roles don't exist, generate using GPT-3
            chat_api = chatgptapi()
            prompt = user_resume.text_content + ". Use this to suggest the top 3 job roles for this user. Reply with the job roles in python list format. Example - [Full stack developer] , [machine learning engineer], [Computer Vision Researcher]: "
            
            # Generate response using the user's resume text
            gpt_response = chat_api.gen_response(prompt)
            
            # Parse the GPT-3 response
            roles = chat_api.parse_gpt_response(gpt_response)

            # Save the generated roles to the database
            for role_name in roles:
                models.JobRole.objects.create(resume=user_resume, role=role_name)

        return render(request, 'dashboard/dashboard.html', {'roles': roles})
    else:
        # Handle case if the user has not uploaded a resume yet
        return render(request, 'dashboard/dashboard.html', {'message': "Please upload a resume first."})
    



