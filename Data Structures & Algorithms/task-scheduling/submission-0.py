class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for task in tasks:
            if task not in count:
                count[task] = 0
            count[task] += 1

        # Python heapq is a min heap.
        # To simulate a max heap, store negative counts.
        maxHeap = []

        for task in count:
            heapq.heappush(maxHeap, -count[task])
        
        # queue stores tasks that are cooling down
        # each item is [remaining_count, time_when_available]
        queue = deque()

        time = 0

        # keep going while:
        # 1. there are tasks available in the heap
        # OR
        # 2. there are tasks cooling down in the queue
        while maxHeap or queue:
            time += 1

            # if a task is available, run the most frequent one
            if maxHeap:
                currentCount = heapq.heappop(maxHeap)

                # We ran one task.
                # Since count is negative, add 1 to move it closer to 0.
                # Example: -3 becomes -2
                currentCount += 1

                # if this task still has remaining uses,
                # put it into cooldown
                if currentCount != 0:
                    queue.append([currentCount, time + n])

            # if the first cooling task is ready,
            # put it back into the heap
            if queue and queue[0][1] == time:
                readyTask = queue.popleft()
                heapq.heappush(maxHeap, readyTask[0])

        return time