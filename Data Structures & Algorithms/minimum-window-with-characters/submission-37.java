class Solution {
    public String minWindow(String s, String t) {
        if (t.isEmpty()) return "";
        HashMap<Character, Integer> hash1 = new HashMap<>();
        for (int i = 0; i < t.length(); i++) {
            hash1.put(t.charAt(i), hash1.getOrDefault(t.charAt(i), 0) + 1);
        }
        HashMap<Character, Integer> hash2 = new HashMap<>();
        int l = 0;
        String res = "";
        int length = Integer.MAX_VALUE;
        int have = 0, need = hash1.size();

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);
            hash2.put(current, hash2.getOrDefault(current, 0) + 1);

            if (hash1.containsKey(current) && hash2.get(current) == hash1.get(current)) {
                have++;
            }
            while (have == need) {
                if (length > i - l + 1) {
                    res = s.substring(l, i + 1);
                    length = res.length();
                }

                char leftChar = s.charAt(l);
                hash2.put(leftChar, hash2.get(leftChar) - 1);

                if (hash1.containsKey(leftChar) && hash2.get(leftChar) < hash1.get(leftChar)) {
                    have--;
                }
                l++;
            }
        }
        return res;
    }
}
