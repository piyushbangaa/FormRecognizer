import fitz  # PyMuPDF
import os

# Function to extract text from a PDF 
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text("text")  
    return text

# Function to merge results (no tables to be processed)
def process_pdf(pdf_path):
    print("Extracting text")
    pdf_text = extract_text_from_pdf(pdf_path)
    
    return {
        "pdf_text": pdf_text
    }

def save_results_to_txt(pdf_path, results):
    folder = os.path.dirname(pdf_path)  
    output_txt_path = os.path.join(folder, os.path.splitext(os.path.basename(pdf_path))[0] + "_output.txt")
    
    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write("Extracted Text:\n")
        f.write(results["pdf_text"])  
    
    print(f"Results saved to {output_txt_path}")

pdf_path = "drylab.pdf"  
results = process_pdf(pdf_path)
save_results_to_txt(pdf_path, results)





