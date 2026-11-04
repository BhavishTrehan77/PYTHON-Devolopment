from app.services.pdf_service import save_pdf_document,process_pdf


def save_pdf_controller(data):
    return save_pdf_document(data)

def process_pdf_controller(text,filename):
    return process_pdf(text,filename)
