# Current Week — LeetCode Practice

> **Current focus:** Re-entry: Python mechanics, hash maps/sets, and two pointers
>
> **Goal:** Complete two new problems and re-solve at least one without notes.
>
> **Time budget:** 2 hours total

## Schedule

| Session | Time | Assignment | Definition of done |
|---|---:|---|---|
| 1 | 60 min | **Two Sum** + Python lookup review | Implement a one-pass hash-map solution; explain why the complement lookup works. |
| 2 | 60 min | **Valid Anagram** + **Valid Palindrome** | Use counting/set reasoning for the first and two pointers for the second; re-solve Two Sum cold for 5–10 minutes. |

## Current problem set

### 1. Two Sum
- **LeetCode:** [Two Sum](https://leetcode.com/problems/two-sum/)
- **Difficulty:** Easy
- **Primary pattern:** Hash map
- **Recognition cues:** Find two values satisfying a target; complement lookup; return indices.
- **Attempt cap:** 20 minutes
- **Target implementation:** One pass; store value → index after checking whether its complement is already seen.
- [x] First attempt
- [x] Implemented independently
- [x] Explained invariant and complexity
- [x] Review scheduled

### 2. Valid Anagram
- **LeetCode:** [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- **Difficulty:** Easy
- **Primary pattern:** Frequency counting / hash map
- **Recognition cues:** Same characters with the same multiplicities; ordering is irrelevant.
- **Attempt cap:** 15 minutes
- **Target implementation:** Count characters and compare counts (or decrement counts while scanning).
- [x] First attempt
- [x] Implemented independently
- [x] Explained invariant and complexity
- [x] Review scheduled

### 3. Valid Palindrome
- **LeetCode:** [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- **Difficulty:** Easy
- **Primary pattern:** Two pointers
- **Recognition cues:** Compare symmetric characters; ignore non-alphanumeric characters; no extra processed string is required.
- **Attempt cap:** 20 minutes
- **Target implementation:** Move left/right pointers inward, skipping non-alphanumeric characters before comparison.
- [x] First attempt
- [x] Implemented independently
- [x] Explained invariant and complexity
- [x] Review scheduled

## Completion notes

Add concise notes after each attempt. Do not paste a full solution.

### Two Sum
- **Pattern:** Hash map
- **Recognition cues:**
- **Brute force:**
- **Optimal idea / invariant:**
- **Complexity:**
- **Mistake or insight:**
- **Review dates:** 2–3 days / 2 weeks / 1–2 months

### Valid Anagram
- **Pattern:** Frequency counting / hash map
- **Recognition cues:**
- **Brute force:**
- **Optimal idea / invariant:**
- **Complexity:**
- **Mistake or insight:**
- **Review dates:** 2–3 days / 2 weeks / 1–2 months

### Valid Palindrome
- **Pattern:** Two pointers
- **Recognition cues:**
- **Brute force:**
- **Optimal idea / invariant:**
- **Complexity:**
- **Mistake or insight:**
- **Review dates:** 2–3 days / 2 weeks / 1–2 months

## Week-end review

- [x] I can classify each problem before coding.
- [x] I can explain the key invariant for each problem.
- [x] I re-solved at least one problem cold.
- [x] I chose next week's pattern group from actual mistakes, not random selection.

### Next-week decision

- If lookup/counting and two pointers feel comfortable: move to **sliding window**.
- If any of this week’s patterns still feels mechanical: repeat the pattern with 2–3 new examples before moving on.
- Notes for next week:
