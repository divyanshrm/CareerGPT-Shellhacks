from django.shortcuts import render

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


def main_board(request):
    user_resume = models.Resume.objects.filter(user=request.user).first()

# Check if the user's resume exists
    if user_resume:
        # Initialize chatgptapi class
        chat_api = chatgptapi()

        # Generate response using the user's resume text
        gpt_response = chat_api.gen_response(user_resume.text_content)

        # Optionally parse the GPT-3 response
        parsed_response = chat_api.parse_gpt_response(gpt_response)

        return render(request, 'dashboard/dashboard.html', {'response': parsed_response})
    else:
        # Handle case if the user has not uploaded a resume yet
        return render(request, 'dashboard/dashboard.html', {'message': "Please upload a resume first."})


