import csv
import os


def get_csv_data(filename):

    parent_dir = os.getcwd()
    filepath = os.path.abspath(parent_dir+filename)

    data = []
    with open(filepath) as file:
        obj = csv.reader(file)
        row_key = next(obj)
        for row in obj:
            data.append({row_key[i]:row[i] for i in range(len(row))})
        return data


"""
username,password,err_msg
Admin,,Password cannot be empty


[{"username":"","password":"admin123","err_msg":"Username cannot be empty"},
 {"username":"Admin","password":"","err_msg":"Password cannot be empty"}]

"""