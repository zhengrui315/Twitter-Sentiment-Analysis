import pandas as pd


filenames = ['./inputs/emoji_nostream_' + str(idx) + '.csv' for idx in range(5)]
dfs = [pd.read_csv(filename) for filename in filenames]
for i in range(5):
    print('df{}.shape= '.format(i), dfs[i].shape)

# downsample to equilize the weights of the five labels
dfs[2] = dfs[2].sample(frac=0.5,random_state=99).reset_index(drop=True)

df_raw = pd.concat(dfs)

#shuffle the row to mix the five categories
df_raw = df_raw.sample(frac=1,random_state=99).reset_index(drop=True)

#drop duplicates
df = df_raw.drop_duplicates(['tweet'],keep=False)


df['tweet'] = df['tweet'].str.replace(r'^ *RT ', ' ')
df['tweet'] = df['tweet'].str.replace(r'@[a-zA-Z0-9_]+', ' ')
# df['tweet'] = df['tweet'].str.replace(r'#\S*', ' ')
df['tweet'] = df['tweet'].str.replace(r'https?://[a-zA-Z0-9/\.]*', ' ')
df['tweet'] = df['tweet'].str.replace(r'[a-zA-Z]*\'[a-zA-Z]*', '')
df['tweet'] = df['tweet'].str.replace(r'\d+[a-zA-Z]{,2}', ' ')
df['tweet'] = df['tweet'].str.replace(r'[^a-zA-Z]', ' ')

pattern = "["u"\U0001F600-\U0001F64F"u"\U0001F300-\U0001F5FF"u"\U0001F680-\U0001F6FF"u"\U0001F1E0-\U0001F1FF""]+"
df['tweet'] = df['tweet'].str.replace(pattern, ' ')

df['tweet'] = df['tweet'].str.lower()
df['tweet'] = df['tweet'].apply(lambda x: ' '.join(x.split()))
df['tweet'] = df['tweet'].apply(lambda x: x.strip())
# df = df.iloc[:,:][len(df['tweet'])==0]    
df['label'] = df['label'].apply(lambda i: int(i))
df = df.drop_duplicates(['tweet'], keep=False)
df = df[df.notnull().tweet]