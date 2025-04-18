from pypdf import PdfReader, PdfWriter


def merge(input1, input2, output):
    reader1 = PdfReader(input1)
    reader2 = PdfReader(input2)
    writer = PdfWriter()

    for page_i in range(max(len(reader1.pages), len(reader2.pages))):
        if page_i < len(reader1.pages):
            writer.add_page(reader1.pages[page_i])
        if page_i < len(reader2.pages):
            writer.add_page(reader2.pages[page_i])

    with open(output, "wb") as f:
        writer.write(f)

    print(f"Merged PDF saved as {output}")
