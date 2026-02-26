def combinationSum2(candidates, target):
    candidates.sort()
    result = []
    
    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(path[:])
            return
        
        for i in range(start, len(candidates)):
            
            # Skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            # Stop if number exceeds remaining target
            if candidates[i] > remaining:
                break
            
            path.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i], path)
            path.pop()
    
    backtrack(0, target, [])
    return result
