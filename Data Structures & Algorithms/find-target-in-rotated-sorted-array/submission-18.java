class Solution {
    public int search(int[] nums, int target) {
        int lo = 0;
        int hi = nums.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] > nums[hi]) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        int pivot = lo;
        
        int result = binarySearch(nums, target, 0, pivot - 1);

        if (result != -1) {
            return result;
        }

        return binarySearch(nums, target, pivot, nums.length - 1);

    }

    public int binarySearch(int[] nums, int target, int left, int right) {
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}
