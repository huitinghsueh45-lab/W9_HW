import json
import os
import shutil

def sync_site():
    docs_dir = 'docs'
    index_md = os.path.join(docs_dir, 'index.md')
    readme_md = os.path.join(docs_dir, 'README.md')

    if os.path.exists(index_md):
        shutil.copyfile(index_md, readme_md)

    fallback_map = {}
    for fn in sorted(os.listdir(docs_dir)):
        if fn.endswith('.md'):
            with open(os.path.join(docs_dir, fn), 'r', encoding='utf-8') as f:
                fallback_map[fn] = f.read()

    html = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <title>生成式 AI 課程摘要與數位索引 — TAICA 生成式 AI：文字與圖像生成的原理與實務</title>
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <meta name="description" content="將每週課堂講義與作業實作化繁為簡，打造快速檢索、高效複習的結構化知識庫。">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
  <!-- Google Fonts: Noto Serif TC, Noto Sans TC, Inter, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Noto+Sans+TC:wght@400;500;600;700&family=Noto+Serif+TC:wght@600;700&display=swap" rel="stylesheet">
  <!-- Docsify Light Base Theme & KaTeX -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@latest/dist/katex.min.css" />
  <!-- Custom Editorial Course Review Theme -->
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <div id="app">載入生成式 AI 課程摘要與數位索引中...</div>
  <script>
    // 內建雙模式載入支援：無論透過本地伺服器 (http://) 或直接點擊開啟 (file://) 皆不會出現 404 Not Found
    window.__DOCS_FALLBACK__ = """ + json.dumps(fallback_map, ensure_ascii=False) + """;

    (function() {
      const OrigXHR = window.XMLHttpRequest;
      function resolveFallbackKey(url) {
        if (!url) return null;
        const clean = url.split('?')[0].split('#')[0].replace(/\\\\/g, '/');
        const parts = clean.split('/');
        const filename = parts[parts.length - 1] || 'index.md';
        if (window.__DOCS_FALLBACK__[filename]) return filename;
        if (clean.endsWith('/docs/') || clean.endsWith('/docs')) return 'index.md';
        return null;
      }

      window.XMLHttpRequest = function() {
        const xhr = new OrigXHR();
        const origOpen = xhr.open;
        const origSend = xhr.send;
        let targetUrl = '';

        xhr.open = function(method, url, ...rest) {
          targetUrl = url;
          return origOpen.call(this, method, url, ...rest);
        };

        xhr.send = function(body) {
          const key = resolveFallbackKey(targetUrl);
          if (window.location.protocol === 'file:' && key) {
            setTimeout(function() {
              const content = window.__DOCS_FALLBACK__[key];
              Object.defineProperty(xhr, 'status', { value: 200, configurable: true });
              Object.defineProperty(xhr, 'readyState', { value: 4, configurable: true });
              Object.defineProperty(xhr, 'responseText', { value: content, configurable: true });
              Object.defineProperty(xhr, 'response', { value: content, configurable: true });
              if (typeof xhr.onreadystatechange === 'function') xhr.onreadystatechange();
              if (typeof xhr.onload === 'function') xhr.onload();
              xhr.dispatchEvent(new Event('load'));
              xhr.dispatchEvent(new Event('loadend'));
            }, 0);
            return;
          }

          xhr.addEventListener('error', function(e) {
            if (key) {
              e.stopImmediatePropagation();
              const content = window.__DOCS_FALLBACK__[key];
              Object.defineProperty(xhr, 'status', { value: 200, configurable: true });
              Object.defineProperty(xhr, 'readyState', { value: 4, configurable: true });
              Object.defineProperty(xhr, 'responseText', { value: content, configurable: true });
              Object.defineProperty(xhr, 'response', { value: content, configurable: true });
              if (typeof xhr.onload === 'function') xhr.onload();
              xhr.dispatchEvent(new Event('load'));
            }
          }, true);

          xhr.addEventListener('load', function() {
            if ((xhr.status === 404 || xhr.status === 0) && key) {
              const content = window.__DOCS_FALLBACK__[key];
              Object.defineProperty(xhr, 'status', { value: 200, configurable: true });
              Object.defineProperty(xhr, 'responseText', { value: content, configurable: true });
              Object.defineProperty(xhr, 'response', { value: content, configurable: true });
            }
          }, true);

          return origSend.call(this, body);
        };
        return xhr;
      };
    })();

    window.$docsify = {
      name: '生成式 AI 課程精要',
      repo: '',
      basePath: './docs/',
      homepage: 'index.md',
      loadSidebar: true,
      subMaxLevel: 2,
      auto2top: true,
      themeColor: '#2d665b',
      search: {
        maxAge: 86400000,
        paths: 'auto',
        placeholder: '搜尋課程理論、作業模型或複習關鍵字...',
        noData: '找不到相符的課程精要內容',
        depth: 4
      }
    };
  </script>
  <!-- Docsify Core & Plugins -->
  <script src="https://cdn.jsdelivr.net/npm/docsify-katex@latest/dist/docsify-katex.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/docsify@4/lib/docsify.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/docsify@4/lib/plugins/search.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1/components/prism-python.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1/components/prism-bash.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1/components/prism-json.min.js"></script>
</body>
</html>
"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Synced docs/README.md and index.html fallback cache for:", list(fallback_map.keys()))

if __name__ == '__main__':
    sync_site()
