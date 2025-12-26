from collections import defaultdict

def update_trends(trend_data, date, topics):
    for topic in topics:
        trend_data[topic][date] += 1
    return trend_data
