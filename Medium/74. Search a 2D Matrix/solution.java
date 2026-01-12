class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for (int[] row: matrix){
            if (row[row.length-1] >= target){
                int l = 0;
                int r = row.length;
                while (r >= l){
                    int curr = (r+l)/2;
                    if (row[curr] == target){
                        return true;
                    }
                    else if (row[curr] > target){
                        r = curr - 1;
                    }
                    else {l = curr + 1;}
                } return false;
            }
        }return false;
        
    }
}