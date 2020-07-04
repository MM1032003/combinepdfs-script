import PyPDF2, os

def is_pdf(filename):
    if filename.endswith(".pdf"):
        return True
    return False

pdf_files    = list(filter(is_pdf, os.listdir()))

if not len(pdf_files) > 1:
    raise Exception("The Combined PDFs Must Be At Least 2")

pdf_files.sort(key = str.lower)

file_writer_obj = PyPDF2.PdfFileWriter()


for pdf_file in pdf_files:
    file_handler    = open(pdf_file, "rb")
    file_reader     = PyPDF2.PdfFileReader(file_handler)
    if not file_reader.isEncrypted:
        for page_num in range(1, file_reader.numPages):
            page_obj    = file_reader.getPage(page_num)

            file_writer_obj.addPage(page_obj)

output_file = open("all.pdf", "wb")
file_writer_obj.write(output_file)
output_file.close()

if file_handler:
    file_handler.close()

