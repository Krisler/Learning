def containsDuplicate(self, nums):
  """
    :type nums: List[int]
    :rtype: bool
  """
  duplicate = set()
  for i,num in enumerate(nums):
    if num in duplicate:
        return True
    duplicate.add(num)
  return False
