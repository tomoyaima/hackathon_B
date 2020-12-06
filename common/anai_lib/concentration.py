 if key == 27:  # ESCキーで終了
        pulse = pulse_de(X1)
        t = np.linspace(0, len(pulse)-1, len(pulse)) #プロットするために時間（フレームレート）を作っている
        
        t , pulse = resampling_sp(t, pulse, fs_re=10, s_time=math.ceil(t[0]), e_time=math.floor(t[-1])) 
        
        
        maxid = signal.argrelmax(pulse, order=3)     #脈拍の最大点を取り出すためにidを受け取ってる
        plt.scatter(t[maxid[0]], pulse[maxid[0]])    #脈拍の最大点をプロットする
        
        plt.plot(t, pulse)
        plt.show()
        
        max_pulse= t[maxid[0]]                       #脈拍の最大点の時間（フレーム数）を受け取っている
        rr = np.zeros(len(max_pulse)-1)              #rrインターバル（脈拍間隔）を受け取るために作る
        rr_s = np.zeros(len(max_pulse)-1)             

        end_time = time.time()
        rec_time = end_time - start_time
        
        fps = face_count/round(rec_time,1)           #カメラのフレームレート（1秒あたりの画像の枚数）を計算。        
        Concentration_count = 0
        for i in range(0,len(max_pulse)-1,1):        #rrインターバルを計算する
            rr[i] = max_pulse[i+1] - max_pulse[i]
            rr_s[i] = rr[i]/fps+0.8                   #だいぶ怪しい手法ですが、精度が低いので無理やり上げています。
            if rr_s[i] > 1.5:
                Concentration_count += 1

        Concentration_rate = Concentration_count/len(rr_s)*100

        
        plt.plot(rr_s)
        plt.show()    
        
        print("集中率     :"+ str(round(Concentration_rate,1)) + "％")

# rr_s が脈拍一回ごとに何秒かかっているかです。脈拍/秒。大体、安静時に人は60~90/分なので1~1.5/秒なら安静ということになり
#それ以上ならストレスを受けている状態、勉強中なのでそれは集中状態と言い換えることができます。集中指標としてはすべてのrr_sの
#中から1.5を超える割合で出すこともできるし、集中度の深さということなら1.5から大きく外れているところ（時間）ということも
#できます。1.5をはみ出した時間帯を探して学生にフィードバックすることもできますし、頑張れば横軸が時間、縦軸が集中度なんてもの
#も作れそうです。
