class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hash = new HashMap<>();
        int[] sol = new int[2];
        for (int i = 0; i < nums.length; i++) {
            if (hash.containsKey(nums[i]) == true) {
                sol[0] = hash.get(nums[i]);
                sol[1] = i;
                break;
            }
            hash.put(target - nums[i], i);
        }
        return sol;
    }
}
