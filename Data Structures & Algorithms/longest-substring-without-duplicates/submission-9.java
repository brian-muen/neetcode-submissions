class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0;
        if (s.length() == 0) return res;
        int count = 0;            
        int l = 0;
        HashMap<Character, Integer> hash = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (!hash.containsKey(s.charAt(i))) {
                count++;
                hash.put(s.charAt(i), i);
            } else {
                int q = hash.get(s.charAt(i));
                int start = l;
                l = hash.get(s.charAt(i)) + 1;
                for (int j = start; j <= q; j++) {
                    hash.remove(s.charAt(j));
                }
                hash.put(s.charAt(i), i);
                count = i - l + 1;
            }
            if (count > res) {
                res = count;
            }
        }
        return res;
        
    }
}
