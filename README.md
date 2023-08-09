# AdaSim: A Recursive Similarity Measure in Graphs

This repository provides a reference implementation of AdaSim as well as the proof of AdaSim scores properties.

## Installation and usage
AdaSim is a recursive link-based similarity measure based on the classic Adamic/Adar philosophy. AdaSim is applicable to **both** directed and undirected graphs. In the case of directed graphs, similarity scores can be computed based on any of in-links or out-links. In order to use AdaSim, the following packages are required:
```
Python       >= 3.8
networkx     >=2.6.*
numpy        >=1.21.*
scipy        >=1.7.*
scikit-learn >=1.0.*
```

## Graph file format
A graph must be represented as a text file under the *edge list format* in which, each line corresponds to an edge in the graph, tab is used as the separator of the two nodes, and the node index is started from 0. 

## Proof of AdaSim Scores Properties

## Citation:
> Masoud Reyhani Hamedani and Sang-Wook Kim. 2021. AdaSim: A Recursive Similarity Measure in Graphs. In Proceedings of the 30th ACM International Conference on Information and Knowledge Management, October 2021, Pages 1528–1537. https://doi.org/10.1145/3459637.3482316
