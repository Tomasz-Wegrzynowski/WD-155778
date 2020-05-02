import pandas as pd
import numpy as np

data = {'Kraj': ['Belgia',  'Indie',  'Brazylia'],
'Stolica': ['Bruksela',  'New Delhi',  'Brasilia'],
'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data, columns=['Kraj',  'Stolica',  'Populacja'])
print(df[df['Populacja']>1200000000])