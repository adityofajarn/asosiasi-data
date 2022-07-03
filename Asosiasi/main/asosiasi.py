import pandas as pd
from apyori import apriori

store_data = pd.read_csv('main/data/store_data.csv', header=None)

def Association(support, confidence):

    records = []
    for i in range (0, 7501):
        records.append([str(store_data.values[i,j]) for j in range(0, 20)])
    #mengubah dataset menjadi element list

    association_rules = apriori(records, min_support=support, min_confidence=confidence, min_lift=3, min_length=2)
    association_results = list(association_rules)
    #menggunakan method apriori untuk analisa asosiasi

    p = 0
    pd.array = []
    for item in association_results:

        pair = item[0]
        items = [x for x in pair]
        q = "Rule : " + items[0] + " -> " + items[1]
        pd.array.append(q)

        w = "Support : " + str(item[1])
        pd.array.append(w)

        e = "Confidence : " + str(item[2][0][2])
        pd.array.append(e)
        
        r = "======================================="
        pd.array.append(r)
        p+=1

    return pd.array  
    
