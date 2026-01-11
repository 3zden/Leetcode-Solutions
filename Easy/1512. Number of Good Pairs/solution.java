import java.util.HashMap;
class Solution {
    public int numIdenticalPairs(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int out = 0;
        for (Integer num: nums){
            if (map.containsKey(num)){
                out += map.get(num);
                map.put(num,map.get(num)+1);
            } else {map.put(num,1);}
        }
        return out;
    }
}