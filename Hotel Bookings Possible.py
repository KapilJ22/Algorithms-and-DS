import heapq
class Solution:
        def hotel(self, arrive, depart, K):
            num_of_rooms = K
            rooms_q = []
            zipped = zip(arrive, depart)
            arrv_dept = sorted(zipped, key=lambda x: x[0])
            # print(arrv_dept)
            for start in arrv_dept:
                # print("i {},start: {},rooms_q: {},num_of_rooms: {}".format(i,start,rooms_q,num_of_rooms))
                while rooms_q and rooms_q[0] <= start[0]:
                    heapq.heappop(rooms_q)
                    num_of_rooms += 1
                if len(rooms_q) < K:
                    heapq.heappush(rooms_q, start[1])
                    num_of_rooms -= 1
                else:
                    # print("i {},start: {},rooms_q: {},num_of_rooms: {}".format(
                    #     i, start, rooms_q, num_of_rooms))
                    return False
            return True
