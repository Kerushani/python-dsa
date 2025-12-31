import collections

tasks = ["A", "B", "C", "D", "E"]

dependencies = [
    ("A", "C"),
    ("B", "C"),
    ("C", "D"),
    ("D", "E")
]

durations = {
    "A": 3,
    "B": 2,
    "C": 4,
    "D": 6,
    "E": 1
}

"""
Directed Graph

3
A ->  4    6    1 = 14 min
      C -> D -> E
B ->
2     

Task graph
{
    "A" : [C]
    "B" : [C]
    "C" : [D]
    "D" : [E]
}

"""

class TaskScheduler:
    def __init__(self):
        pass

    def task_scheduler(self, tasks, dependencies, durations):
        # building a graph -> keep trach of edges
        task_graph = collections.defaultdict(list)
        # indegree -> keep track of prereqs
        indegree = {t: 0 for t in tasks}
        print(indegree)

        for prereq, task in dependencies:
            if task =="C":
                print(prereq)
            task_graph[prereq].append(task)
            indegree[task] += 1

        earliest_start = {t: 0 for t in tasks}
        earliest_finish = {t: 0 for t in tasks}

        queue = collections.deque()
        # initalize the queue with tasks with no prereqs
        for task, num_of_prereqs in indegree.items():
            if num_of_prereqs == 0:
                queue.append(task)
                earliest_start[task] = 0
                earliest_finish[task] = durations[task]
        
        # start with the tasks that don't have prereqs, this is the order that will be outputted
        order = []
        
        # start the look to go to each node
        while queue:
            curr_task = queue.popleft()
            # keep track of order in which tasks are completed
            order.append(curr_task)

            for next_task in task_graph[curr_task]:
                # next task can't start until the current task is finished
                earliest_start[next_task] = max(earliest_start[next_task], earliest_finish[curr_task])
                earliest_finish[next_task] = earliest_start[next_task] + durations[next_task]
                
                indegree[next_task] -= 1

                if indegree[next_task] == 0:
                    earliest_finish[next_task] = earliest_start[next_task] + durations[next_task]
                    # print(queue)
                    queue.append(next_task)

        if len(order) != len(tasks):
            raise ValueError("Length of order output doesn't match length of tasks")
        
        total_time = max(earliest_finish.values()) if tasks else 0
        return total_time, order
    
task_scheduler = TaskScheduler()
print(task_scheduler.task_scheduler(tasks, dependencies, durations))


        

