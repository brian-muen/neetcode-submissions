class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> hash = new HashMap<>();
        hash.put(')', '(');
        hash.put(']', '[');
        hash.put('}', '{');

        for (char c : s.toCharArray()) {
            if (hash.containsKey(c)) {
                if (!stack.isEmpty() && stack.peek() == hash.get(c)) {
                    stack.pop();
                } else {
                    return false;
                } 
            } else {
                stack.push(c);
            }
        }

        return stack.isEmpty();
    }
}
