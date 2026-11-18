# Number of Recent Calls — Easy (#933)
# https://leetcode.com/problems/number-of-recent-calls/

r"""
Build a RecentCounter class that counts the requests made in a recent time window.

  - RecentCounter() starts the counter with no requests.
  - ping(t) records a new request at time t, in milliseconds, and returns how many
    requests happened in the past 3000 milliseconds, including this one. That is,
    it counts the requests in the inclusive range [t - 3000, t].

Each call to ping uses a strictly larger t than the call before.

Example 1:
    Input
    ["RecentCounter", "ping", "ping", "ping", "ping"]
    [[], [1], [100], [3001], [3002]]
    Output
    [null, 1, 2, 3, 3]
    Explanation
    counter = RecentCounter()
    counter.ping(1)     # requests [1], range [-2999, 1], returns 1
    counter.ping(100)   # requests [1, 100], range [-2900, 100], returns 2
    counter.ping(3001)  # requests [1, 100, 3001], range [1, 3001], returns 3
    counter.ping(3002)  # requests [1, 100, 3001, 3002], range [2, 3002], returns 3

Constraints:
  - 1 <= t <= 10^9
  - Each call to ping uses a strictly larger t than the call before.
  - At most 10^4 calls are made to ping."""


class RecentCounter:

    def __init__(self):
        raise NotImplementedError


    def ping(self, t: int) -> int:
        raise NotImplementedError



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

CASES = [
    (
        (
            ["RecentCounter", "ping", "ping", "ping", "ping"],
            [[], [1], [100], [3001], [3002]],
        ),
        [None, 1, 2, 3, 3],
    ),
]

if __name__ == "__main__":
    from leetcode import run_design

    run_design(RecentCounter, CASES)
