import json


# if __name__ == '__main__':
#     with open('qrels/qrels_lim.dev.tsv', 'w') as outfile, open("qrels/qrels.dev.tsv", "r") as f:
#         for line in f:
#             sp = line.split()
#             outfile.write(sp[0] + "\t" + sp[2] + "\n")

#
if __name__ == '__main__':

    counter = 0
    data = []
    with open('data/collection.json', 'w') as outfile, open("data/collection.tsv", "r") as f:
        for line in f:
            sp = line.split("\t")
            holder = {}
            data.append({"id": sp[0], "contents": sp[1]})

        json.dump(data, outfile)
#
#     formatqrels()