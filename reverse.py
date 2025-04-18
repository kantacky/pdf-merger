from pypdf import PdfReader, PdfWriter


def reverse(input_pdf, output_pdf):

    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reversed(reader.pages):
        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"Reversed PDF saved as {output_pdf}")
