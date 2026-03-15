import numpy as np
temperatures = np.random.randint(-20, 40, 10_000)

def temps_validate(temps):
    for t in temps:
        if -16 < t < 36:
            yield t

temperatures = list(temps_validate(temperatures))
temps_array = np.array(temperatures)

temps_array = np.array(list(map(lambda x: (x - temps_array.mean())/(temps_array.std()), temps_array)))
temps_array = list(map(lambda x: np.sin(x) + x**2, temps_array)) 

def window_compression(temps_list):
    window = []
    for t in range(len(temps_list)):
        window.append(temps_list[t])
        if (t+1)%30 == 0:
            yield window
            window = []
    
window_compressor = window_compression(temps_array)

def anomaly_window_searcher(windows):
    max_avg = 0
    avg_sum = 0
    total_windows = 0
    anomaly_windows = 0
    for window in windows:
        total_windows += 1
        window = np.array(window)
        avg_temp = window.mean()
        med_temp = (window[14]+window[15])/2
        standart = window.std()
        minimum = min(window)
        maximum = max(window)
        max_avg = max(max_avg, avg_temp)
        avg_sum += avg_temp
        if np.abs(avg_temp) > 1 or standart > 1:
            anomaly_windows += 1
    return total_windows, anomaly_windows, max_avg, avg_sum

total_windows, anomaly_windows, max_avg, avg_sum = anomaly_window_searcher(window_compressor)
print(f'''Всего окон: {total_windows}
Аномальных окон: {anomaly_windows}
Максимальное среднее значение: {max_avg}
Сумма средних значений: {avg_sum}''')