class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int current = nums[i];
            int lo = i + 1;
            int hi = nums.length - 1; 
            while (lo < hi) {
                int sum = current + nums[hi] + nums[lo];
                if (sum < 0) {
                    lo++;
                } 
                else if (sum > 0) {
                    hi--;
                } 
                else {
                    res.add(List.of(nums[i], nums[lo], nums[hi]));
                    lo++;
                    hi--;
                    while (nums[lo] == nums[lo - 1] && lo < hi) {
                        lo++;
                    }
                    while (nums[hi] == nums[hi + 1] && lo < hi) {
                        hi--;
                    }
                }
            }
        }
        return res;
    }
}
