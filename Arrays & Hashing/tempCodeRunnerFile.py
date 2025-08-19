            for j in range(i+1,len(strs)):
                if sorted(strs[i])==sorted(strs[j]) and strs[j] not in subArr:
                    subArr.append(strs[j])