from os import path, mkdir
import argparse

def create_gitkeep_file(dir_path: str):
    f = open(dir_path + '/.gitkeep', 'w')
    f.write('')
    f.close()

def get_semester_dir_name(semester: int):
    return 'semester-' + str(semester)

def check_semester_existence(semester: int):
    return path.exists(get_semester_dir_name(semester))

def create_semester(semester: int):
    if check_semester_existence(semester):
        print('Semester already exists')
        return

    mkdir(get_semester_dir_name(semester)) 

def check_subject_existence(semester: int, name: str):
    if not check_semester_existence(semester):
        return False
    
    return path.exists(get_semester_dir_name(semester) + '/' + name)

def create_subject(semester: int, name: str):
    if check_subject_existence(semester, name):
        return

    semester_dir = get_semester_dir_name(semester)
    dirs = ['', 'books-and-material', 'exercises', 'projects', 'notes', 'slides-and-resources']
    
    for part_dir in dirs:
        mkdir(f'{semester_dir}/{name}/{part_dir}')
        create_gitkeep_file(f'{semester_dir}/{name}/{part_dir}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create folder structures for UNI subjects')
    parser.add_argument('--semester', '-S', dest='semester', type=int, required=True)
    parser.add_argument('--subject', '-s', dest='subject', type=str, required=False)

    args = parser.parse_args()
    create_semester(args.semester)
    
    if args.subject:
        create_subject(args.semester, args.subject)


