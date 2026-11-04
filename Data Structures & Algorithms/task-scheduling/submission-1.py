class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # populate hashmap
        count = {}
        for task in tasks:
            if task not in count:
                count[task] = 0
            count[task] += 1
        print(count)
        
        # populate maxHeap
        maxHeap = [-freq for freq in count.values()]
        heapq.heapify(maxHeap)

        queue = deque()

        time = 0

        while maxHeap or queue: # tasks remain
            time += 1
            if maxHeap:
                popped = heapq.heappop(maxHeap)
                popped += 1

                if popped != 0: # still remaining
                    queue.append((popped,time+n))

            if queue and queue[0][1] <= time: # when next can be popped
                readyTask = queue.popleft()
                heapq.heappush(maxHeap,readyTask[0]) # count only
        return time

        