class Solution {
    public int maxArea(int[] height) {
      int maxArea=0,right=height.length-1,left=0;
      while(left<right){
          maxArea=Math.max(maxArea,(right-left)*Math.min(height[right],height[left]));
          if(height[right]<height[left]){
              right--;
          }else left++;
      }
      return maxArea;  
    }
}
