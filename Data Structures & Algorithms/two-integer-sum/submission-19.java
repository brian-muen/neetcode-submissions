class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hash = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (hash.containsKey(nums[i]) == true) {
                return new int[]{hash.get(nums[i]), i};
            }
            hash.put(target - nums[i], i);
        }
        return new int[0];
    }
}
