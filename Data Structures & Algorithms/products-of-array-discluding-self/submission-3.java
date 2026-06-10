class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] firstProduct = new int[nums.length];
        int[] secondProduct = new int[nums.length];

        int product = 1;
        for (int i = 0; i < nums.length; i++) {
            firstProduct[i] = product *= nums[i];
        }
        product = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            secondProduct[i] = product *= nums[i];
        }
        int[] res = new int[nums.length];
        res[0] = secondProduct[1];
        res[nums.length - 1] = firstProduct[nums.length - 2];

        for (int i = 1; i < nums.length - 1; i++) {
            res[i] = firstProduct[i - 1] * secondProduct[i + 1];
        }

        return res;
    }
}  
