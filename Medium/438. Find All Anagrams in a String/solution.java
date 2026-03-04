import java.util.ArrayList;

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int l = 0, r = p.length();
        ArrayList<Integer> arr = new ArrayList<>();
        char[] chars = p.toCharArray();
        Arrays.sort(chars);
        p = new String(chars);
        while (r <= s.length()){
            char[] c = s.substring(l,r).toCharArray();
            Arrays.sort(c);
            String ss = new String(c);
            if (ss.equals(p)){
                arr.add(l);
            }
            l += 1;
            r += 1;
        }
        return arr;

        
    }
}