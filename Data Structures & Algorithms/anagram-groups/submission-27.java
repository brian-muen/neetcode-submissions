class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> hash = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            String currStr = strs[i];
            int[] count = new int[26];
            for (int j = 0; j < currStr.length(); j++) {
                count[currStr.charAt(j) - 'a']++;
            }
            String key = Arrays.toString(count);
            ArrayList<String> currentList = new ArrayList<>();
            if (hash.containsKey(key)) {
                currentList = hash.get(key);
            } 
            currentList.add(strs[i]);
            hash.put(key, currentList);
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
