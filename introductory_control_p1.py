'''Design and write a program to calculate Net Run Rate scored by the two teams use controls to validate a condition such that the team with the higher run rate will top the points table and also think for the tie-breaker condition.

Steps to Follow: 
Understand how net run rate getting calculated (Cite the reference in submission comment)
Follow the computational thinking process.
Understand inputs required to calculate various parameters (Give Appropriate Comments to the code)
Design Controls -  Compound Statements and Suites
Provide Feedback to the User (Console level Feedback)
Test (Paper Calculation)
Validate (Paper Calculation = Code  Result)'''

#inputs for team 1
'''taking input like run scored ,total over played,runs conceded ,over bowled by team 2'''
run_scored_1=int(input("enter the run scored by team:"))
total_over_1=int(input("enter total_over faced by team:"))
runs_conceded_1=int(input("enter the run conceded by team:"))
over_bowled_1=int(input("enter total over bowled  by team:"))
team1="TeamA"
team2="TeamB"
#inpus for team2
'''taking input like run scored ,total over played,runs conceded ,over bowled by team 2'''
run_scored_2=int(input("enter the run scored by team:"))
total_over_2=int(input("enter total_over faced by team:"))
runs_conceded_2=int(input("enter the run conceded by team:"))
over_bowled_2=int(input("enter total over bowled  by team:"))
NRR1 = (run_scored_1 / total_over_1) - (runs_conceded_1/over_bowled_1 )#to calculate net run run rate for team1
NRR2 = (run_scored_2 / total_over_2) - (runs_conceded_2/over_bowled_2 )#to calculate net run rate of team 2
if NRR1 > NRR2:
        print(team1, "chances high to win")
elif NRR1<NRR2:
     print(team2,"chances high to win")
else:
    print("both have same NRR and it is tie  breaker condition")

