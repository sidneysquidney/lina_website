from os import listdir
from os.path import isfile, join
from collections import namedtuple

Blog = namedtuple('Blog', 'page title description')
dartmoor = Blog('dartmoor', 'Wild-Camping, Wild-Horses, Wild-Dartmoor', '"Misty mornings, syrupy rivers, ewes and foals in gorse and heather. This trip was the immersion in nature I so badly needed after 4 months of quarantine."')
cornwall = Blog('cornwall', 'Saltwater Serenades', '"We watched from the highest cliff, as below us the tide came in. And just like that, the water divided the land clean into two."')
blogs_dict = {'dartmoor': dartmoor, 'cornwall': cornwall}

# gets urls (relative to templates) for images from the directory given by section/page/col_one & col_two, 
def get_files(section, page):
    c1 = './static/images/' + section + '/' + page + '/col_one/'
    c2 = './static/images/' + section + '/' + page + '/col_two/'
    col_one = ['/.' + c1 + f for f in listdir(c1) if isfile(join(c1, f))]
    col_two = ['/.' + c2 + f for f in listdir(c2) if isfile(join(c2, f))]
    col_one_dict = {c[c.rfind('/') + 1: c.rfind('.')].replace('_', ' '): c for c in col_one}
    col_two_dict = {c[c.rfind('/') + 1: c.rfind('.')].replace('_', ' '): c for c in col_two}
    return col_one_dict, col_two_dict

def get_blog_texts(page):
    path = './static/images/blog/' + page + '/'
    lst = [path + f for f in listdir(path) if isfile(join(path, f)) and '.txt' in f]
    blog_texts = {b[b.rfind('/') + 1:].replace('.', '_'): b for b in lst}
    return blog_texts

def turn_into_string(file_name):
    with open(file_name, 'r') as file:
        content = file.read().replace('\n', ' ')
#         content = [x for x in content.split(' ') if x != '']
    return content

# enter blog page from this level, and get a dictionary including 
# {cover_jpg: url (relative to blog.html), 1_jpg.. 1_txt: 'text', title, description, count}
def get_blog_files(page):
    path = './static/images/blog/' + page + '/'
    lst = ['/.' + path + f for f in listdir(path) if isfile(join(path, f)) and '.jpg' in f]
    blog_files = {b[b.rfind('/') + 1:].replace('.', '_'): b for b in lst}
    for key, value in get_blog_texts(page).items():
        blog_files[key] = turn_into_string(value)
    blog_files['count'] = (len(blog_files) - 2) // 2
    return blog_files

home_page = []