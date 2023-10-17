import os


def get_next_file(dataset_path, class_name):
    class_dir = os.path.join(dataset_path, class_name)
    files = sorted(os.listdir(class_dir))

    for file_name in files:
        yield os.path.join(class_dir, file_name)
    yield None


generator = get_next_file('dataset', 'positive')
for file_path in generator:
    if file_path is None:
        print("No more files!")
        break
    print(file_path)
