# Leetcode Cheatsheet 

List of algorithms that I incounter along practice with leetcode problems. 
Some are just a note to remember, but some like DP logic and backtracking logic are pretty useful when you know the problem should use a specific algorithm but just forgot how to implement them. 

== ：needs more practice, the more = the more practice needed

## Array and Strings

### Prefix Sum

#### (1D array)

=== "python"
    ```python
    def samplePrefix(arr：List[int])->int:
        n = len(arr)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        # sumofNum = prefix[r] - prefix[l], inclusive l and exclusive r        
    ```
=== "c++"

    ```cpp
    vector<int> samplePrefix(const vector<int>& arr) {
        int n = arr.size();
        vector<int> prefix(n + 1, 0);  // prefix[0] = 0
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + arr[i];
        }
        return prefix;
    }
    ```

#### (2D array)

=== "python"
    ```python
    def prefix2D(matrix):
            ROW, COL = len(matrix), len(matrix[0])
        prefix = [[0] * (COL + 1) for _ in range(ROW + 1)]

        for r in range(1, ROW + 1):
            for c in range(1, COL + 1):
                prefix[r][c] = (matrix[r-1][c-1]   # current cell
                            + prefix[r-1][c]    # sum of above
                            + prefix[r][c-1]    # sum of left 
                            - prefix[r-1][c-1]) # remove overlap
        return prefix
    ```
=== "c++"
    ```cpp
    vector<vector<int>> prefix2D(const vector<vector<int>>& matrix) {
        int ROW = matrix.size();
        int COL = matrix[0].size();

        vector<vector<int>> prefix(ROW + 1, vector<int>(COL + 1, 0));

        for (int r = 1; r <= ROW; r++) {
            for (int c = 1; c <= COL; c++) {
                prefix[r][c] = matrix[r - 1][c - 1]  // current cell
                            + prefix[r - 1][c]       // sum above
                            + prefix[r][c - 1]       // sum left
                            - prefix[r - 1][c - 1];  // remove overlap
            }
        }
        return prefix;
    }
    ```
### Two Pointers

```python
def twopt(nums, target): # find two num in sorted array that sum to target
		l, r = 0, len(nums) - 1
		while l < r:
				s = nums[l] + nums[r]
				if s == target:
						return (l, r)
				elif s < target:
						l += 1
				else:
						r -= 1
		return (-1, -1)
```

### Sliding window

problems about subarrays/substrings with constraints

```python
def slidingwindow(s, k): # longest substring with at most k distinct characters
		l = 0
		freq = Counter()
		best = 0
		for r, ch in enumerate(s):
				freq[ch] += 1
				while len(freq) > k:
						freq[s[l]] -= 1
						if freq[s[l]] == 0:
								del freq[s[l]]
						l += 1
				best = max(best, r - l + 1)
		return best
```

### Sorting + Sweep line

problems about interval overlap, scheduling, max concurrency, skyline

```python
def sweepline(intervals):
		events = []
		for s, e in intervals:
				events.append((s, 1))  # +1 when interval starts
				events.append((e, -1)) # -1 when interval ends
		
		events.sort(key = lambda x: (x[0], x[1]))
		
		active = 0
		overlap = 0
		for _, delta in evnets:
				active += delta
				overlap = max(overlap, active)
		return overlap
```

## Hashing

### Counting

```python
from collections import Couter 
s = "hashing"
cnt = Counter(s)
```

### Grouping

```python
def grouping(strs): # eg. group anagrams
		groups = defaultdict(list)
		for s in strs:
				key = tuple(sorted(s))
				groups[key].append(s)
		return list(groups.values())
```

### Deduplicaiton

```python
def dedup(nums): # only one of each can exist in hashset 
		unique = list(set(nums))
```

### Prefix modulo

check if subarray sum is divisible by k, count number of subarray with sum divisible by k, detect cycles in cumulative sums with constraints 

```python
def prefixModulo(nums, k):
		prefix = 0
		seen = {0: -1}
		for i, num in enumerate(nums):
				prefix += num
				remainder = prefix % k
				if remainder in seen:
						if i - seen[remainder] >= 2:
								return True
				else:
						seen[remainder] = i
		return False
```

## Stack & Queue (v1)

### Monotonic Stack

#### NGE =

```python
def nge(nums): # next greater elements
		n = len(nums)
		res = [-1] * n
		stack = []
		
		for i in range(n):
				while stack and nums[i] > nums[stack[-1]]:
						idx = stack.pop()
						res[idx] = nums[i]
				stack.append(i)
		return res
```

#### Largest Rectangle in Histogram =

```python
def largestRec(heights):
		stack = []
		res = 0
		
		for i, h in enumerate(heights):
				start = i
				while stack and h < stack[-1][1]:
						idx, height = stack.pop()
						res = max(res, height * (i - idx))
						start = idx
				stack.append((start, h))
		for idx, height in stack:
				res = max(res, height * (len(heights) - idx))
		return res
```

### Monotonic Queue

#### Sliding Window Maximum ==

```python
def slidingWindowMax(nums, k):
		dq, res = deque(), []
		for i, num in enumerate(nums):
				if dq and dq[0] <= i - k: # remove left index out of window
						dq.popleft()
				while dq and nums[dq[-1]] < num: # maintain decreasing order in deque
						dq.pop()
				dq.append(i)
				if i >= k - 1: 
						res.append(nums[dq[0]])
		return res
```

## Linked Lists

### Reverse Linked List

whole list 

```python
def reverseList(head:ListNode) -> ListNode:
		prev = None
		cur = head
		while cur:
				nxt = cur.next
				cur.next = prev
				prev = cur
				cur = nxt
		return prev
```

k-group

```python
def reversekGroup(head:ListNode, k) -> ListNode:
		def rev(start, end):
				prev, cur = None, start
				while cur != end:
						nxt = xur.next
						cur.next = prev
						prev = cur
						cur = nxt
				return prev
				
		dummy = ListNode(0, head)
		groupPrev = dummy
		
		while True:
				# find kth node
				kth = groupPrev
				for _ in range(k):
						kth = kth.next
						if not kth:
								return dummy.next
				groupNext = kth.next
				# Reverse the group
				start = groupPrev.next
				newHead = rev(start, groupNext)
				# Reconnect
				groupPrev.next = newHead
				start.next = groupNext
				groupPrev = start
```

### Fast & Slow Pointers

#### find middle

```python
def findMiddle(head: ListNode) -> ListNode:
		slow, fast = head, head
		while fast and fast.next:
				slow = slow.next
				fast = fast.next.next
		return slow
```

#### cycle detection =

```python
def cycleDetection(head: ListNode) -> bool:
		slow, fast = head, head
		while fast and fast.next:
				slow = slow.next
				fast = fast.next.next
				if slow == fast:
						return True
		return False
```

### Merge

```python
def merge(l1, l2): # merge two sorted linked lists
		dummy = ListNode()
		cur = dummy
		while l1 and l2:
				if l1.val < l2.val:
						cur.next, l1 = l1, l1.next
				else:
						cur.next, l2 = l2, l2.next
				cur = cur.next
		cur.next = l1 or l2
		return dummy.next
```

### Split

```python
def split(head):
		slow, fast = head, head
		prev = None
		while fast and fast.next:
				prev, slow, fast = slow, slow.next, fast.next.next
		if prev:
				prev.next = None
		return head, slow
```

## Trees & Graphs

### Tree’s Queue  & BFS

```python
from collections import deque
def bfs(root, target):
		queue = deque()
		step = 0
		# initialize
		queue.append(root)
		# bfs
		while queue:
				size = len(queue)
				for _ in range(size):
						cur = queue.popleft()
						if cur == target:
								return step
						for nxt in cur.neighbors:
								queue.append(nxt)
				step += 1
		return -1 # no path from root to target
```

```python
from collections import deque
def bfs(root, target):
		queue = deque()
		visit = set()
		step = 0
		# initialize
		queue.append(root)
		visit.add(root)
		# bfs
		while queue:
				size = len(queue)
				for _ in range(size):
						cur = queue.popleft()
						if cur == target:
								return step
						for nxt in cur.neighbots:
								queue.append(nxt)
								visit.add(nxt)
				step += 1
		return -1 # no path from root to target
```

### Tree’s Stack & DFS

```python
def DFS(root, target):
    visited = set()
    stack = []

    visited.add(root)
    stack.append(root)

    while stack:
        cur = stack.pop()
        if cur == target:
            return True
        for nxt in cur.neighbors:
            if nxt not in visited:
                visited.add(nxt)
                stack.append(nxt)

    return False
```

### Pre-order Traversal

```python
def preorder(root):
		if not root:
				return []
		res, stack = [], [root]
		while stack:
				node = stack.pop()
				res.append(node.val)
				if node.right:
						stack.append(node.right)
				if node.left:
						stack.append(node.left)
		return res
```

### In-order Traversal

```python
def inorder(root):
		stack = []
		cur = root
		res = []
		while cur or stack:
				while cur:
						stack.append(cur)
						cur = cur.left
				cur = stack.pop()
				res.append(cur.val)
				cur = cur.right
		return res
```

### Post-order Traversal

```python
def postorder(root):
		if not root:
				return []
		res, stack1, stack2 = [], [root], []
		while stack1:
				node = stack1.pop()
				stack2.append(node)
				if node.left:
						stack1.append(node.left)
				if node.right:
						stack1.append(node.right)
		while stack2:
				res.append(stack2.pop().val)
		return res
```

### Lowest Common Ancestor ==

lowest (deepest) node in tree that has both p and q as descendants

```python
def lowestCommonAncestor(root, p, q): # binary tree recursive not BST
		if not root or root == p or root == q:
				return root
		left = lowestCommonAncestor(root.left, p, q)
		right = lowestCommonAncestor(root.right, p, q)
		if left and right:
				return root
		return left or right
```

```python
def lowestCommonAncestor(root, p, q): # binary tree iterative
		parent = {root: None}
		stack = [root]
		while p not in parent or q not in parent:
				node = stack.pop()
				if node.left:
						parent[node.left] = node
						stack.append(node.left)
				if node.right:
						parent[node.right] = node
						stack.append(node.right)
		ancestors = set()
		while p:
				ancestors.add(p)
				p = parent[p]
		while q not in ancestors:
				q = parent[q]
		return q
```

### Topological sort ====

#### DFS based Topological Sort =====

```python
def topo(numNodes, edges):
		graph = defaultdict(list)
		for u, v in edges:
				graph[u].append(v)
		visited = [0] * numNodes
		res = []
		def dfs(node):
				if visited[node] == 1:
						return False
				if visited[node] == 2:
						return True
				visited[node] = 1
				for nei in graph[node]:
						if not dfs(nei):
								return False
				visited[node] = 2
				res.append(node)
				return True
		for i in range(numNodes):
				if visited[i] == 0:
						if not dfs(i):
								return []
		return res[::-1]
```

#### BFS based Topological Sort - Kahn’s Algorithm =====

```python
def topoKahn(numNodes, edges):
		graph = defaultdict(list)
		indeg = [0] * numNodes
		for u, v in edges:
				graph[u].append(v)
				indeg[v] += 1
		q = deque([i for i in range(numNodes) if indeg[i] == 0])
		res = []
		while q:
				node = q.popleft()
				res.append(node)
				for nei in graph[node]:
						indeg[nei] -= 1
						if indeg[nei] == 0:
								q.append(nei)
```

### Shortest path - Dijkstra ====

```python
def dijkstra(n, edges, start):
		graph = defaultdict(list)
		for u, v, w in edges:
				graph[u].append((v, w))
		dist = [float('inf')] * n
		dist[start] = 0
		pq = [(0, start)]
		while pq:
				d, u = heapq.heappop(pq)
				if d > dist[u]:
						continue
				for v, w in graph[u]:
						if dist[u] + w < dist[v]:
								dist[v] == dist[u] + w
								heapq.heappush(pq, (dist[v], v))
		return dist
```

### Shortest path - Bellman-Ford ====

```python
def bellmanFord(n, edges, start):
		dist = [float('inf')] * n
		dist[start] = 0
		
		for _ in range(n - 1):
				updated = False
				for u, v, w in edges:
						if dist[u] != float('inf') and dist[u] + w < dist[v]:
								dist[v] = dist[u] + w
								updated = True
				if not updated:
						break
		for u, v, w in edges:
				if dist[u] != float('inf') and dist[u] + w < dist[v]:
						return None
		return dist
```

### Disjoint Set Union ==

Implementation with constructor, find, and union. using path compression and union by rank

```python
class UnionFind: # 有size的版本
		def __init__(self, size):
				self.root = [i for i in range(size)]
				self.rank = [1] * size
				self.count = size
		def find(self, x):
				if x == self.root[x]:
						return x
				self.root[x] = self.find(self.root[x])
				return self.root[x]
		
		def union(self, x, y):
				rootX = self.find(x)
				rootY = self.find(y)
				if rootX != rootY:
						if self.rank[rootX] < self.rank[rootY]:
								self.root[rootX] = rootY
						elif self.rank[rootX] > self.rank[rootY]:
								self.root[rootY] = rootX
						else:
								self.root[rootY] = rootX
								self.rank[rootX] += 1
						self.count -= 1
		def connected(self, x, y):
				return self.find(x) == self.find(y)
```

```python
class UnionFind: # 无size的版本
    def __init__(self):
        self.root = {}
        self.rank = {}
        self.count = 0

    def find(self, x):
        if x not in self.root:
            self.root[x] = x
            self.rank[x] = 1
            self.count += 1
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

```

### MST - Kruskal’s Algorithm ===

Unionfind + seleced min edge from all edge, use union find to check if new edge would form a loop

```python
# Class UnionFind ...###
def kruskal(n, edges): 
		uf = UnionFind(n)
		mstWeight = 0    # MST = Minumum Spanning Tree
		mstEdges = []
		edges.sort()
		for w, u, v in edges:
				if uf.union(u, v):
						mstWeight += w
						mstEdges.append((u, v, w))
				if len(mstEdges) == n - 1:
						break
		return mstWeight, mstEdges
```

### MST - Prim’s Algorithm =====

find all points directly connected to the current mst, put all edges connect those points to current mst, and use min heap to add the edge to mst

```python
def prim(graph, start = 0):
		n = len(graph)
		visited = [False] * n
		mstEdges = []
		totalCost = 0
		minHeap = [(0, -1, start)]
		while minHeap:
				weight, u, v = heapq.heappop(minHeap)
				if visited[v]:
						continue
				visited[v] = True
				totalCost += weight
				if u != -1:
						mstEdges.append((u, v, weight))
				for w, nei in graph[v]:
						if not visited[nei]:
								heapq.heappush(minHeap, (w, v, nei))
		return totalCost, mstEdges
```

### SPFA Algorithm =====

(bellman-ford + queue optimization)

```python
def spfa(n, edges, source = 0):
		INF = float('inf')
		dist = [INF] * n
		inQueue = [False] * n
		dist[source = 0
		queue = deque([source])
		inQueue[source] = True
		while queue:
				u = queue.popleft()
				inQueue[u] = False
				for v, w in edges[u]:
						if dist[u] + w < dist[v]:
								dist[v] = dist[u] + w
								if not inQueue[v]:
										queue.append(v)
										inQueue[v] = True
		return dist
```

## Binary Search

```python
def binarySearch(nums, target): # 闭区间的做法
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1
```

```python
def binarySearch(nums, target): # 左开右闭
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if nums[left] == target:
        return left
    return -1
```

```python
def binarySearch(nums, target): # 双开区间
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1
```

## Backtracking

回溯

```python
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            place(next_candidate)
            # 在新状态下递归，更深一层的解
            backtrack(next_candidate)
            # 回溯
            remove(next_candidate)
```

## Dynamic Programming —

DP思路-核心三要素

1. some function or array that represents the answer for the problem for a given state - 设计某个函数或数组，表示某个状态下的答案
2. transition between states - 状态之间的转移
3. base case - 基础情况（边界条件）

定义好每个状态的含义，找到他们之间的转移关系，并设置好初始状态。

### Linear DP

(note, do I really need to list those examples or can I just genrealize linear DP)

案例感觉有点重复，linear DP留一个应该就ok

#### House Robber =

```python
def houseRobber(nums):
		if not nums: return 0
		n = len(nums)
		if n == 1: return nums[0]
		dp = [0] * n
		dp[0] = nums[0]
		dp[1] = max(nums[0], nums[1])
		for i in range(2, n):
				dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
		return dp[-1]
```

#### Climbing Stairs =

```python
def climbStairs(n):
		if n <= 2: return n
		dp = [0] * (n + 1)
		dp[1], dp[2] = 1, 2
		for i in range(3, n + 1):
				dp[i] = dp[i - 1] + dp[i - 2]
		return dp[n]
```

#### Stock =

```python
def maxProfit(prices):
		minPrice, maxProfit = float('inf'), 0
		for p in prices:
				minPrice = min(minPrice, p)
				paxProfit = max(maxProfit, p - minPrice)
		return maxProfit
```

### Knapsack (0/1, complete, multi)  —

#### 0/1 Knapsack ==

```python
def knapsack01(weights, values, W):
		n = len(weights)
		dp = [0] * (W + 1)
		for i in range(n):
				for w in range(W, weights[i] - 1, -1):
						dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
		return dp[W]
```

#### Complete Knapsack ==

```python
def knapsackComplete(weights, values, W):
		n = len(weights)
		dp = [0] * (W + 1)
		for i in range(n):
				for w in range(weights[i], W + 1):
						dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
		return dp[W]
```

#### Multi Knapsack ==

```python
def knapsackMulti(weights, values, counts, W):
		items = []
		for i in range(len(weights)):
				c = counts[i]
				k = 1
				while k < c:
						items.append((weights[i] * k, values[i] * k))
						c -= k
						k *= 2
				if c > 0:
						items.append((weights[i] * c, values[i] * c))
		dp = [0] * (W + 1)
		for w, v in items:
				for j in range(W, w - 1, -1):
						dp[j] = max(dp[j], dp[j - w] + v)
		return dp[W]
```

### Interval DP - burst balloons ====

state depends on splitting intervals into sub-intervals

```python
def maxCoins(nums):
		nums = [1] + nums + [1]
		n = len(nums)
		dp = [[0] * n for _ in range(n)]
		for length in range(2, n):
				for left in range(0, n - length):
						right = left + length
						for k in range(left + 1, right):
								dp[left][rihgt] = max(dp[left][right], nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right])
		return dp[0][n - 1]
```

### Sequence DP

comparing two sequences or subsequences

#### Longest Increasing Subsequence (LIS) ====

```python
def lengthOfLIS(nums):
		dp = [1] * len(nums)
		for i in range(len(nums)):
				for j in range(i):
						if nums[j] < nums[i]:
								dp[i] = max(dp[i], dp[j] + 1)
		return max(dp)
```

#### Longest Common Subsequence (LCS) =====

```python
def lcs(text1, text2):
		m, n = len(text1), len(text2)
		dp = [[0] * (n + 1) for _ in range(m + 1)]
		for i in range(m):
				for j in range(n):
						if text1[i] == text2[j]:
								dp[i + 1][j + 1] = dp[i][j] + 1
						else:
								dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
		return dp[m][n]
```

#### Edit Distance =====

```python
def minDistance(word1, word2):
		m, n = len(word1), len(word2)
		dp = [[0] * (n + 1) for _ in range(m + 1)]
		for i in range(m + 1):
				dp[i][0] = i
		for j in range(n + 1):
				dp[0][j] = j
		for i in range(1, m + 1):
				for j in range(1, n + 1):
						if word1[i - 1] == word2[j - 1]:
								dp[i][j] = dp[i - 1][j - 1]
						else:
								dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
		return dp[m][n]
```

## Heaps/ Priority Queue —

## String Algorithms  —

### KMP (short template + failure array) ==

### Rabin-Karp Algorithm ==

```python
def rabin_karp(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    if len(needle) > len(haystack):
        return -1

    RADIX = 256  # You can also use 26 if only lowercase letters
    MOD = 10**9 + 7  # Large prime to avoid overflow

    m, n = len(needle), len(haystack)

    # Precompute RADIX^(m-1) % MOD for rolling hash
    max_weight = pow(RADIX, m - 1, MOD)

    # Helper to compute initial hash
    def compute_hash(s):
        h = 0
        for c in s:
            h = (h * RADIX + ord(c)) % MOD
        return h

    target_hash = compute_hash(needle)
    window_hash = compute_hash(haystack[:m])

    for i in range(n - m + 1):
        if i > 0:
            # Roll the hash: remove left char, add right char
            window_hash = (
                (window_hash - ord(haystack[i - 1]) * max_weight) * RADIX + ord(haystack[i + m - 1])
            ) % MOD
        # Check hash and confirm match to handle collisions
        if window_hash == target_hash and haystack[i:i + m] == needle:
            return i

    return -1

```

## Bit Manipulation

### Subset enumeration ==

```python
def subsetEnumeration(nums): # use bit mask return all possible subset
		n = len(nums)
		res = []
		for mask in range(1 << n):
				if mask & (1 << i):
						subset.append(nums[i])
				res.append(subset)
		return res
```

### Counting set bits

popcount, use lowbit to repeatedly remove the lowest set bit

```python
def countBits(x):
		cnt = 0
		while x:
				x -= x & -x
				cnt += 1
		return cnt
```

### Fenwick Tree (BIT) ====

Binary Indexed Tree

```python
class BIT:
		def __init__(self, n):
				self.bit = [0] * (n + 1)
		def update(self, i, delta):
				while i < len(self.bit):
						self.bit[i] += delta
						i ++ i & -i
		def query(self, i):
				s = 0
				while i > 0:
						s ++ self.bit[i]
						i -= i & -i
				return s
```

## Math

### Fast Power ===

binary exponentiation with mod

```python
def fastPow(base, exp, mod):
		res = 1
		base %= mod
		while exp > 0:
				if exp & 1:
						res = (res * base) % mod
				base = (base * base) % mode
				exp >>= 1
		return res
```

### Sive of Eratosthesnes ==

generate primes up to n

```python
def sieve(n): # cross out multiples when finding
		isPrime = [True] * (n + 1)
		isPrime[0] = isPrime[1] = False
		for i in range(2, int(n**0.5) + 1):
				if isPrime[i]:
						for j in range(i * i, n + 1, i):
								isPrime[j] = False
		return [i for i, prime in enumerate(isPrime) if prime]
```

### Extended Euclidean ====

for GCD & Bezout

```python
def extendedEuclidean(a, b):
		if b == 0:
				return (a, 1, 0)
		g, x1, y1 = extendedEuclidean(b, a % b)
		return (g, y1, x1 - (a // b) * y1)
```

### Fermat’s Little Theorem =====

modular inverse 

```python
def modinv(a, mod):
		# Fermat's theorem: a ^ (p - 2) is inverse of a (p is prime)
		return fastPow(a, mod - 2, mod)
```

### nCr Mod Prime =====

combinatorics

```python
MOD = 10**9 + 7
MAXN = 100000

fact = [1] * (MAXN + 1)
invfact = [1] * (MAXN + 1)

# factorial
for i in range(1, MAXN + 1):
    fact[i] = fact[i-1] * i % MOD

# modular inverse factorial
def modinv(a, mod): return pow(a, mod-2, mod)
invfact[MAXN] = modinv(fact[MAXN], MOD)
for i in range(MAXN-1, -1, -1):
    invfact[i] = invfact[i+1] * (i+1) % MOD

# Now nCr is O(1)
def nCr(n, r):
    if r < 0 or r > n: return 0
    return fact[n] * invfact[r] % MOD * invfact[n-r] % MOD
```

### Matrix Exponentiation

technique to calculate powers of a transition matrix quickly, solving linear recurrences (Fibonacci, Tribonacci, etc)

```python
def matMulti(A, B, mod = None):
		n = len(A)
		res = [[0] * n for _ in range(n)]
		for i in range(n):
				for j in range(n):
						for k in range(n):
								res[i][j] += A[i][k] * B[k][j]
								if mod:
										res[i][j] %= mod
		return res
		
def matPow(M, power, mod = None):
		n = len(M)
		res = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
		while power > 0:
				if power % 2 == 1:
						res = matMulti(res, M, mod)
				M = matMulti(M, M, mod)
				power //= 2
		return res
```

## Engineering Nodes —

### Code Style

#### Naming

Functions → snake_case

Classes → PascalCase

Constants → UPPER_SNAKE_CASE

#### Best Practives

Keep function short ( ≤ 30-40 lines ideally)

use type hints

use docstrings for functions

handle edge cases early

### Common pitfalls checklist

#### Mutable defaults

```python
def f(x, arr = []): ... # BAD
def f(x, arr = None):   # GOOD
		if arr is None: arr = []
```

#### Recursion depth errors

convert to iterative DP when depth  ~ 10 ^ 5

#### Shadowing built ins

Don’t name variables “list”, “dict”, “id”, etc

#### Test cases not enough

Always test: empty input, single element, max constraints

### Pytest Testing Usage

not applicable to leetcode

use fixtures, parametrized tests, and exception testing

## Interviews and Tools

### Interview Tips

Think out loud - explain reasoning step by step, even final code did not work, interviewer values clarity + approach

Start with Brute force - outline simple solution first, and then optimize

State invariants - mention what must stay true after each iteration or recursion

Edge case first - get edge case handled at the beginning of the function


## Git Repo Notes

things to add later:
Z-function/Manacher, segment tree