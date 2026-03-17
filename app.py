from search import search_bug

print("🔎 Bug Fix Suggestion AI")

while True:
    query = input("\nEnter your bug (or type exit): ")

    if query.lower() == "exit":
        break

    results = search_bug(query)

    print("\nSuggested Fixes:\n")

    for score, item in results:
        print("Error:", item["error"])
        print("Fix:", item["solution"])
        print("Match score:", round(score, 2))
        print("----------------------")