import PyPDF2

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
o=pdf_to_text('/Users/divyansh/Downloads/Divyansh_Resume (1).pdf')
print(o.extract_text_from_pdf())