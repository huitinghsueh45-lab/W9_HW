import json
import os
import sys
import pypdf

def main():
    target_week = sys.argv[1].zfill(2) if len(sys.argv) > 1 else None
    cache_dir = os.path.join('.agents', 'skills', 'compile-weekly-course', '.cache')
    os.makedirs(cache_dir, exist_ok=True)

    summary = {'PPT': {}, 'HW': {}}
    for sub in ['PPT', 'HW']:
        folder = os.path.join('raw', sub)
        if not os.path.exists(folder):
            continue
        for fn in sorted(os.listdir(folder)):
            if not fn.lower().endswith('.pdf'):
                continue
            prefix = fn[:2]
            if target_week and prefix != target_week:
                continue
            fp = os.path.join(folder, fn)
            reader = pypdf.PdfReader(fp)
            out_txt = os.path.join(cache_dir, f'{sub}_{prefix}.txt')
            with open(out_txt, 'w', encoding='utf-8') as out:
                out.write(f'FILE: {fn} | PAGES: {len(reader.pages)}\n')
                for idx, page in enumerate(reader.pages):
                    text = (page.extract_text() or '').strip()
                    if text:
                        out.write(f'\n--- PAGE {idx + 1} ---\n{text}\n')
            summary[sub][prefix] = {
                'filename': fn,
                'rel_path': f'raw/{sub}/{fn}',
                'pages': len(reader.pages),
                'extracted_txt': out_txt
            }
            print(f'[{sub}] Week {prefix}: {fn} ({len(reader.pages)} pages) -> {out_txt}')

    manifest_path = os.path.join(cache_dir, 'manifest.json')
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f'Manifest saved to {manifest_path}')

if __name__ == '__main__':
    main()
