# Week 2 — LeetCode Practice

> **Current focus:** Medium-level hash-map, two-pointer, and sliding-window recognition
>
> **Goal:** Classify each problem before coding, complete two Medium attempts, and reinforce one core pattern through a cold re-solve.
>
> **Time budget:** 2 hours total

## Why this level

Week 1's problems are deliberately basic pattern primers. This week moves directly to interview-relevant Mediums while staying within the same related family of patterns. The goal is to reason from cues and invariants, not to accumulate Easy completions.

## Schedule

| Session | Time | Assignment | Definition of done |
|---|---:|---|---|
| 1 | 60 min | **Group Anagrams** | Attempt for 30–35 minutes; implement a hashable frequency/signature key; explain why equal signatures form exactly one group. |
| 2 | 60 min | **Longest Substring Without Repeating Characters** + a 10-minute cold re-solve of Group Anagrams | Attempt the Medium for 30–35 minutes; articulate the sliding-window invariant before coding; re-solve the prior problem without notes. |

## Current problem set

### 1. Group Anagrams
- **LeetCode:** [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- **Difficulty:** Medium
- **Primary pattern:** Hash map + canonical representation / frequency signature
- **Recognition cues:** Partition strings into equivalence classes; order within each string does not matter; all members of a group share the same character multiset.
- **Attempt cap:** 35 minutes
- **Target implementation:** Use a dictionary from a canonical character-count signature (for example, a 26-count tuple) to a list of strings.
- **Invariant to state before coding:** Every anagram produces the same signature; strings with differing signatures cannot belong to the same group.
- [ ] Classified before coding
- [ ] First attempt
- [ ] Implemented independently
- [ ] Explained invariant and complexity
- [ ] Review scheduled

### 2. Longest Substring Without Repeating Characters
- **LeetCode:** [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- **Difficulty:** Medium
- **Primary pattern:** Sliding window + hash map
- **Recognition cues:** Longest **contiguous substring** under a validity constraint; repeated values invalidate a window; answer is the best valid window length.
- **Attempt cap:** 35 minutes
- **Target implementation:** Maintain a left boundary and a map of each character's most recent index; advance `left` only forward when a duplicate falls inside the active window.
- **Invariant to state before coding:** The active window contains no duplicate characters, and `left` never moves backward.
- [ ] Classified before coding
- [ ] First attempt
- [ ] Implemented independently
- [ ] Explained invariant and complexity
- [ ] Review scheduled

## Stretch problem — only if time remains

### 3. 3Sum
- **LeetCode:** [3Sum](https://leetcode.com/problems/3sum/)
- **Difficulty:** Medium
- **Primary pattern:** Sorting + fixed index + two pointers
- **Recognition cues:** Find unique value triplets under a target sum; sorting enables monotonic pointer movement and duplicate skipping.
- **Attempt cap:** 35 minutes
- **Target implementation:** Sort; fix the first number; use inward-moving left/right pointers for the remaining target; skip duplicates at every level.
- **Invariant to state before coding:** For a fixed first value in sorted order, moving the left pointer raises the pair sum and moving the right pointer lowers it.
- [ ] Attempted
- [ ] Implemented independently
- [ ] Explained duplicate handling

## Completion notes

Add concise notes after each attempt. Do not paste a full solution.

### Group Anagrams
- **LeetCode:** [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- **Pattern:** Hash map + canonical representation
- **Recognition cues:**
- **Brute force:**
- **Optimal idea / invariant:**
- **Complexity:**
- **Mistake or insight:**
- **Review dates:** 2–3 days / 2 weeks / 1–2 months

### Longest Substring Without Repeating Characters
- **LeetCode:** [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- **Pattern:** Sliding window + hash map
- **Recognition cues:**
- **Brute force:**
- **Optimal idea / invariant:**
- **Complexity:**
- **Mistake or insight:**
- **Review dates:** 2–3 days / 2 weeks / 1–2 months

### 3Sum (stretch)
- **LeetCode:** [3Sum](https://leetcode.com/problems/3sum/)
- **Pattern:** Sorting + two pointers
- **Recognition cues:**
- **Brute force:**
- **Optimal idea / invariant:**
- **Complexity:**
- **Mistake or insight:**
- **Review dates:** 2–3 days / 2 weeks / 1–2 months

## Week-end review

- [ ] I named a plausible pattern before looking at hints or solutions.
- [ ] I can distinguish a substring/sliding-window problem from a general hash-map problem.
- [ ] I can state the window invariant for Longest Substring Without Repeating Characters.
- [ ] I can explain why sorting enables two pointers for 3Sum.
- [ ] I re-solved Group Anagrams cold.

### Next-week decision

- If the sliding-window invariant and pointer moves are clear: continue with **Minimum Size Subarray Sum** and **Longest Repeating Character Replacement**.
- If window boundaries or duplicate handling were unreliable: repeat sliding window with 2–3 targeted problems before increasing difficulty.
- Notes for next week:
