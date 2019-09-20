from statistics import variance, mean, median


# we can also type /// from statistics import variance as v, mean as m, median as me to make shortcut them
#we can import only statistics as module 
#we can import statistics as . anything . to do make it shortcut
#last thing is if we want to import everythings from module -statistics- then we can type like // from statistics import * .(*)

example_list = [5,4,5,2,5]

x= variance(example_list)
y=mean(example_list)
z= median(example_list)
print (x)
print(y)
print(z)