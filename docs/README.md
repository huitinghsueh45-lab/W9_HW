# 生成式 AI 課程摘要與數位索引

<p class="report-subtitle">將每週課堂講義與作業實作化繁為簡，打造快速檢索、高效複習的結構化知識庫。</p>

<div class="pill-row">
  <span class="badge badge-sky">TAICA 生成式 AI</span>
  <span class="badge badge-sky">文字與圖像生成的原理與實務</span>
  <span class="badge badge-sky">結構化複習筆記</span>
</div>

<hr class="report-divider" />

<div class="agent-console-card" id="ta-compiler-panel">
  <div class="section-kicker" style="margin-bottom: 0.45rem;">⚡ 自動化維護 Agent 實測控制台（供助教一鍵體驗 Week 03 教材編譯生成）</div>
  <p style="margin: 0.25rem 0 0.65rem 0; font-size: 0.92rem;">
    系統偵測到 <code>raw/PPT/</code> 與 <code>raw/HW/</code> 已放入<strong>第 03 週原始教材 PDF</strong>（唯讀來源檔）：<br/>
    • <strong>課堂講義</strong>：<a href="raw/PPT/03AI為什麼每次都不一樣？.pdf" target="_blank"><code>raw/PPT/03AI為什麼每次都不一樣？.pdf</code></a>（102 頁）<br/>
    • <strong>作業實作</strong>：<a href="raw/HW/03_中興大學 8113026207 科管博 薛慧婷.pdf" target="_blank"><code>raw/HW/03_中興大學 8113026207 科管博 薛慧婷.pdf</code></a>（2 頁，呆萌型台股預測機器人 AI Canvas）
  </p>
  <div class="agent-btn-row">
    <button id="btn-compile-w03" class="btn-agent-primary" onclick="window.runAgentCompileWeek03()">
      ⚡ 一鍵執行 Agent 編譯生成 Week 03 頁面
    </button>
    <a id="btn-goto-w03" href="#/week-03" class="btn-agent-success" style="display: none;">
      👉 立即前往剛生成的 Week 03 課程精要頁面 →
    </a>
    <button id="btn-reset-w03" class="btn-agent-secondary" style="display: none;" onclick="window.resetAgentCompileWeek03()">
      🔄 重置回「待編譯」狀態（供重複測試）
    </button>
  </div>
  <div id="agent-compile-console" class="agent-terminal"></div>
  <p class="table-footnote" style="margin-top: 0.65rem; margin-bottom: 0;">
    💡 <strong>雙軌執行支援</strong>：助教可直接點擊上方按鈕於前端即時體驗 <code>compile-weekly-course</code> 技能的四階段編譯並解鎖 <code>Week 03</code> 內頁；若於 GitHub 儲存庫後台，亦可透過 <code>Actions → Compile Weekly Course Material → Run workflow</code> 觸發雲端自動化管線。
  </p>
</div>

<div class="dashboard-card">
  <div class="section-kicker">▼ 導覽：每週課程快速索引</div>
  <p style="margin: 0.4rem 0 0.75rem 0;"><strong>收錄週次</strong>　點擊週次標籤即可直接跳轉至該週的課程摘要、作業實作與延伸複習筆記（深綠實心標籤為最新更新週別）：</p>
  <div class="pill-row">
    <a href="#/week-01" style="text-decoration: none;"><span class="badge badge-emerald">Week 01｜如何不焦慮地學 AI</span></a>
    <a href="#/week-02" style="text-decoration: none;"><span class="badge badge-emerald">Week 02｜神經網路與手寫辨識 DNN</span></a>
    <span id="pill-week-03-uncompiled" class="badge badge-amber" style="cursor: pointer;" onclick="window.runAgentCompileWeek03()" title="點擊上方或此處一鍵編譯生成 Week 03">Week 03（待編譯 · 點此生成）</span>
    <a id="pill-week-03-compiled" href="#/week-03" style="text-decoration: none; display: none;"><span class="badge badge-emerald">Week 03｜GAN 與交叉熵・AI Canvas</span></a>
    <span class="badge badge-amber">Week 04</span>
    <a href="#/week-05" style="text-decoration: none;"><span class="badge badge-latest">Week 05｜Transformer 與 Vibe Coding · 最新</span></a>
  </div>
  <p class="table-footnote">各週內容統一依「課程摘要」、「作業摘要」、「技術關聯與延伸應用」三大區段整理，便於考前與課後快速複習。</p>
</div>

<div class="dashboard-card">
  <div class="card-title">
    <span>每週課程精要總覽 <span class="pipe-sep">｜</span> 雙源教材整合（講義 PPT × 作業 HW）</span>
  </div>

  <table>
    <thead>
      <tr>
        <th>週次</th>
        <th>核心主題名稱</th>
        <th>課堂理論 / 作業模型 / 延伸應用</th>
        <th>核心複習關鍵字</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>01</td>
        <td><strong><a href="#/week-01">如何不焦慮地學 AI</a></strong></td>
        <td><span class="val-up">函數映射 $f_\theta$</span> / 簡單與多元迴歸 / <span class="val-down">邏輯斯風控</span></td>
        <td>Colab 四大技能、OLS、3D 迴歸、決策邊界</td>
      </tr>
      <tr>
        <td>02</td>
        <td><strong><a href="#/week-02">神經網路與手寫辨識 DNN</a></strong></td>
        <td><span class="val-up">神經元與梯度下降</span> / 4 版本控制變因 DNN / <span class="val-down">Gradio 部署偏移</span></td>
        <td>Tensor、Softmax、ReLU、Dropout、Distribution Shift</td>
      </tr>
      <tr id="row-week-03" style="display: none;">
        <td>03</td>
        <td><strong><a href="#/week-03">AI 為什麼每次都不一樣？</a></strong> <span class="badge-new">剛生成</span></td>
        <td><span class="val-up">GAN 與交叉熵・KL 散度</span> / 台股 $[20,8]$ 預測 AI Canvas / <span class="val-down">192 萬筆滑動視窗</span></td>
        <td>潛張量 $z$、StyleGAN、AdaIN、Cross-Entropy、Soft Target</td>
      </tr>
      <tr>
        <td>05</td>
        <td><strong><a href="#/week-05">Transformer 與 Vibe Coding 實作</a></strong> <span class="badge-new">最新</span></td>
        <td><span class="val-up">QKV 自注意力與位置編碼</span> / 台股選股報告產生器 / <span class="val-down">GitHub Actions 自動化</span></td>
        <td>RNN、Self-Attention、ResNet、RMSNorm、規格書驅動開發</td>
      </tr>
    </tbody>
  </table>

  <p class="table-footnote">教材來源：每週課堂講義 <code>raw/PPT/XX_*.pdf</code> 與作業實作 <code>raw/HW/XX_*.pdf</code> 雙源交叉比對。</p>
  <p style="margin-top: 0.5rem;"><a href="#/week-05">點選任一週次，查看該週完整課程精要 →</a></p>

  <div class="callout-box">
    <span class="callout-title">最新課程重點（Week 05｜Transformer 注意力機制與 Vibe Coding 互動網頁）</span>
    <ul>
      <li><strong>從 RNN 到 Transformer 自注意力機制</strong>：RNN 透過隱藏狀態 $\mathbf{h}_{t-1}$ 逐步傳遞記憶；Transformer 則以矩陣內積一次平行算完所有字詞的相關性 $\text{Attention}(Q,K,V) = \text{softmax}(QK^T/\sqrt{d_k})V$，並除以 $\sqrt{d_k}$ 解決 Softmax「贏者通吃」問題。</li>
      <li><strong>位置編碼與深層穩定技術</strong>：透過不同頻率的 $(\sin, \cos)$ 時鐘向量補回平行運算缺少的字序資訊，並搭配 <strong>ResNet 殘差連結（$\mathbf{z}+\ell(\mathbf{z})$）</strong>與 <strong>LayerNorm / RMSNorm / Dynamic Tanh (DyT)</strong> 確保深層網路穩定訓練。</li>
      <li><strong>Vibe Coding 必殺技（規格書先行）</strong>：先請 AI 透過問答釐清需求、共同產出完整「程式規格書」，再生成單一檔案 <code>index.html</code> 並部署至 GitHub Pages。</li>
      <li><strong>台股盤後選股報告產生器（W3 模型 + W4 規則 + W5 網站閉環）</strong>：採用台灣 50 成分股（<code>20 交易日 × 8 項價量籌碼特徵</code>）訓練 Softmax 迴歸並將權重內嵌前端，驗證期 $P(\text{上漲})\ge 60\%$ 群組實際上漲率達 <code>58.8%</code>。</li>
      <li><strong>確定性程式與 MLOps 防護</strong>：將 W4 篩選排序與 250~300 字白話重點改由 JavaScript 確定性程式實作，並於 GitHub Actions 每日排程加入「籌碼覆蓋率 &lt; 80% 自動回退前一交易日」機制，避免未公布資料補 0 造成預測失真。</li>
    </ul>
  </div>
</div>
