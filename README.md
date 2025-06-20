# PdfSummerizer

**PdfSummerizer** is a lightweight Python program designed to process PDF documents by extracting both textual and visual content. It provides concise textual summaries of the extracted text and saves any images found within the PDF files. This tool is intended to support more efficient learning by offering summarized content that can be further utilized with other tools or workflows.

---

## Features

- 📄 **Text Extraction**: Extracts all readable text from PDF documents.
- 🧠 **Text Summarization**: Generates brief and informative summaries of the extracted content.
- 🖼️ **Image Extraction**: Identifies and saves all images embedded in the PDF.
- 🧰 **Modular Utility**: Results can be used in conjunction with other tools for enhanced learning or automation.

---

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PdfSummerizer.git
   cd PdfSummerizer
   ```

2. Run the script:
   ```bash
   python pdfsummerizer.py
   ```

---

## Usage

1. Place your PDF files in the designated input folder (or modify the script to point to your folder - default is docs).
2. Run the script.
3. Summaries will be saved as `.txt` files.
4. Extracted images will be saved in a designated image output folder.

---

## Notes

- Ensure you **delete any empty `.txt` files** if using the default folders
- If required, **create your own folders** for inputs, outputs, and images, or modify the script accordingly.
- Designed for educational, research, and productivity-enhancement purposes.

---

## Example Output

```
📄 Input PDF: sample_lesson.pdf  
🧠 Summary saved as: sample_lesson_summary.txt  
🖼️ Images saved in: /images/sample_lesson/
```

---

## Disclaimer

This tool is designed to assist learning by summarizing PDF content. It is not guaranteed to produce perfect summaries and should be used in conjunction with critical reading and understanding.
