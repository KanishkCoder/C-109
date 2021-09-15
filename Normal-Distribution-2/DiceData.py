import random
import statistics
import plotly.figure_factory as ff

dice_result=[]
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)

mean = sum(dice_result)/len(dice_result)
#print(mean)

median = statistics.median(dice_result)
#print(median)

mode = statistics.mode(dice_result)
#print(mode)

#fig = ff.create_distplot([dice_result],["Result"],show_hist=False)
#fig.show()

std_dev=statistics.stdev(dice_result)
print(std_dev)

first_stdev_start, first_stdev_end = mean - std_dev, mean + std_dev
second_stdev_start, second_stdev_end = mean-(2*std_dev), mean+(2*std_dev)
third_stdev_start, third_stdev_end = mean-(3*std_dev), mean+(3*std_dev)

list_of_data_within_1_Standard_deviation = [result for result in dice_result if result> first_stdev_start and result<first_stdev_end]
list_of_data_within_2_Standard_deviation = [result for result in dice_result if result> second_stdev_start and result<second_stdev_end]
list_of_data_within_3_Standard_deviation = [result for result in dice_result if result> third_stdev_start and result<third_stdev_end]

print("{}% of data lies within 1 Standard deviation".format(len(list_of_data_within_1_Standard_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 2 Standard deviation".format(len(list_of_data_within_2_Standard_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 3 Standard deviation".format(len(list_of_data_within_3_Standard_deviation)*100.0/len(dice_result)))