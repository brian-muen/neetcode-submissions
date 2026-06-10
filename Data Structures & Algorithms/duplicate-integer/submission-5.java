class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap hashnums = new HashMap();
        for (int i = 0; i < nums.length; i++) {
            if (hashnums.containsKey(nums[i]) == false) {
                hashnums.put(nums[i], true);
            }
            else {
                return true;
            }
        }
        return false;
    }
}
