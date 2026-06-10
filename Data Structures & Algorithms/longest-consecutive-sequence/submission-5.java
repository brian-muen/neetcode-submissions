class Solution {
    public int longestConsecutive(int[] nums) {
        HashMap<Integer, Integer> hash = new HashMap<>();
        boolean[] marked = new boolean[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (hash.containsKey(nums[i])) {
                marked[i] = true;
                continue;
            } 
            hash.put(nums[i], i);
        }

        int champ = 0;
        for (int i = 0; i < nums.length; i++) {
            int count = 1;
            int j = nums[i] + 1;
            if (marked[i]) {
                continue;
            }
            while (hash.containsKey(j)) {
                count++;
                marked[hash.get(j)] = true;
                j++;
            }
            j = nums[i] - 1;
            while (hash.containsKey(j)) {
                count++;
                marked[hash.get(j)] = true;
                j--;
            }
            if (count > champ) champ = count;
        }

        return champ;
    }
}
