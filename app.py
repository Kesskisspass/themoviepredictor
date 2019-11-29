# python app.py movies list --export chemin_fichier.csv

import mysql.connector as mariadb
import csv
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("table")
parser.add_argument("action")
parser.add_argument("--file")
args = parser.parse_args()

mariadb_connection = mariadb.connect(user='root', password='root', database='themoviepredictor')
cursor = mariadb_connection.cursor()

cursor.execute(f"SELECT * FROM {args.table}")

#os.remove("export.csv")

if args.action == "export":
    if args.file != None:
        with open(f'{args.file}', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([i[0] for i in cursor.description]) # ecrit nom colonnes
            csv_writer.writerows(cursor) # ecrit contenu des lignes
    else:
        for movie in cursor:
            print(movie)
elif args.action == 'import':
    if args.file != None:
        with open(f'{args.file}', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(reader[0], row[2], row[3])
    else:
        print("Veuillez entrer un nom de fichier à lire")
else:
    print('sdkjsqslfd')

cursor.close()
mariadb_connection.close()