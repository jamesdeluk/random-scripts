import fitz # PyMuPDF
pdf_file = fitz.open('input.pdf')
for page_num in range(pdf_file.page_count):
    page = pdf_file.load_page(page_num)
    media_box = page.rect
    crop_box = fitz.Rect(60, 70, media_box.width - 60, media_box.height - 70)
    page.set_cropbox(crop_box)
pdf_file.save('output.pdf')