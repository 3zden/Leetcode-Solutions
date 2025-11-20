# Contains Duplicate

**LeetCode Problem:** [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

---

## Problem Statement

Given an integer array `nums`, return `true` if **any** value appears at least twice in the array, and return `false` if every element is **distinct**. :contentReference[oaicite:0]{index=0}  

**Examples:**

1. Input: `nums = [1, 2, 3, 1]`  
   Output: `true` :contentReference[oaicite:1]{index=1}  
2. Input: `nums = [1, 2, 3, 4]`  
   Output: `false` :contentReference[oaicite:2]{index=2}  
3. Input: `nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]`  
   Output: `true` :contentReference[oaicite:3]{index=3}  

**Constraints:**

- `1 <= nums.length <= 10^5` :contentReference[oaicite:4]{index=4}  
- `-10^9 <= nums[i] <= 10^9` :contentReference[oaicite:5]{index=5}  

---

## Approaches / Solutions

### 1. Brute-Force (Naive)

- Use two nested loops:  
  - Outer loop index `i` from `0` to `n - 2`  
  - Inner loop index `j` from `i + 1` to `n - 1`  
- For each pair `(i, j)`, check if `nums[i] == nums[j]`  
- If yes → return `true`  
- If no duplicates found → return `false`  
- **Time Complexity:** \(O(n^2)\) :contentReference[oaicite:6]{index=6}  
- **Space Complexity:** \(O(1)\) :contentReference[oaicite:7]{index=7}  

---

### 2. Sort + Scan

- Sort the array `nums`  
- Then scan through the sorted array and check whether any **adjacent** elements are equal  
- If any `nums[i] == nums[i + 1]`, return `true`  
- If you finish scanning, return `false`  
- **Time Complexity:** \(O(n \log n)\) (due to sorting) :contentReference[oaicite:8]{index=8}  
- **Space Complexity:** Depending on sort implementation — often \(O(\log n)\) for in-place sorts, or more for other implementations :contentReference[oaicite:9]{index=9}  

---

### 3. Hash Set (Optimal)

- Create an empty hash set (or `Set`) to store seen numbers  
- Iterate through `nums`:  
  - For each `num` in `nums`, check if `num` is already in the set  
    - If yes → **duplicate found** → return `true`  
    - If no → add `num` to the set  
- If you finish the loop without finding a duplicate, return `false`  
- **Time Complexity:** \(O(n)\) on average, because set insert and membership check are \(O(1)\) on average :contentReference[oaicite:10]{index=10}  
- **Space Complexity:** \(O(n)\) in the worst case (if all elements are unique) :contentReference[oaicite:11]{index=11}  

---

## Example Walkthrough (Hash Set)

Suppose `nums = [1, 3, 2, 3]`:

| Step | num | Set “seen” before check | Is it in set? | Action | Set after action |
|---|---|---|---|---|---|
| 1 | 1 | `{}` | No | Add 1 | `{1}` |
| 2 | 3 | `{1}` | No | Add 3 | `{1, 3}` |
| 3 | 2 | `{1, 3}` | No | Add 2 | `{1, 2, 3}` |
| 4 | 3 | `{1, 2, 3}` | **Yes** | Return `true` | — |

---

## Edge Cases / Things to Consider

- **Array of length 1**: Always `false` (no duplicates possible).  
- **All elements are the same**: Should return `true`.  
- **Negative numbers**: Works fine — set/hash doesn’t care about sign.  
- **Very large array**: The hash-set solution handles it efficiently.

---

If you like, I can also include **code snippets** (in Python, Java, etc.) + **time/space complexity analysis** — do you want me to add that?
::contentReference[oaicite:12]{index=12}
