from typing import Dict, List, Tuple 

def get_ranks(scores: List[int]) -> List[int]:
    n = len(scores)
    score_with_index: List[Tuple[int, int]] = [[score, index] for index, score in enumerate(scores)]
    
    ranks: Dict[int, int] = {}
    score_with_index.sort(reverse=True)
    current_rank = 1
    prev_score = None

    for score, index in score_with_index:
        if score != prev_score:
            current_rank = len(ranks) + 1
            prev_score = score

        ranks[index] = current_rank

    return [ranks[i] for i in range(n)]

n = int(input())
scores = [int(i) for i in input().split()]
ranks = get_ranks(scores)

for rank in ranks:
    print(rank)
