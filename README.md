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

**Graph file format**
A graph must be represented as a text file under the *edge list format* in which, each line corresponds to an edge in the graph, tab is used as the separator of the two nodes, and the node index is started from 0. 

## Proof of AdaSim Scores Properties
AdaSim scores are **_symmetric_**, **_bounded_**, **_monotonic_**, **_unique_**, and **_always existent_**.

**(1) Symmetry:** according to Equation (10), if $`a\!=\!b`$, $`S_k(a,b)\!=\!S_k(b,a)\!=\!1`$; if $`a\!\neq\!b`$, $`S_k(a,b)\!=\! S_k(b,a)\! =\! \widehat{S}(a,b)`$ for all $`k \! \ge\!  0`$.

**(2) Bounding: for all $k$,  $0 \le S_k(a,b) \le 1$.**

According to Equation (10), if $`a\!=\!b`$, then $`S_0(a,b)\!=\!S_1(a,b)\!=\!\cdots=1`$; therefore, $`0\! \le\! S_k(a,b)\! \le\! 1`$ for all values of $`k`$. If $`a\!\neq \!b`$ and $`I_a\!=\!\emptyset`$ or $`I_b\!=\!\emptyset`$, then $`S_0(a,b)\!=\!S_1(a,b)\!=\!\cdots\!=\!0`$; therefore, $`0\! \le \!S_k(a,b)\! \le\! 1`$ for all values of $`k`$.

If $a\neq b$, $I_a \neq \emptyset$, and $I_b \neq \emptyset$, then $S_0(a,b) = \widehat{S}_0(a,b) = 0$; therefore, $0 \le S_0(a,b) \le 1$, which means the property holds for $k=0$. Now, we assume that the property holds for $k$, which means $0 \le S_k(a,b) = \widehat{S}_k(a,b) \le 1$, According to the assumption $\widehat{S}_k(a,b) \ge 0$, thus

```math
\widehat{S}_{k+1}(a,b) = C \cdot \Bigg( \frac{\alpha}{m} \sum_{i \in I_a \cap I_b} w_i + (1-\alpha) \bigg( \frac{1}{\sum_{r \in I_a} w_r \cdot \sum_{t \in I_b} w_t } \cdot \sum_{i \in I_a} \sum_{j \in I_b} w_i \cdot \widehat{S}_k(i,j) \cdot w_j \bigg) \Bigg)
```
```math
\ge C \cdot \Bigg( \frac{\alpha}{m} \sum_{i \in I_a \cap I_b} w_i + (1-\alpha) \bigg( \frac{1}{\sum_{r \in I_a} w_r \cdot \sum_{t \in I_b} w_t } \cdot \sum_{i \in I_a} \sum_{j \in I_b} w_i \cdot 0 \cdot w_j \bigg) \Bigg)
```
```math
\ge C \cdot \frac{\alpha}{m} \sum_{i \in I_a \cap I_b} w_i
```

$`m`$ is the maximum Ada score in the dataset, thereby leading to the fact that $`0 \le \frac{1}{m} \sum_{i \in I_a \cap I_b} w_i \le 1`$; also, $`0 < C < 1`$ and $`0 < \alpha \le 1`$, which means $`\widehat{S}_{k+1}(a,b) = S_{k+1}(a,b) \ge 0`$.

According to the assumption $`\widehat{S}_k(a,b) \le 1`$, thus

```math
\widehat{S}_{k+1}(a,b) = C \cdot \Bigg( \frac{\alpha}{m} \sum_{i \in I_a \cap I_b} w_i + (1-\alpha) \bigg( \frac{1}{\sum_{r \in I_a} w_r \cdot \sum_{t \in I_b} w_t } \cdot \sum_{i \in I_a} \sum_{j \in I_b} w_i \cdot \widehat{S}_k(i,j) \cdot w_j \bigg) \Bigg)
```
```math
\le C \cdot \Bigg( \frac{\alpha}{m} \sum_{i \in I_a \cap I_b} w_i + (1-\alpha) \bigg( \frac{1}{\sum_{r \in I_a} w_r \cdot \sum_{t \in I_b} w_t } \cdot \sum_{i \in I_a} \sum_{j \in I_b} w_i \cdot 1 \cdot w_j \bigg) \Bigg)
```

since $`\sum_{r \in I_a} \!w_r\! \cdot \!\sum_{t \in I_b} w_t`$ = $`\sum_{r \in I_a} \sum_{t \in I_b} w_r \!\cdot\! w_t`$ = $`\sum_{i \in I_a} \sum_{j \in I_b}\! w_i\! \cdot\! 1 \!\cdot w_j`$, 
then $`\widehat{S}_{k+1}(a,b) \le C \cdot \big( \frac{\alpha}{m} \sum_{i \in I_a \cap I_b} w_i + (1-\alpha) \cdot 1 \big)`$; we also know that $`\frac{1}{m} \sum_{i \in I_a \cap I_b} w_i \le 1`$, which means $`\widehat{S}_{k+1}(a,b) \le C \cdot \alpha + C \cdot (1-\alpha) `$ = $`C`$; since $`0 < C < 1`$, then also $`\widehat{S}_{k+1}(a,b) = S_{k+1}(a,b) \le 1`$.

**(3) Monotonicity: for every node-pair $(a,b)$, the sequence \{$S_k(a,b)$\} is non-decreasing as $k$ increases.**

If $`a=b`$, $`S_0(a,b) = S_1(a,b) = \cdots = 1`$; thus, the property holds. If $`a \neq b`$ and $`I_a=\emptyset`$ or $`I_b=\emptyset`$, $`S_0(a,b) = S_1(a,b) = \cdots = 0`$; thus, the property holds. If $`a \neq b`$, $`I_a \neq \emptyset`$, and $`I_b \neq \emptyset`$, according to Equation (10), $`S_0(a,b)=0`$ and by the bounding property, $`0 \le S_1(a,b) \le 1`$; therefore, $`S_0(a,b) \le S_1(a,b)`$, which means for $`k=0`$, the property holds. We assume that the property holds for all $`k`$ where $`S_{k-1}(a,b) = \widehat{S}_{k-1}(a,b) \le S_k(a,b) = \widehat{S}_k(a,b)`$, which means $`\widehat{S}_k(a,b) - \widehat{S}_{k-1}(a,b) \ge 0`$. Now, we show the property holds for $`k+1`$ as follows:

```math
\widehat{S}_{k+1}(a,b) - \widehat{S}_k(a,b) = C \cdot \Bigg( \frac{\alpha}{m} \sum_{i \in I_a \cap I_b } w_i + (1-\alpha) \bigg( \frac{1}{\sum_{r \in I_a} w_r \cdot \sum_{t \in I_b} w_t} \cdot \sum_{i \in I_a} \sum_{j \in I_b} w_i \cdot \widehat{S}_k(i,j) \cdot w_j \bigg) \Bigg)
```
```math
- \; C \cdot \Bigg( \frac{\alpha}{m} \sum_{i \in I_a \cap I_b } w_i + (1-\alpha) \bigg( \frac{1}{\sum_{r \in I_a} w_r \cdot \sum_{t \in I_b} w_t} \cdot \sum_{i \in I_a} \sum_{j \in I_b} w_i \cdot \widehat{S}_{k-1}(i,j) \cdot w_j \bigg) \Bigg)
```
```math
= \; \frac{C \cdot (1-\alpha)}{\sum_{r \in I_a} w_r \cdot \sum_{t \in I_b} w_t} \Bigg( \sum_{i \in I_a} \sum_{j \in I_b} w_i \cdot \widehat{S}_k(i,j) \cdot w_j - \sum_{i \in I_a} \sum_{j \in I_b} w_i \cdot \widehat{S}_{k-1}(i,j) \cdot w_j \Bigg)
```
```math
= \; \frac{C \cdot (1-\alpha)}{\sum_{r \in I_a} w_r \cdot \sum_{t \in I_b} w_t}  \Bigg( \sum_{i \in I_a} \sum_{j \in I_b} w_i \cdot w_j \cdot \big(\widehat{S}_k(i,j) - \widehat{S}_{k-1}(i,j)\big) \Bigg)\\
```

according to the assumptions, $`\widehat{S}_k(a,b) - \widehat{S}_{k-1}(a,b) \ge 0`$ and we already know that $`C \cdot (1-\alpha) \ge 0`$ and $`\sum_{r \in I_a} w_r \cdot \sum_{t \in I_b} w_t \ge 0`$; therefore, $`\widehat{S}_{k+1}(a,b) - \widehat{S}_k(a,b) \ge 0`$, which means $`\widehat{S}_{k+1}(a,b) = S_{k+1}(a,b) \ge \widehat{S}_k(a,b) = S_k(a,b)`$.

## Citation:
> Masoud Reyhani Hamedani and Sang-Wook Kim. 2021. AdaSim: A Recursive Similarity Measure in Graphs. In Proceedings of the 30th ACM International Conference on Information and Knowledge Management, October 2021, Pages 1528–1537. https://doi.org/10.1145/3459637.3482316
