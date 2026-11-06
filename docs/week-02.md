<div class="back-nav-bar">
  <a href="#/" class="btn-back-index">← 回到課程總覽目錄</a>
  <div>
    <a href="#/week-01" class="btn-back-index">← 上一週：Week 01</a>
    <a href="#/week-05" class="btn-back-index">下一週：Week 05 →</a>
  </div>
</div>

# 第 02 週課程精要：神經網路原理與 DNN 手寫辨識實作

<p class="report-subtitle">從神經元數學模型、Softmax 機率轉換與梯度下降法，到 MNIST 四版本控制變因實驗與 Gradio 部署診斷。</p>

<div class="pill-row">
  <span class="badge badge-sky">Week 02</span>
  <span class="badge badge-sky">神經網路與函數學習機</span>
  <span class="badge badge-emerald">DNN 手寫辨識實作</span>
</div>

<hr class="report-divider" />

<div class="dashboard-card">
  <div class="section-kicker">▼ 概覽：本週教材來源與複習區段</div>
  <p style="margin: 0.25rem 0 0.75rem 0;">
    <strong>課堂講義來源</strong>：<a href="raw/PPT/02神經網路的概念.pdf" target="_blank">02神經網路的概念.pdf</a>（共 123 頁，政治大學 蔡炎龍老師）<br/>
    <strong>作業實作來源</strong>：<a href="raw/HW/02_中興大學 8113026207 科管博 薛慧婷 打造自己的DNN(全連結)手寫辨識.pdf" target="_blank">02_中興大學 8113026207 科管博 薛慧婷 打造自己的DNN(全連結)手寫辨識.pdf</a>（<a href="https://colab.research.google.com/drive/1JIlBtSHSKK1AKTJZmi7qTWSupFrdFdwi?usp=sharing" target="_blank">開啟 Colab 筆記本</a>）
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
    <span>一、課程摘要 <span class="pipe-sep">｜</span> 神經網路與函數學習機（Tensor・Softmax・梯度下降）</span>
    <a href="raw/PPT/02神經網路的概念.pdf" target="_blank" class="pdf-link">📄 開啟課堂講義 PDF</a>
  </div>

  <table>
    <thead>
      <tr>
        <th>序號</th>
        <th>核心概念模組</th>
        <th>數學定義 / 運算機制</th>
        <th>關鍵結構與性質</th>
        <th>複習關鍵指標</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td><strong>張量 (Tensor) 與編碼</strong></td>
        <td>0 階純量、1 階向量、2 階矩陣、3 階 RGB 影像</td>
        <td>分類目標轉為 <strong>One-Hot Encoding</strong>（如 $[1,0,0]^T$）</td>
        <td>輸入輸出皆須為數字</td>
      </tr>
      <tr>
        <td>2</td>
        <td><strong>Softmax 機率轉換</strong></td>
        <td>$p_i = P_\theta(y_i \mid \mathbf{x}) = \frac{e^{z_i}}{\sum_j e^{z_j}}$</td>
        <td>將任意實數輸出轉為總和等於 $1$、保持大小順序之條件機率</td>
        <td><span class="val-down">多分類輸出層標準配置</span></td>
      </tr>
      <tr>
        <td>3</td>
        <td><strong>人工神經元與激發函數</strong></td>
        <td>$h = \varphi\left(\sum_{i=1}^n w_i x_i + b\right)$</td>
        <td>以非線性激發函數（現代主流為 <strong>ReLU</strong>）突破線性組合限制</td>
        <td>權重 $w_i$ 與偏值 $b$</td>
      </tr>
      <tr>
        <td>4</td>
        <td><strong>神經網路 3+1 架構</strong></td>
        <td><strong>DNN</strong>（全連結）、<strong>CNN</strong>（影像）、<strong>RNN</strong>（記憶）、<strong>Transformer</strong></td>
        <td>每層將輸入 Tensor 映射為新特徵向量；具<strong>萬能近似定理</strong>保證</td>
        <td>決定隱藏層數與神經元數</td>
      </tr>
      <tr>
        <td>5</td>
        <td><strong>損失函數與梯度下降</strong></td>
        <td>$L(\theta) = \frac{1}{2k}\sum \|y_i - f_\theta(x_i)\|^2$；更新式 $\theta \leftarrow \theta - \eta \nabla L(\theta)$</td>
        <td>對各參數取<strong>偏微分</strong>組成梯度 $\nabla L$，乘上學習率 $\eta$ 往極小值移動</td>
        <td><span class="val-up">Backpropagation 反向傳播</span></td>
      </tr>
    </tbody>
  </table>

  <p class="table-footnote">高維度學習本質：根據 Balestriero, Pesenti &amp; LeCun (2021) 研究，高維度空間中的機器學習並非單純「內插（Interpolation）」，而幾乎總是進行「外插（Extrapolation）」。</p>

  <div class="callout-box">
    <span class="callout-title">課程摘要重點</span>
    <ul>
      <li><strong>第一步：輸入與輸出數位化</strong>：將問題轉為張量（例如將 $28 \times 28$ 的手寫數字影像拉平為 $784$ 維向量，分類答案設為 $10$ 維 One-Hot 向量），並以 Softmax 轉換出各類別機率。</li>
      <li><strong>第二步：決定神經網路架構</strong>：全連結神經網路（DNN）只需決定「幾層隱藏層」與「每層幾個神經元」，每個神經元透過加權總和、偏值與 ReLU 非線性激發函數，將輸入逐層轉換為高階特徵向量。</li>
      <li><strong>第三步：損失函數與梯度下降訓練</strong>：定義衡量預測誤差的損失函數 $L(\theta)$，對每個權重與偏值取偏微分構成梯度向量 $\nabla L$，並沿著負梯度方向乘上學習率（$\theta \leftarrow \theta - \eta\nabla L$）迭代找出最佳參數 $\theta^*$。</li>
    </ul>
  </div>
</div>

<div class="module-block block-b">
  <div class="card-title">
    <span>二、作業摘要 <span class="pipe-sep">｜</span> 打造自己的 DNN 手寫辨識（四版本控制變因實驗）</span>
    <a href="raw/HW/02_中興大學 8113026207 科管博 薛慧婷 打造自己的DNN(全連結)手寫辨識.pdf" target="_blank" class="pdf-link">📄 開啟作業實作 PDF</a>
  </div>

  <table>
    <thead>
      <tr>
        <th>實驗版本</th>
        <th>隱藏層架構（神經元數）</th>
        <th>激發函數與正則化</th>
        <th>損失函數 / 優化器</th>
        <th>測試集 Loss / 正確率</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>A 版（老師範例基準）</strong></td>
        <td>3 層：<code>20 - 20 - 20</code></td>
        <td><code>relu / relu / tanh</code></td>
        <td><code>mse</code> ＋ <code>SGD(0.087)</code></td>
        <td>Loss: <code>0.0084</code> / <strong>94.55%</strong></td>
      </tr>
      <tr>
        <td><strong>B 版（加深窄網路）</strong></td>
        <td>4 層：<code>20 - 20 - 20 - 20</code></td>
        <td><code>relu / relu / tanh / relu</code></td>
        <td><code>mse</code> ＋ <code>SGD(0.087)</code></td>
        <td><span class="val-up">正確率降至 92.72%</span></td>
      </tr>
      <tr>
        <td><strong>C 版（最終採用版）</strong></td>
        <td>4 層：<code>512 - 256 - 128 - 64</code></td>
        <td>全 <code>relu</code> ＋ <code>Dropout(0.3)</code>×2</td>
        <td><code>categorical_crossentropy</code> ＋ <code>Adam(0.001)</code></td>
        <td>Loss: <code>0.06598</code> / <span class="val-down">98.12%（最佳）</span></td>
      </tr>
      <tr>
        <td><strong>D 版（控制變因對照）</strong></td>
        <td>4 層：<code>512 - 256 - 128 - 64</code></td>
        <td>全 <code>relu</code> ＋ <code>Dropout(0.3)</code>×2</td>
        <td><code>mse</code> ＋ <code>Adam(0.001)</code></td>
        <td>Loss: <code>0.0036</code> / <strong>97.82%</strong></td>
      </tr>
    </tbody>
  </table>

  <p class="table-footnote">訓練超參數設定：<code>batch_size = 32</code>、<code>epochs = 10</code>、<code>validation_split = 0.1</code>（切分 10% 訓練資料即時監控未見資料之驗證準確率，C 版於第 8 個 epoch 達最高 <code>val_accuracy = 98.27%</code>）。第一層參數量驗證：$784 \times 512 + 512 = 402,192$。</p>

  ```python
  # C 版（最終採用架構）：漸縮式寬隱藏層 + Dropout + Cross-Entropy + Adam
  from tensorflow.keras.models import Sequential
  from tensorflow.keras.layers import Input, Dense, Dropout
  from tensorflow.keras.optimizers import Adam

  model = Sequential([
      Input(shape=(784,)),
      Dense(512, activation='relu'),
      Dropout(0.3),
      Dense(256, activation='relu'),
      Dropout(0.3),
      Dense(128, activation='relu'),
      Dense(64, activation='relu'),
      Dense(10, activation='softmax')
  ])

  model.compile(
      loss='categorical_crossentropy',
      optimizer=Adam(learning_rate=0.001),
      metrics=['accuracy']
  )
  ```

  <div class="callout-box">
    <span class="callout-title">作業摘要重點</span>
    <ul>
      <li><strong>不同 Loss 函數不可直接比數值大小</strong>：<code>mse</code>（D 版 0.0036）與 <code>categorical_crossentropy</code>（C 版 0.06598）的數學公式與數值尺度完全不同，不能因 D 版 Loss 數值小就誤判其收斂較佳。</li>
      <li><strong>控制變因實驗（D 版）找出真正功臣</strong>：固定 C 版架構與 Adam 優化器、僅把 Loss 換回 <code>mse</code> 時，準確率仍達 <code>97.82%</code>，證明拉開 A 版（94.55%）與 C 版（98.12%）差距的主因是<strong>充足的網路容量（512→64）与 Adam 優化器</strong>。</li>
      <li><strong>加深窄網路的反效果</strong>：B 版在每層僅 20 個神經元的窄網路下強行加深至 4 層，準確率反而跌至 <code>92.72%</code>，顯示特徵寬度不足時加深網路反而阻礙梯度傳遞。</li>
    </ul>
  </div>
</div>

<div class="module-block block-c">
  <div class="card-title">
    <span>三、技術關聯與延伸應用 <span class="pipe-sep">｜</span> 測試集 98.12% vs. Gradio 實測落差 <span class="pipe-sep">｜</span> 資料分佈偏移診斷</span>
  </div>

  <table>
    <thead>
      <tr>
        <th>評估面向</th>
        <th>實驗現象與觀察數據</th>
        <th>底層技術成因剖析</th>
        <th>進階工程優化方案</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Loss 函數選擇</strong></td>
        <td>C 版（Cross-Entropy <code>98.12%</code>）略優於 D 版（MSE <code>97.82%</code>）</td>
        <td>Cross-Entropy 針對機率分佈對數懲罰，梯度不會因 Sigmoid/Softmax 飽和而消失</td>
        <td>多分類任務標準配備 <code>categorical_crossentropy</code></td>
      </tr>
      <tr>
        <td><strong>過擬合抑制</strong></td>
        <td>寬網路（首層 40.2 萬參數）易死背訓練集</td>
        <td>在前兩層高維度特徵後加入 <code>Dropout(0.3)</code> 隨機丟棄 30% 神經元</td>
        <td>搭配 <code>validation_split=0.1</code> 監控泛化能力</td>
      </tr>
      <tr>
        <td><strong>Gradio 部署落差</strong></td>
        <td>測試集達 <span class="val-down">98.12%</span>，但手寫板實測（尤其數字 <code>6</code> 與 <code>8</code>）判識率明顯波動</td>
        <td><span class="val-up">資料分佈偏移 (Distribution Shift)</span>：滑鼠手寫筆觸粗細、偏移、比例與歐美 MNIST 樣本不同</td>
        <td>推論前加入影像預處理（邊界裁切、膨脹加粗、28×28 質心置中）</td>
      </tr>
      <tr>
        <td><strong>全連結層空間限制</strong></td>
        <td>將 $28 \times 28$ 影像直接拉平為 $784$ 維向量</td>
        <td>破壞二維像素之空間鄰近關係，缺乏平移與縮放不變性</td>
        <td>延伸升級為具備局部感受野之<strong>卷積神經網路 (CNN)</strong></td>
      </tr>
    </tbody>
  </table>

  <p class="table-footnote">AI 協作除錯紀錄：實作過程中透過生成式 AI 輔助診斷 Colab 執行期問題，包含「舊模型變數殘留於記憶體需重啟執行階段（Restart Runtime）」以及「前後變數命名一致性檢查」。</p>

  <div class="callout-box">
    <span class="callout-title">技術關聯與延伸應用重點</span>
    <ul>
      <li><strong>測試集高分不等於部署表現（Distribution Shift）</strong>：MNIST 訓練集經過粗化、抗鋸齒平滑與嚴格置中，且源自歐美書寫習慣；而使用者在 Gradio 介面以滑鼠手寫時筆觸偏細、位置偏移，導致「6」與「8」等數字實測判識率明顯下滑。</li>
      <li><strong>全連結 DNN 的空間結構盲點</strong>：將 $28 \times 28$ 影像直接拉平（Flatten）為 $784$ 維向量會破壞二維空間鄰近關係，只要手寫位置稍微平移，對應的權重就無法對齊。</li>
      <li><strong>後續優化與跨週次演進</strong>：短期可在 Gradio 推論前端加上影像邊界裁切、筆畫膨脹與質心置中預處理；長期則應將模型架構升級為具備局部感受野與平移不變性的<strong>卷積神經網路（CNN）</strong>。</li>
    </ul>
  </div>
</div>

<div class="back-nav-bar" style="margin-top: 2rem;">
  <a href="#/" class="btn-back-index">← 回到課程總覽目錄</a>
  <div>
    <a href="#/week-01" class="btn-back-index">← 上一週：Week 01</a>
    <a href="#/week-05" class="btn-back-index">下一週：Week 05 →</a>
  </div>
</div>
