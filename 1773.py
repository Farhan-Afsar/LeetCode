class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        keys={
            'type': 0,
            'color':1,
            'name':2
        }
        count = 0
        index = keys[ruleKey]

        for i in items:
            if i[index] == ruleValue:
                count += 1
        return count