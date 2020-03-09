import imageio
import matplotlib.pyplot as plt
import pandas as pd
import os

os.chdir('VIC')

plt.figure(figsize=(15, 10))
for i in range(150):
    s = i * 10
    s = int(s)
    label = f'{s}km^2'
    df1 = pd.read_csv(f'./Simulation_results/{s}sqkm_df.csv')
    df1['Date'] = pd.to_datetime(df1['Date'], format='%Y-%m-%d')
    x = df1['Date']
    y = df1['Storage_level_end_of_day']
    plt.ylim((0, 44401824.25))
    plt.plot(x, y)
    plt.title(label)
    plt.xlabel('Date')
    plt.ylabel('MWh')
    plt.savefig(f'./gif_frames/{s}sqkm_frame.png')
    plt.cla()

image_list = []
for i in range(0, 50):
    t = i * 10
    t = int(t)
    with open(f'./gif_frames/{t}sqkm_frame.png', 'rb') as file_name:
        image_list.append(imageio.imread(file_name))

imageio.mimwrite('./VIC_increasing_solar.gif', image_list)