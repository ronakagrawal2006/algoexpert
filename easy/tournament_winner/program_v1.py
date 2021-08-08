competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]
results = [0, 0, 1]


def tournamentWinnerV2(competitions, results) -> str:
    def get_winner(results, competitions, match_i) -> str:
        if results[match_i] == 0:
            win_i = competitions[match_i][1]
        else:
            win_i = competitions[match_i][0]
        return win_i
    scores = {'': 0} # O(m) space # m = num_teams

    curr_best_team = ''
    for m_i in range(len(competitions)): # O(n) # n= num_mathc time
        winner = get_winner(results, competitions, m_i)
        print(winner)
        if winner in scores:
            scores[winner] += 3
        else:
            scores[winner] = 3
        if scores[winner] > scores[curr_best_team]:
            curr_best_team = winner
    return curr_best_team

competitions=[
    ["Bulls", "Eagles"]

]
results=[1]


tournamentWinnerV2(competitions,results)    