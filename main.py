from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf_path, output_folder, pages_per_split):
    reader = PdfReader(input_pdf_path)
    total_pages = len(reader.pages)
    num_splits = (total_pages + pages_per_split - 1) // pages_per_split

    for i in range(num_splits):
        writer = PdfWriter()
        start_page = i * pages_per_split
        end_page = min(start_page + pages_per_split, total_pages)

        for j in range(start_page, end_page):
            writer.add_page(reader.pages[j])

        output_pdf_path = f"{output_folder}/split_{i + 1}.pdf"
        with open(output_pdf_path, "wb") as output_pdf_file:
            writer.write(output_pdf_file)


split_pdf("C:/Users/you/Downloads/abc.pdf", "D:\SplitPDF\output", 40)
input("Press any key to close the terminal...")
