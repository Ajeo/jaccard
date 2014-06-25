#!/usr/bin/python

import os
import csv
import codecs

def csv_writer(data, path):
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

def readTopics():
    topics = []
    with open('topics.csv', 'rb') as f:
        reader = csv.reader(f)
        reader.next()
        for row in reader:
            topics.append({row[0] : row[1].split(' ')})
    return topics

def jaccard(list1, list2):
    return float(len(set(list1) & set(list2))) / len(set(list1) | set(list2))

if ( __name__ == "__main__"):
    topics = readTopics()
    all_top_terms = []
    with open('./input/acm_trans_design_autom_electr_syst-top-terms.csv', 'rb') as f:
        reader = csv.reader(f)
        reader.next()
        for row in reader:
            all_top_terms.append(row[1].strip().split(' '))

    output = [['Topic', 'Top Terms']]
    names = {}
    for top_terms in all_top_terms:
        max = 0.0
        name = ''
        for topic in topics:
            value = jaccard(top_terms, topic.values()[0])
            if max >= value:
                name = topic.keys()[0]
                if name in names.keys():
                    names[name] = names[name] + 1
                    name = name + '-' + str(names[name])
                else:
                    names[name] = 0
        output.append([name, ' '.join(top_terms)])
    print output
    csv_writer(output, './output/acm_trans_design_autom_electr_syst-top-terms.csv')
