class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        Set<Character> set = new HashSet<>();
        for (int i = 0; i<jewels.length(); i++){
            if (set.contains(jewels.charAt(i))){
                continue;
            } else {
                set.add(jewels.charAt(i));
            } 
        }
        int out = 0;
        for (int i = 0; i<stones.length(); i++){
            if (set.contains(stones.charAt(i))){
                out++;
            } else {
                continue;
            } 
        }
        return out;   
    }
}