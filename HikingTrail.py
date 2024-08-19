class HikingTrail:
    @staticmethod
    def longest_hike(nums, k):
        max_len = 0
        i = 1
        while i < len(nums):
            if nums[i] > nums[i - 1]:
                length = 1
                while i + length < len(nums) and nums[i + length] - nums[i + length - 1] <= k:
                    length += 1
                max_len = max(max_len, length)
            i += 1
        return max_len


if __name__ == "__main__":
    nums = [4, 2, 1, 4, 3, 4, 5, 8, 15]
    k = 3
    print(HikingTrail.longest_hike(nums, k))
