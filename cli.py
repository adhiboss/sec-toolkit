#!/usr/bin/env python3

import argparse
from scripts import port_scanner, network_scanner

def main():
    import argparse
    from scripts import port_scanner, network_scanner

    def banner():
        print("\033[91m")
        print("SEC TOOLKIT")
        print("\033[0m")

    parser = argparse.ArgumentParser(prog="sec-toolkit")
    subparsers = parser.add_subparsers(dest="command")

    port_parser = subparsers.add_parser("scan-port")
    port_parser.add_argument("target")
    port_parser.add_argument("--start", type=int, default=1)
    port_parser.add_argument("--end", type=int, default=100)

    network_parser = subparsers.add_parser("scan-network")

    args = parser.parse_args()

    banner()

    if args.command == "scan-port":
        port_scanner.scan(args.target, args.start, args.end)
    elif args.command == "scan-network":
        network_scanner.scan_network()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
