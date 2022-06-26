import matplotlib.pyplot as pt
scoring=[15,29,39,34]
lab = ['Team1','Team2','Team3','Team4']
pt.bar(lab,scoring,width=0.5,color="red")
pt.xlabel("List of Teams")
pt.ylabel("Scores")
pt.title("Team Score Graph")
pt.show()