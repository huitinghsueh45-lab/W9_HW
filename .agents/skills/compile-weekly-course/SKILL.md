---
name: compile-weekly-course
description: >-
  編譯與維護「生成式 AI 課程摘要與數位索引」網站之標準化工作流。當使用者將新週次的課堂講義與作業 PDF
  放入 raw/PPT/ 與 raw/HW/ 並要求解析編譯 week-XX.md、更新首頁索引、調整全站版型或同步離線快取時，必須啟用此技能。
---

# 每週課程摘要與數位索引 — 自動化編譯與維護技能 (compile-weekly-course)

本技能封裝了專案歷經討論定案的所有**版面視覺規範、全站統一命名、雙源 PDF 交叉解析流程、內頁列點式三段結構，以及 `file://` 零 404 離線快取同步機制**。

---

## 一、全站視覺與命名鐵律 (Design & Terminology Rules)

1. **配色與視覺風格（暖白松石綠・結構化複習筆記風）**：
   - 定義於 `assets/style.css`：採用柔和暖白紙張底色（`#faf9f5`）、純白圓角卡片（`#ffffff`）搭配頂部 `3px` 松石綠細飾條（`#367a6d`）、襯線大標題（`Noto Serif TC`、`#1d312c`）與極簡橫線表格。
2. **全站統一命名對照**：
   - **首頁主標題**：`生成式 AI 課程摘要與數位索引`
   - **首頁副標題**：`將每週課堂講義與作業實作化繁為簡，打造快速檢索、高效複習的結構化知識庫。`
   - **側邊欄（`docs/_sidebar.md`）**：固定分為 **「課程總覽」**（下轄 `課程摘要首頁`）與 **「每週課程精要」**（下轄各週連結）兩大分類。
   - **首頁總覽表格欄位（嚴禁出現「狀態欄」或「三段式結構欄」）**：
     固定為 4 欄：`週次` ｜ `核心主題名稱` ｜ `課堂理論 / 作業模型 / 延伸應用` ｜ `核心複習關鍵字`。
   - **最新週次標示規範（低調沉穩、禁止浮誇亮紅或火焰圖示）**：
     - 首頁上方快速索引膠囊：最新週次使用 `.badge-latest`（深松石綠實心膠囊，文字格式：`Week XX｜{主題簡稱} · 最新`）；已收錄之舊週次使用 `.badge-emerald`（淺鼠尾草綠膠囊）；未收錄週次使用 `.badge-amber`（白底細框）。
     - 首頁總覽表格：於最新週次主題名稱右側加上 `<span class="badge-new">最新</span>`。
     - 側邊欄：於最新週次連結文字末尾加上 ` · 最新`。
   - **重點整理框（`.callout-box`）命名與格式鐵律**：
     - **所有重點框內容一律採用「粗體小標＋列點清單（`<ul><li>...</li></ul>`）」呈現**，嚴禁使用長篇密集純文字段落。
     - **首頁重點框標題**：`最新課程重點（Week XX｜{當週主題}）`
     - **內頁三大區段標題與對應重點框標題**（不使用「區塊 A/B/C」字樣）：
       1. `一、課程摘要` $\rightarrow$ 重點框標題：**`課程摘要重點`**
       2. `二、作業摘要` $\rightarrow$ 重點框標題：**`作業摘要重點`**
       3. `三、技術關聯與延伸應用` $\rightarrow$ 重點框標題：**`技術關聯與延伸應用重點`**

---

## 二、標準執行步驟 (Step-by-Step Execution Pipeline)

### Step 1：執行雙源 PDF 掃描與文字萃取腳本
執行技能內建的萃取腳本，自動從 `raw/PPT/` 與 `raw/HW/` 讀取指定週次（或所有週次）的 PDF 文字：

```powershell
python .agents/skills/compile-weekly-course/scripts/extract_week_pdfs.py [週次編號，例如 03，若省略則自動掃描全部]
```
- 腳本會將萃取出的文字輸出至 `.agents/skills/compile-weekly-course/.cache/PPT_XX.txt` 與 `HW_XX.txt`，並印出精確檔名與頁數。
- **注意**：`raw/` 目錄為唯讀（Immutable），嚴禁修改、重新命名或刪除 `raw/` 下的任何檔案。

### Step 2：雙源深度解析與撰寫 `docs/week-XX.md`
讀取萃取出的講義與作業內容，並**嚴格參照範本 [week-template.md](./resources/week-template.md)** 生成 `docs/week-XX.md`：
1. **頂部與底部雙向導覽列（`.back-nav-bar`）**：
   - 左側固定放置 `<a href="#/" class="btn-back-index">← 回到課程總覽目錄</a>`。
   - 右側放置 `← 上一週：Week XX` 與 `下一週：Week YY →` 按鈕（同時記得更新前一週內頁檔案中的「下一週」連結與移除前一週的 `· 最新` 標記）。
2. **原始 PDF 檔案直連按鈕**：
   - 在上方概覽卡片，以及「**一、課程摘要**」與「**二、作業摘要**」的 `.card-title` 標題列右側，必須放上 `<a href="raw/PPT/檔名.pdf" target="_blank" class="pdf-link">📄 開啟課堂講義 PDF</a>` 與 `<a href="raw/HW/檔名.pdf" target="_blank" class="pdf-link">📄 開啟作業實作 PDF</a>`。
   - 務必保留 `target="_blank"`，確保點擊時直接開啟根目錄 `raw/` 下的 PDF 而不被 Docsify 路由攔截。
3. **三段式內容與列點重點**：
   - 交叉比對課堂公式／理論與作業實驗數據／程式碼，整理為結構化表格、關鍵程式碼區塊與底部的條列式 `.callout-box`。

### Step 3：同步更新 `docs/index.md` 與 `docs/_sidebar.md`
1. **`docs/index.md`**：
   - 更新上方「收錄週次」膠囊列：將新編譯週次設為 `.badge-latest`（`· 最新`），並將原最新週次改為 `.badge-emerald`。
   - 於「每週課程精要總覽」表格新增該週次列，將 `<span class="badge-new">最新</span>` 移至最新週次。
   - 更新底部「**最新課程重點**」區塊為最新週次的 4～5 點核心條列精華。
2. **`docs/_sidebar.md`**：
   - 在 `* **每週課程精要**` 下新增該週次連結，並將 ` · 最新` 移至最新週次。

### Step 4：執行網站同步與離線快取打包腳本，並記錄 `log.md`
每次修改任何 `docs/*.md` 後，**必須執行以下同步腳本**：

```powershell
python .agents/skills/compile-weekly-course/scripts/sync_site.py
```
- 該腳本會自動將 `docs/index.md` 同步複製為 `docs/README.md`，並將 `docs/` 下所有 `.md` 檔案內容打包寫入 `index.html` 的 `window.__DOCS_FALLBACK__` 中，確保使用者無論直接雙擊 `index.html`（`file://`）或透過伺服器（`http://`）開啟，皆**零 404 錯誤**。
- 最後，於根目錄 `log.md` 表格頂部新增一筆時間戳記與 `COMPILE` / `UPDATE` 變更紀錄。
