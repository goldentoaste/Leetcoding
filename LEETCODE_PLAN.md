# LeetCode Interview Prep — Learning Plan

## Purpose

Build interview-specific problem-solving skill: classify a new problem by its structural cues, select a fitting pattern, state the invariant or state transition, and implement a correct solution in Python. The goal is not to memorize individual answers.

## Pace

- **Cadence:** 2 sessions per week × 60 minutes
- **Weekly output:** 2 Medium-level new problems (with an optional stretch) and 1–2 reviews
- **Timeline:** open-ended; progress by pattern mastery rather than a deadline
- **Language:** Python

## Session format

1. **Recall — 5 minutes:** State the pattern, invariant/state, and complexity for a previously solved problem without opening its solution.
2. **Attempt — 30–35 minutes:** Work one fresh problem. Write a brute-force direction first, then optimize.
3. **Learn and reimplement — 15–20 minutes:** If blocked, study the missing idea, close the reference, and write the solution yourself.
4. **Log — 5 minutes:** Add the result to `CURRENT_WEEK.md`.

### Time limits

- Use Easy problems only as focused primers when a pattern or implementation detail is entirely new.
- Default new-problem level: Medium; attempt independently for 25–35 minutes.
- Easy primer: attempt independently for 15–20 minutes.
- If no plausible direction emerges, learn the pattern rather than extending unstructured struggle.
- A problem is complete only when it can be re-solved and explained later without the reference.

## Weekly rhythm

| Session | Focus |
|---|---|
| Session A | One new problem from the current pattern group |
| Session B | One new problem + review of one earlier problem |
| Optional 15 minutes | Re-solve a previously missed problem cold |

At the end of each week, update the current-week file: mark completed problems, capture mistakes, choose the next pattern set, and carry forward only the unfinished work that remains useful.

## Curriculum

Advance when the recognition cues and core implementation feel repeatable—not when every listed problem is complete.

### 0. Re-entry: Python and core mechanics

**Outcome:** Write common interview structures without language friction.

- Python `dict`, `set`, `defaultdict`, `Counter`, `deque`, `heapq`
- sorting with `key=`
- pointer and index safety
- linked-list and tree node basics
- complexity analysis

### 1. Arrays, strings, and lookup patterns

| Pattern | Recognition cues | Core invariant / idea |
|---|---|---|
| Hash map / set | complements, duplicates, membership, frequencies | Record previously seen values or counts for constant-time lookup |
| Sorting + scan | ordering makes comparisons easier | Sorted order supports local decisions or removes combinations |
| Two pointers | sorted pairs, palindromes, partitioning | Pointer movement eliminates impossible candidates |
| Sliding window | contiguous subarray/substrings with a constraint | Maintain a valid range while expanding and shrinking |
| Prefix sum | range sums, target subarray count, balance | Relation between current and earlier prefixes identifies the range |
| Intervals | overlap, scheduling, merging | Sort by start/end and maintain a boundary |

### 2. Linear data structures and monotonic reasoning

| Pattern | Recognition cues | Core invariant / idea |
|---|---|---|
| Linked lists | rewiring, kth from end, cycles | Preserve links; use dummy nodes or fast/slow pointers |
| Stack | nested/matching structures, undo | Most recent unresolved state is handled first |
| Monotonic stack | next greater/smaller, histogram, daily temperatures | Stack holds unresolved candidates in monotonic order |
| Queue / deque | level/order processing, window max/min | FIFO worklist or monotonic candidate list |
| Heap | top-k, repeated min/max, merging streams | Heap contains the relevant frontier only |
| Binary search | sorted data or monotonic feasibility | Find a boundary where a predicate changes |

### 3. Trees, graphs, and search

| Pattern | Recognition cues | Core invariant / idea |
|---|---|---|
| Tree DFS | subtrees, paths, recursive answers | Define exactly what each recursive call returns |
| Tree BFS | nearest/shortest in levels | Process a complete level at a time |
| Graph DFS/BFS | reachability, components, islands | Model nodes/edges and visit each state once |
| Topological sort | prerequisites, dependencies | Process zero-indegree nodes or DFS states |
| Union-Find | merging/dynamic components | Track component representatives efficiently |
| Backtracking | all valid combinations/permutations | Choose → recurse → undo |

### 4. Optimization: dynamic programming and greedy

| Pattern | Recognition cues | Core invariant / idea |
|---|---|---|
| 1D / grid DP | answer depends on earlier choices/states | Define state, transition, base case, and evaluation order |
| Subsequences / knapsack DP | select/skip decisions, minimum/maximum value | Store the best answer for every meaningful subproblem |
| Greedy | a local choice may be provably safe | State why the chosen local option cannot harm an optimum |

### 5. Interview-style mixing

After the main patterns feel familiar:

- Work mostly Medium problems.
- Alternate fresh problems with cold re-solves.
- Practice explaining the approach before coding.
- Use a 35–40 minute cap for a Medium.
- Include occasional two-problem, 45-minute practice sets.

## Classification checklist

Before coding, ask:

1. Is the answer about a **contiguous** range? → sliding window or prefix sums.
2. Would **sorting** make the choices or comparisons monotonic? → two pointers, intervals, greedy.
3. Do I need fast **membership**, counts, or prior state? → hash map/set.
4. Is it asking for nearest greater/smaller, matching, or reversal? → stack / monotonic stack.
5. Do I repeatedly need the current best candidate? → heap.
6. Is there a monotonic yes/no feasibility condition? → binary search.
7. Is it about entities and relationships, a tree, or a grid? → DFS/BFS/graph algorithm.
8. Does it require every valid combination? → backtracking.
9. Does the answer depend on an optimal earlier subproblem? → DP.
10. Can a local choice be proved safe? → greedy.

## Problem note template

Use this for completed or reviewed problems in `CURRENT_WEEK.md`:

```md
### Problem title
- **LeetCode:** [Problem title](https://leetcode.com/problems/problem-slug/)
- **Pattern:**
- **Recognition cues:**
- **Brute force:**
- **Optimal idea / invariant:**
- **Complexity:**
- **Mistake or insight:**
- **Review dates:**
```

## Mastery checks

A pattern is progressing when you can:

- name 1–2 plausible patterns within the first few minutes;
- describe a brute-force solution before optimizing;
- state the invariant, recursive contract, or DP state before implementation;
- code the solution without relying on a saved answer;
- explain correctness, complexity, and edge cases aloud;
- re-solve previously missed questions after a delay.
