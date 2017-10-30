with open('itcont.txt') as InF:
    op=' '
    start=0
    medianvals_by_zip = 1
    for x, line in enumerate (InF):
        if (start==1):
                (str(line.split ("|")[0])
                    + ' | ' + (line.split ("|") [10] [0:5])
                    + ' | ' + (line.split ("|") [14])
                    + ' | ' + (line.split ("|") [15]) != " ")
        else:
            start = 1
#import pandas as pd
#df = pd.read_txt('itcont.txt', [0],[10],[14],[15])
#df.groupby([10]).median()
    #median of [15]
            with open(str('medianvals_by_zip') + '.txt','w') as OutF:
                OutF.write(op)
                OutF.close()
                op=' '
    InF.close()

with open('itcont.txt') as InF2:
    op=' '
    start=2
    medianvals_by_date = 3
    for x, line in enumerate (InF2):
        if (start==3):
                (str(line.split ("|")[0])
                    + ' | ' + (line.split ("|") [13] [0:5])
                    + ' | ' + (line.split ("|") [14])
                    + ' | ' + (line.split ("|") [15]) != " ")
        else:
            start = 3
#import pandas as pd
#df = pd.read_txt('itcont.txt', [0],[10],[14],[15])
#df.groupby([13]).median()
    #median of [15]
            with open(str('medianvals_by_zip') + '.txt','w') as OutF2:
                OutF2.write(op)
                OutF2.close()
                op=' '
    InF2.close()
