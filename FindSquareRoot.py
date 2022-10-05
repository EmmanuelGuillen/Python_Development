    def mySqrt(self, x: int) -> int:
        for a in range (0,x +1):
            if a*a == x:
                return a
            if a*a > x:
                return a-1
        return -1
