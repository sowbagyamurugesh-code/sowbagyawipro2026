import csv
with open("data.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["name","id","age"])
    writer.writerow(["Nithya","1","10"])
    writer.writerow(["Sri","2","11"])