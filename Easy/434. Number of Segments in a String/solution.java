class Solution {
    public int countSegments(String s) {
        String[] out = s.split(" ");
        int count = 0;
        for(String ss: out){
            if (ss.strip().equals(""))
            continue;
            else {
                count += 1;
            }
        }return count;
        
    }
}