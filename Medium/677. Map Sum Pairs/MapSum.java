import java.util.HashMap;
class MapSum {
    HashMap<String, Integer> MapSum;

    public MapSum() {
        MapSum = new HashMap<>(); 
        
    }
    
    public void insert(String key, int val) {
        this.MapSum.put(key,val);
        
    }
    
    public int sum(String prefix) {
        int nval = 0;
        for(String k : this.MapSum.keySet()){
            if (k.startsWith(prefix)){
                nval += MapSum.get(k);
            }
        }return nval;
        
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */