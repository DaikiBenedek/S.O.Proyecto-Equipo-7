from functools import reduce

"""
Class that holds and compiles data of interest for the simulation
"""
class Metrics:

    def __init__(self, name):
        self.name = name
        self.processes = {} # dictionary of completed processes
        self.cpu_use_time = 0 # during how many ticks has a process been processed. Higher = better
        self.simulation_ticks = 0 # how many total ticks has the simulation run for. 
        # Metrics we will measure
        self.throughput = None # completed processes 
        self.avg_turnaround_time = None
        self.avg_waiting_time = None
        self.avg_response_time = None
        self.cpu_utilization = None 

    """
    Increases in-class counter time by one
    used_cpu: whether the cpu was used during this time
    """
    def increase_counter_time(self, used_cpu=True):
        self.simulation_ticks += 1
        if used_cpu:
            self.cpu_use_time += 1

    """
    Adds a new process to the list of processes
    p: process to add to dictionary or to update, if it's already in the dictionary
    """
    def add_to_processes(self, p):
        pid = p.pid
        if pid in self.processes:
            self.processes.update(pid=p)
        else:
            self.processes[pid] = p

    """
    Actualiza las métricas en el tick actual
    """
    def compute_metrics(self):
        finished_processes = 0
        acc_turnaround_time = 0
        acc_waiting_time = 0
        acc_response_time = 0
        if self.processes:
            for p in self.processes.values():
                if p.is_finished():
                    finished_processes += 1 
                acc_turnaround_time += p.turnaround_time
                acc_waiting_time += p.waiting_time
                acc_response_time += p.waiting_time
        self.throughput = finished_processes / len(self.processes)
        self.avg_turnaround_time = acc_turnaround_time / len(self.processes)
        self.avg_waiting_time = acc_waiting_time / len(self.processes)
        self.avg_response_time = acc_response_time / len(self.processes)

    def __str__(self):
        return f"""
        Scheduling Algorithm: {self.name}
        Total Simulation Runtime: {self.simulation_ticks}
        Number of Processes Completed: {len(self.processes)}
        Throughput: {self.throughput}
        Average turnaround time: {self.avg_turnaround_time}
        Average waiting time: {self.avg_waiting_time}
        Average response time: {self.avg_response_time}
        """