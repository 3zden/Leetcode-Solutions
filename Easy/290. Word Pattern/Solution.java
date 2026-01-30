import java.util.HashMap;
import java.util.HashSet;
class Solution {
    public boolean wordPattern(String pattern, String s) {
        HashMap<Character, String> map= new HashMap<>();
        HashSet<String> b = new HashSet<>();
        String[] splitted = s.split(" ");
        if (pattern.length() != splitted.length){return false;}
        for(int i = 0; i < pattern.length();i++){
            if (map.containsKey(pattern.charAt(i))){
                if (!map.get(pattern.charAt(i)).equals(splitted[i])){
                    return false;
                }
            }else {
                if (b.contains(splitted[i])){ return false;}
                else {
                map.put(pattern.charAt(i), splitted[i]);
                b.add(splitted[i]);}
            }
        }return true;
    }
}