import csv
from statistics import mean
from collections import OrderedDict 
from collections import Counter
import heapq
def calculate_averages(input_file_name,output_file_name):
    with open(input_file_name , 'r') as f:
        reader = csv.reader(f)
        with open(output_file_name,'w') as g:
            for row in reader:
                name = row[0]
                these_grades = list()
                for grade in row[1:]:
                    these_grades.append(float(grade))
                g.write(name + ',' + str(mean(these_grades)))
                g.write('\n')

def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name, 'r') as f:
        reader = csv.reader(f)
        with open(output_file_name, 'w') as g:
            mydict = OrderedDict()
            for row in reader:
                name = row[0]
                b = []
                for grade in row[1:]:
                    b.append(float(grade))
                    mydict[name] = (mean(b))
                    c = dict(sorted(mydict.items(), key=lambda x: (x[1], x[0])))
            for key in c:
                g.write(key + ',' + str(c[key]) + ('\n'))


def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name, 'r') as f:
        reader = csv.reader(f)
        with open(output_file_name, 'w') as g:
            mydict = OrderedDict()
            for row in reader:
                name = row[0]
                b = []
                for grade in row[1:]:
                    b.append(float(grade))
                    mydict[name] = (mean(b))
                    mydict = dict(sorted(mydict.items(), key=lambda x: (x[1], x[0])))
                    k = Counter(mydict)
                    high = k.most_common(3)
            for i in high:
                g.write(i[0] + ',' + str (i[1]) + '\n')

def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name, 'r') as f:
        reader = csv.reader(f)
        with open(output_file_name, 'w') as g:
            mydict = OrderedDict()
            for row in reader:
                name = row[0]
                b = []
                c = []
                for grade in row[1:]:
                    b.append(float(grade))
                mydict[name] = (mean(b))
                my_value = mydict.values()
            for i in my_value:
                c.append(i)
                heapq.heapify(c)
                three_worst = (heapq.nsmallest(3 , c))
            for score in three_worst:
                g.write(str(score) + '\n')


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name, 'r') as f:
        reader = csv.reader(f)
        with open(output_file_name, 'w') as g:
            mydict = OrderedDict()
            for row in reader:
                name = row[0]
                b = []
                c = []
                for grade in row[1:]:
                    b.append(float(grade))
                mydict[name] = (mean(b))
                my_value = mydict.values()
            for i in my_value:
                c.append(i)
            g.write(str(mean(c)))