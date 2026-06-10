class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character, Integer> window = new HashMap<>();
        char champ = 0;
        int count = 0;
        int l = 0;
        int res = 0;
        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);
            window.put(c, window.getOrDefault(c, 0) + 1);
            
            count = Math.max(count, window.get(s.charAt(r)));
            while (r - l + 1 - count > k) {
                window.put(s.charAt(l), window.get(s.charAt(l)) - 1);
                l++;
            }
            res = Math.max(res, r - l + 1);
        }
        return res;
    }
}
