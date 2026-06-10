class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int current = -nums[i];
            int lo = i + 1;
            int hi = nums.length - 1; 
            HashMap<Integer, Integer> hash = new HashMap<>();
            while (lo < hi) {
                if (current == nums[hi] + nums[lo]) {
                    res.add(List.of(nums[i], nums[lo], nums[hi]));
                    lo++;
                    hi--;
                    while (nums[lo] == nums[lo - 1] && lo < hi) {
                        lo++;
                    }
                    while (nums[hi] == nums[hi + 1] && lo < hi) {
                        hi--;
                    }
                } else if (nums[lo] + nums[hi] < current) lo++;
                else hi--;
            }
        }
        return res;
    }
}
