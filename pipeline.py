import sys 
import pandas as pd

if (len(sys.argv) != 3):
    print('enter two arguments');
    sys.exit(1);

arg1 = sys.argv[1];
arg2 = sys.argv[2];

df = pd.read_csv(arg1);

for i in range(len(df)):
    df.loc[i,'Cloud'] = float("{:.2f}".format(df.loc[i,'Cloud']));

df.to_csv(arg2, index = False);
