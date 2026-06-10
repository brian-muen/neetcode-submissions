class Solution {
    public int maxArea(int[] height) {
        int lo = 0;
        int hi = height.length - 1;

        int champ = (hi - lo) * Math.min(height[lo], height[hi]);
        if (height[lo] > height[hi]) hi--;
        else lo++;

        while (lo < hi) {
            int current = (hi - lo) * Math.min(height[lo], height[hi]);
            if (current > champ) champ = current;
            if (height[lo] > height[hi]) hi--;
            else lo++;
        }

        return champ;
    }
}