import shutil
import os
import csv


def copy_and_rename(dataset_path, dest_path, annotation_path):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    with open(annotation_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for class_name in ["negative", "positive"]:
            class_path = os.path.join(dataset_path, class_name)
            for file_name in sorted(os.listdir(class_path)):
                new_file_name = f"{class_name}_{file_name}"
                dest_file_path = os.path.join(dest_path, new_file_name)
                shutil.copy(os.path.join(class_path, file_name), dest_file_path)

                abs_path = os.path.abspath(dest_file_path)
                rel_path = os.path.relpath(dest_file_path, dataset_path)

                csvwriter.writerow([abs_path, rel_path, class_name])


copy_and_rename("dataset", "new_dataset", "new_annotation.csv")
