from scipy.interpolate import interp1d
""" データをリサンプリングする関数（3次スプライン補間を使用。時間の単位は「秒」にすること） """
def resampling_sp(time, data, fs_re, s_time, e_time): # 引数：時間[s]、データ、リサンプリング周波数[Hz]、リサンプリング開始時間[s]、リサンプリング終了時間[s]
    f_CS = interp1d(time, data, kind='cubic') # 3次スプライン補間
    time_re = np.arange(s_time, e_time+1/fs_re, 1/fs_re) # リサンプリング後の時間配列を作成（自由に決めてOK）
    data_re = f_CS(time_re) # 3次スプライン補間を用いてリサンプリング    
    return time_re, data_re # リサンプリング後の時間、リサンプリング後のデータ
