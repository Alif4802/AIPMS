"""
extract_pdf.py - Deterministic PDF extractor preserving page boundaries (## Page N)
and structured text/tables.
"""

import sys
import os
import fitz
import pymupdf4llm

def extract_pdf_to_markdown(pdf_path, output_path, metadata):
    doc = fitz.open(pdf_path)
    num_pages = len(doc)
    
    output = []
    output.append("# Source Extraction\n")
    for k, v in metadata.items():
        output.append(f"**{k}:** {v}")
    output.append(f"**Number of pages/sheets/slides:** {num_pages}")
    output.append("\n---\n")
    
    for i in range(num_pages):
        page = doc[i]
        page_num = i + 1
        output.append(f"\n## Page {page_num}\n")
        # Extract page text
        text = page.get_text()
        if text.strip():
            output.append(text.strip())
        else:
            output.append(f"*[Note: Page {page_num} contains scanned image content / no direct text]*\n")
            
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(output))
    print(f"Extracted {pdf_path} ({num_pages} pages) -> {output_path}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python extract_pdf.py <input.pdf> <output.md>")
        sys.exit(1)
    inp = sys.argv[1]
    out = sys.argv[2]
    meta = {
        "Original file": os.path.basename(inp),
        "Original relative path": inp,
        "Source category": "REFERENCE",
        "Extraction method": "PyMuPDF (fitz) page-boundary text extractor",
        "Extraction date": "2026-09-15",
        "Extraction completeness": "Complete text extraction",
        "Notes": "Preserves explicit page boundaries"
    }
    extract_pdf_to_markdown(inp, out, meta)
