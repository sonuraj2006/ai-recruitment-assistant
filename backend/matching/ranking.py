def rank_candidates(candidates):
    """
    Rank candidates based on their match score.
    Highest score gets the highest rank.
    """

    ranked_candidates = sorted(
        candidates,
        key=lambda candidate: candidate["score"],
        reverse=True
    )

    for rank, candidate in enumerate(ranked_candidates, start=1):
        candidate["rank"] = rank

    return ranked_candidates