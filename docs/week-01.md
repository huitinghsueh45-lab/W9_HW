<div class="back-nav-bar">
  <a href="#/" class="btn-back-index">← 回到課程總覽目錄</a>
  <a href="#/week-02" class="btn-back-index">下一週：Week 02 神經網路與手寫辨識 →</a>
</div>

# 第 01 週課程精要：如何不焦慮地學 AI

<p class="report-subtitle">整合課堂函數映射原理、Colab 四大實作技巧與三大迴歸模型（OLS・3D 多元迴歸・邏輯斯分類）複習筆記。</p>

<div class="pill-row">
  <span class="badge badge-sky">Week 01</span>
  <span class="badge badge-sky">課程理論 × 作業實作</span>
  <span class="badge badge-emerald">結構化複習筆記</span>
</div>

<hr class="report-divider" />

<div class="dashboard-card">
  <div class="section-kicker">▼ 概覽：本週教材來源與複習區段</div>
  <p style="margin: 0.25rem 0 0.75rem 0;">
    <strong>課堂講義來源</strong>：<a href="raw/PPT/01如何不焦慮地學AI(學生點開顯示未發佈).pdf" target="_blank">01如何不焦慮地學AI(學生點開顯示未發佈).pdf</a>（政治大學 蔡炎龍老師）<br/>
    <strong>作業實作來源</strong>：<a href="raw/HW/01_中興大學 8113026207 科管博 薛慧婷 在colab中畫一個函數圖形-1.pdf" target="_blank">01_中興大學 8113026207 科管博 薛慧婷 在colab中畫一個函數圖形-1.pdf</a>（<a href="https://colab.research.google.com/drive/1AvKUfqU-4r3NtyNeic_gxuS3W4U2ur45?usp=sharing" target="_blank">開啟 Colab 筆記本</a>）
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
    <span>一、課程摘要 <span class="pipe-sep">｜</span> 用原理對抗 AI 焦慮・萬物皆函數 $Y = f_\theta(X)$</span>
    <a href="raw/PPT/01如何不焦慮地學AI(學生點開顯示未發佈).pdf" target="_blank" class="pdf-link">📄 開啟課堂講義 PDF</a>
  </div>

  <table>
    <thead>
      <tr>
        <th>序號</th>
        <th>核心議題 / 工具模組</th>
        <th>痛點迷思 / 語法特徵</th>
        <th>底層原理與解法</th>
        <th>複習關鍵指標</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td><strong>三大 AI 焦慮破除</strong></td>
        <td><span class="val-up">被取代</span> / 工具學不完 / 名詞太難</td>
        <td>各家基礎模型架構相似；Agent 只是「教 AI 做事的流程」</td>
        <td>用原理對抗焦慮</td>
      </tr>
      <tr>
        <td>2</td>
        <td><strong>呆萌型 AI 機器人</strong></td>
        <td>以為 AI 有自主意識與思考能力</td>
        <td>本質皆為參數化函數映射 $X \xrightarrow{f_\theta} Y$（含分類與生成）</td>
        <td><span class="val-down">Turing &amp; Feynman</span></td>
      </tr>
      <tr>
        <td>3</td>
        <td><strong>Colab 魔術與繪圖</strong></td>
        <td><code>%matplotlib inline</code> / <code>!pwd</code></td>
        <td>以 <code>np</code>, <code>pd</code>, <code>plt</code> 繪圖，並用 <code>zip(*points)</code> 轉換座標</td>
        <td><code>Shift+Enter</code> / <code>Tab</code></td>
      </tr>
      <tr>
        <td>4</td>
        <td><strong>筆記與動態互動</strong></td>
        <td><code>Ctrl+M M</code> / <code>ipywidgets</code></td>
        <td>支援 LaTeX 數學式與 <code>interact(draw, n=(1., 10.))</code> 滑桿</td>
        <td>即時視覺化試驗場</td>
      </tr>
    </tbody>
  </table>

  <p class="table-footnote">全學期技術主線：神經網路（Neural Networks）→ 生成對抗網路（GAN）→ 大型語言模型（LLM / RAG / Agent）→ 擴散模型（Diffusion Models）。</p>

  <div class="callout-box">
    <span class="callout-title">課程摘要重點</span>
    <ul>
      <li><strong>呆萌型函數本質</strong>：現代 AI 模型（包含影像辨識與生成式 AI）本身沒有自主意識，本質上都是一個接收輸入 $X$、計算輸出 $Y$ 的參數化函數 $f_\theta$。</li>
      <li><strong>分類與生成的統一視角</strong>：拍一張八哥照片輸入模型，是算出三個機率數字 $(y_1, y_2, y_3)$ 分別代表土八哥、白尾八哥與家八哥；文字與圖像生成則是將 Prompt 當作輸入 $X$ 映射出生成結果 $Y$。</li>
      <li><strong>破除工具焦慮</strong>：大型語言模型底層原理高度相通，掌握「函數映射」原理與 Colab 實作工具鏈後，就能讓 AI 照我們的方法做事，不再因每日新工具而焦慮。</li>
    </ul>
  </div>
</div>

<div class="module-block block-b">
  <div class="card-title">
    <span>二、作業摘要 <span class="pipe-sep">｜</span> Colab 函數與三大迴歸實作（OLS・3D 平面・Sigmoid）</span>
    <a href="raw/HW/01_中興大學 8113026207 科管博 薛慧婷 在colab中畫一個函數圖形-1.pdf" target="_blank" class="pdf-link">📄 開啟作業實作 PDF</a>
  </div>

  <table>
    <thead>
      <tr>
        <th>階段</th>
        <th>模型名稱與維度</th>
        <th>估計方程式 / 轉換函數</th>
        <th>關鍵特徵與實驗數據</th>
        <th>預測表現 / 診斷結論</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>0</td>
        <td><strong>基礎線性函數 (1D)</strong></td>
        <td>$f(x) = 3x + 2$</td>
        <td><code>np.linspace(-10, 10, 100)</code></td>
        <td>斜率固定為 $3$、截距為 $2$</td>
      </tr>
      <tr>
        <td>I</td>
        <td><strong>簡單線性迴歸 (OLS)</strong></td>
        <td>$\hat{Y} = 40.0 + 8.5X$</td>
        <td>讀書時數 $X \in [1,5]$ → 考分 $Y$</td>
        <td><span class="val-up">+8.5 分/時</span>｜$X=3.5 \Rightarrow 69.75$ 分</td>
      </tr>
      <tr>
        <td>II</td>
        <td><strong>多元線性迴歸 (3D)</strong></td>
        <td>$\hat{Y} = -8.45 + 4.02X_1 + 0.91X_2$</td>
        <td>時數 $X_1$ ＋ 出席率 $X_2 \in [60,95]$</td>
        <td><span class="val-up">+4.02 分/時</span>、<span class="val-down">+0.91 分/1%出席</span></td>
      </tr>
      <tr>
        <td>III</td>
        <td><strong>邏輯斯迴歸 (分類)</strong></td>
        <td>$P(Y=1\mid\mathbf{X}) = \frac{1}{1+e^{-z}}$</td>
        <td>200 筆雙特徵樣本｜預設門檻 <code>50%</code></td>
        <td>輸出 $0\sim 1$ 機率與線性決策邊界</td>
      </tr>
    </tbody>
  </table>

  <p class="table-footnote">Part I 殘差表檢驗：5 筆觀測值之殘差 $e = Y - \hat{Y}$ 分別為 $+1.5, -2.0, -0.5, -4.0, +2.5$，隨機散佈於 $y=0$ 基準線上下，符合線性假設。</p>

  ```python
  # Part I ~ III 核心建模與 3D / 決策邊界視覺化精要
  from sklearn.linear_model import LinearRegression, LogisticRegression
  import numpy as np

  # 1. 多元線性迴歸：讀書時數 (X1) + 出席率 (X2) -> 考試分數 (y)
  X1, X2 = np.array([1, 2, 3, 4, 5]), np.array([60, 70, 75, 90, 95])
  y = np.array([50, 65, 70, 85, 98])
  reg = LinearRegression().fit(np.column_stack((X1, X2)), y)

  # 2. 邏輯斯迴歸：線性組合 z 轉為 Sigmoid 機率 P(Y=1|X)
  # z = clf.decision_function(X_cls)
  # prob = 1 / (1 + np.exp(-z))  # 等同 clf.predict_proba(X_cls)[:, 1]
  ```

  <div class="callout-box">
    <span class="callout-title">作業摘要重點</span>
    <ul>
      <li><strong>從固定公式到數據擬合</strong>：將課堂基礎繪圖 $f(x)=3x+2$ 延伸至最小平方法（OLS），自動從資料點找出使垂直誤差平方和（SSE）最小的最佳擬合線。</li>
      <li><strong>殘差圖（Residual Plot）診斷</strong>：透過檢視誤差項 $e = Y - \hat{Y}$ 是否隨機分佈於 $y=0$ 基準線上下，確認線性模型假設是否成立，並辨識高估（$e < 0$）與低估（$e > 0$）樣本。</li>
      <li><strong>3D 多元迴歸與控制變因（Ceteris Paribus）</strong>：同時納入讀書時數 $X_1$ 與出席率 $X_2$ 後，在固定出席率下每多讀 1 小時平均提升 $+4.02$ 分，固定時數下出席率每增加 1% 則提升 $+0.91$ 分（若讀書 $3.5$ 小時且出席率 $80\%$，聯合預測為 $78.42$ 分）。</li>
    </ul>
  </div>
</div>

<div class="module-block block-c">
  <div class="card-title">
    <span>三、技術關聯與延伸應用 <span class="pipe-sep">｜</span> 銀行信用卡違約審查 <span class="pipe-sep">｜</span> 門檻 50%（可動態調校）</span>
  </div>

  <table>
    <thead>
      <tr>
        <th>決策維度</th>
        <th>觀察圖表與指標</th>
        <th>理想狀態 / 放寬策略 / 緊縮策略</th>
        <th>模型診斷與實務行動</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>信心度判讀</strong></td>
        <td>圖 1：Sigmoid 預測機率分佈</td>
        <td><span class="val-down">兩極化（5% 或 95%）</span> vs. <span class="val-up">集中於 48%~52%</span></td>
        <td>若多數樣本卡在 50% 附近，代表特徵不足、系統在瞎猜</td>
      </tr>
      <tr>
        <td><strong>動態門檻調整</strong></td>
        <td>圖 1：違約拒絕門檻（Threshold）</td>
        <td>預設 <code>50%</code> / <span class="val-down">景氣好放寬至 70%</span> / <span class="val-up">海嘯收緊至 20%</span></td>
        <td>不需重訓模型，直接依總經環境調整核貸風險胃納量</td>
      </tr>
      <tr>
        <td><strong>線性可分檢驗</strong></td>
        <td>圖 2：二維決策邊界（直尺切分）</td>
        <td>紅藍對角分群（線性可分） vs. 紅點包在藍點中間</td>
        <td>若無法用一條直線切開，即需引入多層神經網路（MLP）</td>
      </tr>
      <tr>
        <td><strong>例外客戶挖掘</strong></td>
        <td>圖 2：高風險區的正常還款藍點</td>
        <td>低收入＋高負債卻未違約之離群樣本</td>
        <td>點開個案追查是否具備「隱形資產」，迭代新特徵</td>
      </tr>
    </tbody>
  </table>

  <p class="table-footnote">跨週次演進：本週作業的「線性組合 $z = \mathbf{w}^T\mathbf{x} + b$ ＋ Sigmoid 激活函數 $\sigma(z)$」，正是第 02 週人工神經網路（ANN）中單一人工神經元的完整數學結構。</p>

  <div class="callout-box">
    <span class="callout-title">技術關聯與延伸應用重點</span>
    <ul>
      <li><strong>機率門檻的商業彈性</strong>：在銀行信用卡違約審查中，Sigmoid 機率圖能協助決策者依總經環境動態調整核貸門檻——景氣擴張衝業績時可放寬至 <code>70%</code> 才拒貸，金融海嘯保守風控時則收緊至 <code>20%</code> 即拒貸。</li>
      <li><strong>模型區辨力檢測</strong>：理想模型應讓客戶違約機率集中在 <code>5%</code> 或 <code>95%</code> 兩端；若大量集中在 <code>48%~52%</code>，代表現有特徵不足以區分風險。</li>
      <li><strong>線性分類邊界的極限與神經網路伏筆</strong>：當二維特徵空間中的違約紅點被正常藍點包圍在正中央時，任何一條直線都無法切開，這直接揭示了非線性問題必須引入多層神經網路（DNN）來解決。</li>
    </ul>
  </div>
</div>

<div class="back-nav-bar" style="margin-top: 2rem;">
  <a href="#/" class="btn-back-index">← 回到課程總覽目錄</a>
  <a href="#/week-02" class="btn-back-index">前往 Week 02：神經網路與手寫辨識 →</a>
</div>
