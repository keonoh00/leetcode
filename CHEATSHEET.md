# 기법 고르기

코드를 쓰기 전에 2분 정도, 세 가지를 소리 내어 말한다.

1. **Constraints:** 어떤 알고리즘이면 충분히 빠른가?
2. **Brute Force:** 무엇을 계속 반복하는가?
3. **문제의 단서:** 어떤 기법을 가리키는가?

처음 보는 문제 같으면 1단계가 아니라 0단계부터 시작한다. 규칙을 주석으로 적는 일은
언제든 먼저 할 수 있으니, 빈 화면에서 시작할 일이 없다.

---

## 0단계: 규칙 문제 (잡다 테스트 대부분)

대부분의 단계는 알고리즘을 고르는 문제가 아니라 규칙을 코드로 옮기는 문제다. 앞
단계는 입력이 작아서 단순하게 짜도 통과한다. 1–3단계가 필요한 것은 규모를 키우는
단계뿐이다.

1. 반환값부터 읽는다. 무슨 type인지, 어떤 순서인지, 맞는 것이 없으면 무엇을
   반환하는지.
2. 규칙을 한 줄에 하나씩 주석으로 적는다. Tie-break와 예외 규칙("같으면…",
   "없으면…")도 적는다.
3. 데이터 모양을 정한다. 기록마다 tuple이나 dict, id를 key로 하는 dict, 또는 정렬된
   event list.
4. 규칙 하나에 함수 하나. `solution`은 parse하고, 반복하고, 함수를 부르기만 한다.
   그러면 다음 단계에서 규칙이 바뀌어도 함수 하나만 고친다.
5. 첫 번째 예제를 손으로 풀고, 중간 값을 `print`해서 비교한다.
6. Edge case를 넣어 본다: 빈 입력, 하나뿐인 입력, 같은 시각, 경계가 되는 분, 마지막
   날.
7. 그다음에야 n을 생각한다. 효율성 테스트에서 떨어지면 1단계로 간다.

**출입 기록 (예시 문제)**

`records`는 출입 기록 문자열의 list다. 각 기록은 `"HH:MM 이름 IN"`(들어옴) 또는
`"HH:MM 이름 OUT"`(나감) 꼴이고, 시각 순서대로 주어지지 않을 수도 있다. 모든 사람은
들어온 뒤에 나가고, 마지막에는 모두 나가 있다. 사람마다 안에 있던 시간(분)을 모두
더해, `[이름, 분]` list를 이름 오름차순으로 반환한다.

- `["09:00 kim IN", "09:10 lee IN", "09:40 kim OUT", "10:00 lee OUT"]` →
  `[["kim", 40], ["lee", 50]]`. kim은 09:00–09:40으로 40분, lee는 09:10–10:00으로
  50분이다.
- `["10:00 kim OUT", "09:00 kim IN", "11:00 kim IN", "11:30 kim OUT"]` →
  `[["kim", 90]]`. 시각 순으로 정렬하면 09:00–10:00(60분)과 11:00–11:30(30분)이다.

```python
from collections import defaultdict

# 규칙 1: IN이면 들어온 시각을 적어 둔다
# 규칙 2: OUT이면 (나간 시각 - 들어온 시각)을 그 사람의 합계에 더한다
# 반환: [이름, 합계 분] list, 이름 A→Z

def parse(record):                     # "09:40 kim OUT" -> (580, "kim", "OUT")
    clock, name, kind = record.split()
    h, m = map(int, clock.split(":"))
    return h * 60 + m, name, kind

def enter(inside, time, name):         # 규칙 1
    inside[name] = time

def leave(inside, total, time, name):  # 규칙 2
    total[name] += time - inside.pop(name)

def solution(records):
    events = sorted(parse(r) for r in records)  # 시각 순; 같으면 tuple의 다음 값 순
    inside = {}                        # 이름 -> 들어온 시각
    total = defaultdict(int)           # 이름 -> 합계 분
    for time, name, kind in events:
        if kind == "IN":
            enter(inside, time, name)
        else:
            leave(inside, total, time, name)
    return sorted([name, minutes] for name, minutes in total.items())
```

Parse와 simulation에 쓰는 파이썬:

```python
# 시각: "HH:MM" -> 분, 그리고 다시 "HH:MM"
h, m = map(int, "09:05".split(":"))
minutes = h * 60 + m
f"{minutes // 60:02d}:{minutes % 60:02d}"      # 다시 "09:05"

# 날짜, 한 달이 모두 28일일 때
y, mo, d = map(int, "2026.11.22".split("."))
days = y * 12 * 28 + (mo - 1) * 28 + d

# 날짜, 실제 달력
from datetime import date, timedelta
(date(2026, 11, 22) - date(2026, 1, 1)).days   # 두 날짜 사이의 일수: 325
date(2026, 11, 22).weekday()                   # 월요일 = 0, 이날은 일요일이라 6
date(2026, 11, 22) + timedelta(days=30)        # 30일 뒤

# 개수 세기와 grouping
from collections import Counter, defaultdict, deque
total = defaultdict(int)                       # total[key] += x
groups = defaultdict(list)                     # groups[key].append(x)

# (이름, 점수) row 정렬
sorted(rows, key=lambda r: (-r[1], r[0]))      # 점수 높은 순, 같으면 이름 A→Z

# 올림 나눗셈, 양의 정수일 때
-(-a // b)                                     # a / b를 올림

# 모든 쌍, 순서, 조합
from itertools import combinations, permutations, product

# 정렬된 list에서 개수 세기
from bisect import bisect_left, bisect_right
bisect_right(a, x) - bisect_left(a, x)         # a에 x가 몇 개 있나
```

---

## 1단계: n은 얼마나 큰가?

파이썬은 1초에 간단한 연산을 약 10⁷번 한다. n²이 10¹⁰이면 통과하지 못한다.

왼쪽에서 내 n을 찾되, 올려서 찾는다: n ≤ 10⁴이면 10⁵ 줄을 본다. 표에서 더 아래에
있는 것은 더 빠르니 그것도 된다.

<table>
<tr><th>Constraint</th><th>Time</th><th>Algorithm</th></tr>
<tr><td>n ≤ 20</td><td>O(2ⁿ)</td><td>Backtracking: 모든 subset, 모든 순서</td></tr>
<tr><td rowspan="5">n ≤ 10³</td><td rowspan="4">O(n²)</td><td>Nested loop: 모든 쌍</td></tr>
<tr><td>Sort한 뒤 수마다 Two Pointers: 세 수의 합 (3Sum)</td></tr>
<tr><td>앞의 모든 j &lt; i를 보는 DP: LIS, Word Break</td></tr>
<tr><td>두 문자열 DP: LCS, Edit Distance</td></tr>
<tr><td>O(n × amount)</td><td>합마다 보는 DP: 합을 만드는 방법 수, 합이 target인 subset</td></tr>
<tr><td rowspan="17">n ≤ 10⁵</td><td rowspan="3">O(n log n)</td><td>먼저 Sort</td></tr>
<tr><td>Interval: start로 sort한 뒤 merge</td></tr>
<tr><td>Edge에 cost가 있는 Graph: Heap으로 Dijkstra</td></tr>
<tr><td>O(n log k)</td><td>크기 k인 Heap: 가장 큰, 작은, 가까운 k개</td></tr>
<tr><td>O(n log m)</td><td>답을 Binary Search: 조건을 만족하는 가장 작은 X (Koko)</td></tr>
<tr><td rowspan="10">O(n)</td><td>Hash Map, Set: 본 적 있나, 개수 세기, grouping</td></tr>
<tr><td>Prefix Sum + Hash Map: 합이 k인 subarray</td></tr>
<tr><td>Two Pointers: 정렬된 배열의 쌍, palindrome</td></tr>
<tr><td>Sliding Window: 가장 긴/짧은 substring, subarray</td></tr>
<tr><td>Stack: 다음으로 큰 값, 괄호 짝</td></tr>
<tr><td>for문 하나 DP: 방법의 수, 최고 합계</td></tr>
<tr><td>Linked List: dummy node, slow/fast pointer, in-place reverse</td></tr>
<tr><td>Binary Tree: DFS recursion, level별로는 BFS</td></tr>
<tr><td>Grid: 영역 세기는 DFS, 최소 이동은 BFS, 경로 수는 DP</td></tr>
<tr><td>Graph: adjacency list로 DFS나 BFS, 선수 과목은 Topological Sort</td></tr>
<tr><td>O(log n)</td><td>Binary Search: 정렬된 배열에서 값 찾기</td></tr>
<tr><td>호출마다 O(1)</td><td>Design: Hash Map + Linked List (LRU Cache), Min Stack</td></tr>
</table>

n은 입력의 길이다. Grid면 행 × 열, Graph면 node 수 + edge 수다. k는 문제에 나오는
k, m은 가장 큰 값이다. LIS는 Longest Increasing Subsequence, LCS는 Longest Common
Subsequence다.

---

## 2단계: Brute Force는 무엇을 반복하나?

Brute Force를 먼저 말한다. 그다음 무슨 일을 계속 다시 하는지 묻는다. 그 반복을
없애는 것이 쓸 기법이다.

| 문제 | Brute Force | 더 나은 방법 |
|---|---|---|
| Two Sum | 모든 쌍을 확인한다, O(n²) | Hash Map: 본 수를 저장해 두고 `target - num`을 바로 찾는다, O(n) |
| Maximum Average Subarray I | 구간마다 k개를 처음부터 다시 더한다, O(n × k) | Sliding Window: 새 수를 더하고 빠지는 수를 뺀다, O(n) |
| Binary Search | 앞에서부터 하나씩 확인한다, O(n) | Binary Search: 가운데를 보고 답이 없는 절반을 버린다, O(log n) |

---

## 3단계: 문제의 단서는 어떤 기법을 가리키나?

### Two Pointers
- **단서:** palindrome; 정렬된 배열에서 합이 target인 쌍이나 세 수
- **방법:** 양 끝에서 시작해 가운데로 좁혀 온다. 합을 찾을 때는 합이 작으면 left를
  오른쪽으로, 크면 right를 왼쪽으로 옮긴다.
- **풀어 본 문제:** Two Sum II, 3Sum, Container With Most Water

**Valid Palindrome (125, Easy)**

문자열 `s`가 주어진다. 대문자는 소문자로 바꾸고, 글자와 숫자가 아닌 문자(공백,
쉼표 등)는 모두 지운다. 그렇게 만든 문자열이 앞에서 읽어도 뒤에서 읽어도 같으면
`True`, 아니면 `False`를 반환한다.

- `s = "A man, a plan, a canal: Panama"` → `True`. 지우고 나면
  `"amanaplanacanalpanama"`라서 palindrome이다.
- `s = "race a car"` → `False`. `"raceacar"`를 뒤집으면 `"racaecar"`다.

```python
def is_palindrome(s):
    chars = [ch.lower() for ch in s if ch.isalnum()]  # 글자와 숫자만, 소문자로
    left, right = 0, len(chars) - 1
    while left < right:
        if chars[left] != chars[right]:
            return False
        left += 1
        right -= 1
    return True
```

### Hash Map, Set
- **단서:** "전에 본 적 있나?", 개수 세기, grouping
- **방법:** 본 것을 저장해 두면 찾을 때마다 O(1)
- **풀어 본 문제:** Contains Duplicate, Group Anagrams, Top K Frequent Elements

**Contains Duplicate (217, Easy)**

정수 배열 `nums`가 주어진다. 어떤 값이 두 번 이상 나오면 `True`, 모든 값이 서로
다르면 `False`를 반환한다.

- `nums = [1, 2, 3, 1]` → `True`. 1이 두 번 나온다.
- `nums = [1, 2, 3, 4]` → `False`.

```python
def has_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

### Prefix Sum + Hash Map
- **단서:** 합이 k인 subarray (연속된 부분 배열)
- **방법:** i부터 j까지의 합은 (j까지의 prefix sum) - (i 앞까지의 prefix sum)이다.
  그래서 `total - k`를 Hash Map에서 찾는다.
- **풀어 본 문제:** Subarray Sum Equals K

**Subarray Sum Equals K (560, Medium)**

정수 배열 `nums`와 정수 `k`가 주어진다. 합이 `k`인 subarray의 개수를 반환한다.
`nums`에는 음수도 있을 수 있다.

- `nums = [1, 1, 1], k = 2` → `2`. `[1, 1]`이 index 0–1과 1–2, 두 번 있다.
- `nums = [1, 2, 3], k = 3` → `2`. `[1, 2]`와 `[3]`이다.

```python
def subarray_sum(nums, k):
    count = total = 0
    seen = {0: 1}  # prefix sum -> 지금까지 나온 횟수
    for num in nums:
        total += num
        count += seen.get(total - k, 0)  # 앞에 total - k가 있었으면, 그 뒤부터 여기까지 합이 k
        seen[total] = seen.get(total, 0) + 1
    return count
```

### Sliding Window
- **단서:** substring이나 subarray: 길이가 k인 것, 또는 규칙을 지키는 가장 긴/짧은 것
- **방법:** 오른쪽에 하나를 넣고 왼쪽에서 하나를 뺀다. 구간을 매번 처음부터 다시
  계산하지 않는다. 길이가 정해져 있지 않으면, 규칙이 깨졌을 때만 왼쪽을 줄인다.
- **풀어 본 문제:** Longest Substring Without Repeating Characters, Best Time to Buy
  and Sell Stock

**Maximum Average Subarray I (643, Easy)**

정수 배열 `nums`와 정수 `k`가 주어진다. 길이가 정확히 `k`인 subarray 중 평균이 가장
큰 것의 평균을 반환한다.

- `nums = [1, 12, -5, -6, 50, 3], k = 4` → `12.75`. `[12, -5, -6, 50]`의 합 51을 4로
  나눈 값이다.
- `nums = [5], k = 1` → `5.0`.

```python
def find_max_average(nums, k):
    total = sum(nums[:k])  # 첫 window
    best = total
    for right in range(k, len(nums)):
        total += nums[right] - nums[right - k]  # 새 수를 더하고, 빠지는 수를 뺀다
        best = max(best, total)
    return best / k
```

### Binary Search
- **단서:** 정렬된 입력, 또는 "조건을 만족하는 가장 작은 X" (X 하나를 확인하기는 쉬울
  때)
- **방법:** 가운데를 확인하고, 답이 있을 수 없는 절반을 버린다
- **풀어 본 문제:** Find Minimum in Rotated Sorted Array, Search a 2D Matrix, Koko
  Eating Bananas

정렬된 배열에서 값 찾기:

**Binary Search (704, Easy)**

오름차순으로 정렬된 정수 배열 `nums`(값은 모두 다름)와 `target`이 주어진다.
`target`이 있으면 그 index를, 없으면 `-1`을 반환한다. O(log n)으로 풀어야 한다.

- `nums = [-1, 0, 3, 5, 9, 12], target = 9` → `4`.
- `nums = [-1, 0, 3, 5, 9, 12], target = 2` → `-1`.

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

조건을 만족하는 가장 작은 X 찾기:

**First Bad Version (278, Easy)**

버전 `1, 2, …, n`이 있다. 어느 버전부터 불량이 생겼고, 불량 버전 뒤의 버전은 모두
불량이다. 버전 하나가 불량인지는 LeetCode가 주는 `is_bad_version(v)`(LeetCode에서는
`isBadVersion`)로 확인한다. 이 함수를 되도록 적게 불러서, 처음으로 불량인 버전을
반환한다.

- `n = 5`, 처음 불량이 4일 때 → `4`. `is_bad_version(3)`은 `False`,
  `is_bad_version(4)`와 `is_bad_version(5)`는 `True`다.
- `n = 1`, 처음 불량이 1일 때 → `1`.

```python
def first_bad_version(n):
    low, high = 1, n
    while low < high:
        mid = (low + high) // 2  # 내림
        if is_bad_version(mid):
            high = mid  # mid가 답일 수도 있으니 남긴다
        else:
            low = mid + 1
    return low
```

짝을 맞춘다: `high = mid - 1`은 `while low <= high`와 함께, `high = mid`는
`while low < high`와 내림과 함께 쓴다.

### Stack
- **단서:** 괄호 짝; 다음으로 큰 값
- **방법:** 아직 짝(답)을 기다리는 것을 쌓아 두고, 짝이 오면 pop한다
- **풀어 본 문제:** Daily Temperatures, Valid Parentheses

**Valid Parentheses (20, Easy)**

`(`, `)`, `[`, `]`, `{`, `}`로만 된 문자열 `s`가 주어진다. 모든 여는 괄호가 같은
종류의 닫는 괄호로, 올바른 순서로 닫히면 `True`를 반환한다. 닫는 괄호마다 짝이 되는
여는 괄호가 있어야 한다.

- `s = "()[]{}"` → `True`.
- `s = "([])"` → `True`. 안쪽 `[]`가 먼저 닫히고, 그다음 `()`가 닫힌다.
- `s = "([)]"` → `False`. `[`가 마지막에 열렸는데 `)`가 먼저 왔다.

```python
def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}  # 닫는 괄호 -> 여는 괄호
    stack = []  # 아직 짝을 기다리는 여는 괄호
    for ch in s:
        if ch not in pairs:
            stack.append(ch)  # 여는 괄호: push
        elif not stack or stack.pop() != pairs[ch]:
            return False  # 기다리는 괄호가 없거나, 짝이 틀렸다
    return not stack  # 짝을 못 찾은 여는 괄호가 없어야 한다
```

### Heap
- **단서:** 가장 큰, 작은, 가까운 k개
- **방법:** 크기를 k로 유지하는 Heap (`heapq`는 Min Heap)
- **풀어 본 문제:** Kth Largest Element in an Array, K Closest Points to Origin

**Kth Largest Element in a Stream (703, Easy)**

`KthLargest(k, nums)` class를 만든다. 처음에는 `nums`의 수로 시작한다. `add(val)`이
불릴 때마다 `val`을 넣고, 지금까지 들어온 모든 수 중 k번째로 큰 수를 반환한다. 같은
수도 따로 센다.

- `k = 3, nums = [4, 5, 8, 2]`에서 `add(3)` → `4`. 수는 2, 3, 4, 5, 8이고, 큰 순서로
  8, 5, 4다.
- 이어서 `add(5)` → `5` (8, 5, 5), `add(10)` → `5` (10, 8, 5), `add(9)` → `8`
  (10, 9, 8), `add(4)` → `8`.

```python
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []  # 지금까지 가장 큰 k개
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)  # 가장 작은 것을 버린다
        return self.heap[0]  # 큰 k개 중 가장 작은 것 = k번째로 큰 수
```

### DFS, BFS
- **단서:** Grid의 영역, 퍼져 나가는 것, 최소 이동 횟수
- **방법:** 칸을 방문하면 표시하고, 이웃 칸을 방문한다. 최소 이동 횟수가 필요하면
  BFS(queue)를 쓴다.
- **풀어 본 문제:** Number of Islands, Rotting Oranges

DFS:

**Flood Fill (733, Easy)**

2D grid `image`의 각 칸에는 색을 뜻하는 정수가 있다. 시작 칸 `(sr, sc)`와 새 색
`color`가 주어진다. 시작 칸, 그리고 시작 칸과 상하좌우로 이어진 같은 색의 칸을 모두
`color`로 바꾼 `image`를 반환한다. 그림판의 페인트 통 도구와 같다.

- `image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, color = 2` →
  `[[2, 2, 2], [2, 2, 0], [2, 0, 1]]`. 오른쪽 아래의 `1`은 `0`에 막혀 시작 칸과
  이어지지 않으니 그대로다.
- `image = [[0, 0, 0], [0, 0, 0]], sr = 0, sc = 0, color = 0` → 그대로. 이미 그 색이다.

```python
def flood_fill(image, sr, sc, color):
    rows, cols = len(image), len(image[0])
    old = image[sr][sc]
    if old == color:
        return image  # 이미 그 색: 칠해도 표시가 안 되니 끝없이 돈다

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != old:
            return
        image[r][c] = color  # 칠하는 것이 곧 방문 표시
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)

    dfs(sr, sc)
    return image
```

BFS:

**미로 최단 거리 (예시 문제)**

문자열 list `grid`가 주어진다. `"."`은 지나갈 수 있는 칸, `"#"`은 벽이다. 왼쪽 위
`(0, 0)`에서 시작해 상하좌우로 한 칸씩 움직일 때, 오른쪽 아래 칸까지 가는 가장 적은
이동 횟수를 반환한다. 갈 수 없으면 `-1`. 시작 칸은 항상 `"."`이다.

- `grid = ["..#", "#..", "#.."]` → `4`. (0, 0) → (0, 1) → (1, 1) → (1, 2) → (2, 2).
- `grid = [".#", "#."]` → `-1`. 벽에 막혀 못 간다.

```python
from collections import deque

def fewest_moves(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(0, 0)])
    seen = {(0, 0)}
    steps = 0
    while queue:
        for _ in range(len(queue)):  # 지금 거리에 있는 칸 전부
            r, c = queue.popleft()
            if (r, c) == (rows - 1, cols - 1):
                return steps
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue  # grid 밖
                if grid[nr][nc] == "#" or (nr, nc) in seen:
                    continue  # 벽이거나, 이미 넣은 칸
                seen.add((nr, nc))
                queue.append((nr, nc))
        steps += 1
    return -1
```

### Dijkstra
- **단서:** edge에 cost가 있는 Graph의 최단 경로
- **방법:** Heap에서 가장 가까운 node를 꺼내고, 그 node의 edge를 하나씩 시도한다

**Network Delay Time (743, Medium)**

Node는 `1`부터 `n`까지다. `times[i] = [u, v, w]`는 node `u`에서 `v`로 신호가 가는 데
`w`가 걸린다는 뜻이다 (한 방향 edge). Node `k`에서 신호를 보냈을 때, 모든 node가
신호를 받는 데 걸리는 최소 시간을 반환한다. 받지 못하는 node가 있으면 `-1`.

- `times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], n = 4, k = 2` → `2`. Node 1과 3은 시간
  1에, node 4는 2 → 3 → 4로 시간 2에 받는다.
- `times = [[1, 2, 1]], n = 2, k = 2` → `-1`. 2에서 1로 가는 edge가 없다.

```python
import heapq
from collections import defaultdict
from math import inf

def network_delay_time(times, n, k):
    graph = defaultdict(list)
    for u, v, cost in times:
        graph[u].append((v, cost))  # 양방향이면 graph[v].append((u, cost))도 넣는다
    dist = {k: 0}
    heap = [(0, k)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue  # 더 짧은 길을 이미 찾은, 옛날 기록
        for v, cost in graph[u]:
            if d + cost < dist.get(v, inf):
                dist[v] = d + cost
                heapq.heappush(heap, (d + cost, v))
    return max(dist.values()) if len(dist) == n else -1
```

### Tree Recursion
- **단서:** Binary Tree
- **방법:** 왼쪽과 오른쪽 subtree의 답을 구해 합친다. Level별로 보려면 위의 BFS 틀을
  쓴다.
- **풀어 본 문제:** Validate Binary Search Tree, Binary Tree Level Order Traversal

**Maximum Depth of Binary Tree (104, Easy)**

Binary tree의 `root`가 주어진다. Root에서 가장 먼 leaf까지 가는 경로에 있는 node
수(depth)를 반환한다.

- `root = [3, 9, 20, null, null, 15, 7]` → `3`. 아래 tree에서 3 → 20 → 15다.
- `root = []` → `0`.

```text
    3
   / \
  9   20
     /  \
    15   7
```

```python
def max_depth(node):
    if not node:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))
```

### Backtracking
- **단서:** 모든 subset이나 모든 순서, n ≤ 20
- **방법:** 하나를 고르고, recursion하고, 되돌린 뒤 다음 것을 고른다

**Subsets (78, Medium)**

값이 모두 다른 정수 배열 `nums`가 주어진다. 가능한 모든 subset(빈 집합 포함)을
반환한다. 순서는 상관없고, 같은 subset이 두 번 나오면 안 된다.

- `nums = [1, 2, 3]` → `[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]`.
  2³ = 8개다.
- `nums = [0]` → `[[], [0]]`.

```python
def subsets(nums):
    result = []
    path = []  # 지금까지 고른 수

    def backtrack(start):
        result.append(path[:])  # 지금 고른 것도 subset 하나 (복사해서 저장)
        for i in range(start, len(nums)):
            path.append(nums[i])  # 고른다
            backtrack(i + 1)  # 그 뒤의 수로 이어서 고른다
            path.pop()  # 되돌리고, 다음 수를 고른다

    backtrack(0)
    return result
```

### Sort, then Merge
- **단서:** 겹치는 interval
- **방법:** start로 sort한다. 다음 interval이 지금 interval이 끝나기 전에 시작하면
  merge한다.
- **풀어 본 문제:** Merge Intervals

**Merge Intervals (56, Medium)**

`intervals[i] = [start, end]`의 list가 주어진다. 겹치는 interval을 모두 합쳐, 서로
겹치지 않는 interval의 list를 반환한다. 한 interval의 끝과 다른 interval의 시작이
같아도 겹친다고 본다.

- `[[1, 3], [2, 6], [8, 10], [15, 18]]` → `[[1, 6], [8, 10], [15, 18]]`. `[1, 3]`과
  `[2, 6]`이 겹친다.
- `[[1, 4], [4, 5]]` → `[[1, 5]]`.

```python
def merge(intervals):
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:  # 마지막 interval과 겹친다
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

### Dynamic Programming (DP)
- **단서:** 방법의 수; 가장 적은, 많은, 좋은 합계; "X를 만들 수 있나?"; 각 선택이
  앞의 선택에 달려 있다
- **방법:** 코드를 쓰기 전에 네 가지에 답한다.
  1. `dp[i]`는 무엇인가? "i번째 계단까지 오는 방법의 수"처럼 말로 한다.
  2. `dp[i]`를 더 작은 답으로 어떻게 만드나? 마지막 선택을 본다.
  3. Base case는 무엇인가? `dp[0]` 같은 것.
  4. 답은 어디 있나? `dp[n]`인가, `max(dp)`인가?
- **풀어 본 문제:** Climbing Stairs, House Robber

| 유형 | 단서 | `dp[i]`의 뜻 | 만드는 재료 |
|---|---|---|---|
| 한 줄 | 계단, 한 줄로 선 집 | 앞의 i개에 대한 답 | `dp[i - 1]`과 `dp[i - 2]` |
| i에서 끝남 | LIS | 정확히 i에서 끝나는 것 중 최선 | j < i인 모든 `dp[j]` |
| 문자열 자르기 | s를 단어로 나눌 수 있나? | `s[:i]`를 나눌 수 있다 | `s[j:i]`가 단어인 `dp[j]` |
| 합 만들기 | 같은 수를 몇 번이든 써서 합 만들기 | 합 a를 만드는 방법 수 | 수마다 `dp[a - num]` |
| 한 번씩만 | 합이 target인 subset | 몇 개를 골라 합 s를 만들 수 있다 | `dp[s - num]`, s는 큰 쪽부터 |
| Grid | Grid의 경로 | 칸 (r, c)의 답 | 위 칸과 왼쪽 칸 |
| 두 문자열 | LCS, Edit Distance | `a[:i]`와 `b[:j]`의 답 | `dp[i - 1][j - 1]`, `dp[i - 1][j]`, `dp[i][j - 1]` |

한 줄, 표로:

**Climbing Stairs (70, Easy)**

계단이 `n`칸 있다. 한 번에 1칸이나 2칸을 오를 수 있다. 꼭대기까지 오르는 서로 다른
방법의 수를 반환한다.

- `n = 2` → `2`. 1 + 1, 2.
- `n = 3` → `3`. 1 + 1 + 1, 1 + 2, 2 + 1.

```python
def climb_stairs(n):
    dp = [0] * (n + 1)  # dp[i] = i번째 계단까지 오는 방법 수
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # 마지막에 1칸 올랐거나, 2칸 올랐거나
    return dp[n]
```

같은 문제를 top-down으로: 그냥 recursion을 쓰고 `@cache`를 붙이면 `i`마다 한 번만
계산한다. 파이썬은 recursion이 약 1,000번 깊어지면 멈추니, n이 크면 표로 쓴다.

```python
from functools import cache

def climb_stairs(n):
    @cache
    def ways(i):  # i번째 계단까지 오는 방법 수
        if i <= 1:
            return 1
        return ways(i - 1) + ways(i - 2)

    return ways(n)
```

한 줄, list 대신 변수 두 개로:

**House Robber (198, Medium)**

한 줄로 선 집들에 돈이 있다. `nums[i]`는 i번째 집의 돈이다. 바로 옆 두 집을 같은 밤에
털면 경보가 울린다. 경보 없이 털 수 있는 돈의 최댓값을 반환한다.

- `nums = [1, 2, 3, 1]` → `4`. 첫째 집(1)과 셋째 집(3)을 턴다.
- `nums = [2, 7, 9, 3, 1]` → `12`. 2 + 9 + 1.

```python
def rob(nums):
    prev2 = prev1 = 0  # 두 집 전까지의 최선, 한 집 전까지의 최선
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)  # 이 집을 건너뛰거나, 털거나
    return prev1
```

i에서 끝남:

**Longest Increasing Subsequence (300, Medium)**

정수 배열 `nums`가 주어진다. 가장 긴 strictly increasing subsequence의 길이를
반환한다. Subsequence는 순서를 지키면서 몇 개를 지운 것이다. 연속일 필요는 없다.

- `nums = [10, 9, 2, 5, 3, 7, 101, 18]` → `4`. 예를 들어 `[2, 3, 7, 101]`.
- `nums = [7, 7, 7, 7]` → `1`. 같은 값은 증가가 아니다.

```python
def length_of_lis(nums):
    dp = [1] * len(nums)  # dp[i] = 정확히 i에서 끝나는 가장 긴 increasing subsequence
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:  # nums[i]를 nums[j] 뒤에 붙일 수 있다
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

문자열 자르기:

**Word Break (139, Medium)**

문자열 `s`와 단어 list `word_dict`가 주어진다. `s`를 사전에 있는 단어들로만 빈틈없이
나눌 수 있으면 `True`를 반환한다. 같은 단어를 여러 번 써도 된다.

- `s = "leetcode", word_dict = ["leet", "code"]` → `True`. "leet" + "code".
- `s = "applepenapple", word_dict = ["apple", "pen"]` → `True`. "apple"을 두 번 쓴다.
- `s = "catsandog", word_dict = ["cats", "dog", "sand", "and", "cat"]` → `False`.

```python
def word_break(s, word_dict):
    words = set(word_dict)
    dp = [True] + [False] * len(s)  # dp[i] = s[:i]를 단어로 나눌 수 있다
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:  # s[:j]는 나뉘고, s[j:i]는 단어다
                dp[i] = True
                break
    return dp[-1]
```

합 만들기:

**Combination Sum IV (377, Medium)**

서로 다른 양의 정수 배열 `nums`와 `target`이 주어진다. `nums`의 수를 몇 번이든 골라
차례로 더해 `target`을 만드는 방법의 수를 반환한다. 순서가 다르면 다른 방법이다.
`nums = [1, 2]`이면 Climbing Stairs와 같은 문제다.

- `nums = [1, 2, 3], target = 4` → `7`. 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1.
- `nums = [9], target = 3` → `0`.

```python
def combination_sum4(nums, target):
    dp = [1] + [0] * target  # dp[a] = 합 a를 만드는 방법 수; 0은 아무것도 안 쓰는 1가지
    for a in range(1, target + 1):
        for num in nums:
            if num <= a:
                dp[a] += dp[a - num]  # 마지막에 쓴 수가 num
    return dp[target]
```

한 번씩만:

**Partition Equal Subset Sum (416, Medium)**

양의 정수 배열 `nums`가 주어진다. 모든 수를 두 묶음으로 나눠, 두 묶음의 합이 같게 할
수 있으면 `True`를 반환한다.

- `nums = [1, 5, 11, 5]` → `True`. `[1, 5, 5]`와 `[11]`, 둘 다 합이 11이다.
- `nums = [1, 2, 3, 5]` → `False`. 전체 합 11이 홀수다.

s를 큰 쪽부터 내려가야 `dp[s - num]`이 아직 이 수를 쓰기 전의 답이라서, 같은 수를 두
번 쓰지 않는다.

```python
def can_partition(nums):
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [True] + [False] * target  # dp[s] = 지금까지의 수 몇 개로 합 s를 만들 수 있다
    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]  # num 없이, 또는 num을 써서
    return dp[target]
```

Grid:

**Unique Paths (62, Medium)**

`m × n` grid의 왼쪽 위 칸에 로봇이 있다. 로봇은 한 번에 오른쪽이나 아래로 한 칸만
움직인다. 오른쪽 아래 칸까지 가는 서로 다른 경로의 수를 반환한다.

- `m = 3, n = 2` → `3`. 오른쪽→아래→아래, 아래→오른쪽→아래, 아래→아래→오른쪽.
- `m = 3, n = 7` → `28`.

```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]  # dp[r][c] = (r, c)까지 가는 경로 수; 맨 위 row와 맨 왼쪽 column은 1
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]  # 위에서 왔거나, 왼쪽에서 왔거나
    return dp[-1][-1]
```

두 문자열:

**Longest Common Subsequence (1143, Medium)**

두 문자열 `a`, `b`가 주어진다 (LeetCode에서는 `text1`, `text2`). 둘 다의
subsequence인 문자열 중 가장 긴 것의 길이를 반환한다. 없으면 `0`.

- `a = "abcde", b = "ace"` → `3`. `"ace"`.
- `a = "abc", b = "def"` → `0`.

Row 0과 column 0은 빈 문자열을 뜻하니 0으로 둔다.

```python
def longest_common_subsequence(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]  # dp[i][j] = a[:i]와 b[:j]의 답
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # 마지막 글자가 같다: 둘 다 쓴다
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # a나 b에서 한 글자를 뺀다
    return dp[-1][-1]
```

### Linked List
- **단서:** Linked List
- **방법:** Dummy node를 두면 head를 따로 처리하지 않아도 된다. Slow/fast pointer는
  fast가 2칸, slow가 1칸씩 간다.
- **풀어 본 문제:** Linked List Cycle, Remove Nth Node From End of List

**Linked List Cycle (141, Easy)**

Linked list의 `head`가 주어진다. `next`를 계속 따라가다 이미 지난 node로 돌아오면
cycle이 있는 것이다. Cycle이 있으면 `True`, 없으면 `False`를 반환한다.

- `3 → 2 → 0 → -4`이고 `-4`의 `next`가 다시 `2`일 때 → `True`.
- `1` 하나뿐이고 `next`가 없을 때 → `False`.

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
