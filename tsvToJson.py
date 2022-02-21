import json

if __name__ == '__main__':

    counter = 0
    data = []
    with open('data/data.json', 'w') as outfile, open("data/collection.tsv", "r") as f:
        for line in f:
            sp = line.split("\t")
            holder = {}
            data.append({"id": sp[0], "contents": sp[1]})

        json.dump(data, outfile)