class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        result_list = []
        while nums:     
            alice_min = min(nums)
            nums.remove(alice_min)
            
            bob_min = min(nums)
            nums.remove(bob_min)
            
            result_list.append(bob_min)
            result_list.append(alice_min)
            
        return result_list


        