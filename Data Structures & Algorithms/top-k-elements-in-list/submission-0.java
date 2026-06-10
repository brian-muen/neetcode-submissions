class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<Integer>[] freq = new List[nums.length + 1];
        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<Integer>();
        }
        HashMap<Integer, Integer> hash = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int count = hash.getOrDefault(nums[i], 0);
            hash.put(nums[i], ++count);
        }

        for (Integer items : hash.keySet()) {
            freq[hash.get(items)].add(items);
        }

        int[] result = new int[k];
        int index = 0;

        for (int i = freq.length - 1; i > 0 && index < k; i--) {
            for (Integer n : freq[i]) {
                result[index++] = n; 
                if (index == k) {
                    return result;
                }
            }
        }
        return result;
    }
}