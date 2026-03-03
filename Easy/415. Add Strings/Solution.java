class Solution {
    public String addStrings(String num1, String num2) {
        int l = num1.length()-1, r = num2.length()-1;
        int rst = 0;
        String result = "";
        while (l >= 0 && r >= 0){
            int s = Character.getNumericValue(num1.charAt(l)) + Character.getNumericValue(num2.charAt(r)) + rst;
            if (s >= 10){
                result = String.valueOf(s-10) + result;
                rst = 1;
            }else {
                result = String.valueOf(s) + result;
                rst = 0;
            }
            l -= 1;
            r -= 1;       
        }
        if (l == -1){
            while (r >= 0){
                int s = Character.getNumericValue(num2.charAt(r)) + rst;
                if (s >= 10){
                    result = String.valueOf(s-10) + result;
                    rst = 1;
                }else {
                    result = String.valueOf(s) + result;
                    rst = 0;
                }
                r -= 1;
            }
        }else if (r == -1) {
            while (l >= 0){
                int s = Character.getNumericValue(num1.charAt(l)) + rst;
                if (s >= 10){
                    result = String.valueOf(s-10) + result;
                    rst = 1;
                }else {
                    result = String.valueOf(s) + result;
                    rst = 0;
                }
                l -= 1;
            }

        } if (rst == 1)
           return "1" + result;
        
    return result;  
    }
}