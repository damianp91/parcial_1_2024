





if __name__== '__main__':
    import csv, json
    from app import ts_gestion_proyectos_app
    
    with open('Proyectos.csv', 'r') as file:
        read = csv.DictReader(file)
        
        for row in read:
            print(row)
    
    ts_gestion_proyectos_app()