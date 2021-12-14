import pandas as pd
import glob

data = list()

for filePath in glob.glob('./BabyMother/*.txt'):
    with open(filePath, 'r', encoding='utf-8') as f:
        tmpList = f.read().split('---split---')[1].split('\n')
        data.append(tmpList[1:-1])

columns = [c.split(': ')[0] for c in data[0]]
df = pd.DataFrame(data=data, columns=columns)
for c in df:
    df[c] = df[c].apply(lambda s: s.split(': ')[1])
df.to_csv('./ptt.csv', index=0, encoding='utf-8-sig')

print(df)



