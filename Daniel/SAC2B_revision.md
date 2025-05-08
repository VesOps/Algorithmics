<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Comprehensive Analysis of Graph Algorithms

This report provides an in-depth analysis of six important graph algorithms: Dijkstra's, Bellman-Ford, Prim's, Kruskal's, Floyd-Warshall, and PageRank. For each algorithm, we'll cover pseudocode in VCE Algorithmics style, proof of correctness, design approach, and constraints.

## Dijkstra's Algorithm

### Description

Dijkstra's algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph. It builds the solution incrementally by always choosing the vertex with the minimum distance value.

### Pseudocode

```
FUNCTION Dijkstra(Graph, source)
    SET distance[source] = 0
    FOR EACH vertex v in Graph
        IF v ≠ source THEN
            SET distance[v] = INFINITY
        END IF
        SET visited[v] = FALSE
    END FOR
    
    WHILE NOT all vertices are visited
        SET u = vertex with minimum distance value and not visited
        SET visited[u] = TRUE
        
        FOR EACH neighbor v of u
            IF visited[v] = FALSE AND distance[u] + weight(u,v) < distance[v] THEN
                SET distance[v] = distance[u] + weight(u,v)
            END IF
        END FOR
    END WHILE
    
    RETURN distance
END FUNCTION
```


### Proof of Correctness

1. **Base Case**: The distance to the source vertex is correctly set to 0.
2. **Inductive Step**: When we select a vertex u with the minimum distance, that distance is final (optimal).
    - This is because if there were a shorter path to u, it would have to go through another unvisited vertex v.
    - If distance[v] < distance[u], we would have selected v instead.
3. Each time we relax an edge (u,v), we ensure that if we have a shorter path to v through u, we update v's distance.
4. By the time all vertices are visited, all shortest paths are found.

### Algorithm Design Approach

Dijkstra's algorithm uses a greedy approach[^17]. At each step, it selects the vertex with the smallest known distance, which locally seems to be the best choice. This greedy choice eventually leads to a globally optimal solution[^19].

### Constraints

- Does not work with negative edge weights, as once a vertex is marked as visited, its distance is considered final[^17].
- Requires all edges to have non-negative weights.
- Most efficient when implemented with a priority queue, giving a time complexity of O(E + V log V).


## Bellman-Ford Algorithm

### Description

The Bellman-Ford algorithm computes shortest paths from a single source vertex to all other vertices in a weighted graph, handling graphs with negative weight edges and detecting negative weight cycles.

### Pseudocode

```
FUNCTION BellmanFord(Graph, source)
    // Initialize distances
    FOR EACH vertex v in Graph
        SET distance[v] = INFINITY
    END FOR
    SET distance[source] = 0
    
    // Relax all edges V-1 times
    FOR i = 1 to |V| - 1
        FOR EACH edge (u,v) with weight w in Graph
            IF distance[u] + w < distance[v] THEN
                SET distance[v] = distance[u] + w
            END IF
        END FOR
    END FOR
    
    // Check for negative weight cycles
    FOR EACH edge (u,v) with weight w in Graph
        IF distance[u] + w < distance[v] THEN
            PRINT "Graph contains a negative weight cycle"
            RETURN
        END IF
    END FOR
    
    RETURN distance
END FUNCTION
```


### Proof of Correctness

1. After the first iteration, correct distances to vertices that are 1 edge away from the source are computed.
2. After the second iteration, correct distances to vertices that are 2 edges away are computed.
3. This pattern continues, so after V-1 iterations (where V is the number of vertices), all shortest paths are computed.
4. The final check for negative weight cycles ensures any such cycle will be detected.

### Algorithm Design Approach

Bellman-Ford uses a dynamic programming approach. It builds solutions to subproblems (finding shortest paths with a limited number of edges) and uses these to solve the main problem.

### Constraints

- Can handle negative edge weights but will report an error if there's a negative weight cycle.
- Has a time complexity of O(V*E), which is less efficient than Dijkstra's for non-negative weight graphs.
- Requires more iterations than Dijkstra's, making it slower in practice for many graph scenarios.


## Prim's Algorithm

### Description

Prim's algorithm finds a minimum spanning tree (MST) for a connected weighted graph. It grows the MST one vertex at a time, always choosing the edge with the minimum weight that connects the tree to a new vertex.

### Pseudocode

```
FUNCTION Prim(Graph, startVertex)
    SET mst = empty set
    SET visited[startVertex] = TRUE
    FOR EACH vertex v in Graph EXCEPT startVertex
        SET visited[v] = FALSE
    END FOR
    
    WHILE NOT all vertices are visited
        SET minEdge = edge with minimum weight connecting a visited vertex to an unvisited vertex
        ADD minEdge to mst
        SET visited[endpoint of minEdge] = TRUE
    END WHILE
    
    RETURN mst
END FUNCTION
```


### Proof of Correctness

The proof is based on the cut property of MSTs:

1. Start with an empty tree and a single vertex.
2. At each step, consider the cut (S, V-S) where S is the set of visited vertices and V-S is the set of unvisited vertices.
3. The algorithm adds the minimum weight edge crossing this cut to the MST.
4. By the cut property, this edge must be in the MST.
5. After V-1 steps, all vertices are connected by a minimum weight spanning tree[^16].

### Algorithm Design Approach

Prim's algorithm is a greedy algorithm. At each step, it selects the edge with the minimum weight that connects the current tree to a new vertex[^16].

### Constraints

- The graph must be connected; otherwise, the algorithm will only find an MST for the connected component containing the start vertex.
- Most efficient when implemented with a priority queue, with a time complexity of O(E log V).
- Works best on dense graphs where E is close to V².


## Kruskal's Algorithm

### Description

Kruskal's algorithm finds a minimum spanning tree for a connected weighted graph by sorting all edges in non-decreasing order of weight and then adding edges one by one, skipping those that would create a cycle.

### Pseudocode

```
FUNCTION Kruskal(Graph)
    SET mst = empty set
    SORT edges of Graph in non-decreasing order of weight
    SET disjointSet = DisjointSet(vertices of Graph)
    
    FOR EACH edge (u,v) in sorted edges
        IF disjointSet.Find(u) ≠ disjointSet.Find(v) THEN
            ADD edge (u,v) to mst
            disjointSet.Union(u, v)
        END IF
    END FOR
    
    RETURN mst
END FUNCTION
```


### Proof of Correctness

1. Sort all edges by weight.
2. Start with an empty MST.
3. For each edge (u,v) in order of increasing weight:
    - If adding the edge doesn't create a cycle, add it to the MST.
    - This is the minimum weight edge that connects the set containing u to the set containing v.
    - By the cut property, this edge must be in the MST.
4. After adding V-1 edges, the MST is complete.

### Algorithm Design Approach

Kruskal's algorithm is a greedy algorithm. It always selects the edge with the smallest weight that doesn't form a cycle.

### Constraints

- The graph must be connected for the algorithm to find a spanning tree.
- Requires an efficient way to check if adding an edge creates a cycle, typically using a disjoint-set data structure.
- Has a time complexity of O(E log E) due to the sorting of edges.
- More efficient than Prim's for sparse graphs.


## Floyd-Warshall Algorithm

### Description

The Floyd-Warshall algorithm finds the shortest paths between all pairs of vertices in a weighted graph using an iterative approach to consider all possible intermediate vertices.

### Pseudocode

```
FUNCTION FloydWarshall(Graph)
    SET dist[i][j] = weight of edge (i,j) if it exists, INFINITY otherwise
    FOR EACH vertex i in Graph
        SET dist[i][i] = 0
    END FOR
    
    FOR k = 1 to |V|
        FOR i = 1 to |V|
            FOR j = 1 to |V|
                IF dist[i][k] + dist[k][j] < dist[i][j] THEN
                    SET dist[i][j] = dist[i][k] + dist[k][j]
                END IF
            END FOR
        END FOR
    END FOR
    
    RETURN dist
END FUNCTION
```


### Proof of Correctness

1. Let dist[i][j]^k be the shortest distance from vertex i to j using vertices 1 to k as intermediate.
2. Base case: dist[i][j]^0 is the direct edge weight if there's an edge, INFINITY otherwise.
3. Inductive step: dist[i][j]^k = min(dist[i][j]^(k-1), dist[i][k]^(k-1) + dist[k][j]^(k-1)).
4. This represents the choice: either the shortest path from i to j uses vertex k as an intermediate, or it doesn't.
5. After considering all vertices as intermediates, dist[i][j]^|V| gives the shortest path from i to j.

### Algorithm Design Approach

Floyd-Warshall uses a dynamic programming approach. It solves the all-pairs shortest path problem by breaking it down into smaller subproblems and building up to the final solution.

### Constraints

- Can handle negative edge weights but will not work correctly if there are negative weight cycles.
- Has a time complexity of O(V³), making it suitable for small to medium-sized graphs.
- More efficient than running Dijkstra's or Bellman-Ford from each vertex for dense graphs.


## PageRank Algorithm

### Description

PageRank is an algorithm used to rank web pages in search engine results. It operates on the principle that more important websites are likely to receive more links from other websites.

### Pseudocode

```
FUNCTION PageRank(Graph, damping_factor, iterations)
    SET N = number of vertices in Graph
    SET initial_value = 1/N
    
    FOR EACH vertex v in Graph
        SET PR[v] = initial_value
    END FOR
    
    FOR iter = 1 to iterations
        FOR EACH vertex v in Graph
            SET sum = 0
            FOR EACH vertex u with an edge to v
                SET sum = sum + PR[u] / outDegree(u)
            END FOR
            SET PR_new[v] = (1 - damping_factor) / N + damping_factor * sum
        END FOR
        SET PR = PR_new
    END FOR
    
    RETURN PR
END FUNCTION
```


### Explanation of Formulas

The PageRank formula for a page A is:

PR(A) = (1 - d)/N + d * (PR(T₁)/C(T₁) + PR(T₂)/C(T₂) + ... + PR(Tₙ)/C(Tₙ))

Where:

- PR(A) is the PageRank of page A
- d is the damping factor (typically 0.85)
- N is the total number of pages
- PR(Tᵢ) is the PageRank of pages Tᵢ which link to page A
- C(Tᵢ) is the number of outbound links from page Tᵢ

The damping factor represents the probability that a random surfer will continue clicking on links rather than starting a new random page.

### Algorithm Design Approach

PageRank uses an iterative approach and probabilistic modeling. It models the behavior of a "random surfer" who keeps clicking on links at random.

### Constraints

- Requires several iterations to converge, with more iterations generally leading to more accurate results.
- The convergence rate depends on the graph structure and the damping factor.
- Assumes that links between pages are a good indicator of page importance.
- May not work well for certain specialized domains or when manipulated through artificial link structures.


## Conclusion

Graph algorithms form the backbone of many computational problems, from finding the shortest path to ranking web pages. Each algorithm has its strengths, constraints, and appropriate use cases. Understanding their design approaches – whether greedy, dynamic programming, or probabilistic – helps us select the right algorithm for a particular problem. When implementing these algorithms, it's essential to consider their constraints, such as Dijkstra's inability to handle negative weights or the computational complexity of Floyd-Warshall for large graphs.

The pseudocode representations provided follow the VCE Algorithmics 3/4 style, making them accessible for educational purposes[^16][^18][^20]. By studying these algorithms, their proofs of correctness, and their constraints, we gain valuable insights into algorithmic thinking and problem-solving approaches.

<div style="text-align: center">⁂</div>

[^1]: https://www.vcaa.vic.edu.au/curriculum/vce-curriculum/vce-study-designs/pseudocode

[^2]: https://www.monash.edu/it/future-students/vce-algorithmics

[^3]: https://www.reddit.com/r/vce/comments/1ijuoav/algorithmics_34_answering_examstyle_questions/

[^4]: https://tex.stackexchange.com/questions/204592/how-to-format-a-pseudocode-algorithm

[^5]: https://www.cs.cornell.edu/courses/cs312/2002sp/lectures/lec20/lec20.htm

[^6]: https://www.programiz.com/dsa/bellman-ford-algorithm

[^7]: https://www.freecodecamp.org/news/prims-algorithm-explained-with-pseudocode/

[^8]: https://en.wikipedia.org/wiki/Kruskal's_algorithm

[^9]: https://en.wikipedia.org/wiki/PageRank

[^10]: https://www.ccs.neu.edu/home/daikeshi/notes/PageRank.pdf

[^11]: https://en.wikipedia.org/wiki/Floyd–Warshall_algorithm

[^12]: https://www.vcaa.vic.edu.au/curriculum/vce/vce-study-designs/Pages/PseudoCode.aspx

[^13]: https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/04GreedyAlgorithmsII.pdf

[^14]: https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture14.pdf

[^15]: https://en.wikipedia.org/wiki/Prim's_algorithm

[^16]: https://www.youtube.com/watch?v=RCI4N3bSZeY

[^17]: https://cs.stackexchange.com/questions/154420/dijkstra-as-a-greedy-algorithm

[^18]: https://www.mav.vic.edu.au/Tenant/C0000019/00000001/downloads/Resources/annual-conferences/2024/A25 - Implementing pseudocode and algorithms in Python on computer and CAS.pdf

[^19]: https://stackoverflow.com/questions/2856670/why-does-dijkstras-algorithm-work

[^20]: https://mathspace.co/textbooks/syllabuses/Syllabus-1162/topics/Topic-21987/subtopics/Subtopic-280344/

[^21]: https://www.youtube.com/watch?v=_tnWbA05yR8

[^22]: https://discussion.atarnotes.com/d/7387-should-i-do-vce-algorithmics-without-prior-knowledge-of-coding

[^23]: https://www.vsv.vic.edu.au/subject/year-12-algorithmics-hess-units-3-and-4/

[^24]: https://cs.uwaterloo.ca/~dstinson/papers/pseudocode.pdf

[^25]: https://www.reddit.com/r/vce/comments/1440yeg/methods_pseudocode_help/

[^26]: https://www.youtube.com/watch?v=LDurwsLi6Q0

[^27]: https://discussion.atarnotes.com/d/7673-methods-study-design-change-next-year-34

[^28]: https://builtin.com/data-science/pseudocode

[^29]: https://www.mav.vic.edu.au/Tenant/C0000019/00000001/downloads/Resources/annual-conferences/2024/H15 - Cracking the pseudocodeTeaching algorithms from a student perspective.pdf

[^30]: https://www.youtube.com/watch?v=kbEaedtkfKU

[^31]: https://www.bbc.co.uk/bitesize/guides/z7kkw6f/revision/2

[^32]: https://archive.atarnotes.com/forum/index.php?topic=134146.0

[^33]: https://blog.quantinsti.com/dijkstra-algorithm/

[^34]: https://www.simplilearn.com/tutorials/data-structure-tutorial/bellman-ford-algorithm

[^35]: https://en.wikipedia.org/wiki/Bellman–Ford_algorithm

[^36]: https://stackoverflow.com/questions/15931461/difference-constraints-on-bellman-ford-algorithm

[^37]: https://www.youtube.com/watch?v=0hXj05XXT7M

[^38]: https://brilliant.org/wiki/bellman-ford-algorithm/

[^39]: https://www.w3schools.com/dsa/dsa_algo_graphs_bellmanford.php

[^40]: https://herovired.com/learning-hub/topics/bellman-ford-algorithm/

[^41]: https://courses.csail.mit.edu/6.006/spring11/lectures/lec17.pdf

[^42]: https://courses.csail.mit.edu/6.006/spring11/lectures/lec15.pdf

[^43]: https://www.cs.fsu.edu/~xyuan/paper/99ic3n.pdf

[^44]: https://cs.stackexchange.com/questions/127121/clarification-in-the-proof-for-the-bellamn-ford-algorithm

[^45]: https://algorithms.discrete.ma.tum.de/spp/bellman-ford/

[^46]: https://journals.iucr.org/d/issues/2006/04/00/sx5049/sx5049sup1.pdf

[^47]: https://courses.grainger.illinois.edu/cs374/fa2020/lec_prerec/18/18_2_3_1.pdf

[^48]: https://www.uvm.edu/~cbcafier/cs2240/content/13_graph_algos/01_shortest_path.html

[^49]: https://www.youtube.com/watch?v=R1KdSgtTPss

[^50]: https://stackoverflow.com/questions/15931461/difference-constraints-on-bellman-ford-algorithm/35850319

[^51]: https://www.wscubetech.com/resources/dsa/kruskal-algorithm

[^52]: https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/04GreedyAlgorithmsII.pdf

[^53]: https://www.positional.com/blog/pagerank

[^54]: https://towardsdatascience.com/pagerank-algorithm-fully-explained-dc794184b4af/

[^55]: https://github.com/cy94/floyd-warshall/blob/master/README.md~

[^56]: https://stackoverflow.com/questions/16270272/how-is-floyd-warshall-a-dynamic-algorithm

[^57]: https://www.youtube.com/watch?v=WTkyp5AnmNU

[^58]: https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/a9e76885a78c729f2375e14830caebf2_MIT6_046JS12_lec07.pdf

[^59]: https://www.wscubetech.com/resources/dsa/floyd-warshall-algorithm

[^60]: https://www.youtube.com/watch?v=oNI0rf2P9gE

[^61]: https://imada.sdu.dk/~jbj/DM85/lec6a.pdf

[^62]: https://stackoverflow.com/questions/27259205/what-kind-of-cycle-isnt-allowed-in-floyd-warshall-algorithm

[^63]: https://www.vaia.com/en-us/textbooks/computer-science/foundations-of-algorithms-using-c-pseudocode-2-edition/chapter-3/problem-8-implement-floyds-algorithm-for-the-shortest-paths-/

[^64]: https://www.youtube.com/watch?v=4OQeCuLYj-4

[^65]: https://wcipeg.com/wiki/Floyd–Warshall_algorithm

[^66]: https://espace.library.uq.edu.au/view/UQ:05d7251/s4558812_final_thesis.pdf

[^67]: https://www.youtube.com/watch?v=XqCP_2Vcas4

[^68]: http://graphstream-project.org/doc/Algorithms/Shortest-path/Dijkstra/1.0/

[^69]: https://www.reddit.com/r/algorithms/comments/nhnot5/what_is_the_pseudocode_for_finding_the_all_pairs/

[^70]: https://www.cs.huji.ac.il/course/2002/dast/slides/BellmanFord.pdf

[^71]: https://people.csail.mit.edu/alinush/6.006-spring-2014/mit-fall-2010-bellman-ford.pdf

[^72]: https://gist.github.com/travishen/82e7a8aadf38b46f27652d758dc75261

[^73]: https://www.wscubetech.com/resources/dsa/prim-algorithm

[^74]: https://courses.cs.duke.edu/fall14/cps130/notes/scribe8.pdf

[^75]: https://www.acsce.edu.in/acsce/wp-content/uploads/2020/03/Module3_DAA.pdf

[^76]: https://nriit.edu.in/files/IT-Notes/DAA/DAA-Unit-III.pdf

[^77]: https://people.eecs.berkeley.edu/~vazirani/sp04/notes/greedy

[^78]: https://www.youtube.com/watch?v=meonLcN7LD4

[^79]: https://www.searchenginewatch.com/2018/10/25/googles-pagerank-algorithm-explained/

[^80]: https://cs.brown.edu/courses/cs016/static/files/assignments/projects/GraphHelpSession.pdf

[^81]: https://www.mathworks.com/help/matlab/math/use-page-rank-algorithm-to-rank-websites.html

[^82]: https://pi.math.cornell.edu/~mec/Winter2009/RalucaRemus/Lecture3/lecture3.html

[^83]: https://cs.brown.edu/courses/csci0160/static/files/assignments/projects/GraphHelpSession.pdf

[^84]: https://www.programiz.com/dsa/floyd-warshall-algorithm

[^85]: https://www.tutorialspoint.com/data_structures_algorithms/floyd_warshall_algorithm.htm

[^86]: https://www.cs.umd.edu/class/fall2021/cmsc351-0301/files/floydWarshall.pdf

[^87]: https://www.youtube.com/watch?v=uSjsgdb4oK4

[^88]: https://brilliant.org/wiki/floyd-warshall-algorithm/

[^89]: https://cs.stackexchange.com/questions/98971/confirmation-of-alternative-correctness-proof-for-floyd-warshalls-all-pair-shor

[^90]: https://cs.stackexchange.com/questions/133606/floyd-warshall-with-constraints

