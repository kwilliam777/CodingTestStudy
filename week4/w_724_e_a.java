class Solution {
    public int pivotIndex(int[] nums) {
        int left = 0;
        int right = 0;
        int idx = 0;
        for(int i = 0; i<nums.length; i++){
            left = 0;
            right = 0;
            idx = i;
            if(idx == 0){
                left = 0;
                for(int j = i+1; j<nums.length; j++){
                    right += nums[j];
                }
            }
            
            else if(idx == nums.length){
                right = 0;
                for(int j = 0; j<i-1; j++){
                    left += nums[j];
                }
            } else{
                for(int k = 0; k<i; k++){
                    left += nums[k];
                }
                for(int a = i+1; a<nums.length; a++){
                    right += nums[a];
                }
            }
            
            if(left == right){
                return idx;
            }
            
        }
         
        return -1;
       
    }
}
