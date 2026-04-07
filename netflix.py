import pandas as pd

# ---------------- LOAD DATA ----------------
df = pd.read_csv(r"C:\30 days\p7\netflix_skewed_100k.csv")

# ---------------- CLEANING ----------------
print(df.isnull().sum())
df.drop_duplicates(inplace=True)

# ---------------- FEATURE ENGINEERING ----------------

# Convert minutes → hours
df['watch_hours'] = df['watch_time_min'] / 60

# Engagement level
df['engagement'] = df['watch_hours'].apply(lambda x:
                                           'Low' if x < 1 else
                                           'Medium' if x < 3 else 'High')

# ---------------- KPI (ROW LEVEL) ----------------
total_revenue = df['monthly_fee'].sum()
avg_watch = df['watch_hours'].mean()
binge_rate = df['is_binge_watch'].mean() * 100

print(total_revenue, avg_watch, binge_rate)

# =====================================================
# 🔥 ADD YOUR NEW CODE RIGHT HERE 👇
# =====================================================

# ---------------- USER-LEVEL ANALYSIS ----------------
user_df = df.groupby('user_id').agg({
    'watch_hours': 'sum',
    'monthly_fee': 'mean',
    'rating_given': 'mean',
    'is_binge_watch': 'mean'
}).reset_index()

# Convert binge to %
user_df['binge_rate'] = user_df['is_binge_watch'] * 100

# ---------------- PRINT RESULTS ----------------
print(user_df.head())

print("Avg Total Watch Hours per User:",
      user_df['watch_hours'].mean())

# ---------------- EXPORT ----------------
df.to_csv("cleaned_netflix_data.csv", index=False)
user_df.to_csv("user_level_data.csv", index=False)