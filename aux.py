from docx import Document

def split_docx_by_headers(docx_path, header_list):
    """
    Reads a docx file and splits it into chunks based on the headers in header_list.
    Returns a dict: {header: text_block}
    """
    doc = Document(docx_path)

    # Convert headers list to lowercase for easier matching
    header_list = [h.lower() for h in header_list]

    chunks = {}
    current_header = None
    current_text = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue  # skip empty lines

        # Check if this paragraph is one of the headers
        if text.lower() in header_list:
            # Save previous block (if exists)
            if current_header:
                chunks[current_header] = "\n".join(current_text).strip()
            
            # Start a new block
            current_header = text
            current_text = []
        else:
            # Append text to the current block
            if current_header:
                current_text.append(text)

    # Save last block
    if current_header:
        chunks[current_header] = "\n".join(current_text).strip()

    return chunks

# Example usage:
headers_to_split = ["Introduction", "Methodology", "Results", "Conclusion"]
chunks = split_docx_by_headers("my_document.docx", headers_to_split)

for h, txt in chunks.items():
    print(f"\n=== {h} ===\n{txt}\n")
