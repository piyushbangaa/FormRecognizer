PDF Text Extractor
A Python-based tool that extracts text from PDF files using the fitz (PyMuPDF) library. This tool processes PDF documents to extract and save their content as plain text files.

Features
Text Extraction: Extracts all the text content from PDF files, including multi-page documents.
Output: Saves the extracted text as a .txt file, with the same name as the input PDF.
Requirements
To use this tool, you'll need to install the required Python library, PyMuPDF (referred to as fitz in the code).

INSTALLATION

1. Clone the repository:

#bash
git clone https://github.com/your-username/FormRecognizer.git

2. Navigate to the project directory:

#bash
cd FormRecognizer

3. Install the required dependencies:

#bash
pip install -r requirements.txt

4. Alternatively, you can manually install the PyMuPDF library (fitz):

#bash
pip install pymupdf
This will install the fitz library, which is used in the code to handle PDF parsing.

USAGE
Place the PDF file (e.g., drylab.pdf) you want to process in the project directory or specify its full path in the code.

Run the script:

#bash
python index.py

The extracted text will be saved in a .txt file, located in the same directory as the original PDF. The file will have the same name as the PDF (e.g., drylab_output.txt).

Example
If your input file is drylab.pdf, the output file will be named drylab_output.txt and will contain the extracted text from the PDF.

How It Works
extract_text_from_pdf(pdf_path): This function loads a PDF file and extracts its text page by page using the fitz (PyMuPDF) library.
process_pdf(pdf_path): This function calls extract_text_from_pdf and processes the PDF to return the extracted text.
save_results_to_txt(pdf_path, results): This function saves the extracted text to a .txt file in the same folder as the input PDF.
Example Output
The extracted text from the PDF will be saved in the output.txt file with the following structure:

mathematica
Copy code
Extracted Text:
<Extracted content of the PDF here>
Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome!

Additional Details:
fitz (PyMuPDF) Overview:
PyMuPDF (imported as fitz) is a Python binding for the MuPDF library. It allows you to interact with and extract content from PDF, XPS, and other document formats efficiently.
For more information about the library, check out the official documentation.
