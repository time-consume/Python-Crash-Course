import matplotlib.pyplot as plt
import csv

hours_study = []
score = []

with open('hours_study_vs_score.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        hours_study.append(float(row[,0]))
        score.append(float(row[,1]))

plt.scatter(hours_study,score, label='Hours Spent Studying vs. Grade')
plt.xlabel('Hours Studied')
plt.ylabel('Grade')
plt.title('Relationship between Hours Spent Studying and Grade')
plt.legend()
plt.show()
