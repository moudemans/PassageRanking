

def loadFiles(filename):
    file = open(filename, "r", encoding="utf8")
    writeFile = open(f"{filename}.json", "w", encoding="utf8")
    writeFile.write("[\n")

    for l in file:
        l = l.strip()
        id = l.split("\t")[0]
        contents = l.split("\t")[1]
        writeFile.write(f"\t{{ \"id\" :  \"doc{id}\", \"contents\" : \"{contents}\" }},\n")

    writeFile.write("\n]")
    writeFile.close()
    file.close()

if __name__ == "__main__":
    loadFiles("data/collection.tsv")

