class Solution {
    public boolean isPalindrome(String s) {
        String cleaned = s.replaceAll("[^a-zA-Z0-9]", "");
        String lower = cleaned.toLowerCase();

        for (int i = 0; i < lower.length()/2; i++) {
            if (lower.charAt(i) != lower.charAt(lower.length() - i - 1)) {
                return false;
            }
        }
        return true;
    }
}