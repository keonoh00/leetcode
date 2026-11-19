# 기법 고르기

코드를 쓰기 전에 2분 정도, 세 가지를 소리 내어 말한다.

1. **제약:** 어떤 알고리즘이면 충분히 빠른가?
2. **완전 탐색:** 무엇을 계속 반복하는가?
3. **문제의 단서:** 어떤 기법을 가리키는가?

처음 보는 문제 같으면 1단계가 아니라 0단계부터 시작한다. 규칙을 주석으로 적는 일은
언제든 먼저 할 수 있으니, 빈 화면에서 시작할 일이 없다.

---

## 0단계: 규칙 문제 (잡다 테스트 대부분)

대부분의 단계는 알고리즘을 고르는 문제가 아니라 규칙을 코드로 옮기는 문제다. 앞
단계는 입력이 작아서 단순하게 짜도 통과한다. 1–3단계가 필요한 것은 규모를 키우는
단계뿐이다.

1. 반환값부터 읽는다. 무슨 타입인지, 어떤 순서인지, 맞는 것이 없으면 무엇을
   반환하는지.
2. 규칙을 한 줄에 하나씩 주석으로 적는다. 동점 처리와 예외 규칙("같으면…",
   "없으면…")도 적는다.
3. 데이터 모양을 정한다. 기록마다 튜플이나 딕셔너리, id를 키로 하는 딕셔너리, 또는
   정렬된 이벤트 목록.
4. 규칙 하나에 함수 하나. `solution`은 파싱하고, 반복하고, 함수를 부르기만 한다.
   그러면 다음 단계에서 규칙이 바뀌어도 함수 하나만 고친다.
5. 첫 번째 예제를 손으로 풀고, 중간 값을 `print`해서 비교한다.
6. 예외 경우를 넣어 본다: 빈 입력, 하나뿐인 입력, 같은 시각, 경계가 되는 분, 마지막
   날.
7. 그다음에야 n을 생각한다. 효율성 테스트에서 떨어지면 1단계로 간다.

출입 기록 (예시 문제): `records`의 각 줄은 `"시각 이름 IN"` 또는 `"시각 이름 OUT"`이다.
사람마다 안에 있던 시간(분)을 더해 `[이름, 분]` 목록을 이름순으로 반환한다.

```python
from collections import defaultdict

# 규칙 1: IN이면 들어온 시각을 적어 둔다
# 규칙 2: OUT이면 (나간 시각 - 들어온 시각)을 그 사람의 합계에 더한다
# 반환: [이름, 합계 분] 목록, 이름 A→Z

def parse(record):                     # "09:40 kim OUT" -> (580, "kim", "OUT")
    clock, name, kind = record.split()
    h, m = map(int, clock.split(":"))
    return h * 60 + m, name, kind

def enter(inside, time, name):         # 규칙 1
    inside[name] = time

def leave(inside, total, time, name):  # 규칙 2
    total[name] += time - inside.pop(name)

def solution(records):
    events = sorted(parse(r) for r in records)  # 시각 순; 같으면 튜플의 다음 값 순
    inside = {}                        # 이름 -> 들어온 시각
    total = defaultdict(int)           # 이름 -> 합계 분
    for time, name, kind in events:
        if kind == "IN":
            enter(inside, time, name)
        else:
            leave(inside, total, time, name)
    return sorted([name, minutes] for name, minutes in total.items())

# solution(["09:00 kim IN", "09:10 lee IN", "09:40 kim OUT", "10:00 lee OUT"])
# -> [["kim", 40], ["lee", 50]]
```

파싱과 시뮬레이션에 쓰는 파이썬:

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

# 개수 세기와 묶기
from collections import Counter, defaultdict, deque
total = defaultdict(int)                       # total[key] += x
groups = defaultdict(list)                     # groups[key].append(x)

# (이름, 점수) 행 정렬
sorted(rows, key=lambda r: (-r[1], r[0]))      # 점수 높은 순, 같으면 이름 A→Z

# 올림 나눗셈, 양의 정수일 때
-(-a // b)                                     # a / b를 올림

# 모든 쌍, 순서, 조합
from itertools import combinations, permutations, product

# 정렬된 리스트에서 개수 세기
from bisect import bisect_left, bisect_right
bisect_right(a, x) - bisect_left(a, x)         # a에 x가 몇 개 있나
```

---

## 1단계: n은 얼마나 큰가?

파이썬은 1초에 간단한 연산을 약 10⁷번 한다. n²이 10¹⁰이면 통과하지 못한다.

왼쪽에서 내 n을 찾되, 올려서 찾는다: n ≤ 10⁴이면 10⁵ 줄을 본다. 표에서 더 아래에
있는 것은 더 빠르니 그것도 된다.

<table>
<tr><th>제약</th><th>시간</th><th>알고리즘</th></tr>
<tr><td>n ≤ 20</td><td>O(2ⁿ)</td><td>백트래킹: 모든 부분집합, 모든 순서</td></tr>
<tr><td rowspan="5">n ≤ 10³</td><td rowspan="4">O(n²)</td><td>이중 for문: 모든 쌍</td></tr>
<tr><td>정렬한 뒤 수마다 투 포인터: 세 수의 합 (3Sum)</td></tr>
<tr><td>앞의 모든 j &lt; i를 보는 DP: 최장 증가 부분 수열, Word Break</td></tr>
<tr><td>두 문자열 DP: 공통 부분 수열, 편집 거리</td></tr>
<tr><td>O(n × amount)</td><td>합마다 보는 DP: 합을 만드는 방법 수, 합이 target인 부분집합</td></tr>
<tr><td rowspan="17">n ≤ 10⁵</td><td rowspan="3">O(n log n)</td><td>먼저 정렬</td></tr>
<tr><td>구간: 시작점으로 정렬한 뒤 합치기</td></tr>
<tr><td>간선에 비용이 있는 그래프: 힙으로 다익스트라</td></tr>
<tr><td>O(n log k)</td><td>크기 k인 힙: 가장 큰, 작은, 가까운 k개</td></tr>
<tr><td>O(n log m)</td><td>답을 이분 탐색: 조건을 만족하는 가장 작은 X (Koko)</td></tr>
<tr><td rowspan="10">O(n)</td><td>해시맵, 집합: 본 적 있나, 개수 세기, 묶기</td></tr>
<tr><td>누적합 + 해시맵: 합이 k인 부분 배열</td></tr>
<tr><td>투 포인터: 정렬된 배열의 쌍, 회문</td></tr>
<tr><td>슬라이딩 윈도우: 가장 긴/짧은 부분 문자열, 부분 배열</td></tr>
<tr><td>스택: 다음으로 큰 값, 괄호 짝</td></tr>
<tr><td>for문 하나 DP: 방법의 수, 최고 합계</td></tr>
<tr><td>연결 리스트: 더미 노드, 느린/빠른 포인터, 제자리 뒤집기</td></tr>
<tr><td>이진 트리: DFS 재귀, 층별로는 BFS</td></tr>
<tr><td>격자: 영역 세기는 DFS, 최소 이동은 BFS, 경로 수는 DP</td></tr>
<tr><td>그래프: 인접 리스트로 DFS나 BFS, 선수 과목은 위상 정렬</td></tr>
<tr><td>O(log n)</td><td>이분 탐색: 정렬된 배열에서 값 찾기</td></tr>
<tr><td>호출마다 O(1)</td><td>설계: 해시맵 + 연결 리스트 (LRU Cache), Min Stack</td></tr>
</table>

n은 입력의 길이다. 격자면 행 × 열, 그래프면 노드 수 + 간선 수다. k는 문제에 나오는
k, m은 가장 큰 값이다.

---

## 2단계: 완전 탐색은 무엇을 반복하나?

완전 탐색을 먼저 말한다. 그다음 무슨 일을 계속 다시 하는지 묻는다. 그 반복을 없애는
것이 쓸 기법이다.

| 문제 | 완전 탐색 | 더 나은 방법 |
|---|---|---|
| Two Sum | 모든 쌍을 확인한다, O(n²) | 해시맵: 본 수를 저장해 두고 `target - num`을 바로 찾는다, O(n) |
| Maximum Average Subarray I | 구간마다 k개를 처음부터 다시 더한다, O(n × k) | 슬라이딩 윈도우: 새 수를 더하고 빠지는 수를 뺀다, O(n) |
| Binary Search | 앞에서부터 하나씩 확인한다, O(n) | 이분 탐색: 가운데를 보고 답이 없는 절반을 버린다, O(log n) |

---

## 3단계: 문제의 단서는 어떤 기법을 가리키나?

### 투 포인터
- **단서:** 회문; 정렬된 배열에서 합이 target인 쌍이나 세 수
- **방법:** 양 끝에서 시작해 가운데로 좁혀 온다. 합을 찾을 때는 합이 작으면 왼쪽
  포인터를 오른쪽으로, 크면 오른쪽 포인터를 왼쪽으로 옮긴다.
- **풀어 본 문제:** Two Sum II, 3Sum, Container With Most Water

Valid Palindrome (125, Easy): 글자와 숫자만 보고 대소문자를 무시하면 회문인가?

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

### 해시맵, 집합
- **단서:** "전에 본 적 있나?", 개수 세기, 묶기
- **방법:** 본 것을 저장해 두면 찾을 때마다 O(1)
- **풀어 본 문제:** Contains Duplicate, Group Anagrams, Top K Frequent Elements

Contains Duplicate (217, Easy): 같은 수가 두 번 나오나?

```python
def has_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

### 누적합 + 해시맵
- **단서:** 합이 k인 연속 부분 배열
- **방법:** i부터 j까지의 합은 (j까지의 누적합) - (i 앞까지의 누적합)이다. 그래서
  `total - k`를 맵에서 찾는다.
- **풀어 본 문제:** Subarray Sum Equals K

Subarray Sum Equals K (560, Medium): 합이 k인 연속 부분 배열은 몇 개인가?

```python
def subarray_sum(nums, k):
    count = total = 0
    seen = {0: 1}  # 누적합 -> 지금까지 나온 횟수
    for num in nums:
        total += num
        count += seen.get(total - k, 0)  # 앞에 total - k가 있었으면, 그 뒤부터 여기까지 합이 k
        seen[total] = seen.get(total, 0) + 1
    return count
```

### 슬라이딩 윈도우
- **단서:** 연속된 부분 문자열이나 부분 배열: 길이가 k인 것, 또는 규칙을 지키는 가장
  긴/짧은 것
- **방법:** 오른쪽에 하나를 넣고 왼쪽에서 하나를 뺀다. 구간을 매번 처음부터 다시
  계산하지 않는다. 길이가 정해져 있지 않으면, 규칙이 깨졌을 때만 왼쪽을 줄인다.
- **풀어 본 문제:** Longest Substring Without Repeating Characters, Best Time to Buy
  and Sell Stock

Maximum Average Subarray I (643, Easy): 길이 k인 연속 구간의 평균 중 가장 큰 값은?

```python
def find_max_average(nums, k):
    total = sum(nums[:k])  # 첫 구간
    best = total
    for right in range(k, len(nums)):
        total += nums[right] - nums[right - k]  # 새 수를 더하고, 빠지는 수를 뺀다
        best = max(best, total)
    return best / k
```

### 이분 탐색
- **단서:** 정렬된 입력, 또는 "조건을 만족하는 가장 작은 X" (X 하나를 확인하기는 쉬울
  때)
- **방법:** 가운데를 확인하고, 답이 있을 수 없는 절반을 버린다
- **풀어 본 문제:** Find Minimum in Rotated Sorted Array, Search a 2D Matrix, Koko
  Eating Bananas

정렬된 배열에서 값 찾기, Binary Search (704, Easy): `target`의 위치, 없으면 -1.

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

조건을 만족하는 가장 작은 X, First Bad Version (278, Easy): 1부터 n까지의 버전 중 처음
나온 불량 버전은? 불량 다음은 모두 불량이고, `is_bad_version(v)`는 LeetCode가 준다.

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

### 스택
- **단서:** 괄호 짝; 다음으로 큰 값
- **방법:** 아직 짝(답)을 기다리는 것을 쌓아 두고, 짝이 오면 꺼낸다
- **풀어 본 문제:** Daily Temperatures, Valid Parentheses

Valid Parentheses (20, Easy): `()[]{}`로 된 문자열의 괄호 짝이 맞나?

```python
def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}  # 닫는 괄호 -> 여는 괄호
    stack = []  # 아직 짝을 기다리는 여는 괄호
    for ch in s:
        if ch not in pairs:
            stack.append(ch)  # 여는 괄호: 쌓는다
        elif not stack or stack.pop() != pairs[ch]:
            return False  # 기다리는 괄호가 없거나, 짝이 틀렸다
    return not stack  # 짝을 못 찾은 여는 괄호가 없어야 한다
```

### 힙
- **단서:** 가장 큰, 작은, 가까운 k개
- **방법:** 크기를 k로 유지하는 힙 (`heapq`는 최소 힙)
- **풀어 본 문제:** Kth Largest Element in an Array, K Closest Points to Origin

Kth Largest Element in a Stream (703, Easy): 수가 하나씩 들어올 때마다 k번째로 큰 수는?

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
- **단서:** 격자의 영역, 퍼져 나가는 것, 최소 이동 횟수
- **방법:** 칸을 방문하면 표시하고, 이웃 칸을 방문한다. 최소 이동 횟수가 필요하면
  BFS(큐)를 쓴다.
- **풀어 본 문제:** Number of Islands, Rotting Oranges

DFS, Flood Fill (733, Easy): `(sr, sc)`와 이어진 같은 색 칸을 모두 `color`로 칠한다.

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

BFS, 미로 최단 거리 (예시 문제): `"."`은 길, `"#"`은 벽이다. 왼쪽 위에서 오른쪽
아래까지 최소 몇 번 움직이나? 못 가면 -1.

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
                    continue  # 격자 밖
                if grid[nr][nc] == "#" or (nr, nc) in seen:
                    continue  # 벽이거나, 이미 넣은 칸
                seen.add((nr, nc))
                queue.append((nr, nc))
        steps += 1
    return -1
```

### 다익스트라
- **단서:** 간선에 비용이 있는 그래프의 최단 경로
- **방법:** 힙에서 가장 가까운 노드를 꺼내고, 그 노드의 간선을 하나씩 시도한다

Network Delay Time (743, Medium): 노드 k에서 보낸 신호가 모든 노드에 닿는 시간은? 못
닿는 노드가 있으면 -1. 간선은 한 방향이다.

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

### 트리 재귀
- **단서:** 이진 트리
- **방법:** 왼쪽과 오른쪽 서브트리의 답을 구해 합친다. 층별로 보려면 위의 BFS 틀을
  쓴다.
- **풀어 본 문제:** Validate Binary Search Tree, Binary Tree Level Order Traversal

Maximum Depth of Binary Tree (104, Easy): 트리의 깊이는?

```python
def max_depth(node):
    if not node:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))
```

### 백트래킹
- **단서:** 모든 부분집합이나 모든 순서, n ≤ 20
- **방법:** 하나를 고르고, 재귀하고, 되돌린 뒤 다음 것을 고른다

Subsets (78, Medium): 모든 부분집합을 반환한다.

```python
def subsets(nums):
    result = []
    path = []  # 지금까지 고른 수

    def backtrack(start):
        result.append(path[:])  # 지금 고른 것도 부분집합 하나 (복사해서 저장)
        for i in range(start, len(nums)):
            path.append(nums[i])  # 고른다
            backtrack(i + 1)  # 그 뒤의 수로 이어서 고른다
            path.pop()  # 되돌리고, 다음 수를 고른다

    backtrack(0)
    return result
```

### 정렬 후 합치기
- **단서:** 겹치는 구간
- **방법:** 시작점으로 정렬한다. 다음 구간이 지금 구간이 끝나기 전에 시작하면
  합친다.
- **풀어 본 문제:** Merge Intervals

Merge Intervals (56, Medium): 겹치는 구간을 모두 합친다.

```python
def merge(intervals):
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:  # 마지막 구간과 겹친다
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

### 동적 계획법 (DP)
- **단서:** 방법의 수; 가장 적은, 많은, 좋은 합계; "X를 만들 수 있나?"; 각 선택이
  앞의 선택에 달려 있다
- **방법:** 코드를 쓰기 전에 네 가지에 답한다.
  1. `dp[i]`는 무엇인가? "i번째 계단까지 오는 방법의 수"처럼 말로 한다.
  2. `dp[i]`를 더 작은 답으로 어떻게 만드나? 마지막 선택을 본다.
  3. 시작 값은 무엇인가? `dp[0]` 같은 것.
  4. 답은 어디 있나? `dp[n]`인가, `max(dp)`인가?
- **풀어 본 문제:** Climbing Stairs, House Robber

| 유형 | 단서 | `dp[i]`의 뜻 | 만드는 재료 |
|---|---|---|---|
| 한 줄 | 계단, 한 줄로 선 집 | 앞의 i개에 대한 답 | `dp[i - 1]`과 `dp[i - 2]` |
| i에서 끝남 | 최장 증가 부분 수열 | 정확히 i에서 끝나는 것 중 최선 | j < i인 모든 `dp[j]` |
| 문자열 자르기 | s를 단어로 나눌 수 있나? | `s[:i]`를 나눌 수 있다 | `s[j:i]`가 단어인 `dp[j]` |
| 합 만들기 | 같은 수를 몇 번이든 써서 합 만들기 | 합 a를 만드는 방법 수 | 수마다 `dp[a - num]` |
| 한 번씩만 | 합이 target인 부분집합 | 몇 개를 골라 합 s를 만들 수 있다 | `dp[s - num]`, s는 큰 쪽부터 |
| 격자 | 격자의 경로 | 칸 (r, c)의 답 | 위 칸과 왼쪽 칸 |
| 두 문자열 | 공통 부분 수열, 편집 거리 | `a[:i]`와 `b[:j]`의 답 | `dp[i - 1][j - 1]`, `dp[i - 1][j]`, `dp[i][j - 1]` |

한 줄, 표로. Climbing Stairs (70, Easy): 한 번에 1칸이나 2칸을 오를 때, n칸 계단을
오르는 방법은 몇 가지인가?

```python
def climb_stairs(n):
    dp = [0] * (n + 1)  # dp[i] = i번째 계단까지 오는 방법 수
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # 마지막에 1칸 올랐거나, 2칸 올랐거나
    return dp[n]
```

같은 것을 위에서 아래로: 그냥 재귀를 쓰고 `@cache`를 붙이면 `i`마다 한 번만 계산한다.
파이썬은 재귀가 약 1,000번 깊어지면 멈추니, n이 크면 표로 쓴다.

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

한 줄, 리스트 대신 변수 두 개로. House Robber (198, Medium): 바로 옆집은 함께 털 수
없을 때, 털 수 있는 가장 큰 금액은?

```python
def rob(nums):
    prev2 = prev1 = 0  # 두 집 전까지의 최선, 한 집 전까지의 최선
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)  # 이 집을 건너뛰거나, 털거나
    return prev1
```

i에서 끝남. Longest Increasing Subsequence (300, Medium): 가장 긴 증가 부분 수열의
길이는?

```python
def length_of_lis(nums):
    dp = [1] * len(nums)  # dp[i] = 정확히 i에서 끝나는 가장 긴 증가 부분 수열
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:  # nums[i]를 nums[j] 뒤에 붙일 수 있다
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

문자열 자르기. Word Break (139, Medium): `s`를 사전에 있는 단어들로 나눌 수 있나?

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

합 만들기. Combination Sum IV (377, Medium): `nums`의 수를 몇 번이든 써서 합
`target`을 만드는 순서는 몇 가지인가? `nums = [1, 2]`이면 Climbing Stairs와 같다.

```python
def combination_sum4(nums, target):
    dp = [1] + [0] * target  # dp[a] = 합 a를 만드는 방법 수; 0은 아무것도 안 쓰는 1가지
    for a in range(1, target + 1):
        for num in nums:
            if num <= a:
                dp[a] += dp[a - num]  # 마지막에 쓴 수가 num
    return dp[target]
```

한 번씩만. Partition Equal Subset Sum (416, Medium): 합이 같은 두 묶음으로 나눌 수
있나? 큰 쪽부터 내려가야 `dp[s - num]`이 아직 이 수를 쓰기 전의 답이라서, 같은 수를 두
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

격자. Unique Paths (62, Medium): 오른쪽이나 아래로만 갈 때, m × n 격자의 왼쪽 위에서
오른쪽 아래까지 가는 길은 몇 가지인가?

```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]  # dp[r][c] = (r, c)까지 가는 길 수; 맨 위 줄과 맨 왼쪽 줄은 1
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]  # 위에서 왔거나, 왼쪽에서 왔거나
    return dp[-1][-1]
```

두 문자열. Longest Common Subsequence (1143, Medium): 두 문자열의 가장 긴 공통 부분
수열의 길이는? 0번 행과 0번 열은 빈 문자열을 뜻하니 0으로 둔다.

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

### 연결 리스트
- **단서:** 연결 리스트
- **방법:** 더미 노드를 두면 head를 따로 처리하지 않아도 된다. 느린/빠른 포인터는
  빠른 쪽이 2칸, 느린 쪽이 1칸씩 간다.
- **풀어 본 문제:** Linked List Cycle, Remove Nth Node From End of List

Linked List Cycle (141, Easy): 리스트에 사이클이 있나?

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
