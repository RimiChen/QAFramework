import os

def file_function(folder_name):
    #dir = os.path.dirname("./projects/"+folder_name)
    dir = os.path.join('./projects/', folder_name)
    if not os.path.exists(dir):
        os.makedirs(dir)
        folder_path = "./projects/"+str(folder_name)
        input_dir = os.path.join( folder_path, "input")
        os.makedirs(input_dir)
        output_dir = os.path.join(folder_path, "output")
        os.makedirs(output_dir)
        algorithm_dir = os.path.join(folder_path, "algorithm")
        os.makedirs(algorithm_dir)
        print("=============="+ folder_name +" has created.")


    else:
        print("=============="+ folder_name +" exist.")

    