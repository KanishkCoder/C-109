import csv
from statistics import mean
import statistics
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv('data.csv')
height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()

height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)

height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)

height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

height_stdev=statistics.stdev(height_list)
weight_stdev=statistics.stdev(weight_list)

height_first_stdev_start, height_first_stdev_end = height_mean-height_stdev,height_mean+height_stdev
height_second_stdev_start, height_second_stdev_end = height_mean-(2*height_stdev),height_mean+(2*height_stdev)
height_third_stdev_start, height_third_stdev_end = height_mean-(3*height_stdev),height_mean+(3*height_stdev)

weight_first_stdev_start, weight_first_stdev_end = weight_mean-weight_stdev,weight_mean+weight_stdev
weight_second_stdev_start, weight_second_stdev_end = weight_mean-(2*height_stdev),weight_mean+(2*weight_stdev)
weight_third_stdev_start, weight_third_stdev_end = weight_mean-(3*weight_stdev),weight_mean+(3*weight_stdev)

height_list_of_data_within_1_Standard_deviation = [result for result in height_list if result> height_first_stdev_start and result<height_first_stdev_end]
height_list_of_data_within_2_Standard_deviation = [result for result in height_list if result> height_second_stdev_start and result<height_second_stdev_end]
height_list_of_data_within_3_Standard_deviation = [result for result in height_list if result> height_third_stdev_start and result<height_third_stdev_end]

weight_list_of_data_within_1_Standard_deviation = [result for result in weight_list if result> weight_first_stdev_start and result<weight_first_stdev_end]
weight_list_of_data_within_2_Standard_deviation = [result for result in weight_list if result> weight_second_stdev_start and result<weight_second_stdev_end]
weight_list_of_data_within_3_Standard_deviation = [result for result in weight_list if result> weight_third_stdev_start and result<weight_third_stdev_end]

print("{}% of data lies within 1 Standard deviation".format(len(height_list_of_data_within_1_Standard_deviation)*100.0/len(height_list)))
print("{}% of data lies within 2 Standard deviation".format(len(height_list_of_data_within_2_Standard_deviation)*100.0/len(height_list)))
print("{}% of data lies within 3 Standard deviation".format(len(height_list_of_data_within_3_Standard_deviation)*100.0/len(height_list)))

print("{}% of data lies within 1 Standard deviation".format(len(weight_list_of_data_within_1_Standard_deviation)*100.0/len(weight_list)))
print("{}% of data lies within 2 Standard deviation".format(len(weight_list_of_data_within_2_Standard_deviation)*100.0/len(weight_list)))
print("{}% of data lies within 3 Standard deviation".format(len(weight_list_of_data_within_3_Standard_deviation)*100.0/len(weight_list)))

#fig=ff.create_distplot([df['Height(Inches)'].tolist()],['Height'], show_hist=False)
#fig.show()