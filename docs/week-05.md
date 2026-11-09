<div class="back-nav-bar">
  <a href="#/" class="btn-back-index">← 回到課程總覽目錄</a>
  <a href="#/week-03" class="btn-back-index">← 上一週：Week 03 AI 為什麼每次都不一樣</a>
</div>

# 第 05 週課程精要：Transformer 注意力機制與 Vibe Coding 互動網頁實作

<p class="report-subtitle">從 RNN 記憶機制、QKV 自注意力與位置編碼原理，到結合 Softmax 預測模型與 GitHub Actions 的台股盤後選股互動網站。</p>

<div class="pill-row">
  <span class="badge badge-latest">Week 05 · 最新</span>
  <span class="badge badge-sky">RNN 與 Transformer 原理</span>
  <span class="badge badge-emerald">Vibe Coding 互動網頁</span>
</div>

<hr class="report-divider" />

<div class="dashboard-card">
  <div class="section-kicker">▼ 概覽：本週教材來源與複習區段</div>
  <p style="margin: 0.25rem 0 0.75rem 0;">
    <strong>課堂講義來源</strong>：<a href="raw/PPT/05AI怎麼記得前面說過什麼？.pdf" target="_blank">05AI怎麼記得前面說過什麼？.pdf</a>（共 86 頁，政治大學 蔡炎龍老師）<br/>
    <strong>作業實作來源</strong>：<a href="raw/HW/05_中興大學 8113026207 科管博 薛慧婷 用 Vibe Coding 做出一個互動網頁.pdf" target="_blank">05_中興大學 8113026207 科管博 薛慧婷 用 Vibe Coding 做出一個互動網頁.pdf</a>（<a href="https://huitinghsueh45-lab.github.io/tw-stock-report/" target="_blank">開啟線上互動網站</a>｜<a href="https://github.com/huitinghsueh45-lab/tw-stock-report" target="_blank">GitHub 原始碼</a>）
  </p>
  <div class="pill-row">
    <span class="badge badge-emerald">一、課程摘要</span>
    <span class="badge badge-outline">二、作業摘要</span>
    <span class="badge badge-outline">三、技術關聯與延伸應用</span>
  </div>
  <p class="table-footnote">本頁依「課程摘要」、「作業摘要」、「技術關聯與延伸應用」結構編排，各區段標題右側均可直接點選開啟原始 PDF 檔案。</p>
</div>

<div class="module-block block-a">
  <div class="card-title">
    <span>一、課程摘要 <span class="pipe-sep">｜</span> AI 怎麼記得前面說過什麼？（RNN・QKV 注意力・Vibe Coding）</span>
    <a href="raw/PPT/05AI怎麼記得前面說過什麼？.pdf" target="_blank" class="pdf-link">📄 開啟課堂講義 PDF</a>
  </div>

  <table>
    <thead>
      <tr>
        <th>序號</th>
        <th>核心概念模組</th>
        <th>數學定義 / 運算機制</th>
        <th>設計目的與關鍵特性</th>
        <th>複習關鍵指標</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td><strong>遞歸神經網路 (RNN)</strong></td>
        <td>$\mathbf{h}_t = \sigma(W_X^T \mathbf{x}_t + W_H^T \mathbf{h}_{t-1} + \mathbf{b})$</td>
        <td>將上一步的隱藏狀態 $\mathbf{h}_{t-1}$ 傳回當下步驟，使網路具備序列記憶</td>
        <td>逐步依序讀取、難以平行化</td>
      </tr>
      <tr>
        <td>2</td>
        <td><strong>QKV 縮放點積注意力</strong></td>
        <td>$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$</td>
        <td>以內積計算 Query 與 Key 的相關強度；除以 $\sqrt{d_k}$ 避免 Softmax 贏者通吃</td>
        <td><span class="val-down">Attention Is All You Need</span></td>
      </tr>
      <tr>
        <td>3</td>
        <td><strong>多頭與跨模態注意力</strong></td>
        <td>$Q=XW_Q^n, K=XW_K^n, V=XW_V^n$</td>
        <td>Decoder 透過 Mask 遮蔽未來資訊；中間層以 $Q_{\text{dec}}$ 查詢 Encoder 的 $K, V$</td>
        <td>文字生圖混入語意之核心機制</td>
      </tr>
      <tr>
        <td>4</td>
        <td><strong>位置編碼 (Positional Encoding)</strong></td>
        <td>$p_{2k}=\sin(\omega_k t), \; p_{2k+1}=\cos(\omega_k t)$，$\omega_k = 10000^{-2k/d}$</td>
        <td>為平行化 Self-Attention 補回字詞先後順序（低位數時鐘快、高位數時鐘慢）</td>
        <td>$\mathbf{x}_t + \mathbf{p}_t$ 疊加位置資訊</td>
      </tr>
      <tr>
        <td>5</td>
        <td><strong>深層穩定技術 (ResNet &amp; Norm)</strong></td>
        <td>殘差 $\mathbf{z} + \ell(\mathbf{z})$；LayerNorm / RMSNorm / DyT</td>
        <td>殘差連結讓網路只學「未學會的差值 $\ell(\mathbf{z})=f(\mathbf{z})-\mathbf{z}$」，撫平損失地形</td>
        <td><span class="val-up">Llama RMSNorm / Meta DyT</span></td>
      </tr>
      <tr>
        <td>6</td>
        <td><strong>Vibe Coding 規格書工作流</strong></td>
        <td>正確的資訊 ＋ 清楚的指引 $\rightarrow$ 規格書 $\rightarrow$ <code>index.html</code></td>
        <td>先請 AI 提問釐清需求產出規格書，再生成單檔網頁並部署至 GitHub Pages</td>
        <td>HTML + CSS + JS 單檔部署</td>
      </tr>
    </tbody>
  </table>

  <p class="table-footnote">線性代數核心直覺：矩陣乘法「先列後行」，向量乘以矩陣（如 $\text{softmax}(QK^T)V$）本質上就是用注意力權重係數 $\alpha_t$ 對 $V$ 矩陣的列向量 $\mathbf{v}_t$ 做線性組合 $\sum_{t=1}^T \alpha_t \mathbf{v}_t$。</p>

  <div class="callout-box">
    <span class="callout-title">課程摘要重點</span>
    <ul>
      <li><strong>從 RNN 到 Transformer 的典範轉移</strong>：RNN 透過把上一步輸出 $\mathbf{h}_{t-1}$ 傳回來記憶前文，但必須逐字計算；Google 在 2017 年提出 Transformer，改用矩陣乘法一次平行算完所有字詞間的 <strong>Self-Attention（自注意力）</strong>。</li>
      <li><strong>看懂 QKV 與 $\sqrt{d_k}$ 縮放技巧</strong>：每個詞向量經線性轉換產生 Query（問題）、Key（索引）與 Value（內容），透過內積 $QK^T$ 算出關聯度；為了防止 Softmax「贏者通吃」導致權重過度極端，除以 $\sqrt{d_k}$ 將數值拉回 $0$ 附近再對 $V$ 做加權平均。</li>
      <li><strong>位置編碼與殘差穩定機制</strong>：利用不同頻率的 $(\sin, \cos)$ 時鐘向量為平行輸入補上位置資訊，並搭配 <strong>ResNet 殘差連結（$\mathbf{z}+\ell(\mathbf{z})$）</strong>與 <strong>LayerNorm / RMSNorm</strong>，讓深層網路穩定收斂。</li>
      <li><strong>Vibe Coding 必殺技</strong>：寫出好程式的關鍵是「和 AI 一起寫規格書」——先要求 AI 不要急著寫 code，而是透過問答釐清需求、產出完整規格書，再一次轉換為互動網頁並透過 GitHub Pages 發布。</li>
    </ul>
  </div>
</div>

<div class="module-block block-b">
  <div class="card-title">
    <span>二、作業摘要 <span class="pipe-sep">｜</span> Vibe Coding 實作「盤後快訊：台股選股報告產生器」</span>
    <a href="raw/HW/05_中興大學 8113026207 科管博 薛慧婷 用 Vibe Coding 做出一個互動網頁.pdf" target="_blank" class="pdf-link">📄 開啟作業實作 PDF</a>
  </div>

  <table>
    <thead>
      <tr>
        <th>系統模組</th>
        <th>實作規格與技術細節</th>
        <th>關鍵參數 / 驗證數據</th>
        <th>工程設計亮點</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>預測模型（W3 落地）</strong></td>
        <td>台灣 50 成分股（FinMind 約 1 年資料），輸入 <strong>20 交易日 × 8 項價量籌碼特徵</strong>，預測未來 5 日三分類（$\pm 3\%$）</td>
        <td>訓練集 <code>10,240</code> 筆 / 驗證集 <code>3,000</code> 筆（中間留空防重疊）；L2 正則化 <code>0.0002</code></td>
        <td>Softmax 權重內嵌前端，瀏覽器即時推論與 Python 核對一致</td>
      </tr>
      <tr>
        <td><strong>模型驗證期表現</strong></td>
        <td>整體準確率 <code>49.1%</code>（基準 <code>44.5%</code>）、Log-loss <code>0.948</code>（基準 <code>1.083</code>）</td>
        <td>$P(\text{上漲})\ge 50\%$ 實際上漲率 <span class="val-up">54.6%</span>；$\ge 60\%$ 達 <span class="val-up">58.8%</span>；$\ge 70\%$ 僅 18 筆（<code>66.7%</code>）</td>
        <td>誠實揭露 $\ge 70\%$ 樣本過少限制，不人為調降預設門檻迎合</td>
      </tr>
      <tr>
        <td><strong>確定性報告規則（W4 落地）</strong></td>
        <td>依原始機率篩選排序、最多列前 5 檔、異常資料自動剔除並提示、自動換算上漲/下跌比與勝率優勢</td>
        <td>門檻滑桿 <code>50% ~ 90%</code>（預設 <code>70%</code>）；低於 70% 自動改標「自訂門檻觀察股」</td>
        <td>以確定性 JS 程式取代 LLM 即時生成，精準控制 250~300 字白話重點</td>
      </tr>
      <tr>
        <td><strong>個股明細互動抽屜</strong></td>
        <td>點擊個股展開三機率長條、週(5日)/月(20日)/季(60日)標準化收盤走勢、量能倍數與外資投信買賣超</td>
        <td>支援滑鼠/觸控移動即時讀數，並列出近 5 日外資與投信買賣超張數合計</td>
        <td>桌面版右側滑出、手機版底部滑出＋RWD 卡片式排版（v9 修正）</td>
      </tr>
      <tr>
        <td><strong>GitHub Actions 自動更新</strong></td>
        <td><code>daily.yml</code> + <code>update_daily.py</code> 每週一至五 22:00 自動抓取並重算最近 10 個交易日</td>
        <td>三大法人或融資覆蓋率 <span class="val-down">&lt; 80% 自動退回前一交易日</span>；離線備援 <code>2026/10/15</code> 快照</td>
        <td>徹底解決籌碼未公布時以 0 補值導致預測失準之隱患</td>
      </tr>
    </tbody>
  </table>

  <p class="table-footnote">專案架構：由單一入口 <code>index.html</code>（內含 HTML/CSS/JS 與模型權重）、每日資料檔 <code>real_data.json</code>、更新腳本 <code>update_daily.py</code> 與排程檔 <code>.github/workflows/daily.yml</code> 組成。</p>

  ```javascript
  // 前端確定性報告篩選、排序與換算指標核心邏輯（對應 W4 規格程式化）
  function generateReport(stocks, threshold = 0.70) {
    // 1. 資料異常檢查：三機率加總與 100% 相差超過 1 個百分點則剔除並記錄提示
    const valid = stocks.filter(s => Math.abs((s.pUp + s.pFlat + s.pDown) - 1.0) <= 0.01);

    // 2. 原始機率篩選（不四捨五入）與雙重排序：P(上漲) 降序 -> P(下跌) 升序
    const passed = valid
      .filter(s => s.pUp >= threshold)
      .sort((a, b) => (b.pUp - a.pUp) || (a.pDown - b.pDown));

    // 3. 換算衍生指標：上漲/下跌比、勝率優勢（百分點）、五級星等（僅 >= 70% 計星）
    return passed.slice(0, 5).map(s => ({
      ...s,
      upDownRatio: s.pDown === 0 ? '無下跌機率' : (s.pUp / s.pDown).toFixed(1),
      edgePts: ((s.pUp - s.pDown) * 100).toFixed(1),
      stars: s.pUp >= 0.70 ? Math.floor((s.pUp - 0.65) / 0.05) : '不計星'
    }));
  }
  ```

  <div class="callout-box">
    <span class="callout-title">作業摘要重點</span>
    <ul>
      <li><strong>跨週次構想的完整閉環（W3 模型 + W4 規則 + W5 互動網站）</strong>：將第三週停留於規劃的「台股趨勢預測模型」與第四週「選股報告 Prompt」實際打造成每天可打開、30 秒讀完重點的線上系統。</li>
      <li><strong>前端內嵌模型與誠實量化評估</strong>：以台灣 50 成分股 $20 \times 8$ 特徵訓練 Softmax 迴歸，驗證期證明 $P(\text{上漲}) \ge 60\%$ 群組實際上漲率提升至 <code>58.8%</code>；面對預設 <code>70%</code> 門檻下最新日無股票達標（最高 68.5%），誠實呈現「0 檔版面」並引導使用者操作門檻滑桿。</li>
      <li><strong>九輪迭代（v1～v9）的工程除錯</strong>：透過與 Claude 協作經歷 9 個版本演進，不僅解決了手機版表格裁切問題（改為 RWD 卡片），更抓出「籌碼未公布時補 0 導致預測失真」的關鍵 Bug，建立覆蓋率 $<80\%$ 自動回退前一交易日的防護機制。</li>
    </ul>
  </div>
</div>

<div class="module-block block-c">
  <div class="card-title">
    <span>三、技術關聯與延伸應用 <span class="pipe-sep">｜</span> 規格驅動開發（Spec-Driven）與混合式 AI 系統設計</span>
  </div>

  <table>
    <thead>
      <tr>
        <th>技術維度</th>
        <th>課堂理論基礎 (`raw/PPT/05_*.pdf`)</th>
        <th>作業系統落實 (`raw/HW/05_*.pdf`)</th>
        <th>軟體工程與 AI 實務啟示</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>序列特徵與機率輸出</strong></td>
        <td>時間序列張量表示與 Softmax 機率正規化</td>
        <td>以 <code>20 日 × 8 特徵</code> 預測上漲/盤整/下跌三類機率，加總嚴格為 100%</td>
        <td>金融時序預測需留空切分訓練/驗證期，防止未來資訊洩漏（Data Leakage）</td>
      </tr>
      <tr>
        <td><strong>確定性邏輯 vs. LLM</strong></td>
        <td>Prompt 強調「正確資訊＋清楚指引」與規格書先行</td>
        <td>將 W4 中 LLM 做不好的「字數控制、精確排序、邊界條件」改由 JS 確定性程式實作</td>
        <td><span class="val-down">Neuro-Symbolic 混合思維</span>：用 AI 寫出嚴謹的確定性規則程式，比每次叫 LLM 硬算更可靠</td>
      </tr>
      <tr>
        <td><strong>人機協作分工模式</strong></td>
        <td>領域專家（人類）定義問題與驗收，AI 負責撰寫規格與程式碼</td>
        <td>作者負責決策方向（縮減規模為台灣 50、定義籌碼回退規則、手機實測），Claude 負責實作</td>
        <td>印證第 02 週 Dive Point：「AI 落地為什麼領域專家才是關鍵」</td>
      </tr>
      <tr>
        <td><strong>自動化資料管線</strong></td>
        <td>GitHub 儲存庫建置與 GitHub Pages 靜態網站發布</td>
        <td>結合 GitHub Actions 定時爬蟲、資料完整性驗證與前端離線快照備援</td>
        <td>將靜態展示頁升級為具備 MLOps 每日自動推論能力之輕量級生產系統</td>
      </tr>
    </tbody>
  </table>

  <p class="table-footnote">延伸思考：目前作業採用線性 Softmax 迴歸處理拉平後的 $20 \times 8$ 特徵；未來若要進一步捕捉跨日時間依賴性，即可直接套用本週課堂所學之 <strong>RNN 或 Transformer Self-Attention 層</strong>！</p>

  <div class="callout-box">
    <span class="callout-title">技術關聯與延伸應用重點</span>
    <ul>
      <li><strong>用 AI 寫「確定性程式」解決 LLM 幻覺</strong>：第四週發現直接叫 LLM 產出報告時，常在排序、小數點判斷與字數控制上出錯；第五週透過 Vibe Coding 請 AI 將這些規則寫成 JavaScript 函數，完美兼具「規則零誤差」與「零 API 推論成本」。</li>
      <li><strong>規格驅動與漸進式驗證（Mock → Real → MLOps）</strong>：先以模擬數據（v1~v4）驗收所有極端情境（>5檔、0檔、資料異常），再接上 Colab 訓練的真實模型（v5），最後部署 GitHub Actions 自動化管線（v6~v9），是極佳的 AI 輔助軟體工程範本。</li>
      <li><strong>模型演進方向</strong>：本系統已具備完整的 $20 \times 8$ 時間序列資料管線與驗證基準（Log-loss <code>0.948</code>），後續可將底層模型由 Softmax 迴歸替換為本週課堂講授的 <strong>Transformer Encoder（以 20 個交易日為 Token 序列計算 Self-Attention）</strong>，進一步捕捉關鍵交易日的量價注意力權重。</li>
    </ul>
  </div>
</div>

<div class="back-nav-bar" style="margin-top: 2rem;">
  <a href="#/" class="btn-back-index">← 回到課程總覽目錄</a>
  <a href="#/week-03" class="btn-back-index">← 上一週：Week 03 AI 為什麼每次都不一樣</a>
</div>
