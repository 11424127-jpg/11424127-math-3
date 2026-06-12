# 傅立葉分析與 RLC 電路頻率回應 (Fourier Analysis and RLC Circuit Frequency Response)

本倉庫包含方波信號的傅立葉分析與 RLC 串聯帶通濾波器的頻率回應分析。

## 作業資訊 (Assignment Information)

- **學號 (Student ID):** 11424127
- **課程名稱 (Course):** 電路學 / 信號與系統 (Circuits / Signals and Systems)
- **作業內容 (Content):**
    - **問題一:** 方波信號分析 (Square Wave Signal Analysis)
        - 數位電路中，時鐘信號是標準的週期性方波，用於同步數位晶片的邏輯動作。某 FPGA 系統的時鐘週期為 T = 10ns (對應頻率 100MHz)，高電平 VOH = 3.3V，低電平 VOL = 0V，佔空比為 50%。將該時鐘方波展開為傅里葉級數，分析其頻率成分，解釋方波時鐘經長導線傳輸後沿變緩的原因。
    - **問題二:** RLC 電路頻率回應 (RLC Circuit Frequency Response)
        - RLC 串聯帶通濾波器是射頻接收機的核心選頻電路，已知參數：R = 10Ω, L = 1mH, C = 2.53 × 10^-8 F，輸入為包含直流分量、基波、3 次諧波的週期矩形脈衝信號：
        
        $$ v_i(t) = \begin{cases} V_m, & 0 < t < T/2 \\ 0, & T/2 < t < T \end{cases} $$
        
        其中 Vm = 5V，基波頻率 f0 = 1MHz (週期 T = 1μs)，輸出為電容兩端電壓 vo(t)，用傅里葉級數分析濾波器的選頻特性。

## 檔案說明 (Files)

- `square_wave_fourier_analysis.py`: 方波信號的傅立葉級數展開與頻譜分析程式。
- `square_wave_fourier_approximation.png`: 方波傅立葉級數近似圖。
- `square_wave_frequency_spectrum.png`: 方波頻譜圖。
- `rlc_frequency_response.py`: RLC 串聯帶通濾波器頻率回應分析程式。
- `rlc_magnitude_response.png`: RLC 濾波器增益響應圖。
- `rlc_phase_response.png`: RLC 濾波器相位響應圖。
- `README.md`: 倉庫說明文件。

## 解題方法摘要 (Methods)

1. **方波傅立葉分析 (Square Wave Fourier Analysis):**
    - 使用 Python 程式計算方波信號的傅立葉級數直流分量 (a0) 及餘弦 (an) 和正弦 (bn) 係數。
    - 利用計算出的傅立葉係數重建方波，並繪製其頻譜圖以分析頻率成分。
    - 解釋方波時鐘信號經長導線傳輸後沿變緩的原因，主要歸因於傳輸介質的頻寬限制導致高次諧波成分的衰減或相移。

2. **RLC 電路頻率回應 (RLC Circuit Frequency Response):**
    - 根據給定的 RLC 串聯電路參數，建立其轉移函數 (Transfer Function)。
    - 透過 Python 程式計算並繪製 RLC 濾波器的增益 (Magnitude) 和相位 (Phase) 頻率響應圖，以分析其選頻特性。
