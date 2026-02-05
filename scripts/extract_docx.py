import sys
from docx import Document
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / 'Data'
OUT_DIR = DATA_DIR / 'extracted'
OUT_DIR.mkdir(exist_ok=True)

for path in DATA_DIR.glob('*.docx'):
    try:
        doc = Document(path)
        text = []
        for para in doc.paragraphs:
            text.append(para.text)
        out_path = OUT_DIR / (path.stem + '.txt')
        out_path.write_text('\n'.join(text), encoding='utf-8')
        print(f'Wrote {out_path}')
    except Exception as e:
        print(f'Failed to extract {path}: {e}', file=sys.stderr)
        sys.exit(1)
print('Done')
