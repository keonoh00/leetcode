# AGENTS.md

Instructions for AI assistants working in this repo.

The user is practicing for a live DS&A interview on Friday 2 October 2026. Each file
is one LeetCode problem: the statement, a `Solution` stub, and LeetCode's examples
as tests. Run one with:

```bash
uv run problems/<problem>.py
```

There are two folders:

- `daily/YYYY-MM-DD/` holds that day's set. Each file is named by its place in the
  set, then the LeetCode number, like `1_0136_single_number.py`. Problems are moved
  here from `problems/`.
- `problems/` holds everything else in one flat folder, named after the LeetCode
  number, padded to 4 digits, and the title in snake_case, like `0001_two_sum.py`.
  A second file for the same problem keeps that name and adds a suffix: `_resolve`
  for a re-solve, or the approach for another approach, like
  `0876_middle_of_the_linked_list_slow_fast.py`.

Keep things simple. Don't add tooling such as progress tracking, timers or prompts
unless the user asks for it.

## Re-solving

A `_resolve` file is a problem already solved, done again for practicing recall.
Don't review these, but test them and say in one line whether it's good or bad.
LeetCode hasn't accepted them, so the examples aren't enough. In a scratch script,
also compare against a simple brute force on many random small inputs, try the edge
cases the constraints allow (smallest input, largest values), and time a max-size
input. Good means all of that passes and it uses the idea the question is built
around, so one that would time out is bad. If it's bad, name an input that fails and
what it got against what it should get, or say that it's too slow, but don't say
what to change unless asked. Answer the user's questions, but skip
the understanding check. Commit only a good one, on its own, with the message
`Re-solve <Problem name>`.

## Reviewing a solution

The user brings solutions that LeetCode has already accepted, so don't re-test
correctness or edge cases; LeetCode does that. They don't need the best-known
approach, but be strict about two things:

1. **Understanding.** The solution uses the idea the question is built around,
   such as a hash map, two pointers or binary search, and the user could explain
   why it works. Brute force where the question is about a hash map, or an
   approach that only passes because LeetCode's inputs are small, fails this. If
   they needed a big hint, check that they can explain the idea, but don't ask
   for a second version of the solution; the user finds that too much.
2. **Clean code.** No waste an interviewer would call out: the same value computed
   several times, clumsy conversions such as `str()` of a list used as a key, or
   steps that do nothing. This is usually why LeetCode ranks a correct solution
   near the bottom, so a low "beats X%" is worth a look, though it's noisy.

If both hold, send a short ping and let them move on. If either fails, stop them
before they move on. In one short list, most important first, quote each piece of
code that's wrong, give its exact change, and say why in one plain sentence. Say
what's already right too, so they know what to leave alone. Don't rewrite the whole
solution, and don't circle with hints or analogies. Before sending the list, apply
it to a scratch copy and run it, so you know the next round is the last.

Exact changes count as a big hint, so check understanding before you pass it. Ask
two or three short questions, each with one concrete answer such as a list or a
number. Each one restates the input and quotes the code that runs. Open "why"
questions, and sentences with several blanks, have both confused the user.

Give the review in chat, not in the file. Quote code rather than giving line
numbers, because the user reads the chat without the file open beside it. The user
is new to time and space complexity, so say what n stands for and explain the "why"
in plain words. Time their version against faster ones only when they ask why it's
slow.

## Review template

When it passes both checks:

```markdown
**<Problem name>: good, move on.** <one line on the main idea it uses>
Time O(...), where n = <what n is>; space O(...). <one line on why>
Tip (optional): <a likely interview follow-up, or a handy Python idiom>
```

When it fails either one:

```markdown
**<Problem name>: not yet.** <one line on what's wrong>

- **What the question is teaching:** <the main idea; only when they missed it>
- **What to fix:** <quoted code → exact change, one line on why; most important first>
- **Already right:** <what to leave alone>
```

When the fixes are in but it needed a big hint, before passing:

```markdown
**<Problem name>: the code is done.** Before I commit it, for <the input>:

1. <What runs and why, quoting the code>. What is <one concrete thing>? (Write it like <format>.)
```

## Committing

Commit work once it's finished, without waiting to be asked:

- **A problem, once its review says "good, move on",** or the user says it's
  done. Commit only that file, with the message `Solve <Problem name>`, or
  `Improve <Problem name>` for a redo of one already committed. If the review says
  "not yet", don't commit it.
- **Other finished changes**, such as docs. Commit them on their own with a short
  message in the imperative, like `Add review template`.

Leave unfinished work uncommitted, and never sweep it into another commit. Commit
straight to the current branch; this is a solo practice repo, so there are no
feature branches. Don't push unless asked. Don't add Co-Authored-By lines or any
other AI attribution, because the user is the only author.
