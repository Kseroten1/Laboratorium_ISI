import csv

with open('pc.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["pc_name", "ip"]

    writer.writerow(field)
    for i in range(1, 101):
        a = "p" + (str(i))
        b = "172.30.2." + (str(i))
        writer.writerow([a, b])