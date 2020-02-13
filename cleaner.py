# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:31:09 2020

@author: GOlmos01
"""

import pandas as pd
from dataloader import DataLoader


# full_df = DataLoader().load_pickle('full')

base_path = './Data/data_1-2019/'

# df_concat.append(DataLoader().load_adv(base_path + 'carat_1_2019.csv'))
# df_concat.append(DataLoader().load_adv(base_path + 'amnet_1_2019.csv'))
# df_concat.append(DataLoader().load_adv(base_path + 'deepblue_1_2019.csv'))
# df_concat.append(DataLoader().load_adv(base_path + 'dentsux_1_2019.csv'))
# df_concat.append(DataLoader().load_adv(base_path + 'iprospect_1_2019.csv'))
# df_concat.append(DataLoader().load_adv(base_path + 'vizeum_1_2019.csv'))

carat_df = DataLoader().load_adv(base_path + 'carat_1_2019.csv')
amnet_df = DataLoader().load_adv(base_path + 'amnet_1_2019.csv')
deepblue_df = DataLoader().load_adv(base_path + 'deepblue_1_2019.csv')
dentsux_df = DataLoader().load_adv(base_path + 'dentsux_1_2019.csv')
iprospect_df = DataLoader().load_adv(base_path + 'iprospect_1_2019.csv')
vizeum_df = DataLoader().load_adv(base_path + 'vizeum_1_2019.csv')

#Add columns CARAT
carat_df.insert(0, 'Macro DB', 'Advertmind')
carat_df.insert(1, 'DB', 'CARAT')
carat_df.insert(2, 'Macro Agencia', 'CARAT')
carat_df.insert(3, 'Agencia', 'CARAT')
#Add columns DEEPBLUE
deepblue_df.insert(0, 'Macro DB', 'Advertmind')
deepblue_df.insert(1, 'DB', 'DEEPBLUE')
deepblue_df.insert(2, 'Macro Agencia', 'CARAT')
deepblue_df.insert(3, 'Agencia', 'DEEPBLUE')
#Add columns DENTSUX
dentsux_df.insert(0, 'Macro DB', 'Advertmind')
dentsux_df.insert(1, 'DB', 'DENTSUX')
dentsux_df.insert(2, 'Macro Agencia', 'CARAT')
dentsux_df.insert(3, 'Agencia', 'DENTSUX')
#Add columns AMNET
amnet_df.insert(0, 'Macro DB', 'Advertmind')
amnet_df.insert(1, 'DB', 'AMNET')
amnet_df.insert(2, 'Macro Agencia', 'IPROSPECT')
amnet_df.insert(3, 'Agencia', 'AMNET')
#Add columns IPROSPECT
iprospect_df.insert(0, 'Macro DB', 'Advertmind')
iprospect_df.insert(1, 'DB', 'IPROSPECT')
iprospect_df.insert(2, 'Macro Agencia', 'IPROSPECT')
iprospect_df.insert(3, 'Agencia', 'IPROSPECT')
#Add columns VIZEUM
vizeum_df.insert(0, 'Macro DB', 'Advertmind')
vizeum_df.insert(1, 'DB', 'VIZEUM')
vizeum_df.insert(2, 'Macro Agencia', 'VIZEUM')
vizeum_df.insert(3, 'Agencia', 'VIZEUM')

df = pd.concat([carat_df, deepblue_df, dentsux_df, amnet_df, iprospect_df, vizeum_df], ignore_index=True)

print(df)
