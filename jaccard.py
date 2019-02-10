#!/usr/bin/python

from os import listdir
from os.path import isfile, join
import csv
import json


def csv_writer(data, path):
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


def get_index(seq, attr, value):
    return next(index for (index, d) in enumerate(seq) if d[attr] == value)


def read_topics():
    topics = []
    with open('topics.csv', 'rb') as f:
        reader = csv.reader(f)
        reader.next()
        for row in reader:
            topics.append({row[0] : row[1].split(' ')})
    return topics


def jaccard(list1, list2):
    return float(len(set(list1) & set(list2))) / len(set(list1) | set(list2))


def set_sliced_usage_topic(fi, topic_maps):
    file_name = fi.replace('top-terms.csv', 'sliced-usage.json')

    json_data = open('./input/json/' + file_name)
    sliced_usages = json.load(json_data)
    json_data.close()

    if len(sliced_usages) > 0:
        for topic_map in topic_maps:
            index = get_index(sliced_usages, "key", topic_map["id"])
            sliced_usages[index]["key"] = topic_map["name"]

    with open('./output/json/'+ file_name, 'w') as outfile:
        json.dump(sliced_usages, outfile, indent=4)


def set_top_terms_topic(fi, topics):
    output = [['Topic', 'Top Terms']]
    topic_names = {}
    topic_name = ''
    all_top_terms = []
    topic_maps = []

    with open('./input/csv/' + fi, 'rb') as f:
        reader = csv.reader(f)
        reader.next()
        for row in reader:
            all_top_terms.append({"topic_id": row[0], "terms": row[1].strip().split(' ')})

    for top_terms in all_top_terms:
        max = 0.0
        for topic in topics:
            jaccard_index = jaccard(top_terms["terms"], topic.values()[0])
            if jaccard_index >= max:
                max = jaccard_index
                topic_name = topic.keys()[0]

        if topic_name in topic_names.keys():
            topic_names[topic_name] = topic_names[topic_name] + 1
            topic_name = topic_name + '-' + str(topic_names[topic_name])
        else:
            topic_names[topic_name] = 0

        topic_maps.append({"id": top_terms["topic_id"], "name": topic_name})
        output.append([topic_name, ' '.join(top_terms['terms'])])
        topic_name = ''

    csv_writer(output, './output/csv/' + fi)

    return topic_maps


if __name__ == "__main__":
    topics = read_topics()

    root_dir = "./input/csv"
    files = [ f for f in listdir(root_dir) if isfile(join(root_dir,f)) ]

    if files[0] == '.DS_Store':
        files.pop(0)

    for f in files:
        topic_maps = set_top_terms_topic(f, topics)
        set_sliced_usage_topic(f, topic_maps)
        print(f)
