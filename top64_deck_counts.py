import pandas as pd

df = pd.read_csv("standings.csv")
df["rank"] = df["rank"].astype(int)

top64 = df[df["rank"] <= 64]

deck_counts = top64["deck"].value_counts().reset_index()
deck_counts.columns = ["deck", "count"]

deck_counts["deck"] = deck_counts["deck"].str.capitalize()

print(deck_counts)
deck_counts.to_csv("top64_deck_counts.csv", index=False)