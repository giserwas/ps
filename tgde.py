# import geopandas as gpd
# from shapely.geometry import Point
# from shapely.ops import nearest_points
# import csv
# import pandas as pd
# import numpy as np

def calculate_distances(layer1, layer2):
    my_2d_array = []

    # Initialize the 2D array
    for i in range(len(layer2)):
        my_2d_array.append([])

    # Calculate distances and populate the 2D array
    for i in range(len(layer2)):
        pointi = layer2.iloc[i].geometry
        for j in range(len(layer1)):
            pointj = layer1.iloc[j].geometry
            distances = pointj.distance(pointi)
            my_2d_array[i].append(distances)

    # Convert the 2D array to a DataFrame and save to CSV
    df = pd.DataFrame(my_2d_array)
    df.to_csv('result/distance.csv', header=0, index=None)
    print("OK")

def TGDE(input_file, output_file, n, time, velocity):
    with open(input_file, 'r', encoding='utf-8', newline='') as csv_in_file:
        with open(output_file, 'w', newline='') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)

            my_2d_array = [[]]

            # Process each row in the input CSV
            for row_list in filereader:
                for i in range(1):  # Using 1 to iterate only once
                    column1_value = float(row_list[i])
                    column2_value = float(row_list[i + 1])
                    total_sum = column1_value + column2_value

                    # Calculate G based on conditions
                    if total_sum <= time * velocity:
                        G = (time * velocity) / total_sum
                    else:
                        G = 0

                    my_2d_array[i].append(G)

            # Convert the 2D array to a DataFrame and save to CSV
            df = pd.DataFrame(my_2d_array)
            df.to_csv(output_file, header=None, index=False)
            print("Finish")
