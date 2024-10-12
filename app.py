"""
python version : 3.11.1
numpy version: 1.25.2
matplotlib version: 3.7.2
scipy version: 1.13.0
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

FONTSIZE = 15

# 変調度
m = 2

# 搬送波の周波数 [Hz]
f_c = 10000
# 搬送波の振幅 [mV]
A_cp_p = 2

# 信号源の周波数 [Hz]
f_s = 100
# 信号源の振幅 [mV]
A_sp_p = A_cp_p * m

# 時間 [ms] : 4周期表示
t = np.linspace(0, 4 * (1 / f_s), 1000)

v_c = A_cp_p / 2 * np.cos(2 * np.pi * f_c * t)
v_s = A_sp_p / 2 * np.cos(2 * np.pi * f_s * t)

# 変調波
v_am = A_sp_p / 2 * (1 + m * np.cos(2 * np.pi * f_s * t)) * np.cos(2 * np.pi * f_c * t)

# 変調波の包絡線から復調波求める
v_d = np.abs(signal.hilbert(v_am))
# 復調波の基準を0Vにする
#v_d = v_d - np.mean(v_d)

# 変調波の基準を求める
demodulation_base = np.mean(v_d)
base_line = np.full_like(t, demodulation_base)

# 各軸の交点を設定
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# グラフの描画
plt.plot(t, v_s, label='source')
plt.plot(t, v_d, label='demodulation')
plt.plot(t, base_line, label='base')

# グラフの書式設定
plt.minorticks_on()
plt.grid(True, which='both', axis='both')
plt.xlabel('Time [ms]')
plt.ylabel('Voltage [mV]')

plt.legend(fontsize=FONTSIZE)
plt.xticks(fontsize=FONTSIZE)
plt.yticks(fontsize=FONTSIZE)
plt.show()