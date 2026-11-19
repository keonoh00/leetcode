# Choosing a technique

Before writing code, take about two minutes and say three things out loud:

1. **The constraints:** which algorithms are fast enough?
2. **The brute force:** what does it keep repeating?
3. **The clue in the wording:** which technique does it point to?

When a problem looks unfamiliar, start from Step 0, not Step 1. Writing out the rules
as comments is something you can always do first, so you never start from an empty
editor.

---

## Step 0: Rule problems (most of the Jobda test)

Most stages are rules to turn into code, not an algorithm to pick. Early stages have
small inputs, so the straightforward version passes. Only the scale stage needs
Steps 1–3.

1. Read the return value first. What type is it, in what order, and what comes back
   when nothing matches?
2. Write the rules as comments, one per line. Include the tie-breaks and edge rules
   ("if equal…", "if missing…").
3. Pick the data. Use a tuple or dict per record, a dict keyed by id, or a sorted
   list of events.
4. One function per rule. `solution` only parses, loops and calls them, so the next
   stage changes one function.
5. Work the first example by hand, and `print` your intermediate values to compare.
6. Try edge cases: empty input, one item, equal times, the boundary minute, the last
   day.
7. Only then think about n. If the efficiency tests fail, use Step 1.

```python
def solution(records):
    events = sorted(parse(r) for r in records)  # strings -> (time, id, kind); tuple order = tie-break
    state = {}                                  # id -> what the rules track
    for time, uid, kind in events:
        apply_rule(state, time, uid, kind)      # one rule = one function
    return build_answer(state)                  # exact output format and order
```

Python for parsing and simulation:

```python
# Time: "HH:MM" to minutes and back
h, m = map(int, "09:05".split(":"))
minutes = h * 60 + m
f"{minutes // 60:02d}:{minutes % 60:02d}"      # "09:05" again

# Dates, when every month has 28 days
y, mo, d = map(int, "2026.11.22".split("."))
days = y * 12 * 28 + (mo - 1) * 28 + d

# Dates, on a real calendar
from datetime import date, timedelta
(date(2026, 11, 22) - date(2026, 1, 1)).days   # days between them: 325
date(2026, 11, 22).weekday()                   # Monday = 0, so this Sunday is 6
date(2026, 11, 22) + timedelta(days=30)        # 30 days later

# Counting and grouping
from collections import Counter, defaultdict, deque
total = defaultdict(int)                       # total[key] += x
groups = defaultdict(list)                     # groups[key].append(x)

# Sorting rows of (name, score)
sorted(rows, key=lambda r: (-r[1], r[0]))      # score high to low, then name A to Z

# Rounding up, for positive ints
-(-a // b)                                     # a / b rounded up

# Every pair, order or combination
from itertools import combinations, permutations, product

# Counting in a sorted list
from bisect import bisect_left, bisect_right
bisect_right(a, x) - bisect_left(a, x)         # how many times x appears in a
```

---

## Step 1: How big is n?

Python does roughly 10⁷ simple steps per second. If n² is 10¹⁰, it won't pass.

Find your n on the left, rounding up: n ≤ 10⁴ uses the 10⁵ row. Everything further
down the table is faster, so it also works.

<table>
<tr><th>Constraint</th><th>Time</th><th>Algorithm</th></tr>
<tr><td>n ≤ 20</td><td>O(2ⁿ)</td><td>Backtracking: every subset or every order</td></tr>
<tr><td rowspan="5">n ≤ 10³</td><td rowspan="4">O(n²)</td><td>Two nested loops: every pair</td></tr>
<tr><td>Sort, then two pointers for each item: triplets (3Sum)</td></tr>
<tr><td>DP that looks back at every j &lt; i: longest increasing subsequence, Word Break</td></tr>
<tr><td>DP on two strings: common subsequence, edit distance</td></tr>
<tr><td>O(n × amount)</td><td>DP over every amount: Coin Change, a subset that adds up to a target</td></tr>
<tr><td rowspan="17">n ≤ 10⁵</td><td rowspan="3">O(n log n)</td><td>Sort first</td></tr>
<tr><td>Intervals: sort by start, then merge</td></tr>
<tr><td>Graph with edge costs: Dijkstra with a heap</td></tr>
<tr><td>O(n log k)</td><td>Heap of size k: the k largest, smallest or closest</td></tr>
<tr><td>O(n log m)</td><td>Binary search on the answer: the smallest X that works (Koko)</td></tr>
<tr><td rowspan="10">O(n)</td><td>Hash map or set: seen before, counting, grouping</td></tr>
<tr><td>Running total + hash map: a subarray whose sum is k</td></tr>
<tr><td>Two pointers: a pair in a sorted array, palindromes</td></tr>
<tr><td>Sliding window: the longest or shortest substring or subarray</td></tr>
<tr><td>Stack: the next greater item, matching brackets</td></tr>
<tr><td>DP with one loop: the number of ways, the best total</td></tr>
<tr><td>Linked list: dummy node, slow and fast pointers, reverse in place</td></tr>
<tr><td>Binary tree: DFS recursion, or BFS for level by level</td></tr>
<tr><td>Grid: DFS to count regions, BFS for the fewest steps, DP to count paths</td></tr>
<tr><td>Graph: DFS or BFS on an adjacency list, topological sort for prerequisites</td></tr>
<tr><td>O(log n)</td><td>Binary search: find a target in a sorted array</td></tr>
<tr><td>O(1) per call</td><td>Design: hash map + linked list (LRU Cache), Min Stack</td></tr>
</table>

n is the length of the input; for a grid it's rows × cols, and for a graph it's nodes
+ edges. k is the k in the question, and m is the largest value.

---

## Step 2: What does the brute force repeat?

Say the brute force first. Then ask what work it keeps doing again. The technique is
whatever removes that repeat.

| Problem | Brute force | Better |
|---|---|---|
| 3Sum | checks every triplet, O(n³) | sort, then two pointers: one sum rules out a whole row, O(n²) |
| Longest Substring | restarts from every letter | sliding window: keep the window, drop from the front, O(n) |
| Koko Eating Bananas | tries speeds 1, 2, 3, … | binary search: "too slow" rules out every slower speed too |

---

## Step 3: Which technique does the wording point to?

### Two pointers
- **Clue:** a sorted array; a pair or triplet that adds up to a target
- **How:** start at both ends. If the sum is too small, move the left pointer right.
  If it's too big, move the right pointer left.
- **Done:** Two Sum II, 3Sum, Container With Most Water

```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1
        else:
            right -= 1
    return []
```

### Hash map or set
- **Clue:** "seen this before?", counting, grouping
- **How:** store what you've seen, so each lookup is O(1)
- **Done:** Contains Duplicate, Group Anagrams, Top K Frequent Elements

```python
def has_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

### Running total + hash map
- **Clue:** a contiguous subarray whose sum is k
- **How:** the sum from i to j is the total at j minus the total before i, so look up
  `total - k` in the map
- **Done:** Subarray Sum Equals K

```python
def subarray_sum(nums, k):
    count = total = 0
    seen = {0: 1}  # running total -> how many times we've had it
    for num in nums:
        total += num
        count += seen.get(total - k, 0)
        seen[total] = seen.get(total, 0) + 1
    return count
```

### Sliding window
- **Clue:** the longest or shortest *contiguous* substring or subarray that follows
  a rule
- **How:** grow the right end. When the rule breaks, shrink from the left until it
  holds again.
- **Done:** Longest Substring Without Repeating Characters, Best Time to Buy and Sell
  Stock

```python
def longest_unique(s):
    window = set()
    left = best = 0
    for right, ch in enumerate(s):
        while ch in window:  # rule broken: shrink from the left
            window.remove(s[left])
            left += 1
        window.add(ch)
        best = max(best, right - left + 1)
    return best
```

### Binary search
- **Clue:** sorted input, or "the smallest X that works" where checking one X is easy
- **How:** check the middle and throw away the half that can't hold the answer
- **Done:** Find Minimum in Rotated Sorted Array, Search a 2D Matrix, Koko Eating
  Bananas

Find a target in a sorted list:

```python
def search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

Find the smallest X that works, as in Koko:

```python
def smallest_that_works(low, high, works):
    while low < high:
        mid = (low + high) // 2  # round down
        if works(mid):
            high = mid  # mid might be the answer, so keep it
        else:
            low = mid + 1
    return low
```

Keep the pairs together: `high = mid - 1` goes with `while low <= high`, and
`high = mid` goes with `while low < high` and rounding down.

### Stack
- **Clue:** the next greater or warmer item; matching brackets
- **How:** keep the items still waiting for an answer, and pop each one when its
  answer arrives
- **Done:** Daily Temperatures, Valid Parentheses

```python
def daily_temps(temps):
    answer = [0] * len(temps)
    stack = []  # indices still waiting for a warmer day
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
```

### Heap
- **Clue:** the k largest, smallest or closest
- **How:** keep a heap of size k (`heapq` is a min-heap)
- **Done:** Kth Largest Element in an Array, K Closest Points to Origin

```python
import heapq

def kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # drop the smallest
    return heap[0]
```

### DFS or BFS
- **Clue:** regions in a grid, something spreading, the fewest steps
- **How:** visit a cell, mark it, then visit its neighbours. Use BFS (a queue) when
  you need the fewest steps.
- **Done:** Number of Islands, Rotting Oranges

DFS, which counts islands:

```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"  # mark as visited
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                dfs(r, c)
                count += 1
    return count
```

BFS, which finds the fewest steps. Replace `neighbours(node)` with the problem's own
moves:

```python
from collections import deque

def bfs_steps(start, goal):
    queue = deque([start])
    seen = {start}
    steps = 0
    while queue:
        for _ in range(len(queue)):  # everything at this distance
            node = queue.popleft()
            if node == goal:
                return steps
            for nxt in neighbours(node):
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        steps += 1
    return -1
```

### Dijkstra
- **Clue:** the shortest path in a graph whose edges have costs
- **How:** pop the closest node from a heap, then try each of its edges

```python
import heapq
from collections import defaultdict
from math import inf

def dijkstra(edges, start):
    graph = defaultdict(list)
    for u, v, cost in edges:
        graph[u].append((v, cost))
        graph[v].append((u, cost))        # drop this line if one-way
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist.get(u, inf):
            continue                      # an old, longer entry
        for v, cost in graph[u]:
            if d + cost < dist.get(v, inf):
                dist[v] = d + cost
                heapq.heappush(heap, (d + cost, v))
    return dist
```

### Tree recursion
- **Clue:** any binary tree
- **How:** solve for the left and right subtrees, then combine them. For level by
  level, use the BFS template above.
- **Done:** Validate Binary Search Tree, Binary Tree Level Order Traversal

```python
def max_depth(node):
    if not node:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))
```

### Backtracking
- **Clue:** every subset or every order, with n ≤ 20
- **How:** add a choice, recurse, then undo it and try the next choice

Every subset that adds up to a target, with positive numbers:

```python
def subsets_with_sum(nums, target):
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
        for i in range(start, len(nums)):
            if total + nums[i] > target:
                continue                  # too big: skip this number
            path.append(nums[i])
            backtrack(i + 1, path, total + nums[i])
            path.pop()                    # undo, then try the next choice

    backtrack(0, [], 0)
    return result
```

### Sort, then merge
- **Clue:** overlapping intervals
- **How:** sort by start. If the next interval starts before the current one ends,
  merge them.
- **Done:** Merge Intervals

```python
def merge(intervals):
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:  # overlaps the last one
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

### Dynamic programming
- **Clue:** the number of ways; the fewest, most or best total; "can you make X?";
  each choice depends on earlier ones
- **How:** answer four questions before coding:
  1. What does `dp[i]` mean? Say it in words, like "the number of ways to reach
     step i".
  2. How is `dp[i]` built from smaller answers? Look at the last choice made.
  3. What are the base cases, like `dp[0]`?
  4. Where is the answer: `dp[n]`, or `max(dp)`?
- **Done:** Climbing Stairs, House Robber

| Pattern | Clue | `dp[i]` means | Built from |
|---|---|---|---|
| One line | steps, houses in a row | the answer for the first i items | `dp[i - 1]` and `dp[i - 2]` |
| Ends at i | longest increasing subsequence | the best that ends exactly at i | every `dp[j]` with j < i |
| Split a string | can s be split into words? | `s[:i]` can be split | `dp[j]` where `s[j:i]` is a word |
| Make an amount | coins, as many of each as you like | the fewest coins that make amount a | `dp[a - coin]` for each coin |
| Use each once | a subset that adds up to a target | some numbers add up to s | `dp[s - num]`, with s going down |
| Grid | paths through a grid | the answer at cell (r, c) | the cell above and the cell to the left |
| Two strings | common subsequence, edit distance | the answer for `a[:i]` and `b[:j]` | `dp[i - 1][j - 1]`, `dp[i - 1][j]`, `dp[i][j - 1]` |

One line, as a table (Climbing Stairs):

```python
def climb_stairs(n):
    dp = [0] * (n + 1)  # dp[i] = ways to reach step i
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # last move was 1 step, or 2 steps
    return dp[n]
```

The same, top-down: write the plain recursion, then add `@cache` so each `i` is
worked out only once. Python stops recursion about 1,000 calls deep, so for a bigger n
use the table.

```python
from functools import cache

def climb_stairs(n):
    @cache
    def ways(i):  # ways to reach step i
        if i <= 1:
            return 1
        return ways(i - 1) + ways(i - 2)

    return ways(n)
```

One line, with two variables instead of a list (House Robber):

```python
def rob(nums):
    prev2 = prev1 = 0  # best up to i - 2, best up to i - 1
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)  # skip it, or take it
    return prev1
```

Ends at i (Longest Increasing Subsequence):

```python
def length_of_lis(nums):
    dp = [1] * len(nums)  # dp[i] = longest increasing subsequence that ends at i
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:  # nums[i] can go after nums[j]
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

Split a string (Word Break):

```python
def word_break(s, word_dict):
    words = set(word_dict)
    dp = [True] + [False] * len(s)  # dp[i] = s[:i] can be split into words
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:  # s[:j] splits, and s[j:i] is a word
                dp[i] = True
                break
    return dp[-1]
```

Make an amount (Coin Change):

```python
from math import inf

def coin_change(coins, amount):
    dp = [0] + [inf] * amount  # dp[a] = fewest coins that make a
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)  # the last coin was `coin`
    return dp[amount] if dp[amount] != inf else -1
```

Use each once (Partition Equal Subset Sum). Going down means `dp[s - num]` still
holds the answer from before this number, so it isn't used twice:

```python
def can_partition(nums):
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [True] + [False] * target  # dp[s] = some numbers so far add up to s
    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]  # without num, or with it
    return dp[target]
```

Grid (Unique Paths):

```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]  # dp[r][c] = paths to (r, c); edges have 1
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]  # came from above, or from the left
    return dp[-1][-1]
```

Two strings (Longest Common Subsequence). Row 0 and column 0 stand for an empty
string, so they stay 0:

```python
def longest_common_subsequence(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]  # dp[i][j] = answer for a[:i], b[:j]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # last letters match: keep both
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # drop a letter from a, or from b
    return dp[-1][-1]
```

### Linked list tricks
- **Clue:** any linked list
- **How:** a dummy node saves special cases for the head. For slow and fast pointers,
  fast moves 2 steps and slow moves 1.
- **Done:** Linked List Cycle, Remove Nth Node From End of List

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```
