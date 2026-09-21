class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        on=set()
        for i in bulbs:
            if i in on:
                on.remove(i)
            else:
                on.add(i)
        return sorted(on)
        