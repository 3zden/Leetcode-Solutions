def topKFrequent( nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        out = []
        dicto = {}
        for i in nums :
            if i not in dicto :
                dicto[i] = 1
            else :
                dicto[i] += 1
        sorted_dict = sorted(dicto.items(), key=lambda item: item[1], reverse = True)
        out = sorted_dict[0:k]
        return [ num for (num, freq) in sorted_dict[0:k]]

