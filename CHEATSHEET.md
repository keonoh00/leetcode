# 알고리즘 Cheat Sheet

## 문제를 받으면

코드를 쓰기 전에 2분 동안 세 가지를 소리 내어 말한다.

1. **Constraints:** n이 얼마인가? 아래 표에서 시간 안에 도는 알고리즘을 고른다.
2. **Brute Force:** 가장 단순한 방법은 무엇이고, 무엇을 계속 반복하나? 그 반복을 없애는
   것이 쓸 기법이다. 기법마다 **왜 빠른가** 줄을 본다.
3. **단서:** 문제의 말이 어떤 기법을 가리키나? 기법마다 **단서** 줄을 본다.

알고리즘보다 규칙을 그대로 옮기는 게 일인 문제(Simulation)라면:

1. 반환값부터 읽는다: type, 순서, 맞는 게 없을 때 무엇을 반환하는지.
2. 규칙을 한 줄에 하나씩 주석으로 적는다. Tie-break("같으면…")와 예외("없으면…")도.
3. 데이터 모양을 정한다: 기록마다 tuple, id → 정보 dict, 정렬된 event list.
4. 규칙 하나에 함수 하나. `solution`은 parse, 반복, 함수 호출만 한다.
5. 첫 예제를 손으로 풀고, 중간 값을 `print`해서 맞춰 본다.

---

## n으로 고르기

파이썬은 1초에 간단한 연산을 약 10⁷번 한다. n = 10⁵인데 O(n²)이면 10¹⁰번이라 시간
초과가 난다.

n이 표의 값 사이에 있으면 큰 쪽 줄을 본다 (n ≤ 10⁴이면 n ≤ 10⁵ 줄). 아래쪽 줄의
알고리즘은 더 빠르니 위쪽 줄의 n에서도 쓸 수 있다. 기법 이름을 누르면 아래의 정리로
간다.

<table>
<tr><th>Constraint</th><th>Time</th><th>Algorithm</th></tr>
<tr><td>n ≤ 20</td><td>O(2ⁿ)</td><td><a href="#backtracking">Backtracking</a>: 모든 subset, 모든 순서</td></tr>
<tr><td rowspan="5">n ≤ 10³</td><td rowspan="4">O(n²)</td><td>이중 for문 (Brute Force): 모든 쌍 (i, j)</td></tr>
<tr><td>Sort + <a href="#two-pointers">Two Pointers</a>: 세 수의 합 (3Sum)</td></tr>
<tr><td><a href="#dynamic-programming-dp">DP</a>, 앞의 모든 j를 봄: LIS, Word Break</td></tr>
<tr><td><a href="#dynamic-programming-dp">DP</a>, 두 문자열: LCS</td></tr>
<tr><td>O(n × target)</td><td><a href="#dynamic-programming-dp">DP</a>, 합마다: Combination Sum IV, Partition Equal Subset Sum</td></tr>
<tr><td rowspan="15">n ≤ 10⁵</td><td rowspan="3">O(n log n)</td><td>Sort 먼저: 정렬하면 쉬워지는 문제</td></tr>
<tr><td><a href="#sort-then-merge">Sort, then Merge</a>: 겹치는 interval</td></tr>
<tr><td><a href="#dijkstra">Dijkstra</a>: edge에 cost가 있는 최단 경로</td></tr>
<tr><td>O(n log k)</td><td><a href="#heap">Heap</a>: 가장 큰, 작은, 가까운 k개</td></tr>
<tr><td>O(n log m)</td><td><a href="#binary-search">Binary Search</a>: 조건을 만족하는 가장 작은 X</td></tr>
<tr><td rowspan="9">O(n)</td><td><a href="#hash-map-set">Hash Map, Set</a>: 본 적 있나, 개수 세기, grouping</td></tr>
<tr><td><a href="#prefix-sum--hash-map">Prefix Sum + Hash Map</a>: 합이 k인 subarray</td></tr>
<tr><td><a href="#two-pointers">Two Pointers</a>: palindrome, 정렬된 배열에서 합이 target인 쌍</td></tr>
<tr><td><a href="#sliding-window">Sliding Window</a>: 길이 k인 구간, 가장 긴/짧은 연속 구간</td></tr>
<tr><td><a href="#stack">Stack</a>: 괄호 짝, 다음으로 큰 값</td></tr>
<tr><td><a href="#dfs-bfs">DFS, BFS</a>: grid의 영역, 최소 이동 횟수</td></tr>
<tr><td><a href="#tree-recursion">Tree Recursion</a>: binary tree</td></tr>
<tr><td><a href="#linked-list">Linked List</a>: cycle, 가운데 node, 뒤집기</td></tr>
<tr><td><a href="#dynamic-programming-dp">DP</a>, 한 줄: 계단, House Robber</td></tr>
<tr><td>O(log n)</td><td><a href="#binary-search">Binary Search</a>: 정렬된 배열에서 값 찾기</td></tr>
</table>

n은 입력의 길이다. Grid면 행 × 열, Graph면 node 수 + edge 수다. k는 문제에 나오는
k, m은 답이 될 수 있는 가장 큰 값, target은 만들 합이다. LIS는 Longest Increasing
Subsequence, LCS는 Longest Common Subsequence다.

---

## 기법별 정리

기법마다 위에는 한눈에 볼 요약(단서, 방법, 왜 빠른가)이 있고, 아래에는 가장 쉬운 예시
문제의 설명, 풀이, 작은 입력으로 따라가 본 표, 코드가 있다.

### Two Pointers
- **단서:** palindrome; 정렬된 배열에서 합이 target인 쌍이나 세 수
- **방법:** 양 끝에서 시작해 가운데로 좁혀 온다. 합을 찾을 때는 합이 작으면 left를
  오른쪽으로, 크면 right를 왼쪽으로 옮긴다.
- **왜 빠른가:** Brute Force는 모든 쌍을 본다, O(n²). 비교 한 번마다 한쪽 끝을
  버리니 O(n).
- **같은 기법:** Two Sum II, 3Sum, Container With Most Water

#### 예: Valid Palindrome (125, Easy)

**문제.** 문자열 `s`가 주어진다. 대문자는 소문자로 바꾸고, 글자와 숫자가 아닌
문자(공백, 쉼표 등)는 모두 지운다. 남은 문자열이 앞에서 읽어도 뒤에서 읽어도
같으면(palindrome) `True`, 아니면 `False`를 반환한다.

- `s = "A man, a plan, a canal: Panama"` → `True`. 지우면
  `"amanaplanacanalpanama"`다.
- `s = "race a car"` → `False`. 지우면 `"raceacar"`인데, 뒤집으면 `"racaecar"`다.

**풀이.**
1. 비교할 글자만 `chars`에 남긴다.
2. `left`는 맨 앞, `right`는 맨 뒤에서 시작해 두 글자를 비교한다.
3. 같으면 둘 다 한 칸씩 안으로 들어온다. 다르면 palindrome이 아니니 바로 `False`.
4. 둘이 만날 때까지 다른 쌍이 없었으면 `True`.

`s = "race a car"`, `chars = "raceacar"`일 때:

| left | right | 비교 | 다음 |
|---|---|---|---|
| 0 | 7 | `r` = `r` | 안으로 |
| 1 | 6 | `a` = `a` | 안으로 |
| 2 | 5 | `c` = `c` | 안으로 |
| 3 | 4 | `e` ≠ `a` | `False` |

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

시간 O(n), 공간 O(n). n = `len(s)`. 글자마다 한 번씩 본다.

### Hash Map, Set
- **단서:** "전에 본 적 있나?", 개수 세기, grouping
- **방법:** 본 것을 set이나 dict에 저장해 두고 찾는다
- **왜 빠른가:** list에서 찾으면 O(n)이지만 set과 dict는 O(1). 모든 쌍을 비교하는
  O(n²)이 O(n)이 된다.
- **같은 기법:** Two Sum, Group Anagrams, Top K Frequent Elements

#### 예: Contains Duplicate (217, Easy)

**문제.** 정수 배열 `nums`가 주어진다. 어떤 값이 두 번 이상 나오면 `True`, 모든 값이
서로 다르면 `False`를 반환한다.

- `nums = [1, 2, 3, 1]` → `True`. 1이 두 번 나온다.
- `nums = [1, 2, 3, 4]` → `False`.

**풀이.**
1. 지금까지 본 수를 `seen`(set)에 모은다.
2. 새 수가 이미 `seen`에 있으면 전에 본 수다 → `True`.
3. 없으면 `seen`에 넣고 다음 수로 간다. 끝까지 없으면 `False`.

`nums = [1, 2, 3, 1]`일 때:

| num | 확인 전 `seen` | `num in seen` | 다음 |
|---|---|---|---|
| 1 | 비어 있음 | 아니오 | 넣는다 |
| 2 | 1 | 아니오 | 넣는다 |
| 3 | 1, 2 | 아니오 | 넣는다 |
| 1 | 1, 2, 3 | 예 | `True` |

```python
def has_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

시간 O(n), 공간 O(n). n = `len(nums)`.

### Prefix Sum + Hash Map
- **단서:** 합이 k인 subarray (연속된 부분 배열), 음수도 있음
- **방법:** i부터 j까지의 합 = (j까지의 prefix sum) - (i 앞까지의 prefix sum). 그래서
  지금의 `total`에서 `total - k`가 앞에 몇 번 나왔는지 Hash Map에서 찾는다.
- **왜 빠른가:** Brute Force는 모든 (i, j) 구간의 합을 구한다, O(n²). 구간 합을
  prefix sum의 차로 바로 알고, 필요한 값은 O(1)에 찾으니 O(n).
- **같은 기법:** Subarray Sum Equals K

#### 예: Subarray Sum Equals K (560, Medium)

**문제.** 정수 배열 `nums`와 정수 `k`가 주어진다. 합이 `k`인 subarray의 개수를
반환한다. `nums`에는 음수도 있을 수 있다.

- `nums = [1, 1, 1], k = 2` → `2`. `[1, 1]`이 index 0–1과 1–2, 두 번 있다.
- `nums = [1, 2, 3], k = 3` → `2`. `[1, 2]`와 `[3]`이다.

**풀이.**
1. `total`은 처음부터 지금 수까지의 합(prefix sum)이다.
2. 앞의 어느 지점까지의 합이 `total - k`였다면, 그 다음부터 지금까지의 합은
   `total - (total - k) = k`다. 그 구간이 답 하나다.
3. 그래서 지금까지 나온 prefix sum을 `seen`에 횟수와 함께 적어 두고, 수마다
   `seen[total - k]`를 `count`에 더한다.
4. `seen = {0: 1}`로 시작하는 것은 "아무것도 더하지 않은 합 0"이 한 번 있었다는
   뜻이다. 처음부터 지금까지가 답일 때 필요하다.

`nums = [1, 2, 3], k = 3`일 때:

| num | total | total - k | `seen`에서 찾은 횟수 | count | 찾은 구간 |
|---|---|---|---|---|---|
| 1 | 1 | -2 | 0 | 0 | |
| 2 | 3 | 0 | 1 | 1 | `[1, 2]`: 합 0(시작) 다음부터 |
| 3 | 6 | 3 | 1 | 2 | `[3]`: 합 3(`[1, 2]` 끝) 다음부터 |

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

시간 O(n), 공간 O(n). n = `len(nums)`.

### Sliding Window
- **단서:** 연속된 substring이나 subarray: 길이가 k인 것, 또는 규칙을 지키는 가장
  긴/짧은 것
- **방법:** 구간을 한 칸 밀 때 새 값을 넣고 빠지는 값을 뺀다. 길이가 정해져 있지
  않으면 오른쪽을 늘리다가, 규칙이 깨지면 왼쪽을 줄인다.
- **왜 빠른가:** Brute Force는 구간마다 처음부터 다시 계산한다, O(n × k). 한 칸 밀
  때 바뀌는 것은 두 값뿐이니 O(n).
- **같은 기법:** Longest Substring Without Repeating Characters, Best Time to Buy
  and Sell Stock

#### 예: Maximum Average Subarray I (643, Easy)

**문제.** 정수 배열 `nums`와 정수 `k`가 주어진다. 길이가 정확히 `k`인 subarray 중
평균이 가장 큰 것의 평균을 반환한다.

- `nums = [1, 12, -5, -6, 50, 3], k = 4` → `12.75`. `[12, -5, -6, 50]`의 합 51을
  4로 나눈 값이다.
- `nums = [5], k = 1` → `5.0`.

**풀이.**
1. 길이가 모두 k로 같으니, 평균이 가장 큰 구간은 합이 가장 큰 구간이다. 합만
   비교하고 마지막에 k로 나눈다.
2. 첫 window `nums[0:k]`의 합을 구한다.
3. Window를 오른쪽으로 한 칸 밀면 `nums[right]`가 들어오고 `nums[right - k]`가
   빠진다. 합에서 그 둘만 고친다.
4. 밀 때마다 가장 큰 합을 `best`에 남긴다.

`nums = [1, 12, -5, -6, 50, 3], k = 4`일 때:

| right | 들어오는 수 | 빠지는 수 | window | total | best |
|---|---|---|---|---|---|
| 처음 | | | `[1, 12, -5, -6]` | 2 | 2 |
| 4 | 50 | 1 | `[12, -5, -6, 50]` | 51 | 51 |
| 5 | 3 | 12 | `[-5, -6, 50, 3]` | 42 | 51 |

답은 51 / 4 = 12.75.

```python
def find_max_average(nums, k):
    total = sum(nums[:k])  # 첫 window
    best = total
    for right in range(k, len(nums)):
        total += nums[right] - nums[right - k]  # 새 수를 더하고, 빠지는 수를 뺀다
        best = max(best, total)
    return best / k
```

시간 O(n), 공간 O(1). n = `len(nums)`.

### Binary Search
- **단서:** 정렬된 입력, 또는 "조건을 만족하는 가장 작은 X" (X 하나를 확인하기는 쉬울
  때)
- **방법:** 가운데를 확인하고, 답이 있을 수 없는 절반을 버린다
- **왜 빠른가:** 하나씩 보면 O(n). 볼 때마다 절반을 버리니 O(log n). 10⁹개도 30번이면
  된다.
- **같은 기법:** Find Minimum in Rotated Sorted Array, Search a 2D Matrix, Koko
  Eating Bananas

#### 예 1: Binary Search (704, Easy)

**문제.** 오름차순으로 정렬된 정수 배열 `nums`(값은 모두 다름)와 `target`이
주어진다. `target`이 있으면 그 index를, 없으면 `-1`을 반환한다. O(log n)으로 풀어야
한다.

- `nums = [-1, 0, 3, 5, 9, 12], target = 9` → `4`.
- `nums = [-1, 0, 3, 5, 9, 12], target = 2` → `-1`.

**풀이.**
1. 답이 있을 수 있는 범위를 `low`부터 `high`까지로 둔다. 처음에는 배열 전체.
2. 가운데 `nums[mid]`를 본다. `target`이면 끝.
3. `nums[mid] < target`이면, 정렬되어 있으니 mid와 그 왼쪽은 모두 target보다 작다 →
   `low = mid + 1`.
4. 반대면 mid와 그 오른쪽을 버린다 → `high = mid - 1`.
5. 범위가 비면(`low > high`) target이 없다 → `-1`.

`target = 9`일 때:

| low | high | mid | nums[mid] | 다음 |
|---|---|---|---|---|
| 0 | 5 | 2 | 3 | 3 < 9 → `low = 3` |
| 3 | 5 | 4 | 9 | 찾음 → `4` |

`target = 2`면 범위가 0–5, 0–1, 1–1로 줄다가 `low = 2 > high = 1`이 되어 `-1`이다.

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

시간 O(log n), 공간 O(1). n = `len(nums)`.

#### 예 2: First Bad Version (278, Easy)

**문제.** 버전 `1, 2, …, n`이 있다. 어느 버전부터 불량이 생겼고, 불량 버전 뒤의
버전은 모두 불량이다. 버전 `v`가 불량인지는 LeetCode가 주는 `is_bad_version(v)`
(LeetCode에서는 `isBadVersion`)로 확인한다. 이 함수를 되도록 적게 불러서, 처음으로
불량인 버전을 반환한다.

- `n = 5`, 처음 불량이 4 → `4`. 버전 1–3은 정상, 4–5는 불량이다.
- `n = 1`, 처음 불량이 1 → `1`.

**풀이.**
1. 버전을 늘어놓으면 `정상 정상 정상 불량 불량`처럼 앞은 모두 정상, 뒤는 모두
   불량이다. 찾는 것은 처음 불량인 자리다.
2. `mid`가 불량이면 답은 mid이거나 그 왼쪽이다. mid가 답일 수도 있으니 버리지 않고
   `high = mid`.
3. `mid`가 정상이면 답은 mid의 오른쪽이다 → `low = mid + 1`.
4. `low == high`가 되면 범위에 하나만 남았고, 그것이 답이다.

`n = 5`, 처음 불량이 4일 때:

| low | high | mid | 불량? | 다음 |
|---|---|---|---|---|
| 1 | 5 | 3 | 아니오 | `low = 4` |
| 4 | 5 | 4 | 예 | `high = 4` |
| 4 | 4 | | | 끝 → `4` |

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

시간 O(log n), 공간 O(1). 짝을 맞춘다: `high = mid - 1`은 `while low <= high`와 함께,
`high = mid`는 `while low < high`와 내림과 함께 쓴다.

### Stack
- **단서:** 괄호 짝; 다음으로 큰 값
- **방법:** 아직 짝(답)을 기다리는 것을 쌓아 두고, 짝이 오면 pop한다
- **왜 빠른가:** 짝을 찾으려고 매번 앞을 다시 뒤지면 O(n²). 기다리는 것만 쌓아 두면
  짝은 항상 맨 위에 있으니 O(n).
- **같은 기법:** Daily Temperatures, Valid Parentheses

#### 예: Valid Parentheses (20, Easy)

**문제.** `(`, `)`, `[`, `]`, `{`, `}`로만 된 문자열 `s`가 주어진다. 모든 여는 괄호가
같은 종류의 닫는 괄호로, 올바른 순서로 닫히면 `True`를 반환한다. 닫는 괄호마다 짝이
되는 여는 괄호가 있어야 한다.

- `s = "()[]{}"` → `True`.
- `s = "([])"` → `True`. 안쪽 `[]`가 먼저 닫히고, 그다음 `()`가 닫힌다.
- `s = "([)]"` → `False`. `[`가 마지막에 열렸는데 `)`가 먼저 왔다.

**풀이.**
1. 닫는 괄호는 가장 마지막에 열린, 아직 안 닫힌 괄호와 짝이어야 한다.
2. 그래서 여는 괄호를 stack에 쌓는다. 맨 위가 가장 마지막에 열린 괄호다.
3. 닫는 괄호가 오면 맨 위를 pop해서 짝이 맞는지 본다. Stack이 비었거나 짝이 틀리면
   `False`.
4. 끝까지 읽은 뒤 stack에 여는 괄호가 남아 있으면 안 닫힌 것이니 `False`.

`s = "([)]"`일 때:

| ch | 하는 일 | stack (오른쪽이 맨 위) |
|---|---|---|
| `(` | push | `(` |
| `[` | push | `( [` |
| `)` | pop한 `[`는 `)`의 짝 `(`가 아니다 → `False` | `(` |

`s = "([])"`라면 `]`에서 `[`를, `)`에서 `(`를 pop해 짝이 맞고, 끝에 stack이 비어서
`True`다.

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

시간 O(n), 공간 O(n). n = `len(s)`.

### Heap
- **단서:** 가장 큰, 작은, 가까운 k개
- **방법:** 크기를 k로 유지하는 Heap. `heapq`는 Min Heap이라 맨 위가 가장 작은 값이다.
- **왜 빠른가:** 매번 정렬하면 O(n log n). Heap에 넣고 빼기는 O(log k).
- **같은 기법:** Kth Largest Element in an Array, K Closest Points to Origin, Last
  Stone Weight

#### 예: Kth Largest Element in a Stream (703, Easy)

**문제.** `KthLargest(k, nums)` class를 만든다. 처음에는 `nums`의 수들로 시작한다.
`add(val)`이 불릴 때마다 `val`을 넣고, 지금까지 들어온 모든 수 중 k번째로 큰 수를
반환한다. 같은 수도 따로 센다.

- `k = 3, nums = [4, 5, 8, 2]`에서 `add(3)` → `4`. 수는 2, 3, 4, 5, 8이고, 큰
  순서로 8, 5, 4다.
- 이어서 `add(5)` → `5`, `add(10)` → `5`, `add(9)` → `8`, `add(4)` → `8`.

**풀이.**
1. k번째로 큰 수를 알려면 가장 큰 k개만 있으면 된다. 그보다 작은 수는 앞으로도 답이
   될 수 없다.
2. 가장 큰 k개를 Min Heap에 둔다. 그러면 맨 위 `heap[0]`이 k개 중 가장 작은 수, 곧
   k번째로 큰 수다.
3. 새 수를 넣어 k + 1개가 되면, 가장 작은 것을 pop해서 다시 k개로 맞춘다.

`k = 3`일 때 (heap 안의 수를 작은 순서로 적었다):

| 호출 | 넣은 뒤 | pop | 남은 heap | 반환 |
|---|---|---|---|---|
| 처음 `[4, 5, 8, 2]` | 2, 4, 5, 8 | 2 | 4, 5, 8 | |
| `add(3)` | 3, 4, 5, 8 | 3 | 4, 5, 8 | 4 |
| `add(5)` | 4, 5, 5, 8 | 4 | 5, 5, 8 | 5 |
| `add(10)` | 5, 5, 8, 10 | 5 | 5, 8, 10 | 5 |
| `add(9)` | 5, 8, 9, 10 | 5 | 8, 9, 10 | 8 |

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

`add` 한 번에 시간 O(log k), 공간 O(k).

### DFS, BFS
- **단서:** Grid의 영역, 퍼져 나가는 것, 최소 이동 횟수
- **방법:** 칸을 방문하면 표시하고, 이웃 칸을 방문한다. 최소 이동 횟수가 필요하면
  BFS(queue)를 쓴다.
- **왜 빠른가:** 방문 표시 덕에 칸마다 한 번만 본다, O(rows × cols). BFS는 가까운
  칸부터 보니, 목표에 처음 닿을 때가 최소 이동이다.
- **같은 기법:** Number of Islands, Max Area of Island, Rotting Oranges

#### 예 1, DFS: Flood Fill (733, Easy)

**문제.** 2D grid `image`의 각 칸에는 색을 뜻하는 정수가 있다. 시작 칸 `(sr, sc)`와
새 색 `color`가 주어진다. 시작 칸, 그리고 시작 칸과 상하좌우로 이어진 같은 색의 칸을
모두 `color`로 바꾼 `image`를 반환한다. 그림판의 페인트 통 도구와 같다.

- `image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, color = 2` →
  `[[2, 2, 2], [2, 2, 0], [2, 0, 1]]`. 오른쪽 아래의 `1`은 `0`에 막혀 시작 칸과
  이어지지 않으니 그대로다.
- `image = [[0, 0, 0], [0, 0, 0]], sr = 0, sc = 0, color = 0` → 그대로. 이미 그
  색이다.

**풀이.**
1. 시작 칸의 원래 색 `old`를 기억한다.
2. `dfs(r, c)`는 그 칸이 grid 안이고 색이 `old`일 때만 칠한 뒤, 상하좌우 네 칸에 다시
   `dfs`를 부른다.
3. 칠한 칸은 색이 `old`가 아니게 되니 다시 칠하지 않는다. 칠하는 것이 방문 표시를
   겸한다.
4. `old == color`면 칠해도 색이 그대로라 같은 칸을 끝없이 다시 부르니, 처음에 그냥
   반환한다.

예 1에서 칠하는 순서 (숫자가 순서, `·`은 칠하지 않은 칸). 아래, 위, 오른쪽, 왼쪽
순서로 부르니 (1, 1)에서 시작해 위로 올라간 뒤 왼쪽 column을 타고 내려간다:

```text
4 2 3
5 1 ·
6 · ·
```

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

시간 O(rows × cols), 공간 O(rows × cols) (recursion 깊이).

#### 예 2, BFS: 미로 최단 거리 (예시 문제)

**문제.** 문자열 list `grid`가 주어진다. `"."`은 지나갈 수 있는 칸, `"#"`은 벽이다.
왼쪽 위 `(0, 0)`에서 시작해 상하좌우로 한 칸씩 움직일 때, 오른쪽 아래 칸까지 가는 가장
적은 이동 횟수를 반환한다. 갈 수 없으면 `-1`. 시작 칸은 항상 `"."`이다.

- `grid = ["..#", "#..", "#.."]` → `4`.
- `grid = [".#", "#."]` → `-1`. 벽에 막혀 못 간다.

**풀이.**
1. Queue에 시작 칸을 넣는다. Queue에는 다음에 볼 칸이 거리 순서대로 들어 있다.
2. `for _ in range(len(queue))`로 지금 거리의 칸을 모두 꺼낸다. 꺼낸 칸이 목표면
   지금 `steps`가 답이다.
3. 꺼낸 칸의 이웃 중 grid 안이고, 벽이 아니고, 아직 안 넣은 칸을 queue에 넣는다.
   넣을 때 `seen`에 표시해서 같은 칸을 두 번 넣지 않는다.
4. 한 거리의 칸을 다 보면 `steps += 1`. 가까운 칸부터 보니, 목표에 처음 닿을 때가 최소
   이동이다.

예 1에서 각 칸까지의 거리. 0인 칸, 1인 칸, 2인 칸… 순서로 퍼지고, 오른쪽 아래에 닿을
때 `steps = 4`다:

```text
0 1 #
# 2 3
# 3 4
```

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

시간 O(rows × cols), 공간 O(rows × cols).

### Dijkstra
- **단서:** edge에 cost가 있는 Graph의 최단 경로 (cost는 음수가 아님)
- **방법:** Heap에서 가장 가까운 node를 꺼내고, 그 node의 edge를 하나씩 시도한다
- **왜 맞는가:** 가장 가까운 node부터 꺼내면, 그 거리는 다른 길로 더 짧아질 수 없다.
  Cost가 모두 1이면 BFS로 충분하다.
- **같은 기법:** Network Delay Time

#### 예: Network Delay Time (743, Medium)

**문제.** Node는 `1`부터 `n`까지다. `times[i] = [u, v, w]`는 node `u`에서 `v`로
신호가 가는 데 `w`가 걸린다는 뜻이다 (한 방향 edge). Node `k`에서 신호를 보냈을 때,
모든 node가 신호를 받는 데 걸리는 최소 시간을 반환한다. 받지 못하는 node가 있으면
`-1`.

- `times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], n = 4, k = 2` → `2`. Node 1과 3은
  시간 1에, node 4는 2 → 3 → 4로 시간 2에 받는다.
- `times = [[1, 2, 1]], n = 2, k = 2` → `-1`. 2에서 1로 가는 edge가 없다.

**풀이.**
1. `dist[v]`는 지금까지 찾은 k → v의 가장 짧은 시간이다. 처음에는 `dist[k] = 0`.
2. Heap에서 `d`가 가장 작은 `(d, u)`를 꺼낸다. Cost가 음수가 아니니 u까지 이보다 짧은
   길은 더 없다.
3. u에서 나가는 edge `u → v`마다 `d + cost`가 `dist[v]`보다 짧으면 고치고 heap에
   넣는다.
4. 같은 node가 heap에 여러 번 들어갈 수 있다. 꺼낸 `d`가 `dist[u]`보다 크면 더 짧은
   길을 이미 찾은 옛날 기록이니 건너뛴다.
5. 모든 node의 `dist` 중 가장 큰 값이 답이다. `dist`에 없는 node가 있으면 `-1`.

바로 가는 길보다 돌아가는 길이 짧은 작은 예:
`times = [[1, 2, 4], [1, 3, 1], [3, 2, 1]], n = 3, k = 1` → `2`.

| 꺼낸 (d, u) | 하는 일 | dist |
|---|---|---|
| (0, 1) | node 2는 0 + 4 = 4, node 3은 0 + 1 = 1로 적는다 | 1: 0, 2: 4, 3: 1 |
| (1, 3) | node 2는 1 + 1 = 2 < 4라서 고친다 | 1: 0, 2: 2, 3: 1 |
| (2, 2) | 나가는 edge가 없다 | 그대로 |
| (4, 2) | 4 > dist[2] = 2, 옛날 기록이라 건너뛴다 | 그대로 |

답은 `max(0, 2, 1) = 2`.

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

시간 O(E log E), 공간 O(n + E). E = edge 수(`len(times)`). Edge마다 Heap에 최대 한 번
넣는다.

### Tree Recursion
- **단서:** Binary Tree
- **방법:** 왼쪽과 오른쪽 subtree의 답을 구해 합친다. Level별로 보려면 위의 BFS 틀을
  쓴다.
- **같은 기법:** Validate Binary Search Tree, Invert Binary Tree, Diameter of Binary
  Tree, Binary Tree Level Order Traversal

#### 예: Maximum Depth of Binary Tree (104, Easy)

**문제.** Binary tree의 `root`가 주어진다. Root에서 가장 먼 leaf까지 가는 경로에 있는
node 수(depth)를 반환한다. LeetCode는 tree를 위에서부터 한 줄씩 읽은 list로 보여
준다. `null`은 빈 자리다.

- `root = [3, 9, 20, null, null, 15, 7]` → `3`. 아래 tree에서 3 → 20 → 15
  (또는 7)다.
- `root = []` → `0`.

```text
    3
   / \
  9   20
     /  \
    15   7
```

**풀이.**
1. 빈 tree의 depth는 0이다 (base case).
2. 그 밖의 tree의 depth = 1 (자기 자신) + 왼쪽 subtree와 오른쪽 subtree 중 더 깊은 쪽.
3. 왼쪽과 오른쪽의 답은 같은 함수를 다시 불러서 구한다. 가장 아래의 작은 tree부터
   답이 돌아온다.

위 tree에서는 아래부터 이렇게 계산된다:
- `max_depth(9)` = 1 + max(0, 0) = 1. 15와 7도 1이다.
- `max_depth(20)` = 1 + max(1, 1) = 2.
- `max_depth(3)` = 1 + max(1, 2) = 3.

```python
def max_depth(node):
    if not node:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))
```

시간 O(n), 공간 O(h). n = node 수, h = tree 높이 (recursion 깊이).

### Backtracking
- **단서:** 모든 subset이나 모든 순서, n ≤ 20
- **방법:** 하나를 고르고, recursion하고, 되돌린 뒤 다음 것을 고른다
- **왜 되는가:** n ≤ 20이면 2ⁿ ≈ 10⁶이라 전부 만들어 봐도 시간 안에 든다.
- **같은 기법:** Subsets, Permutations

#### 예: Subsets (78, Medium)

**문제.** 값이 모두 다른 정수 배열 `nums`가 주어진다. 가능한 모든 subset(빈 집합
포함)을 반환한다. 순서는 상관없고, 같은 subset이 두 번 나오면 안 된다.

- `nums = [1, 2, 3]` → `[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]`.
  2³ = 8개다.
- `nums = [0]` → `[[], [0]]`.

**풀이.**
1. `path`는 지금까지 고른 수다. `backtrack(start)`는 지금의 `path`를 결과에 넣고,
   `start`부터의 수를 하나씩 더 골라 본다.
2. 하나를 고르면 그 수보다 뒤의 수만 다음 후보로 넘긴다(`i + 1`). 그래서 `[1, 2]`와
   `[2, 1]`처럼 같은 subset이 두 번 나오지 않는다.
3. 다녀온 뒤 `path.pop()`으로 고른 수를 빼야, 같은 `path`로 다음 후보를 시도할 수
   있다.
4. `path[:]`로 복사해서 넣는다. `path`를 그대로 넣으면 나중에 pop할 때 결과 안의
   list도 같이 바뀐다.

`nums = [1, 2, 3]`일 때 `backtrack` 호출 하나가 node 하나다. 위에서부터 이 순서로
결과에 들어간다:

```text
[]
├── [1]
│   ├── [1, 2]
│   │   └── [1, 2, 3]
│   └── [1, 3]
├── [2]
│   └── [2, 3]
└── [3]
```

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

시간 O(n × 2ⁿ): subset이 2ⁿ개이고 하나를 복사하는 데 최대 n.

### Sort, then Merge
- **단서:** 겹치는 interval
- **방법:** start로 sort한다. 다음 interval이 지금 interval이 끝나기 전에 시작하면
  merge한다.
- **왜 빠른가:** 정렬해 두면 겹칠 수 있는 것은 바로 앞 interval뿐이다. 모든 쌍을
  비교하는 O(n²)이 정렬 O(n log n)이 된다.
- **같은 기법:** Merge Intervals, Insert Interval, Non-overlapping Intervals

#### 예: Merge Intervals (56, Medium)

**문제.** `intervals[i] = [start, end]`의 list가 주어진다. 겹치는 interval을 모두
합쳐, 서로 겹치지 않는 interval의 list를 반환한다. 한 interval의 끝과 다른 interval의
시작이 같아도 겹친다고 본다.

- `[[1, 3], [2, 6], [8, 10], [15, 18]]` → `[[1, 6], [8, 10], [15, 18]]`.
  `[1, 3]`과 `[2, 6]`이 겹친다.
- `[[1, 4], [4, 5]]` → `[[1, 5]]`.

**풀이.**
1. start 순으로 정렬한다. 그러면 지금 interval과 겹칠 수 있는 것은 `merged`의 마지막
   interval뿐이다.
2. 지금 interval의 start가 마지막 interval의 end 이하면 겹친다. 마지막 interval의
   end를 둘 중 큰 end로 바꾼다. `[1, 10]` 다음 `[2, 3]`처럼 안에 쏙 들어가는 경우가
   있어서 `max`를 쓴다.
3. 안 겹치면 새 interval로 `merged`에 붙인다.

`[[1, 3], [2, 6], [8, 10], [15, 18]]`일 때:

| interval | `merged`의 마지막 | 겹치나 | `merged` |
|---|---|---|---|
| `[1, 3]` | | 처음 | `[[1, 3]]` |
| `[2, 6]` | `[1, 3]` | 2 ≤ 3, 예 | `[[1, 6]]` |
| `[8, 10]` | `[1, 6]` | 8 > 6, 아니오 | `[[1, 6], [8, 10]]` |
| `[15, 18]` | `[8, 10]` | 15 > 10, 아니오 | `[[1, 6], [8, 10], [15, 18]]` |

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

시간 O(n log n), 공간 O(n). n = interval 수.

### Linked List
- **단서:** Linked List
- **방법:** Dummy node를 두면 head를 따로 처리하지 않아도 된다. Slow/fast pointer는
  fast가 2칸, slow가 1칸씩 간다.
- **같은 기법:** Reverse Linked List, Middle of the Linked List, Remove Nth Node From
  End of List

#### 예: Linked List Cycle (141, Easy)

**문제.** Linked list의 `head`가 주어진다. `next`를 계속 따라가다 이미 지난 node로
돌아오면 cycle이 있는 것이다. Cycle이 있으면 `True`, 없으면 `False`를 반환한다.

- `3 → 2 → 0 → -4`이고 `-4`의 `next`가 다시 `2` → `True`.
- `1` 하나뿐이고 `next`가 없음 → `False`.

**풀이.**
1. `slow`는 한 칸씩, `fast`는 두 칸씩 간다.
2. Cycle이 없으면 `fast`가 먼저 끝(`None`)에 닿는다 → `False`.
3. Cycle이 있으면 둘 다 cycle 안을 계속 돈다. 한 번 움직일 때마다 `fast`가 `slow`에
   한 칸씩 가까워지니 언젠가 같은 node에서 만난다 → `True`.
4. 본 node를 set에 저장해도 풀리지만 공간이 O(n)이다. 두 pointer는 O(1).

`3 → 2 → 0 → -4 → (다시 2)`일 때:

| 움직인 횟수 | slow | fast |
|---|---|---|
| 0 | 3 | 3 |
| 1 | 2 | 0 |
| 2 | 0 | 2 |
| 3 | -4 | -4 → 만남, `True` |

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:  # cycle 안에서 fast가 slow를 따라잡았다
            return True
    return False
```

시간 O(n), 공간 O(1). n = node 수.

### Dynamic Programming (DP)
- **단서:** 방법의 수; 가장 적은, 많은, 좋은 합계; "X를 만들 수 있나?"; 각 선택이
  앞의 선택에 달려 있다
- **방법:** 코드를 쓰기 전에 네 가지에 답한다.
  1. `dp[i]`는 무엇인가? "i번째 계단까지 오는 방법의 수"처럼 말로 한다.
  2. `dp[i]`를 더 작은 답으로 어떻게 만드나(점화식)? 마지막 선택을 본다.
  3. Base case는 무엇인가? `dp[0]` 같은 것.
  4. 답은 어디 있나? `dp[n]`인가, `max(dp)`인가?
- **왜 빠른가:** 그냥 recursion은 같은 작은 문제를 계속 다시 푼다 (Climbing Stairs는
  O(2ⁿ)). 답을 표에 저장하면 작은 문제마다 한 번만 푼다 (O(n)).

| 유형 | 예시 문제 | `dp`의 뜻 | 점화식 |
|---|---|---|---|
| 한 줄 | Climbing Stairs | `dp[i]` = i번째 계단까지 오는 방법 수 | `dp[i] = dp[i - 1] + dp[i - 2]` |
| 한 줄 | House Robber | `dp[i]` = 0번부터 i번 집까지에서 털 수 있는 최대 | `dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])` |
| i에서 끝남 | LIS | `dp[i]` = 정확히 i에서 끝나는 LIS 길이 | `nums[j] < nums[i]`인 j마다 `dp[j] + 1` 중 최대 |
| 문자열 자르기 | Word Break | `dp[i]` = `s[:i]`를 단어로 나눌 수 있나 | `dp[j]`가 True이고 `s[j:i]`가 단어인 j가 있나 |
| 합 만들기 | Combination Sum IV | `dp[a]` = 합 a를 만드는 방법 수 | num마다 `dp[a - num]`을 더한다 |
| 한 번씩만 | Partition Equal Subset Sum | `dp[s]` = 합 s를 만들 수 있나 | `dp[s] = dp[s] or dp[s - num]`, s는 큰 쪽부터 |
| Grid | Unique Paths | `dp[r][c]` = (r, c)까지 경로 수 | `dp[r][c] = dp[r - 1][c] + dp[r][c - 1]` |
| 두 문자열 | LCS | `dp[i][j]` = `a[:i]`와 `b[:j]`의 LCS 길이 | 마지막 글자가 같으면 `dp[i - 1][j - 1] + 1`, 다르면 `max(dp[i - 1][j], dp[i][j - 1])` |

#### 한 줄: Climbing Stairs (70, Easy)

**문제.** 계단이 `n`칸 있다. 한 번에 1칸이나 2칸을 오를 수 있다. 꼭대기까지 오르는
서로 다른 방법의 수를 반환한다.

- `n = 2` → `2`. 1 + 1, 2.
- `n = 3` → `3`. 1 + 1 + 1, 1 + 2, 2 + 1.

**풀이.**
1. `dp[i]` = i번째 계단까지 오는 방법의 수.
2. i번째 계단에 오는 마지막 움직임은 i - 1에서 1칸이거나 i - 2에서 2칸이다. 그래서
   `dp[i] = dp[i - 1] + dp[i - 2]`.
3. Base case: `dp[0] = 1` (아무것도 안 하는 1가지), `dp[1] = 1`.
4. 답은 `dp[n]`.

| i | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| dp[i] | 1 | 1 | 2 | 3 | 5 | 8 |

```python
def climb_stairs(n):
    dp = [0] * (n + 1)  # dp[i] = i번째 계단까지 오는 방법 수
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # 마지막에 1칸 올랐거나, 2칸 올랐거나
    return dp[n]
```

시간 O(n), 공간 O(n).

같은 문제를 top-down으로: 그냥 recursion을 쓰고 `@cache`를 붙인다. `ways(5)`는
`ways(4)`와 `ways(3)`을 부르고, `ways(4)`도 `ways(3)`을 부른다. `@cache`가 없으면 같은
계산을 계속 반복해 O(2ⁿ)이고, 있으면 두 번째부터는 저장된 답을 돌려줘서 O(n)이다.
파이썬은 recursion이 약 1,000번 깊어지면 멈추니, n이 크면 위의 표로 쓴다.

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

#### 한 줄, 변수 두 개로: House Robber (198, Medium)

**문제.** 한 줄로 선 집들에 돈이 있다. `nums[i]`는 i번째 집의 돈이다. 바로 옆 두 집을
같은 밤에 털면 경보가 울린다. 경보 없이 털 수 있는 돈의 최댓값을 반환한다.

- `nums = [1, 2, 3, 1]` → `4`. 1 + 3.
- `nums = [2, 7, 9, 3, 1]` → `12`. 2 + 9 + 1.

**풀이.**
1. `dp[i]` = 0번부터 i번 집까지에서 털 수 있는 최댓값.
2. i번 집을 털지 않으면 `dp[i - 1]`. 털면 i - 1번 집은 못 터니 `dp[i - 2] + nums[i]`.
   둘 중 큰 것.
3. `dp[i]`는 바로 앞 두 값만 쓰니 list 대신 `prev2`(= `dp[i - 2]`)와
   `prev1`(= `dp[i - 1]`) 두 변수면 된다. 처음에는 둘 다 0.
4. 답은 마지막 `prev1`.

`nums = [2, 7, 9, 3, 1]`일 때:

| num | 건너뛰기 (`prev1`) | 털기 (`prev2 + num`) | 새 `prev1` |
|---|---|---|---|
| 2 | 0 | 0 + 2 = 2 | 2 |
| 7 | 2 | 0 + 7 = 7 | 7 |
| 9 | 7 | 2 + 9 = 11 | 11 |
| 3 | 11 | 7 + 3 = 10 | 11 |
| 1 | 11 | 11 + 1 = 12 | 12 |

```python
def rob(nums):
    prev2 = prev1 = 0  # 두 집 전까지의 최선, 한 집 전까지의 최선
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)  # 이 집을 건너뛰거나, 털거나
    return prev1
```

시간 O(n), 공간 O(1).

#### i에서 끝남: Longest Increasing Subsequence (300, Medium)

**문제.** 정수 배열 `nums`가 주어진다. 가장 긴 strictly increasing subsequence의
길이를 반환한다. Subsequence는 순서를 지키면서 몇 개를 지운 것이다. 연속일 필요는 없다.

- `nums = [10, 9, 2, 5, 3, 7, 101, 18]` → `4`. 예를 들어 `[2, 3, 7, 101]`.
- `nums = [7, 7, 7, 7]` → `1`. 같은 값은 증가가 아니다.

**풀이.**
1. `dp[i]` = 정확히 `nums[i]`로 끝나는 가장 긴 increasing subsequence의 길이.
2. `nums[i]` 바로 앞에 올 수 있는 것은 더 작은 `nums[j]` (j < i)다. 그 중 가장 긴 것
   뒤에 붙인다: `dp[i] = dp[j] + 1` 중 최대.
3. Base case: 모든 `dp[i] = 1` (자기 혼자).
4. 답은 어디서 끝나도 되니 `max(dp)`.

| i | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| nums[i] | 10 | 9 | 2 | 5 | 3 | 7 | 101 | 18 |
| dp[i] | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 4 |
| 뒤에 붙은 수 | | | | 2 | 2 | 5나 3 | 7 | 7 |

답은 `max(dp) = 4`.

```python
def length_of_lis(nums):
    dp = [1] * len(nums)  # dp[i] = 정확히 i에서 끝나는 가장 긴 increasing subsequence
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:  # nums[i]를 nums[j] 뒤에 붙일 수 있다
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

시간 O(n²), 공간 O(n).

#### 문자열 자르기: Word Break (139, Medium)

**문제.** 문자열 `s`와 단어 list `word_dict`가 주어진다. `s`를 사전에 있는 단어로만
빈틈없이 나눌 수 있으면 `True`를 반환한다. 같은 단어를 여러 번 써도 된다.

- `s = "leetcode", word_dict = ["leet", "code"]` → `True`. "leet" + "code".
- `s = "applepenapple", word_dict = ["apple", "pen"]` → `True`. "apple"을 두 번
  쓴다.
- `s = "catsandog", word_dict = ["cats", "dog", "sand", "and", "cat"]` → `False`.

**풀이.**
1. `dp[i]` = 앞의 i글자 `s[:i]`를 단어로 나눌 수 있나.
2. `s[:i]`의 마지막 단어가 `s[j:i]`라면, 그 앞 `s[:j]`도 나눌 수 있어야 한다. 그런
   j가 하나라도 있으면 `dp[i] = True`.
3. Base case: `dp[0] = True` (빈 문자열).
4. 답은 `dp[len(s)]`.

`s = "leetcode"`일 때 `True`가 되는 자리는 둘뿐이다:
- `dp[4]`: `dp[0]`이 True이고 `s[0:4] = "leet"`가 단어.
- `dp[8]`: `dp[4]`가 True이고 `s[4:8] = "code"`가 단어. → 답 `True`.

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

시간 O(n³): (j, i) 쌍이 n²개이고 `s[j:i]`를 자르는 데 최대 n. 공간 O(n).

#### 합 만들기: Combination Sum IV (377, Medium)

**문제.** 서로 다른 양의 정수 배열 `nums`와 `target`이 주어진다. `nums`의 수를 몇
번이든 골라 차례로 더해 `target`을 만드는 방법의 수를 반환한다. 순서가 다르면 다른
방법이다. `nums = [1, 2]`이면 Climbing Stairs와 같은 문제다.

- `nums = [1, 2, 3], target = 4` → `7`. 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3,
  3+1.
- `nums = [9], target = 3` → `0`.

**풀이.**
1. `dp[a]` = 합 a를 만드는 방법 수.
2. 마지막에 더한 수가 `num`이면, 그 앞까지는 합 `a - num`을 만든 것이다. 그래서 num
   마다 `dp[a - num]`을 더한다.
3. Base case: `dp[0] = 1` (아무것도 안 더하는 1가지).
4. 답은 `dp[target]`.

`nums = [1, 2, 3], target = 4`일 때:

| a | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 계산 | | dp[0] | dp[1] + dp[0] | dp[2] + dp[1] + dp[0] | dp[3] + dp[2] + dp[1] |
| dp[a] | 1 | 1 | 2 | 4 | 7 |

```python
def combination_sum4(nums, target):
    dp = [1] + [0] * target  # dp[a] = 합 a를 만드는 방법 수; 0은 아무것도 안 쓰는 1가지
    for a in range(1, target + 1):
        for num in nums:
            if num <= a:
                dp[a] += dp[a - num]  # 마지막에 쓴 수가 num
    return dp[target]
```

시간 O(target × len(nums)), 공간 O(target).

#### 한 번씩만: Partition Equal Subset Sum (416, Medium)

**문제.** 양의 정수 배열 `nums`가 주어진다. 모든 수를 두 묶음으로 나눠, 두 묶음의 합이
같게 할 수 있으면 `True`를 반환한다.

- `nums = [1, 5, 11, 5]` → `True`. `[1, 5, 5]`와 `[11]`, 둘 다 합이 11이다.
- `nums = [1, 2, 3, 5]` → `False`. 전체 합 11이 홀수다.

**풀이.**
1. 두 묶음의 합이 같으려면 각각 전체 합의 절반이어야 한다. 합이 홀수면 바로 `False`.
   아니면 "몇 개를 골라 합 `target`(= 절반)을 만들 수 있나?"로 바뀐다.
2. `dp[s]` = 지금까지 본 수 중 몇 개로 합 s를 만들 수 있나. `dp[0] = True`.
3. 새 수 `num`을 볼 때, 합 s는 num 없이 이미 만들 수 있거나(`dp[s]`), num을 더해서
   만들 수 있다(`dp[s - num]`).
4. s를 큰 쪽부터 내려가야 한다. 작은 쪽부터 올라가면 이번 num으로 방금 True가 된
   `dp[s - num]`을 다시 써서 같은 수를 두 번 쓴다. 예: `nums = [5]`인데 올라가면
   `dp[5]`가 True가 된 뒤 `dp[10]`도 `dp[5]`를 보고 True가 된다.

`nums = [1, 5, 11, 5]`, target = 11일 때 만들 수 있는 합:

| 본 수 | `dp[s]`가 True인 s |
|---|---|
| 처음 | 0 |
| 1 | 0, 1 |
| 5 | 0, 1, 5, 6 |
| 11 | 0, 1, 5, 6, 11 → 11을 만들 수 있다 |
| 5 | 0, 1, 5, 6, 10, 11 |

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

시간 O(n × target), 공간 O(target). n = `len(nums)`, target = 전체 합의 절반.

#### Grid: Unique Paths (62, Medium)

**문제.** `m × n` grid의 왼쪽 위 칸에 로봇이 있다. 로봇은 한 번에 오른쪽이나 아래로
한 칸만 움직인다. 오른쪽 아래 칸까지 가는 서로 다른 경로의 수를 반환한다.

- `m = 3, n = 2` → `3`. 오른쪽→아래→아래, 아래→오른쪽→아래, 아래→아래→오른쪽.
- `m = 3, n = 7` → `28`.

**풀이.**
1. `dp[r][c]` = (r, c)까지 가는 경로 수.
2. (r, c)에는 위 칸이나 왼쪽 칸에서만 온다. 그래서 `dp[r][c] = dp[r - 1][c] +
   dp[r][c - 1]`.
3. Base case: 맨 위 row와 맨 왼쪽 column은 한 방향으로만 갈 수 있으니 모두 1.
4. 답은 오른쪽 아래 `dp[m - 1][n - 1]`.

`m = 3, n = 3`일 때 `dp` (답 6):

```text
1 1 1
1 2 3
1 3 6
```

```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]  # dp[r][c] = (r, c)까지 가는 경로 수; 맨 위 row와 맨 왼쪽 column은 1
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]  # 위에서 왔거나, 왼쪽에서 왔거나
    return dp[-1][-1]
```

시간 O(m × n), 공간 O(m × n).

#### 두 문자열: Longest Common Subsequence (1143, Medium)

**문제.** 두 문자열 `a`, `b`가 주어진다 (LeetCode에서는 `text1`, `text2`). 둘 다의
subsequence인 문자열 중 가장 긴 것의 길이를 반환한다. 없으면 `0`.

- `a = "abcde", b = "ace"` → `3`. `"ace"`.
- `a = "abc", b = "def"` → `0`.

**풀이.**
1. `dp[i][j]` = `a`의 앞 i글자와 `b`의 앞 j글자의 LCS 길이.
2. 마지막 글자 `a[i - 1]`과 `b[j - 1]`이 같으면, 그 글자를 LCS의 끝에 쓴다:
   `dp[i - 1][j - 1] + 1`.
3. 다르면 둘 중 하나는 LCS에 못 쓴다. `a`에서 한 글자를 뺀 답과 `b`에서 뺀 답 중 큰
   것.
4. Base case: row 0과 column 0은 빈 문자열이라 0. 답은 `dp[len(a)][len(b)]`.

`a = "abcde", b = "ace"`일 때 `dp` (답은 오른쪽 아래 3):

| | "" | a | c | e |
|---|---|---|---|---|
| **""** | 0 | 0 | 0 | 0 |
| **a** | 0 | 1 | 1 | 1 |
| **b** | 0 | 1 | 1 | 1 |
| **c** | 0 | 1 | 2 | 2 |
| **d** | 0 | 1 | 2 | 2 |
| **e** | 0 | 1 | 2 | 3 |

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

시간 O(len(a) × len(b)), 공간도 같다.

---

## Python 도구

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
from collections import Counter, defaultdict
count = Counter("banana")                      # {"a": 3, "n": 2, "b": 1}; 없는 key는 0
total = defaultdict(int)                       # total[key] += x
groups = defaultdict(list)                     # groups[key].append(x)

# 정렬
sorted(rows, key=lambda r: (-r[1], r[0]))      # 점수 높은 순, 같으면 이름 A→Z
nums.sort()                                    # 제자리 정렬, None을 반환한다

# Max Heap: heapq는 Min Heap이라 음수로 넣고 꺼낼 때 다시 뒤집는다
import heapq
heapq.heappush(heap, -x)
largest = -heapq.heappop(heap)

# 올림 나눗셈, 양의 정수일 때
-(-a // b)                                     # a / b를 올림

# 모든 쌍, 순서, 조합
from itertools import combinations, permutations, product

# 정렬된 list에서 개수 세기
from bisect import bisect_left, bisect_right
bisect_right(a, x) - bisect_left(a, x)         # a에 x가 몇 개 있나
```

---

## 제출 전 체크

- **Edge case:** 빈 입력, 원소 하나, 모두 같은 값, 음수와 0, 가장 큰 입력.
- **답이 없을 때:** 문제가 정한 값(`-1`, `[]`, `False`)을 반환하나?
- **Index 범위:** `range(n)`은 n - 1까지, `s[i:j]`는 j 앞까지다.
- **2D list:** `[[0] * cols for _ in range(rows)]`로 만든다. `[[0] * cols] * rows`는
  모든 row가 같은 list라서 한 칸을 바꾸면 그 column 전체가 바뀐다.
- **Recursion 깊이:** 파이썬은 약 1,000번에서 멈춘다. 입력이 크면 BFS나 반복문으로
  바꾼다.
