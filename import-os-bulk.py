import json
import random
import string
#this is code
categories = ["electronics", "clothing", "home", "sports", "books", "toys", "food", "automotive"]
bulk_lines = []

fo0r i in range(12000):
    # Each doc ~800-1000 bytes to reach ~10 MB total
    filler = ''.join(random.choices(string.ascii_lowercase + ' ', k=600))
    doc = {
        "title": f"Product {i} - {filler[:50]}",
        "description": f"Description for product {i}. {filler}",
        "timestamp": f"2026-07-{random.randint(1,22):02d}T{random.randint(0,23):02d}:00:00Z",
        "category": random.choice(categories),
        "price": round(random.uniform(5.0, 500.0), 2),
        "tags": random.sample(["sale","new","popular","premium","limited","bulk","featured","trending"], 3)
    }
    bulk_lines.append(json.dumps({"index": {}}))
    bulk_lines.append(json.dumps(doc))

# Write to file
with open("bulk_data.json", "w") as f:
    f.write("\n".join(bulk_lines) + "\n")

print("Generated bulk_data.json - upload with:")
print("curl -XPOST 'https://search-my-opensearch-domain-test-frpkfufbh5eo44hednir6gctoa.us-east-1.es.amazonaws.com/source-index/_bulk' -H 'Content-Type: application/x-ndjson' --data-binary @bulk_data.json")
