import heapq
class Solution:
        def hotel(self, arrive, depart, K):
            num_of_rooms = K
            rooms_q = []
            zipped = zip(arrive, depart)
            arrv_dept = sorted(zipped, key=lambda x: x[0])
            for a_d in arrv_dept:
                while rooms_q and rooms_q[0] <= a_d[0]:
                    heapq.heappop(rooms_q)
                    num_of_rooms += 1
                if len(rooms_q) < K:
                    heapq.heappush(rooms_q, a_d[1])
                    num_of_rooms -= 1
                else:
                    return False
            return True
