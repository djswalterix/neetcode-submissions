class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum_speed=max(piles)
        if(h==len(piles)):
            return maximum_speed
        minimum_speed=1

        last_good_speed=maximum_speed
        while minimum_speed<=maximum_speed:
            candidate_speed=(minimum_speed+maximum_speed)//2
            time_spent=0
            for pile in piles:
                time_spent+=math.ceil(pile/candidate_speed)
            print("candidate_speed",candidate_speed,"time_spent",time_spent,"minimum_speed",minimum_speed,"maximum_speed",maximum_speed)
            if time_spent>h:
                minimum_speed=candidate_speed+1
            else:
                last_good_speed = candidate_speed
                maximum_speed=candidate_speed-1

        return last_good_speed
        