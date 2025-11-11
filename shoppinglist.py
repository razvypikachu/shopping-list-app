import sys
import argparse

def main():
	mainparser = argparse.ArgumentParser()
	subparsers = mainparser.add_subparsers(dest="command", required=True, help="Comenzi disponibile:")
	
	if len(sys.argv) == 1:
		mainparser.print_help(sys.stderr)
		sys.exit(1)
		
	args = mainparser.parse_args()
	print(f"Comanda {args.command}")

if __name__ == "__main__":
	main()
