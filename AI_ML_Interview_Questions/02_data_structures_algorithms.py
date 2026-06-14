"""
DATA STRUCTURES & ALGORITHMS FOR AI/ML INTERVIEWS
⭐⭐ Medium to Hard difficulty questions

These questions test:
- Arrays and matrix operations
- Searching and sorting algorithms
- Graph algorithms (for knowledge graphs)
- Dynamic programming
- Heap and priority queues (for ranking/sorting)
- Hash tables for efficiency
"""

# ============================================================================
# Q1: BINARY SEARCH - Similarity Search in Embeddings
# ============================================================================
# Question: Find the closest embedding in a sorted list

def binary_search_similarity(embeddings, target, tolerance=0.01):
    """
    ⭐⭐ Medium
    Binary search to find embedding close to target value
    Used in vector similarity search optimization
    
    Input: embeddings=[0.1, 0.3, 0.5, 0.7, 0.9], target=0.6, tolerance=0.01
    Output: Index of value closest to 0.6 or -1 if not found
    
    Time: O(log n), Space: O(1)
    """
    pass


# ============================================================================
# Q2: MATRIX TRANSPOSE & OPERATIONS - Batch Processing
# ============================================================================
# Question: Transpose embedding matrix for batch operations

def matrix_transpose(matrix):
    """
    ⭐ Easy
    Transpose a 2D matrix
    Common in ML when processing batches of embeddings
    
    Input: [[1, 2, 3], [4, 5, 6]]
    Output: [[1, 4], [2, 5], [3, 6]]
    
    Tip: Use zip(*matrix)
    Time: O(n*m), Space: O(n*m)
    """
    pass


# ============================================================================
# Q3: TWO POINTER TECHNIQUE - Context Window Management
# ============================================================================
# Question: Find optimal context window for RAG

def find_optimal_context_window(tokens, window_size):
    """
    ⭐⭐ Medium
    Find subarray (context window) of given size with maximum sum
    Used to identify best context chunk in RAG
    
    Input: tokens=[1, 3, 2, 6, 4, 5], window_size=3
    Output: [6, 4, 5] or sum=15
    
    Time: O(n), Space: O(1)
    Tip: Use sliding window technique
    """
    pass


# ============================================================================
# Q4: MERGE SORTED ARRAYS - Combining Search Results
# ============================================================================
# Question: Merge ranked results from multiple sources

def merge_sorted_results(results1, results2):
    """
    ⭐⭐ Medium
    Merge two sorted arrays while removing duplicates
    Used when combining results from different RAG sources
    
    Input: [0.1, 0.5, 0.9], [0.2, 0.6]
    Output: [0.1, 0.2, 0.5, 0.6, 0.9]
    
    Time: O(n + m), Space: O(n + m)
    """
    pass


# ============================================================================
# Q5: HEAP/PRIORITY QUEUE - Top-K Results
# ============================================================================
# Question: Find top-K most relevant documents

def get_top_k_documents(documents, k=5):
    """
    ⭐⭐ Medium
    Return top K documents by relevance score
    Common in RAG to get most relevant context
    
    Input: 
    documents = [
        {'id': 1, 'score': 0.8},
        {'id': 2, 'score': 0.6},
        {'id': 3, 'score': 0.95},
    ]
    k = 2
    
    Output: [{'id': 3, 'score': 0.95}, {'id': 1, 'score': 0.8}]
    
    Time: O(n log k), Space: O(k)
    Tip: Use heapq.nlargest()
    """
    pass


# ============================================================================
# Q6: GRAPH DFS - Knowledge Graph Traversal
# ============================================================================
# Question: Traverse knowledge graph to find related entities

def graph_dfs(graph, start_node):
    """
    ⭐⭐ Medium
    Depth-first search on graph (adjacency list representation)
    Used to traverse knowledge graphs for entity relationships
    
    Input: 
    graph = {
        'entity_a': ['entity_b', 'entity_c'],
        'entity_b': ['entity_d'],
        'entity_c': [],
        'entity_d': []
    }
    start_node = 'entity_a'
    
    Output: ['entity_a', 'entity_b', 'entity_d', 'entity_c']
    
    Time: O(V + E), Space: O(V)
    """
    pass


# ============================================================================
# Q7: LONGEST COMMON SUBSTRING - Prompt Similarity
# ============================================================================
# Question: Find similarity between two prompts

def longest_common_substring(str1, str2):
    """
    ⭐⭐⭐ Hard
    Find longest common substring between two strings
    Used to measure prompt similarity or detect duplicates
    
    Input: "hello world", "world peace"
    Output: "world" or length 5
    
    Time: O(n*m), Space: O(min(n,m))
    Tip: Use dynamic programming
    """
    pass


# ============================================================================
# Q8: GRAPH BFS - Shortest Path in Knowledge Graph
# ============================================================================
# Question: Find shortest path between two concepts

def graph_bfs_shortest_path(graph, start, end):
    """
    ⭐⭐ Medium
    Breadth-first search to find shortest path
    Used in knowledge graphs to find concept relationships
    
    Input:
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': ['E'],
        'E': []
    }
    start = 'A', end = 'E'
    
    Output: ['A', 'B', 'D', 'E'] or ['A', 'C', 'D', 'E']
    
    Time: O(V + E), Space: O(V)
    """
    pass


# ============================================================================
# Q9: COUNTING SORT - Frequency-based Ranking
# ============================================================================
# Question: Sort items by frequency efficiently

def counting_sort_by_frequency(items):
    """
    ⭐⭐ Medium
    Sort by frequency using counting sort (O(n) when range is known)
    Used to rank tokens or documents by frequency
    
    Input: [5, 2, 8, 2, 9, 5, 5]
    Output: [2, 2, 5, 5, 5, 8, 9]
    
    Time: O(n + k) where k is range, Space: O(k)
    """
    pass


# ============================================================================
# Q10: EDIT DISTANCE - Typo Tolerance in Search
# ============================================================================
# Question: Find similar prompts considering typos

def edit_distance(str1, str2):
    """
    ⭐⭐⭐ Hard
    Calculate Levenshtein distance between two strings
    Used for typo-tolerant search, fuzzy matching
    
    Input: "kitten", "sitting"
    Output: 3 (substitute k->s, e->i, insert g)
    
    Time: O(n*m), Space: O(n*m)
    Tip: Use dynamic programming (DP table)
    """
    pass


# ============================================================================
# SOLUTION TEMPLATE
# ============================================================================

"""
SOLUTIONS:

# Q1: Binary Search Similarity
def binary_search_similarity(embeddings, target, tolerance=0.01):
    left, right = 0, len(embeddings) - 1
    closest_idx = -1
    min_diff = float('inf')
    
    while left <= right:
        mid = (left + right) // 2
        diff = abs(embeddings[mid] - target)
        
        if diff < min_diff:
            min_diff = diff
            closest_idx = mid
        
        if min_diff <= tolerance:
            return closest_idx
        
        if embeddings[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return closest_idx

# Q2: Matrix Transpose
def matrix_transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# Q3: Optimal Context Window
def find_optimal_context_window(tokens, window_size):
    max_sum = sum(tokens[:window_size])
    current_sum = max_sum
    max_idx = 0
    
    for i in range(window_size, len(tokens)):
        current_sum = current_sum - tokens[i - window_size] + tokens[i]
        if current_sum > max_sum:
            max_sum = current_sum
            max_idx = i - window_size + 1
    
    return tokens[max_idx:max_idx + window_size]

# Q4: Merge Sorted Arrays
def merge_sorted_results(results1, results2):
    result = []
    i = j = 0
    while i < len(results1) and j < len(results2):
        if results1[i] < results2[j]:
            if not result or result[-1] != results1[i]:
                result.append(results1[i])
            i += 1
        else:
            if not result or result[-1] != results2[j]:
                result.append(results2[j])
            j += 1
    
    result.extend([x for x in results1[i:] if not result or result[-1] != x])
    result.extend([x for x in results2[j:] if not result or result[-1] != x])
    return result

# Q5: Top-K Documents
def get_top_k_documents(documents, k=5):
    import heapq
    return heapq.nlargest(k, documents, key=lambda x: x['score'])

# Q6: Graph DFS
def graph_dfs(graph, start_node):
    visited = []
    stack = [start_node]
    visited_set = set()
    
    while stack:
        node = stack.pop()
        if node not in visited_set:
            visited.append(node)
            visited_set.add(node)
            stack.extend(reversed(graph.get(node, [])))
    
    return visited

# Q7: Longest Common Substring
def longest_common_substring(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_length = max(max_length, dp[i][j])
    
    return max_length

# Q8: Graph BFS
def graph_bfs_shortest_path(graph, start, end):
    from collections import deque
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return []

# Q9: Counting Sort
def counting_sort_by_frequency(items):
    if not items:
        return []
    
    min_val, max_val = min(items), max(items)
    count = [0] * (max_val - min_val + 1)
    
    for item in items:
        count[item - min_val] += 1
    
    result = []
    for i in range(len(count)):
        result.extend([i + min_val] * count[i])
    
    return result

# Q10: Edit Distance
def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[m][n]
"""


if __name__ == "__main__":
    # Q2: Test Matrix Transpose
    print("Q2: Matrix Transpose")
    result = matrix_transpose([[1, 2, 3], [4, 5, 6]])
    print(f"Result: {result}")
    print(f"Expected: [[1, 4], [2, 5], [3, 6]]")
    print()
    
    # Q3: Test Context Window
    print("Q3: Optimal Context Window")
    result = find_optimal_context_window([1, 3, 2, 6, 4, 5], window_size=3)
    print(f"Result: {result}, Sum: {sum(result)}")
    print(f"Expected: [6, 4, 5], Sum: 15")
    print()
    
    # Q10: Test Edit Distance
    print("Q10: Edit Distance")
    result = edit_distance("kitten", "sitting")
    print(f"Result: {result}")
    print(f"Expected: 3")
