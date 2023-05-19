import csv 


def get_coordinates():
    with open('../NYPD_Complaint_Data_Historic.csv') as f: 
        reader = csv.reader(f) 
        output = open("output.txt", "a") 
        for row in reader: 
            # print the latitude and longitude into the output file
            # out 
            print((row[27], row[28]), file=output)
