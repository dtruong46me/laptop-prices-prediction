import pickle as pk
import pandas as pd
from mapping import *

PARENT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PARENT_PATH = os.path.abspath(os.path.join(PARENT_PATH, '..'))
DATA_PATH = os.path.abspath(os.path.join(PARENT_PATH, "data", "raw", "cpu_gpu_mark"))

CPU_FILENAME = "cpu_mark.csv"
GPU_FILENAME = "gpu_mark.csv"

cpu_df = pd.read_csv(os.path.abspath(os.path.join(DATA_PATH, CPU_FILENAME)), index_col = 0)
gpu_df = pd.read_csv(os.path.abspath(os.path.join(DATA_PATH, GPU_FILENAME)), index_col = 0)

cpu_name_list = [cpu_df['CPU Name'][idx].lower() for idx in cpu_df.index]
gpu_name_list = [gpu_df['GPU Name'][idx].lower() for idx in gpu_df.index]

def predict(model_name: pk.Pickler, 
            brand: str, 
            cpu_name: str, 
            gpu_name: str,
            monitor: str,
            monitor_size: str,
            ram: str,
            storage: str,
            os: str,
            weight: str) -> float:

    # Transform data to predict
    name_cpu, cpu_mark = get_cpu_name(cpu_name)
    name_gpu, gpu_mark = get_gpu_name(gpu_name)

    # Monitor to Float
    if "\"" in monitor or "\'" in monitor:
        elements = monitor.split()
        if len(elements) == 2:
            pros_monitor, _ = elements[0], elements[1]
            pros_monitor = float(pros_monitor[:-1])

        if len(elements) == 1:
            monitor = elements[0]
            pros_monitor = float(pros_monitor[:-1])
    else:
        pros_monitor = float(monitor[:-1])

    # Monitor size
    width, height = [float(x.strip()) for x in monitor_size.split("x")]

    