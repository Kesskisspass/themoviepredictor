import argparse

parser = argparse.ArgumentParser()
parser.add_argument("table")
parser.add_argument("action")
parser.add_argument("--file", action="store_true")
args = parser.parse_args()

if args.file:
    print("Table :", args.table, "Action : ", args.action, "chemin fichier : ", args.file)
else:
    print("Table :", args.table, ", Action : ", args.action)