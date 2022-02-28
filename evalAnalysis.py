
if __name__ == '__main__':

    documents_file = "data/collection.tsv"
    ranking_result_file = "runs/run.queries.dev.txt"
    evaluation_result_file = "eval/eval.txt"
    metric_count = 3

    documents = []
    rankings = []
    evaluations = []

    with open(evaluation_result_file, 'r') as eval_f:
        lines = eval_f.readlines()
        for i in range(0, len(lines) , metric_count):
            id = lines[i].split()[1]
            dict = {}
            dict['q_id'] = id
            for j in range(metric_count):
                elements = lines[i+j].split()
                dict[elements[0]] = elements[2]
            evaluations.append(dict)

        print("Finished loading evaluation")
        a = 1


    # lines = doc_f.readlines()
    # for l in lines:
    #     documents.append(l.split())
    #
    # print('Finished loading documents')
    #
    # lines = rank_f.readlines()
    # for l in lines:
    #     rankings.append(l.split())

    print('Finished loading rankings')
