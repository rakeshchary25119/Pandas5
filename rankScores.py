import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['score_rank'] = scores['score'].rank(method='dense', ascending=False)
    scores.sort_values(by = 'score_rank', inplace = True)
    scores.rename(columns = {'score_rank' : 'rank'}, inplace = True)
    return scores[['score', 'rank']]