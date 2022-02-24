# PassageRanking

To run bm25 on an input set, use the command bellow in the root folder, changing the index, topics and output accordingly
```
python -m pyserini.search  --index indexes/sample_collection_jsonl \
--topics data/msmarco-test2019-queries.tsv \
--output run.sample.txt  \
--bm25 
```

To run the trec_eval evaluation tool, first transform the output of the bm25 to trec format using:
```
python -m pyserini.eval.convert_msmarco_run_to_trec_run \
   --input runs/run.msmarco-passage.bm25tuned.txt \
   --output runs/run.msmarco-passage.bm25tuned.trec
  ```

Then, this new file can be used to apply trec_eval using the following command:
```
tools/eval/trec_eval.9.0.4/trec_eval -c -mrecall.1000 -mmap \
   collections/msmarco-passage/qrels.dev.small.trec \\
    runs/run.msmarco-passage.bm25tuned.trec
```
The second line in the command being the actual query relevance document
The third line in the command being the transformed output of bm25

(more info at: https://github.com/castorini/pyserini/blob/master/docs/experiments-msmarco-passage.md)


## 200 query assignment:
