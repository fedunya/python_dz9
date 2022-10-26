import csv, json

def unload(file_name):
    fields = []
    data_base = []
    with open(file_name, 'r', encoding = 'utf-8') as f:
        csv_f = csv.reader(f)
        fields = next(csv_f)            
        for row in csv_f:            
            data_base.append(row)
        count_entrys = csv_f.line_num
    return data_base, fields, count_entrys
def export_txt(file_name, data, fields, count):
    with open(file_name, 'w', encoding = 'utf-8') as txt:
        txt.write('')
    for row in data:
        with open(file_name, 'a') as txt:
            txt.write(f'{fields[0]}: {row[0]},{fields[1]}: {row[1]},'
                f'{fields[2]}: {row[2]},{fields[3]}: {row[3]}\n')
    return
def export_json(file_name, data, fields, count):
    d_json = []
    for row in data:
        d_json.append(dict(zip(fields, row)))
    with open(file_name, 'w', encoding = 'utf-8') as json_file:
        json.dump(d_json, json_file, indent = 5)
def import_txt(file_name):    
    with open(file_name, 'r', encoding = 'utf-8') as f:
        data = f.read()    
    list_data = []
    for line in data.splitlines():
        line = line.replace(',',' ')                
        data_list = list(filter(lambda x: ':' not in x, line.split()))
        list_data.append(data_list)
    return list_data
def data_to_csv(file_name, list_data):
    with open(file_name, 'a', encoding = 'utf-8') as csvfile:
        wr_csv = csv.writer(csvfile, lineterminator = '\r')    
        for i in list_data:
            wr_csv.writerow(i)
    return
def import_json(file_name):
    with open(file_name, 'r', encoding = 'utf-8') as jsonfile:
        data = json.load(jsonfile)        
    list_data = []
    for d in data:
        data_list = list(map(str, d.values()))
        list_data.append(data_list)    
    return list_data
