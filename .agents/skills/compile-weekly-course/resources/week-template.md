<div class="back-nav-bar">
  <a href="#/" class="btn-back-index">← 回到課程總覽目錄</a>
  <div>
    <a href="#/week-PREV" class="btn-back-index">← 上一週：Week PREV</a>
    <!-- 若有下一週則加上：<a href="#/week-NEXT" class="btn-back-index">下一週：Week NEXT →</a> -->
  </div>
</div>

# 第 XX 週課程精要：{當週核心主題名稱}

<p class="report-subtitle">{一句話濃縮本週課堂理論、作業模型與延伸應用之複習副標}</p>

<div class="pill-row">
  <!-- 若為最新週次使用 badge-latest，否則使用 badge-sky -->
  <span class="badge badge-latest">Week XX · 最新</span>
  <span class="badge badge-sky">{理論關鍵字}</span>
  <span class="badge badge-emerald">{實作關鍵字}</span>
</div>

<hr class="report-divider" />

<div class="dashboard-card">
  <div class="section-kicker">▼ 概覽：本週教材來源與複習區段</div>
  <p style="margin: 0.25rem 0 0.75rem 0;">
    <strong>課堂講義來源</strong>：<a href="raw/PPT/{PPT檔名}.pdf" target="_blank">{PPT檔名}.pdf</a>（共 N 頁，政治大學 蔡炎龍老師）<br/>
    <strong>作業實作來源</strong>：<a href="raw/HW/{HW檔名}.pdf" target="_blank">{HW檔名}.pdf</a>（<a href="{Colab或成品連結}" target="_blank">開啟實作連結</a>）
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
    <span>一、課程摘要 <span class="pipe-sep">｜</span> {課堂理論副標}</span>
    <a href="raw/PPT/{PPT檔名}.pdf" target="_blank" class="pdf-link">📄 開啟課堂講義 PDF</a>
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
        <td><strong>{概念名稱}</strong></td>
        <td>{公式或機制}</td>
        <td>{核心說明}</td>
        <td>{關鍵指標}</td>
      </tr>
    </tbody>
  </table>

  <p class="table-footnote">{補充說明或文獻註腳}</p>

  <div class="callout-box">
    <span class="callout-title">課程摘要重點</span>
    <ul>
      <li><strong>{重點小標 1}</strong>：{條列說明 1}</li>
      <li><strong>{重點小標 2}</strong>：{條列說明 2}</li>
      <li><strong>{重點小標 3}</strong>：{條列說明 3}</li>
    </ul>
  </div>
</div>

<div class="module-block block-b">
  <div class="card-title">
    <span>二、作業摘要 <span class="pipe-sep">｜</span> {作業實作副標}</span>
    <a href="raw/HW/{HW檔名}.pdf" target="_blank" class="pdf-link">📄 開啟作業實作 PDF</a>
  </div>

  <table>
    <thead>
      <tr>
        <th>階段 / 模組</th>
        <th>實作規格與架構設計</th>
        <th>關鍵超參數 / 實驗數據</th>
        <th>預測表現 / 診斷結論</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>{模組 1}</strong></td>
        <td>{規格說明}</td>
        <td>{參數與數據}</td>
        <td>{成果結論}</td>
      </tr>
    </tbody>
  </table>

  <p class="table-footnote">{實驗環境與補充註腳}</p>

  ```python
  # 關鍵實作程式碼精要
  ```

  <div class="callout-box">
    <span class="callout-title">作業摘要重點</span>
    <ul>
      <li><strong>{重點小標 1}</strong>：{條列說明 1}</li>
      <li><strong>{重點小標 2}</strong>：{條列說明 2}</li>
      <li><strong>{重點小標 3}</strong>：{條列說明 3}</li>
    </ul>
  </div>
</div>

<div class="module-block block-c">
  <div class="card-title">
    <span>三、技術關聯與延伸應用 <span class="pipe-sep">｜</span> {延伸應用副標}</span>
  </div>

  <table>
    <thead>
      <tr>
        <th>評估 / 決策維度</th>
        <th>課堂理論基礎 (`raw/PPT/`)</th>
        <th>作業實作印證 (`raw/HW/`)</th>
        <th>實務落地與進階優化方向</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>{維度 1}</strong></td>
        <td>{理論對應}</td>
        <td>{實作對應}</td>
        <td>{延伸洞察}</td>
      </tr>
    </tbody>
  </table>

  <p class="table-footnote">{跨週次演進關聯註腳}</p>

  <div class="callout-box">
    <span class="callout-title">技術關聯與延伸應用重點</span>
    <ul>
      <li><strong>{重點小標 1}</strong>：{條列說明 1}</li>
      <li><strong>{重點小標 2}</strong>：{條列說明 2}</li>
      <li><strong>{重點小標 3}</strong>：{條列說明 3}</li>
    </ul>
  </div>
</div>

<div class="back-nav-bar" style="margin-top: 2rem;">
  <a href="#/" class="btn-back-index">← 回到課程總覽目錄</a>
  <div>
    <a href="#/week-PREV" class="btn-back-index">← 上一週：Week PREV</a>
  </div>
</div>
