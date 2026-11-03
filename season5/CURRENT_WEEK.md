# Week 3 — LeetCode Practice

> **Current focus:** Medium-level sliding-window recognition and window-boundary control
>
> **Goal:** Classify contiguous-range problems, state a window invariant, complete two Medium attempts, and reinforce the pattern through a cold re-solve.
>
> **Time budget:** 2 hours total

## Why this level

Week 2 established hash-map grouping and the basic no-duplicates sliding window. This week focuses on the key distinction within sliding windows: whether the window is repaired when it violates an upper-bound constraint or shrunk after it reaches a lower-bound target. The goal is to reason from cues and invariants, not to memorize templates.

## Schedule

| Session | Time | Assignment | Definition of done |
|---|---:|---|---|
| 1 | 60 min | **Minimum Size Subarray Sum** | Attempt for 30–35 minutes; use the positivity of values to justify when the left boundary may move; explain the valid-window invariant. |
| 2 | 60 min | **Longest Repeating Character Replacement** + a 10-minute cold re-solve of Minimum Size Subarray Sum | Attempt the Medium for 30–35 minutes; maintain counts and a maximum frequency; articulate why a window needing more than `k` replacements must shrink. |

## Current problem set

### 1. Minimum Size Subarray Sum
- **LeetCode:** [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
- **Difficulty:** Medium
- **Primary pattern:** Sliding window + running sum
- **Recognition cues:** Find the shortest **contiguous** subarray whose sum reaches a target; all values are positive, so expanding cannot lower the sum and shrinking cannot raise it.
- **Attempt cap:** 35 minutes
- **Target implementation:** Expand the right boundary and add to a running sum; while the sum is at least `target`, record the length and advance the left boundary.
- **Invariant to state before coding:** The active window sum equals the values from `left` through `right`; whenever its sum is at least `target`, repeatedly shrinking it finds the shortest valid window ending at `right`.
- [ ] Classified before coding
- [ ] First attempt
- [ ] Implemented independently
- [ ] Explained invariant and complexity
- [ ] Review scheduled

### 2. Longest Repeating Character Replacement
- **LeetCode:** [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- **Difficulty:** Medium
- **Primary pattern:** Sliding window + frequency counts
- **Recognition cues:** Find the longest **contiguous substring** that can be made uniform with at most `k` replacements; the fewest replacements needed is window length minus the most frequent character's count.
- **Attempt cap:** 35 minutes
- **Target implementation:** Expand right while counting characters and tracking `max_frequency`; while `window_length - max_frequency > k`, advance left and decrement its count.
- **Invariant to state before coding:** The active window requires at most `k` replacements to become all one character; `left` never moves backward.
- [ ] Classified before coding
- [ ] First attempt
- [ ] Implemented independently
- [ ] Explained invariant and complexity
- [ ] Review scheduled

## Stretch problem — only if time remains

### 3. Subarray Product Less Than K
- **LeetCode:** [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)
- **Difficulty:** Medium
- **Primary pattern:** Sliding window + running product
- **Recognition cues:** Count contiguous subarrays with a product under a threshold; all numbers are positive, so growing the window can only increase the product.
- **Attempt cap:** 35 minutes
- **Target implementation:** Expand the right boundary; while the product is at least `k`, divide out the left value and advance left; add the current window length to the answer.
- **Invariant to state before coding:** The active window product is less than `k`; every suffix ending at `right` is therefore also valid.
- [ ] Attempted
- [ ] Implemented independently
- [ ] Explained why the window length counts valid suffixes

## Completion notes

Add concise notes after each attempt. Do not paste a full solution.

### Minimum Size Subarray Sum
- **LeetCode:** [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
- **Pattern:** Sliding window + running sum
- **Recognition cues:**
- **Brute force:**
- **Optimal idea / invariant:**
- **Complexity:**
- **Mistake or insight:**
- **Review dates:** 2–3 days / 2 weeks / 1–2 months

### Longest Repeating Character Replacement
- **LeetCode:** [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- **Pattern:** Sliding window + frequency counts
- **Recognition cues:**
- **Brute force:**
- **Optimal idea / invariant:**
- **Complexity:**
- **Mistake or insight:**
- **Review dates:** 2–3 days / 2 weeks / 1–2 months

### Subarray Product Less Than K (stretch)
- **LeetCode:** [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)
- **Pattern:** Sliding window + running product
- **Recognition cues:**
- **Brute force:**
- **Optimal idea / invariant:**
- **Complexity:**
- **Mistake or insight:**
- **Review dates:** 2–3 days / 2 weeks / 1–2 months

## Week-end review

- [ ] I named a plausible pattern before looking at hints or solutions.
- [ ] I can distinguish a shrinking-window problem from a general hash-map or prefix-sum problem.
- [ ] I can state why positive values make shrinking valid for Minimum Size Subarray Sum.
- [ ] I can derive the replacement count, `window_length - max_frequency`, for Longest Repeating Character Replacement.
- [ ] I re-solved Minimum Size Subarray Sum cold.

### Next-week decision

- If lower-bound and upper-bound window invariants are clear: continue with **Subarray Sum Equals K** and **Merge Intervals**.
- If window boundaries or the role of positive values were unreliable: repeat sliding window with 2–3 targeted problems before moving to prefix sums.
- Notes for next week:
