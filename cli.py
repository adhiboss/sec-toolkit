import argparse
from scripts import port_scanner

parser = argparse.ArgumentParser(description="Security Toolkit CLI")

parser.add_argument("--port-scan", help="Target IP")
parser.add_argument("--start-port", type=int, default=1)
parser.add_argument("--end-port", type=int, default=100)

args = parser.parse_args()

if args.port_scan:
    port_scanner.scan(args.port_scan, args.start_port, args.end_port)
