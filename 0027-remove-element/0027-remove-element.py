class Solution(object):
  def removeElement(self, nums: List[int], val: int) -> int:
    """
    Removes elements equal to 'val' from the list 'nums' in-place and returns the new length.

    Args:
      nums: A list of integers.
      val: The value to remove from the list.

    Returns:
      The new length of the list after removing elements equal to 'val'.
    """

    i = 0  # Index to keep track of non-target elements

    for num in nums:
      if num != val:
        nums[i] = num  # Move non-target elements to the beginning
        i += 1  # Increment index for next non-target element

    return i 
        
        