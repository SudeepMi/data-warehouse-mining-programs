from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

# Create a list of transactions
transactions = [['milk', 'bread', 'eggs'],
                ['bread', 'butter'],
                ['milk', 'bread', 'butter'],
                ['milk', 'eggs'],
                ['bread', 'eggs']]

# Create a TransactionEncoder object
te = TransactionEncoder()

# Use the TransactionEncoder to transform the transactions into a DataFrame
te_ary = te.fit_transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Use the apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)

# Use the association_rules function to generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

# Print the association rules
print(rules)
