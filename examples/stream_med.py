import heapq

def calc_med(num_stream):
    min_heap = []
    max_heap = []
    for num in num_stream:
        if len(min_heap) == 0:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappush(max_heap, -num)
        if len(min_heap) - len(max_heap) > 1:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        elif len(max_heap) - len(min_heap) > 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        if len(min_heap) == len(max_heap):
            print((min_heap[0] - max_heap[0]) / 2)
        elif len(min_heap) > len(max_heap):
            print(min_heap[0])
        else:
            print(-max_heap[0])

calc_med([2, 1, 5, 7, 3, 0, 5]+[2, 1, 5, 7, 2, 0, 5]+[2, 1, 5, 7, 2, 0, 5])

print(sorted([2, 1, 5, 7, 2, 0, 5]+[2, 1, 5, 7, 2, 0, 5]+[2, 1, 5, 7, 2, 0, 5]))