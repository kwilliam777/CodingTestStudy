class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return True if "".join(sorted(str(n))) in ["".join(sorted(str(2**i))) for i in range(35)] else False
