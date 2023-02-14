import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Question1 import generate_boxplot,generate_relplot
from Question2 import generate_lineplot
from Question3 import generate_boxplot_female, generate_boxplot_male
from readit import csv

sns.set_theme(style = "white")
#  Get the "raw" URL from the offical website
url = "https://ncaaorg.s3.amazonaws.com/research/academics/2020RES_APR2019PubDataShare.csv"
df =csv("data/2020RES_APR2019PubDataShare.csv")

#print the whole csv file from the offical website
#print(df)


new_column_1 = {'APR_RATE_2019_1000':'2019','APR_RATE_2018_1000':'2018','APR_RATE_2017_1000':'2017','APR_RATE_2016_1000':'2016','APR_RATE_2015_1000':'2015','APR_RATE_2014_1000':'2014','APR_RATE_2013_1000':'2013','APR_RATE_2012_1000':'2012','APR_RATE_2011_1000':'2011','APR_RATE_2010_1000':'2010','APR_RATE_2009_1000':'2009','APR_RATE_2008_1000':'2008','APR_RATE_2007_1000':'2007','APR_RATE_2006_1000':'2006','APR_RATE_2005_1000':'2005','APR_RATE_2004_1000':'2004'}
df = df.rename(columns = new_column_1)

#Start of question1
#Data cleaning for question 1

#check whether renaming worked
#print(df1['2019'])

#clean the data by using melt() method
df1 = pd.melt(df, id_vars=['SCL_UNITID','SCL_NAME','SPORT_NAME'], value_vars=['2019','2018','2017','2016','2015','2014','2013','2012','2011','2010','2009','2008','2007','2006','2005','2004'], var_name="Academic Year",value_name="APR")
#print the dataframe after cleaned
#print(df1)

#Sort the Academic Year so that it can display in the right order on the plot.
df1.sort_values(by = 'Academic Year',ascending=True,inplace=True)
#check the order
#print(df1)



#draw the boxplot
generate_boxplot(df1, "Academic Year", "APR")


#Draw the relplot

generate_relplot(df1, "Academic Year","APR",8,2)





#Start of question2

#First we should delete rows in which contain no sports with 'gender'
df2 = df.query('SPORT_CODE != 37')

df2 = df2.query('SPORT_CODE != 1')

df2 = df2.query('SPORT_CODE != 4')

#Convert the corresponding SPORT_CODE to 'MALE' AND 'FEMALE'


df2['SPORT_CODE'] = np.select([df2['SPORT_CODE'] > 17, df2['SPORT_CODE'] <= 17], ['FEMALE', 'MALE'], default=df2['SPORT_CODE'].astype(str))

#check
#print(df2['SPORT_CODE'])



#Then we should rename the SPORT_CODE column to GENDER
new_column2 = {'SPORT_CODE':'GENDER'}
df2 = df2.rename(columns = new_column2)
#print(df2['GENDER'])

#Then we should clean the data by using melt()
df3 = pd.melt(df2, id_vars=['SCL_UNITID','SCL_NAME','GENDER','SPORT_NAME'], value_vars=['2019','2018','2017','2016','2015','2014','2013','2012','2011','2010','2009','2008','2007','2006','2005','2004'], var_name="Academic Year",value_name="APR")
df3.sort_values(by = 'Academic Year',ascending=True,inplace=True)

#print df3
#print(df3)

#Draw the lineplot
generate_lineplot(df3, "Academic Year", "APR", "GENDER")

#From the lineplot, we can safely reach the conclusion that APRs of Females' sports are always higher than those of Males. 
# This might be due to that Female student-athletes may have a stronger focus on academics and a greater commitment to academic success. 
# And also APRs of all genders are gradually. From my point of view.
# One possible reason for the gradual increase in APRs in NCAA sports of all genders from 2004 to 2019 could be the increased emphasis and focus on academic performance and accountability within college sports programs. 
# The NCAA introduced the APR in 2004 as a way to measure the academic progress and success of student-athletes, and since then, many schools and programs have implemented stricter academic policies and initiatives to improve their APR scores. 
# Additionally, the NCAA has implemented penalties for teams with low APR scores, which may have also motivated schools to prioritize academics more. Another possible reason could be the increased focus on student-athlete welfare and well-being, which includes academic success as a key component


#Start of question 3

#First visualize a plot for Men's sports
df_male  = df3.loc[df3['GENDER'] == 'MALE']
#print(df_male)
df_female = df3.loc[df3['GENDER'] == 'FEMALE']


#Draw a boxplot of APRs for Men's sports
generate_boxplot_male(df_male, "SPORT_NAME", "APR", "Academic Year")
#In general, APRs of Men's sports are going up chronologically. 
# And APRs of Men's basketball are not clustered compared to other sports. 
# One possible reason is that basketball is one of the most popular sports 
# in the states and hence more athletes are involved which gives a rise to the clustered APRs. 
# And also, we can find that APRs of Men's swimming are clusterred on the chart, 
# showing relatively higher performance. One possible explanation could be that there is a relatively small number of teams and/or a high degree of consistency in performance among those teams

#Draw a boxplot of APRs for Women's sports
generate_boxplot_female(df_female, "Academic Year", "APR", "SPORT_NAME")

#In general, APRs of Men's sports are going up chronologically. 
# Women's bowling has a wide range of scattering on the plot.
# This could be due to factors such as the level of resources available to the teams,
# the academic support provided to the student-athletes, 
# or the overall academic performance of the student-athletes on the teams.