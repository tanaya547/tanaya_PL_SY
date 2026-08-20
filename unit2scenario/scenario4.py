# scenario 4 - unit 2
# House Robber Problem
# Determine the maximum amount that can be collected without selecting two adjacent houses.


class HouseRobber:
    @staticmethod
    def rob(nums: list[int]) -> int:
       
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # DP array to store the maximum amount robbed up to house i
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]


# Main Program
if __name__ == "__main__":
    try:
        user_input = input("Enter the amount in each house (separated by spaces): ")
        
        if not user_input.strip():
            print("No houses entered.")
        else:
            house_values = [int(x) for x in user_input.strip().split()]
            
            if any(val < 0 for val in house_values):
                print("Please enter non-negative amounts for the houses.")
            else:
                max_loot = HouseRobber.rob(house_values)
                print(f"\nMaximum amount that can be collected: {max_loot}")

    except ValueError:
        print("Invalid input! Please enter valid integers separated by spaces.")

#OUTPUT
#Enter the amount in each house (separated by spaces): 5 7 8 9 10

#Maximum amount that can be collected: 23
