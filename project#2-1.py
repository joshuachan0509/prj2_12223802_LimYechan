import pandas as pd

data_df = pd.read_csv('./2019_kbo_for_kaggle_v2.csv').copy()

#1
print("1번")
columns = ['H', 'avg', 'HR', 'OBP']
full_columns = ['hit', 'average', 'homerun', 'on base percentage']
year = 2015
for i in range(4):
    new_df = data_df[data_df['year'] == year]
    for j in range(4):
        nnew_df = new_df.sort_values(by=columns[j], ascending=False)
        print("\n\tTop 10 players in " + full_columns[j] + " from " + str(year))
        print(nnew_df['batter_name'].head(10))
        j+=1
    year += 1

#2
print("\n2번")
positions_kr = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']
positions = ['Catcher', 'First baseman', 'Second baseman', 'Third baseman',
             'Shorstop', 'Left fielder', 'Center fielder', 'Right fielder']
quiz2_df = data_df[data_df['year'] == 2018]
for i in range(8):
    new_quiz2_df = quiz2_df[quiz2_df['cp'] == positions_kr[i]].sort_values(by='war', ascending=False)
    player = new_quiz2_df['batter_name'].head(1).values[0]
    print("The player with the highest war by " + positions[i] + "(" + positions_kr[i] + ") : " + player + "\n")

#3
print("3번")
compare = ['R','H','HR','RBI','SB','war','avg','OBP','SLG','salary']
quiz3_df = data_df[compare].corr().sort_values(by='salary', ascending=False)
correlation = quiz3_df['salary'].values[1]
category = quiz3_df.index[1]
print(f"The highest correlation with salary : {category} ({correlation})")



