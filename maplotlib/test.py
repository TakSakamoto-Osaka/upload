import numpy as np
import matplotlib.pyplot as plt


def gen_wave ():
    # sin, cos波形を生成する
    
    # 波形諸元
    a1 = 1
    f1 = 1
    phi1 = 0
    
    a2 = 1
    f2 = 1
    phi2 = 30
    
    t = np.arange(0, 2, 0.01)
    
    # 波形生成
    x1 = a1 * np.sin(2 * np.pi * f1 * t + np.deg2rad(phi1))
    x2 = a2 * np.sin(2 * np.pi * f2 * t + np.deg2rad(phi2))
    
    return x1, x2, t


def gen_wave2():
    # 正規分布生成
    u = 5       # 平均
    s = 1.2     # 標準偏差
    n = 1000    # 個数
    
    data = np.random.normal(loc=u, scale=s, size=n)
    
    return data
    


def plot(x1, x2, t):
    # 波形プロット
    
    # matplotlibの設定
    plt.rcParams["font.size"] = 14
    plt.rcParams["font.family"] = "Time New Roman"
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.yaxis.set_ticks_position("both")
    ax.xaxis.set_ticks_position("both")
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Amplitude")
   
    # 波形データをプロット
    ax.plot(t, x1, lw=1, color="red", label="x1") 
    ax.plot(t, x2, lw=1, color="blue", label="x2")
    ax.legend()
    fig.tight_layout()
    
    # plt.show() 
    plt.savefig("./wave.jpeg")


def plot2(data):
    plt.rcParams["font.family"] = "MS Gothic"
    plt.rcParams["axes.unicode_minus"] = False
    
    plt.hist(data, bins=50, density=True, alpha=0.7)
    plt.xlabel("value")
    plt.ylabel("density")
    plt.title("正規分布グラフ")
    plt.show()


def plot3(x1, x2, t, data):
    # matplotlibの設定
    plt.rcParams["font.size"] = 8
    plt.rcParams["font.family"] = "Meiryo"
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_axis_off()
    gs = fig.add_gridspec(2, 2, height_ratios=[2, 1]) 

    # 時間波形
    ax_wave = fig.add_subplot(gs[0, :]) 
    ax_wave.yaxis.set_ticks_position("both")
    ax_wave.set_ylim(-2, 2)
    ax_wave.xaxis.set_ticks_position("both")
    ax_wave.set_xlabel("時間 [s]")
    ax_wave.set_ylabel("振幅")
    
    ax_wave.plot(t, x1, lw=1, color="blue", label="x1")
    ax_wave.plot(t, x2, lw=1, color="red", label="x2")
    ax_wave.legend()
    
    # 正規分布波形
    ax_norm = fig.add_subplot(gs[1, 0]) 
    ax_norm.hist(data, bins=50, density=True, alpha=0.7)
    ax_norm.set_xlabel("value")
    ax_norm.set_ylabel("density")
    ax_norm.set_title("正規分布グラフ")
    
    plt.show()


if __name__ == "__main__":
    x1, x2, t = gen_wave()
    # plot(x1, x2, t)
    data = gen_wave2()
    # plot2(data)
    plot3(x1, x2, t, data)
   
    plt.close()
