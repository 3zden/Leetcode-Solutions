# Two Sum

**LeetCode Problem:** [Two Sum](https://leetcode.com/problems/two-sum/description/)

---

## Problem Statement

Given an array of integers `nums` and an integer `target`, return *indices* of the two numbers such that they add up to `target`.

- You may assume that each input would have **exactly one solution**. :contentReference[oaicite:0]{index=0}  
- You may not use the same element twice. :contentReference[oaicite:1]{index=1}  
- You can return the answer in **any order**. :contentReference[oaicite:2]{index=2}  

**Examples:**

1. Input: `nums = [2, 7, 11, 15]`, `target = 9`  
   Output: `[0, 1]`  
   Explanation: `nums[0] + nums[1] == 9`. :contentReference[oaicite:3]{index=3}  

2. Input: `nums = [3, 2, 4]`, `target = 6`  
   Output: `[1, 2]` :contentReference[oaicite:4]{index=4}  

3. Input: `nums = [3, 3]`, `target = 6`  
   Output: `[0, 1]` :contentReference[oaicite:5]{index=5}  

**Constraints:**

- `2 <= nums.length <= 10^4` :contentReference[oaicite:6]{index=6}  
- `-10^9 <= nums[i] <= 10^9` :contentReference[oaicite:7]{index=7}  
- `-10^9 <= target <= 10^9` :contentReference[oaicite:8]{index=8}  
- Exactly **one** valid answer exists. :contentReference[oaicite:9]{index=9}  

---

## Approaches / Solutions

### 1. Brute-Force (Naive)

- Use two nested loops:  
  - Outer loop over index `i` from `0` to `n-1`  
  - Inner loop over index `j` from `i+1` to `n-1`  
- For each pair `(i, j)`, check if `nums[i] + nums[j] == target`  
- If yes, return `[i, j]`  
- Time Complexity: **O(n²)**  
- Space Complexity: **O(1)** :contentReference[oaicite:10]{index=10}  

---

### 2. Hash Map (Optimal)

- Create a hash map (or dictionary) to store *value → index* as you iterate.  
- Iterate through the array once:  
  - For each element `nums[i]`, compute its complement: `complement = target - nums[i]`  
  - Check if `complement` is already in the map:  
    - If yes → return `[map[complement], i]`  
    - If no → store `nums[i]` with its index: `map[nums[i]] = i`  
- This is a **one-pass** solution. :contentReference[oaicite:11]{index=11}  
- Time Complexity: **O(n)**  
- Space Complexity: **O(n)** :contentReference[oaicite:12]{index=12}  

---

## Example Walkthrough (Hash Map)

Suppose `nums = [3, 2, 4]`, `target = 6`:

| i | nums[i] | complement = target - nums[i] | Map before insert | Check complement? | Action |
|---|---------|-------------------------------|---------------------|-------------------|--------|
| 0 | 3       | 3                             | `{}`                | No                | Add `{3: 0}` |
| 1 | 2       | 4                             | `{3: 0}`            | No                | Add `{2: 1}` |
| 2 | 4       | 2                             | `{3: 0, 2: 1}`      | **Yes** (2 in map) | Return `[1, 2]` |

---

## Edge Cases / Things to Consider

- You may assume there's exactly one solution, so no need to handle multiple pairs. :contentReference[oaicite:13]{index=13}  
- Negative numbers in `nums`: the same logic applies, since the complement formula works for negative values too.  
- Large arrays: the hash-map approach scales well (O(n) time), whereas brute force may be too slow.  
- Duplicate values: allowed (e.g., `nums = [3, 3]`, `target = 6`) — but you must ensure you don’t pick the *same* element twice (i.e., same index). The hash-map approach handles this because when you check for a complement, you check among previously seen elements.

---

## Summary

- **Goal:** find two distinct indices `i` and `j` such that `nums[i] + nums[j] == target`.  
- **Brute-force:** simple but O(n²).  
- **Hash-map:** optimal O(n), using extra space to store seen values and their indices.

---

If you like, I can also give you a **template solution** in Python, Java, or any language you prefer (with comments). Do you want me to include that?
