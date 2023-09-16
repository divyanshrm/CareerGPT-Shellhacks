from django.shortcuts import render, redirect
import PyPDF2
from PyPDF2 import PdfFileReader
from io import BytesIO
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class pdf_to_text:
    def __init__(self,filename):
        self.file = filename
    def extract_text_from_pdf(self):
        pdf_file_obj = open(self.file, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page_obj = pdf_reader.pages[page_num]
            text += page_obj.extract_text()

        pdf_file_obj.close()

        return text

@login_required
def upload_resume(request):
    if request.method == 'POST':
        form = forms.UploadResumeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Save the uploaded PDF file temporarily
                uploaded_file = request.FILES['resume_file']
                with open('temp_pdf_file.pdf', 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)

                # Parse the saved PDF file to text
                parser = pdf_to_text('temp_pdf_file.pdf')
                text_content = parser.extract_text_from_pdf()
                
                
                # Save or update the parsed text to the Resume model
                resume, created = models.Resume.objects.get_or_create(user=request.user)
                resume.text_content = text_content
                models.JobRole.objects.filter(resume=resume).delete()
                resume.save()

                messages.success(request, 'Resume uploaded successfully!')
                return redirect('upload_resume')  # Redirect to the same form page

            except Exception as e:
                # Handle errors here (like file not being a valid PDF)
                messages.error(request, 'Failed to upload resume. Ensure it is a valid PDF.')
                print(e)  # Optionally log or print the error for debugging

    else:
        form = forms.UploadResumeForm()
    has_uploaded_resume = models.Resume.objects.filter(user=request.user).exists()

    context = {'has_uploaded_resume': has_uploaded_resume, 'form': form}
    return render(request, 'resume/upload_resume.html', context)
# Create your views here.
