from backend.matching.ranking import rank_candidates


candidates = [
    {
        "name": "Candidate A",
        "score": 72
    },
    {
        "name": "Candidate B",
        "score": 95
    },
    {
        "name": "Candidate C",
        "score": 84
    }
]


ranked_candidates = rank_candidates(candidates)


print("Candidate Ranking")
print("------------------")

for candidate in ranked_candidates:
    print(
        f"Rank {candidate['rank']}: "
        f"{candidate['name']} - "
        f"{candidate['score']}%"
    )