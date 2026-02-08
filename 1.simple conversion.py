from pathlib import Path

from docling.document_converter import DocumentConverter

source = Path("test-data") / "PUC_MP 40-40.pdf"
if not source.exists():
    raise FileNotFoundError(
        f"Source PDF not found: {source}. Place the file there or update the path."
    )

converter = DocumentConverter()
result = converter.convert(str(source))

# Save Markdown to a file.
output_path = "1.simple conversion output.txt"
with open(output_path, "w", encoding="utf-8") as output_file:
    output_file.write(result.document.export_to_markdown())

