class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0;
        if (s.length() == 0) return res;
        int l = 0;
        HashMap<Character, Integer> hash = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            while (hash.containsKey(s.charAt(i))) {
                hash.remove(s.charAt(l));
                l++;
            }
            hash.put(s.charAt(i), i);
            res = Math.max(res, i - l + 1);
        }
        return res;
        
    }
}
