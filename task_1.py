#!/usr/bin/env python

import os
import time
import psutil
import csv
from csv import DictWriter


def get_cpu():
    cpu = psutil.cpu_percent()
    print(f'CPU usage is: {cpu} %')
    return cpu


def get_vms():
    vms = psutil.Process(os.getpid()).memory_info().vms
    print(f'Virtual Memory Size - vms: {vms} B')
    return vms


def get_rss():
    rss = psutil.Process(os.getpid()).memory_info().rss
    print(f'Resident Set Size - rss: {rss} B')
    return rss


def get_file_descriptors():
    fds = psutil.Process(os.getpid()).num_fds()
    print(f'Number of file descriptors: {fds}')
    return fds


def create_csv():
    provided_interval = int(input('Input time interval in seconds: '))
    headers_csv = ['cpu', 'vms', 'rss', 'fds']
    with open('data.csv', 'w') as csvfile:
        wr = csv.writer(csvfile)
        wr.writerow(headers_csv)
    while (True):
        csv_data = {'cpu': get_cpu(), 'vms': get_vms(), 'rss': get_rss(), 'fds': get_file_descriptors()}
        with open('data.csv', 'a', newline='') as csvfile:
            writer = DictWriter(csvfile, fieldnames=headers_csv)
            writer.writerow(csv_data)
        time.sleep(provided_interval)


if __name__ == '__main__':
    create_csv()
