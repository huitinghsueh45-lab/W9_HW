# 📋 專案變更與編譯日誌 (Audit Log)

| 時間戳記 (Timestamp) | 類型 (Type) | 影響範圍 (Affected Paths) | 變更摘要 (Summary) |
| :--- | :---: | :--- | :--- |
| `2026-11-09 10:09` | `UPDATE` | `.gitignore`, `log.md` | 新增 `.gitignore`，排除 `W9_HW_協作歷程與成果摘要.md` 與 `.agents/skills/compile-weekly-course/.cache/` 暫存檔，避免上傳至 GitHub。 |
| `2026-11-09 10:00` | `COMPILE` | `docs/week-03.md`, `docs/index.md`, `docs/_sidebar.md`, `assets/style.css`, `index.html`, `.github/workflows/compile_week.yml`, `log.md` | 1. 雙源解析 `raw/PPT/03AI為什麼每次都不一樣？.pdf` 與 `raw/HW/03_中興大學 8113026207 科管博 薛慧婷.pdf`，編譯生成 `docs/week-03.md`（涵蓋 GAN 對抗網路、StyleGAN AdaIN、Cross-Entropy/KL 散度與台股 [20,8] 張量預測 AI Canvas）；2. 於首頁新增「⚡ 自動化維護 Agent 實測控制台（供助教一鍵編譯生成 Week 03 頁面）」互動按鈕與即時終端機日誌；3. 新增 `.github/workflows/compile_week.yml` 支援雲端 `workflow_dispatch` 手動按鈕觸發與 `raw/` 推播自動編譯。 |
| `2026-11-06 15:46` | `UPDATE` | `W9_HW_協作歷程與成果摘要.md`, `log.md` | 彙整本次專案從骨架建置、雙源 PDF 編譯（Week 01/02/05）、六階段修改歷程、404 離線快取排解到封裝 Agent Skill 之完整紀錄，產出供後續與 Gemini 協作撰寫作業報告之摘要檔。 |
| `2026-11-06 15:41` | `UPDATE` | `.agents/skills/compile-weekly-course/`, `log.md` | 將專案所有版面規範、全站統一命名、雙源 PDF 萃取腳本（`extract_week_pdfs.py`）、內頁標準範本（`week-template.md`）與雙模式零 404 同步腳本（`sync_site.py`）封裝為可重複執行的 Agent Skill（`compile-weekly-course`）。 |
| `2026-11-06 15:37` | `COMPILE` | `docs/week-05.md`, `docs/week-02.md`, `docs/index.md`, `docs/_sidebar.md`, `index.html`, `log.md` | 雙源解析 `raw/PPT/05AI怎麼記得前面說過什麼？.pdf` 與 `raw/HW/05_中興大學 8113026207 科管博 薛慧婷 用 Vibe Coding 做出一個互動網頁.pdf`；生成 `docs/week-05.md`（涵蓋 RNN/Transformer QKV 注意力機制、位置編碼、ResNet/Norm 與台股盤後選股報告互動網站實作），並同步更新首頁、側邊欄與離線快取。 |
| `2026-11-06 15:05` | `STYLE` | `assets/style.css`, `docs/index.md`, `docs/week-01.md`, `docs/week-02.md`, `docs/_sidebar.md`, `index.html` | 1. 調整色調為暖白松石綠（`#faf9f5` 紙張底色、`#2d665b` 深松石綠主色與卡片頂部細飾條），建立專屬學術筆記識別度；2. 首頁與內頁所有重點框改為條列式（Bullet Points）呈現；3. 收斂最新週次標示為沉穩深綠實心膠囊與淡綠 `最新` 小標籤；4. 於內頁「課程摘要」與「作業摘要」標題列新增直接開啟 `raw/PPT/` 與 `raw/HW/` 原始 PDF 之按鈕連結。 |
| `2026-11-06 14:58` | `UPDATE` | `docs/index.md`, `docs/week-01.md`, `docs/week-02.md`, `docs/_sidebar.md`, `assets/style.css`, `index.html`, `AGENTS.md` | 1. 移除首頁表格「三段式結構」欄並簡化內頁區段標題；2. 網站主標題定為「生成式 AI 課程摘要與數位索引」；3. 內頁頂部與底部新增「← 回到課程總覽目錄」與前後週次導覽按鈕；4. 首頁重點框改名為「最新課程重點」。 |
| `2026-11-06 14:51` | `COMPILE` | `docs/week-02.md`, `docs/index.md`, `docs/_sidebar.md`, `index.html`, `log.md` | 雙源解析 `raw/PPT/02神經網路的概念.pdf` 與 `raw/HW/02_中興大學 8113026207 科管博 薛慧婷 打造自己的DNN(全連結)手寫辨識.pdf`，生成 `docs/week-02.md` 並同步更新總覽索引與側邊欄。 |
| `2026-11-06 14:41` | `UPDATE` | `docs/index.md`, `docs/week-01.md`, `docs/_sidebar.md`, `index.html`, `AGENTS.md` | 全站名詞統一與內容修訂：移除首頁狀態欄；內頁各區段重點框改為「課程摘要重點 / 作業摘要重點 / 技術關聯與延伸應用重點」；側邊欄改為「課程總覽」與「每週課程精要」。 |
| `2026-11-06 14:20` | `STYLE` | `assets/style.css`, `index.html`, `docs/index.md`, `docs/week-01.md`, `docs/_sidebar.md` | 依附圖調整網頁為淺色極簡一頁式簡報風格；修正 `index.html` 在 `file://` 與相對路徑下的 `404 - Not found` 問題。 |
| `2026-11-06 14:02` | `COMPILE` | `docs/week-01.md`, `docs/index.md`, `log.md` | 雙源解析 `raw/PPT/01如何不焦慮地學AI(學生點開顯示未發佈).pdf` 與 `raw/HW/01_中興大學 8113026207 科管博 薛慧婷 在colab中畫一個函數圖形-1.pdf`；生成 `docs/week-01.md`。 |
| `2026-11-06 13:55` | `UPDATE` | `raw/PPT/`, `raw/HW/`, `AGENTS.md`, `docs/index.md` | 新增 `raw/PPT/` 與 `raw/HW/` 子目錄；於 `AGENTS.md` 寫入兩位數週次命名規範（`01_xxx.pdf`）與雙源自動讀取、交叉比對流程。 |
| `2026-11-06 13:45` | `INIT` | `raw/`, `docs/`, `assets/`, `AGENTS.md`, `index.html`, `assets/style.css`, `docs/index.md`, `log.md` | 初始化專案骨架、Docsify 主題與三段式模組規範。 |
