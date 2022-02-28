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


## Assignment steps
To run the data set, perform the following steps:
* Download trec_eval
* Read information about trec_eval on http://www.rafaelglater.com/en/post/learn-how-to-use-trec_eval-to-evaluate-your-information-retrieval-system
* Index the data collection
* Run the ranking method with the command below.  
```
python -m pyserini.search  --index indexes/sample_collection_jsonl \
--topics data/msmarco-test2019-queries.tsv \
--output runs/run.sample.txt  \
--bm25 
```
* The output file has the following format: (query-id Q0 document-id rank score STANDARD)
* Evaluate the results by running the command below. The q_rels document needs to have the following format (query-id 0 document-id relevance)
``` 
sudo trec_eval -q -m map -m P.10,100  qrels/qrels.dev.tsv runs/run.queries.dev.txt >> eval.txt 
```
* The output file has the following format (measure query-id score)


## Error analysis
The following steps have been retrieved from the template in the referenced document in the assignement
### Behavior on top relevant documents 
[How many of the top documents for this system were relevant and could they be categorized and distinguished from others?]
### Behavior on top non-relevant documents 
[Why were the top non-relevant documents retrieved?]
### Behavior on unretrieved relevant documents 
[Why weren’t these relevant documents retrieved within the top 1000?]
### Beadplot observations 
[How does the ranking (especially among the top 50 documents) of this system compare to all other systems?]

### Base Query observations 
[What did the system think were the important terms of the original query, and were they good?]
### Expanded Query observations 
[If the system expanded the query (4 out of 6 systems did), what were the important terms of the expansion, and were they helpful?]
### Blunders of system 
[What obvious mistakes did the system make that it could have easily avoided? Examples might be bad stemming of words or bad handling of hyphenation]

### Other features of note 
[Anything else.]

### What should system to do improve performance? 
[The individual’s conclusion as to why the system did not retrieve well, and recommendations as to what would have made a better retrieval.]
### What added information would help performance? How can system get that information? 
[Is there implicit information in the query, that a human would understand but the system didn’t? Examples might be world knowledge (like Germany is part of Europe).]
### Assessing agreement (were there major issues? was relevance determined by “Desc”?) 
[The NIST assessor who originally judged relevance of documents might have a different idea of what was relevant than the text of the description indicates or than the workshop participant thinks should be relevant. It also may be unclear where and why the NIST assessor drew the line between marginally relevant and non-relevant] 