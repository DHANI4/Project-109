import random 
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

diceResult=[]
for i in range(0,1000):
    dice1=random.randint(0,6)
    dice2=random.randint(0,6)
    diceResult.append(dice1+dice2)

mean=statistics.mean(diceResult)
mode=statistics.mode(diceResult)
median=statistics.median(diceResult)
sd=statistics.stdev(diceResult)

#first sd start and end value
fsds,fsde=mean-sd,mean+sd

#Second sd start and end value
ssds,ssde=mean-(2*sd),mean+(2*sd)

#Third sd start and end value
tsds,tsde=mean-(3*sd),mean+(3*sd)

fig=ff.create_distplot([diceResult],["DICE"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[fsds,fsds],y=[0,0.17],mode="lines",name="Fsds"))
fig.add_trace(go.Scatter(x=[fsde,fsde],y=[0,0.17],mode="lines",name="Fsde"))

fig.add_trace(go.Scatter(x=[ssds,ssds],y=[0,0.17],mode="lines",name="Ssds"))
fig.add_trace(go.Scatter(x=[ssde,ssde],y=[0,0.17],mode="lines",name="Ssde"))
fig.show()

print("Mean of this data is {}".format(mean))
print("Mode of this data is {}".format(mode))
print("Median of this data is {}".format(median))
print("SD of this data is {}".format(sd))

#calculating sd in %
list_of_data_within_1_std_deviation=[result for result in diceResult if result>fsds and result<fsde]
list_of_data_within_2_std_deviation=[result for result in diceResult if result>ssds and result<ssde]
list_of_data_within_3_std_deviation=[result for result in diceResult if result>tsds and result<tsde]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(diceResult)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(diceResult)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(diceResult)))