import csv
def mainmenu():
    print("..Welcome to CSV Module Program..")
    print("1. for checking rating of all movie's greater than 4.3")
    print("2. for checking movie's Name and release Date before 1990")
    print("3. for checking wild and west and no rating movie's name")
    print("4. List all movie names and release year for the movie names beginning with ‟A” and rating is null and release year is before 1978.")
    print("5.Display the count of the movies released in the year 1989 and duration is less than 1.5 hrs and rating is null")
    ch = eval(input("Enter your choice.."))
    if ch == 1:
        rating()
    elif ch == 2:
        release()
    elif ch == 3:
        name()
    elif ch == 4:
        starts_with_a()
    elif ch == 5:
        count_file()
    else:
        print("Error")
def rating():
    for i in csvread:
        if i[3]>'4.3' and i[3]!='':
            print(i)

def release():
    f = open("newmovies.csv",'w',newline='')
    csvwrite = csv.writer(f)
    for i in csvread:
        if i[2]<="1990" and i[3]!="":
            csvwrite.writerow([i[1],i[2]])
            print(i[1]," ",i[2])
    f.close()
def name():
    flag =0
    for i in csvread:
        if ("West" in i[1] or "Wild" in i[1]) and (i[3]==" " and i[4]>"7200"):
            flag =1
            print(i[1],' ',i[3])
    if flag == 0:
        print("No Data Found...")
def starts_with_a():
    fi = open("StartsA.csv",'w',newline='')
    csvwri = csv.writer(fi)
    for i in csvread:
        if i[1].startswith("A") and i[3]=="" and i[2]<"1978":
            csvwri.writerow([i[1],i[2]])
            print(i[1],' ',i[2])
    fi.close()
def count_file():
    count1 = 0 
    for i in csvread:
        if i[2]=="1989" and i[4]<"5400" and i[3]=="":
            count1+=1
    print("Count of movies =",count1)
file = open("dataset-movies.csv",'r')
csvread = csv.reader(file)
mainmenu()
file.close()