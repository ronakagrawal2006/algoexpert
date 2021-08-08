

# def tournamentWinner(competitions, results):
competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]
results = [0, 0, 1]
def tournamentWinner(competitions, results):
    #get unique set of teams
    teams=list(set([inner for outer in zip(*competitions) for inner in outer]))

    #create score dictionary
    score_d=dict(zip(teams,[0]*len(teams))) 

    for match_i in range(len(competitions)):
        #get winner
        if results[match_i]==0:
            win_i=competitions[match_i][1]
        else:
            win_i=competitions[match_i][0]
        print(win_i)
        #update score
        score_d[win_i]=score_d[win_i]+3
    print(score_d)
    winner=max(score_d.keys(), key=(lambda key: score_d[key]))
    return winner 

competitions=[
    ["Bulls", "Eagles"]

]
results=[1]

tournamentWinner(competitions,results)    

