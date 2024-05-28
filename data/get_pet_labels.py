#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Marah
# DATE CREATED:   26/5/2024
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    in_files = listdir(image_dir)
    results_dic ={}
    for file in range(0, len(in_files), 1):

        # Skips file if starts with . (like .DS_Store of Mac OSX) because it
        # isn't an pet image file
        if in_files[file][0] != ".":

            # Sets string to lower case letters
            # Splits lower case string by _ to break into words
            pet_image = in_files[file].lower().split("_")
            pet_label = ""
            for word in pet_image:
                if word.isalpha():
                    pet_label += word + " "
            pet_label = pet_label.strip()
            if in_files[file] not in results_dic:
                results_dic[in_files[file]] = [pet_label]

            else:
                print("** Warning: Duplicate files exist in directory:",
                      in_files[file])

    return results_dic
