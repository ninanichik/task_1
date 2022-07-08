#!/usr/bin/env python3

import time
import psutil
import csv
from csv import DictWriter
import sys
import subprocess


def get_cpu():
    cpu = psutil.cpu_percent()
    print(f'CPU usage is: {cpu} %')
    return cpu


def get_vms(process_id):
    vms = psutil.Process(process_id).memory_info().vms
    print(f'Virtual Memory Size - vms: {vms} B')
    return vms


def get_rss(process_id):
    rss = psutil.Process(process_id).memory_info().rss
    print(f'Resident Set Size - rss: {rss} B')
    return rss


def get_file_descriptors(process_id):
    fds = psutil.Process(process_id).num_fds()
    print(f'Number of file descriptors: {fds}')
    return fds


def create_csv(process_id):
    provided_interval = int(input('Input time interval in seconds: '))
    headers_csv = ['cpu', 'vms', 'rss', 'fds']
    with open('data.csv', 'w') as csvfile:
        wr = csv.writer(csvfile)
        wr.writerow(headers_csv)
    while (True):
        csv_data = {'cpu': get_cpu(), 'vms': get_vms(process_id), 'rss': get_rss(process_id), 'fds': get_file_descriptors(process_id)}
        with open('data.csv', 'a', newline='') as csvfile:
            writer = DictWriter(csvfile, fieldnames=headers_csv)
            writer.writerow(csv_data)
        time.sleep(provided_interval)


if __name__ == '__main__':
    exec_path = sys.argv[1]
    process = subprocess.Popen(exec_path, stdout=subprocess.PIPE)
    create_csv(process.pid)
