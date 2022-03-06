import json

if __name__ == '__main__':

    counter = 0
    data = []
    with open('data/data.json', 'w', encoding="utf-8") as outfile, open("data/collection.tsv", "r", encoding="utf-8") as f:
        for line in f:
            sp = line.split("\t")
            holder = {}
            data.append({"id": sp[0], "contents": sp[1]})

        json.dump(data, outfile)