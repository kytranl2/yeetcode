def update_priorities(processes):
    from collections import deque, defaultdict
    from math import floor

    # Initialize the queue and the dictionary for priority counts
    process_queue = deque(processes)
    priority_count = defaultdict(int)
    for p in processes:
        priority_count[p] += 1

    while True:
        # Find the highest priority that is shared by at least two processes
        bp = 0
        for priority in sorted(priority_count.keys(), reverse=True):
            if priority_count[priority] > 1:
                bp = priority
                break

        # Terminate if no such priority exists
        if bp == 0:
            break

        # Execute process 1 and update priority of process 2
        first_index = next(i for i, p in enumerate(process_queue) if p == bp)
        second_index = next(i for i, p in enumerate(process_queue) if p == bp and i != first_index)

        # Remove process 1
        process_queue[first_index] = None
        priority_count[bp] -= 1
        # Update priority of process 2
        new_priority = floor(bp / 2)
        process_queue[second_index] = new_priority
        priority_count[new_priority] += 1
        priority_count[bp] -= 1

        # Clean up the queue and priority count dictionary
        process_queue = deque(p for p in process_queue if p is not None)
        if priority_count[bp] == 0:
            del priority_count[bp]

    return list(process_queue)
process_priorities = [4,4,2,1]
final_priorities = update_priorities(process_priorities)
print(final_priorities)