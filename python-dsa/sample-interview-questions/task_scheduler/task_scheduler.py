"""
You’re building a simplified task scheduler that runs periodic jobs based on timestamps. Each task has:

- a task_id (string)
- a start_time (integer, in seconds)
- a repeat_interval (in seconds)
- a run_duration (in seconds)

The scheduler receives a system uptime (in seconds) and needs to determine which tasks would currently be running.

A task begins running at start_time, and every repeat_interval after that.

A task is considered running if the current uptime falls within the interval:
start_time + n * repeat_interval <= uptime < start_time + n * repeat_interval + run_duration

You must return a list of currently running task_ids.

Handle edge cases like:
- tasks with start_time > uptime
- tasks with repeat_interval = 0 (should only run once)
- tasks that would have already stopped repeating
"""