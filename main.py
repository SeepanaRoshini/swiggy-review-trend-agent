import os
import pandas as pd
from collections import defaultdict

from agents.topic_extractor import extract_topics
from agents.topic_merger import merge_topics
from agents.trend_analyzer import update_trends

DATA_PATH = "data/raw"
OUTPUT_PATH = "output/trend_report.csv"

trend_data = defaultdict(lambda: defaultdict(int))

for file in sorted(os.listdir(DATA_PATH)):
    if not file.endswith(".csv"):
        continue

    date = file.replace(".csv", "")
    df = pd.read_csv(os.path.join(DATA_PATH, file))

    reviews = df["review"].tolist()

    topics = extract_topics(reviews)
    topics = merge_topics(topics)

    trend_data = update_trends(trend_data, date, topics)

trend_df = pd.DataFrame(trend_data).fillna(0).astype(int)
trend_df = trend_df.T

trend_df.to_csv(OUTPUT_PATH)

print("✅ Trend report generated at:", OUTPUT_PATH)
