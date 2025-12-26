def extract_topics(reviews):
    topics = []

    for review in reviews:
        text = review.lower()

        if "delivery" in text and ("rude" in text or "badly" in text):
            topics.append("delivery partner rude")

        elif "delivery" in text and "delay" in text:
            topics.append("delivery issue")

        elif "cold" in text or "stale" in text:
            topics.append("food quality issue")

        elif "map" in text:
            topics.append("maps not working properly")

        elif "instamart" in text:
            topics.append("instamart should be open all night")

        elif "10 minute" in text or "bolt" in text:
            topics.append("bring back 10 minute bolt delivery")

    return topics
