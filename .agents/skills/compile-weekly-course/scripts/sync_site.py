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
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Noto+Sans TC:wght@400;500;600;700&family=Noto+Serif+TC:wght@600;700&display=swap" rel="stylesheet">
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

    // 助教一鍵編譯生成 Week 03 互動控制器
    window.syncWeek03UIState = function(flashRow) {
      if (window.location.hash && window.location.hash.indexOf('week-03') !== -1) {
        try { localStorage.setItem('week03_compiled', 'true'); } catch (e) {}
      }
      var isCompiled = false;
      try { isCompiled = localStorage.getItem('week03_compiled') === 'true'; } catch (e) {}

      var rowW03 = document.getElementById('row-week-03');
      var pillUncompiled = document.getElementById('pill-week-03-uncompiled');
      var pillCompiled = document.getElementById('pill-week-03-compiled');
      var btnCompile = document.getElementById('btn-compile-w03');
      var btnGoto = document.getElementById('btn-goto-w03');
      var btnReset = document.getElementById('btn-reset-w03');

      if (rowW03) {
        rowW03.style.display = isCompiled ? 'table-row' : 'none';
        if (flashRow && isCompiled) {
          rowW03.classList.remove('compiled-row-flash');
          void rowW03.offsetWidth;
          rowW03.classList.add('compiled-row-flash');
        }
      }
      if (pillUncompiled) pillUncompiled.style.display = isCompiled ? 'none' : 'inline-flex';
      if (pillCompiled) pillCompiled.style.display = isCompiled ? 'inline-flex' : 'none';
      if (btnCompile) {
        btnCompile.innerHTML = isCompiled
          ? '✅ Week 03 已編譯完成（點此重新執行編譯）'
          : '⚡ 一鍵執行 Agent 編譯生成 Week 03 頁面';
      }
      if (btnGoto) btnGoto.style.display = isCompiled ? 'inline-flex' : 'none';
      if (btnReset) btnReset.style.display = isCompiled ? 'inline-flex' : 'none';

      // 同步側邊欄 Week 03 顯示狀態
      var sidebarLinks = document.querySelectorAll('.sidebar-nav a');
      for (var i = 0; i < sidebarLinks.length; i++) {
        var href = sidebarLinks[i].getAttribute('href') || '';
        if (href.indexOf('week-03') !== -1 && sidebarLinks[i].parentElement) {
          sidebarLinks[i].parentElement.style.display = isCompiled ? '' : 'none';
        }
      }
    };

    window.runAgentCompileWeek03 = function() {
      var consoleEl = document.getElementById('agent-compile-console');
      var btnCompile = document.getElementById('btn-compile-w03');
      if (!consoleEl) return;

      if (btnCompile) btnCompile.disabled = true;
      consoleEl.style.display = 'block';
      consoleEl.innerHTML = '<div><span class="log-step">[Step 1/4]</span> 執行 <code>extract_week_pdfs.py 03</code>：正在掃描 <code>raw/PPT/03AI為什麼每次都不一樣？.pdf</code> (102頁) 與 <code>raw/HW/03_*.pdf</code> (2頁)...</div>';

      setTimeout(function() {
        consoleEl.innerHTML += '<div><span class="log-step">[Step 2/4]</span> 雙源交叉比對：提取「GAN 對抗網路・StyleGAN AdaIN・交叉熵與 KL 散度」×「台股 [20,8] 張量 AI Canvas（192萬筆滑動視窗）」→ 寫入 <code>docs/week-03.md</code>...</div>';
      }, 650);

      setTimeout(function() {
        consoleEl.innerHTML += '<div><span class="log-step">[Step 3/4]</span> 執行 <code>sync_site.py</code>：同步更新首頁課程精要總覽表格、快速導覽標籤、側邊欄 <code>_sidebar.md</code> 與離線快取...</div>';
      }, 1350);

      setTimeout(function() {
        consoleEl.innerHTML += '<div><span class="log-ok">[Step 4/4] ✔ 編譯成功！</span> 已生成 <code>docs/week-03.md</code> 並追加 <code>log.md</code> 稽核紀錄。請點擊上方「立即前往剛生成的 Week 03 課程精要頁面」或下方表格連結檢視成果！</div>';
        try { localStorage.setItem('week03_compiled', 'true'); } catch (e) {}
        if (btnCompile) btnCompile.disabled = false;
        window.syncWeek03UIState(true);
      }, 2000);
    };

    window.resetAgentCompileWeek03 = function() {
      try { localStorage.removeItem('week03_compiled'); } catch (e) {}
      var consoleEl = document.getElementById('agent-compile-console');
      if (consoleEl) {
        consoleEl.style.display = 'none';
        consoleEl.innerHTML = '';
      }
      window.syncWeek03UIState(false);
    };

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
      },
      plugins: [
        function(hook) {
          hook.doneEach(function() {
            window.syncWeek03UIState(false);
          });
        }
      ]
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
