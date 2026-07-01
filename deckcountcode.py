import pandas as pd

df = pd.read_csv("standings.csv")

deck_counts = df["deck"].value_counts().reset_index()
deck_counts.columns = ["deck", "count"]

deck_counts["deck"] = deck_counts["deck"].str.capitalize()

print(deck_counts)
deck_counts.to_csv("deck_counts.csv", index=False)