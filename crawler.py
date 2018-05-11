import os

def create_project_dir(directory): #checks to make sure directory doesn't exist already and creates if not
    if not os.path.exists(directory):
        print('creating directory' + directory)
        os.makedirs(directory)

def create_data_files(project_name, base_url): #checks for the presence of our text files and creates them if they don't exist
    queue = os.path.join(project_name,'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    if not os.path.exists(queue):
        write_file(queue, base_url)
    if not os.path.exists(crawled):
        write_file(crawled, '')

def write_file(path, data): #writes the text files to disk
    with open(path, 'w') as f:
        f.write(data)

def append_to_file(path, data): #opens the file and appends the data
    with open(path, 'a') as f:
        f.write(data, '\n')

def delete_file_contents(path): #opens the file and clears the data
    open(path, 'w').close()

def file_to_set(file_name): #takes a set of links, rather than opening the file to retrieve them over and oer
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

def set_to_file(links, file_name): #sets the links back to the file when we're done dealing with them in the set
    with open(file_name, "w") as f:
        for l in sorted(links):
            f.write(l+"\n")



