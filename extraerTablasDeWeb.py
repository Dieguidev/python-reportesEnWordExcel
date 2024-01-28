import pandas as pd

simp = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')
print(simp[5])