class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> hash = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            char[] charArray = strs[i].toCharArray();
            Arrays.sort(charArray); 
            String sorted = new String(charArray);
            ArrayList<String> currentList = new ArrayList<>();
            if (hash.containsKey(sorted)) {
                currentList = hash.get(sorted);
            } 
            currentList.add(strs[i]);
            hash.put(sorted, currentList);
        }

        ArrayList<ArrayList<String>> output = new ArrayList<>();
        for (String entry:hash.keySet()) {
            output.add(hash.get(entry));
        }
        List<List<String>> result = new ArrayList<>();
        result.addAll(output);
        return result;

    }
}
