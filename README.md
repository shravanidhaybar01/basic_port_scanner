
# Basic Port Scanner

A multithreaded Python Port Scanner that scans a target IP address or hostname to identify open TCP ports efficiently.

## Features

- TCP port scanning
- Multithreaded scanning for faster performance
- Scans a user-defined port range
- Displays open ports
- Lightweight and beginner-friendly cybersecurity project
- Command-line based interface

## Technologies Used

- Python 3
- Socket Module
- Threading Module
- Sys Module

## Requirements

No external libraries are required. The project uses Python's built-in modules:

- socket
- threading
- sys

## How It Works

The scanner creates multiple threads to scan ports simultaneously. Each thread attempts to establish a TCP connection with a specific port on the target host. If the connection succeeds, the port is reported as open.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/shravanidhaybar01/basic_port_scanner.git
