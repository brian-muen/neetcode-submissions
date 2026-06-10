class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> hash = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char character = s.charAt(i);
            if (hash.containsKey(character) == true) {
                Integer count = hash.get(character);
                hash.put(character, count + 1);
            } else {
                hash.put(character, 1);
            }
        }
        for (int i = 0; i < t.length(); i++) {
            char character = t.charAt(i);
            if (hash.containsKey(character) == true) {
                Integer count = hash.get(character);
                if (count - 1 == 0) {
                    hash.remove(character);
                } else {
                    hash.put(character, count - 1);
                }
            } else {
                return false;
            }
        }
        return true;
    }
}
