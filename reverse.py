from pypdf import PdfReader, PdfWriter


def reverse(input, output):
    reader = PdfReader(input)
    writer = PdfWriter()

    for page in reversed(reader.pages):
        writer.add_page(page)

    with open(output, "wb") as f:
        writer.write(f)

    print(f"Reversed PDF saved as {output}")
