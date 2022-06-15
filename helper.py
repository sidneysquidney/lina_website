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

about = 'https://lh3.googleusercontent.com/pw/AM-JKLU6awzEssLZ7lvBFGJK1r5ac2eA-aESAQJ98issx2qVrrVBZ1CMMzNZzp9UWNgpxWQaVWQoO4M4wcdqZFc1xGDab-SRg59fsiSXfg7dTF9LwMcXi9gciaqLpL5nJ3BabIJFRl6qXqh-a8i2zY5Rv6ya=w1582-h1188-no?authuser=0'

# home_page
drops = 'https://lh3.googleusercontent.com/pw/AM-JKLVQT0I8a-aOpTUXrce6jSxHLPddJvNbuDhLbG8EHs8e5lB94JWZVUK5S3cn4jvFBFWZMUsezPClC9jWG-3sbni7pJP_lH2IQlESCHr7ERVx2YjmVta6soTbX6n_aNJAd3w4RXU97F9Fu1lpwx9p-jcR=w1780-h1186-no?authuser=0'
pool = 'https://lh3.googleusercontent.com/pw/AM-JKLU6ubtAba6S_Mb2ZkjXv1ExHykJiwIUnx8dcjdiarjBMftTCm0PlWmSCN5LajQcFVnDaC7gjn7B1xtsdJKH-n8_O5CwTM5SnpaviFA58UpnzC9dfhtDnGmSSv5rt1X0y3z0h22-Y3hbrddrXJaT8ini=w1780-h1186-no?authuser=0'
freckles = 'https://lh3.googleusercontent.com/pw/AM-JKLU_yG1ggXzROPYaxeNhcCmL7LSI4BEJWjG4fEfoEoOyAG6hySRM6xxGduMcBdCGFWx89ae7Y5ObEtqX8d8sAZLieLPyQCGuOxBaaFTWgrPoxq2x-EZ_0Wt3lCd07txgZyMpozEFkjnO2N4IgF_0mY7F=w1780-h1186-no?authuser=0'
skate = 'https://lh3.googleusercontent.com/pw/AM-JKLXgVRp3yoiJ5dgz7CxfXA9TGC70MoVASOntO6HIAqRsnF_IeM3jTZYWiVhiSjCSkJixLPkCX4l3rYxB8wCZhrgLFg67nqCmwJMVe-4bva3T6d4Ard3xyAD8_RPlDNYp56mDyIf0YOdpzPwNv3l26wcl=w1784-h1186-no?authuser=0'
book = 'https://lh3.googleusercontent.com/pw/AM-JKLXyrHbFockrS1WyJv3H-OWEOuZghvVCJUzmNdUj4yBfzu3PWASM1smSGzwQ16eGL19Gv0TlRgAlgwFw2MCuI5JECxoqc1G-e7alojR6sh_Oq1jrKhWcQjDA7DH2-nO8zt7ggJWHkJkXbk-iqJDrYkgf=w1780-h1186-no?authuser=0'
blue = 'https://lh3.googleusercontent.com/pw/AM-JKLUSdOJZ5hhasv4W65g5hJozagVdE4KH_AomzuRPdnap9sxxMvzfFgxOIsXj4tfry_Dnn89Z323MgLT0TdTUP4WyYRyxl6rYxx3bMRn4w6gBrTvh5_nNJg14tgk-MgSq6WRnCTNMsl7qjh3NuwOG4cUD=w1780-h1186-no?authuser=0'
stallion = 'https://lh3.googleusercontent.com/pw/AM-JKLWzky0XhmJtlpAi_GmpoC8J7Jqxr9ykJ9vObhrVvntDAoh3qt6kuEuu1H2cKb8GaYVGE20gkoweycfQuak7Xh-14AYEB7voAcUxRlG7UIQyYuMETVWiaJ9wQL-k_JOwYIBia-MWk1TAeSVqAmkByI_f=w1780-h1186-no?authuser=0'
# dartmoor
joy_pic = 'https://lh3.googleusercontent.com/pw/AM-JKLVfyiD7J50WMaA3PfaWzy6lXz4bZJedlWhFupZLZF2MQhyHZdskxampcGTnvr0KUwKbDPpaZaip5BFSzJ1iAga5NnUgGnWOlTh-hKHXsYLy1S9ORGctJAi41wfx903ISrh9Ep95E9VYm76EaDlrGnv4=w1780-h1186-no?authuser=0'
julia = 'https://lh3.googleusercontent.com/pw/AM-JKLWxWjyVHNoVwFb4GuOdYTgqsMy1GY0KPjgLyYaP7YekRJoRylo3jMLiVxAx4vgmzK-U2wVQTLeSXu1ViAZQEIahOJRutZLEE9fopW0bUOp6QO0xexykD7UrGj-_JAq0rL4VTmLC7QxkdxP_988JKHbt=w1780-h1186-no?authuser=0'
yoga = 'https://lh3.googleusercontent.com/pw/AM-JKLX0wndDxiHK3e3IA85WGB_lZGwC9LtokcCQORMUHNdVnlX0jEYNtux14keOlIVg-QSmq44BuUM0bKoBS2aLwMlKIH1JzJRHsGwgbB2q39g9LrvS5b1Wxo-EKmD5_1seI60MILsISN9Q8Gt8mY-C3PAT=w792-h1186-no?authuser=0'
yoga2 = 'https://lh3.googleusercontent.com/pw/AM-JKLWgmk83Abkw6mPfKKcJ575qHotMn84AfJEJ5LkXzH2CnxP0c3GgjrdWt0GumO6IKRpI32_LKBJTsw441fRZ6VG_T3n2FxLSwRIRne1e3KwWtyyhbbo7SpOwWfwdG602e1qel2IzM6txL5RdPZFmdHwZ=w792-h1186-no?authuser=0'
fabi = 'https://lh3.googleusercontent.com/pw/AM-JKLVlwYw_JJUNyEww7Qhq5ITmnqPy3uOuPwRNW6xjJCN475b3pQ_y2X4SWAI3jbMlZd2OzHxVFJDvtgF8qAXOFt7JZZCgbtKgw8gsmM4ArMfuxNfMimyfPZ-QOD1XfMYUhVlR9gs2kGZfzYFoZtw14EyM=w1780-h1186-no?authuser=0'
fabi2 = 'https://lh3.googleusercontent.com/pw/AM-JKLV9QeGXF4_4VsQR509jCgf6BL04K7Lksb1O0t7bLNwArdUA6oXYKMY_L1jrcKdEkBxysvt1rv2r5RYAhchoezWXWVmsNJuax3ol1gkO664FmPuEZ_bpIt8iizuuzyIXzhTMqY37nMUW8CYYUNEkA836=w1780-h1186-no?authuser=0'


# portraits
smoking = 'https://lh3.googleusercontent.com/pw/AM-JKLUmaUr3g_hs3Vqs_Ff9ZUFvbXmcXbnmpuXqXJj1u47YnFpEo5WbhBrlkfk5J_foYSIQjPCp6UAxDwAo9JE3oGcRnbZy6sWK5O9FhGSBPBCAFY9cTi1yeRam-G3MZSMYQ9IGCqkAejLNbMqJRa86xWr2=w1772-h1186-no?authuser=0'
shadow = 'https://lh3.googleusercontent.com/pw/AM-JKLV28ptehDJCMnA_nKxf9ROWJuP5gLxVGu-8ScDJiMZMfLVuEZVzH2MIx1CeDf054WdE3C-XUMVq5S-SML_M3Y0bkyyClBFW6Y8rgs5YrzE7N6Pofebv2SaPYmdWTs7tmITi2qh2_GwLGbygpoKhPO9b=w1772-h1186-no?authuser=0'
paint = 'https://lh3.googleusercontent.com/pw/AM-JKLUM-0gyQFl544CjTqdNNf4rDUQzSoZf_T0O2YAPcWyUOF86x7jCB9g8Apf0lP45_vXb2dhW32cinvoolnSgJPviJRsUGXBo52Wlc0fCMhAndV-3MCW_vgo7Ri-kY83EjIRKU_dFUC1-ym37u96kf0g6=w824-h1186-no?authuser=0'
milk = 'https://lh3.googleusercontent.com/pw/AM-JKLXm7CBiZ3ZBi8JfRQVnlhTbxKMk7tXpu7yTw_Lx9JqLWoD7b8SwDXwq3MWLSSO6syfIuuZv6OytjlRfbk8wBmHIKpyVBgydNMcclVdkDI1eKRzjO3vr73ENroTX7DfU3_myjxMkv1KFf9fZ-bT64zXz=w792-h1186-no?authuser=0'
kiss = 'https://lh3.googleusercontent.com/pw/AM-JKLXrZJqhLK04oQvlfEXrLhmj0lbZjn3SKEXDohg2hTVD-EbouAeNvJggCyKZcCwwxIhOp7b92CYnGAY2K9z0k5Yvvne9o7H0rBZcL3dqo4MvkmbxRLiN8_fo3APpDP3VaE33MR83NUSU1TQZKlt2bYuO=w1780-h1186-no?authuser=0'
mum = 'https://lh3.googleusercontent.com/pw/AM-JKLVPbcVvkabSj8-0_XYU1KV_5bOQCC8nTyN6Imi56NIJaquUUsgxVSpQKDfy9WDJw5odDyvIDpaemEU8S8rdXkc7MGJV_4mjgdIucZ278XeYsAQ8XDRLP6PeKCInZ_vOv-C8t1hHaqadqS-32dZsnLEz=w792-h1186-no?authuser=0'
bicepking3000 = 'https://lh3.googleusercontent.com/pw/AM-JKLUB7IFsowzvSkT1luuXh6uvw5QE_HPHaxrQiadtNJp07Whj9jFoUa3agT3z9Y_kTHd2Oeuqjkgc26eZBJs3RLsYfA-iHPm6FYayvd6UH-kJTvImZSHRzXf6erVC8k-ILnE_Mes8xI48qUOwXAIrOn7R=w1780-h1186-no?authuser=0'
kabir = 'https://lh3.googleusercontent.com/pw/AM-JKLUQ7cocUgrp85hOXISBxgtHeLcFkio265NrCkD-df6QPwYZ2MKK8gm0TpDk7S5NUHtKZvCDCWekSku0SsUGcbUKFAD7BkQqx652EAYP4xHVaAq4zmu_A-P_Qd-EKlxIyP6M7gXCJVZbHWNkz0xyfy6Z=w792-h1186-no?authuser=0'
dartmoor = 'https://lh3.googleusercontent.com/pw/AM-JKLUc2_ZPYoo5NrE3YRjVfPD1XGVKh9eD5UfKJli2WNEH9z47inmqa3BP1Gbi8O_MkUsyEkqaXkqsYbN3l2-FH9-ph5ITDU9gCsVNG_xTfMztrsQpIxvE0DxB7LyzsZmfLrTZvbEcUekMo7cbLOmlikbd=w792-h1186-no?authuser=0'
ben = 'https://lh3.googleusercontent.com/pw/AM-JKLVvwvlWsCt_Fdq-GIGbd1Wq_TZ6wrzOqPnpKEekyKvHUXZ9CpglWM3dUTsMgCa12FRWTtLZpto3ND-Z4sqAn7ZLHPFLRDBx9_8FNrtxjwuDm8lo-1Ti1q491wxjI_acFAaC3cAr5sMWwmRcd2knuuw4=w792-h1186-no?authuser=0'

home = [drops, blue, freckles, yoga, book, fabi, kiss, pool, stallion, joy_pic, julia, yoga2, fabi2, skate]

portraits = [smoking, shadow, paint, mum, ben, milk, dartmoor, bicepking3000, kabir, kiss]

# fashion
fashion = ['https://lh3.googleusercontent.com/pw/AM-JKLWci9xEq2f1WrzaWjUZ_Pq6V2ZgH8xnUnboWzW0qOZ7WNmC3GZMow6UIIldfcLMQkmLcERYBfaWvQPB-Zoe0RZ0NcBa-I1h-nnq6Gq4haW3aFd901x7lPwC-ApEgt6aF4-_RQLzK0GVt3wOvsFDzeNg=w1950-h1300-no?authuser=0', 
 'https://lh3.googleusercontent.com/pw/AM-JKLVhsK5biX_-GEFeeZBI1s7SXA5QAW8n-sn5N_vNPMil7mlBWmQ9W1gyvk2imYY3UnoAevY0ooiqTnv35YQT-cEboEKYYk4h6WcZZT0AdXoS5mFS4NAj9EqmYySzcObnmk6LEy0nYD6NPG5Lk6i9BKYq=w868-h1300-no?authuser=0', 
 
 'https://lh3.googleusercontent.com/pw/AM-JKLXWLOfzCqjuZfFAAl7Dg_KqWjK--BbUGtdSGPdry-LNpEafXocD9IezvjfKqGe4TshObESv_fAUU7zisGutlq9T2N9gMiwe9JmjNsbAyADFXbKv-lP7RjVSu5bE3jE-13NQyVZs4h8UCSPF9AGssb5d=w1950-h1300-no?authuser=0', 
 'https://lh3.googleusercontent.com/pw/AM-JKLX_3xeW4Dcbf0DexK41qU27SOeOVDISgSkdemOOOSq-_6c56N2Qjv5cTyvS18d7hovXrp6MJUlOJcqBmvA-BpXw6Kl8Urv_da9QgV9uhLTMbOCbohf8V_V4aSxWzFr8gbFqUFTKImZp1pzO3sIAbZBa=w868-h1300-no?authuser=0',
 pool, 
 'https://lh3.googleusercontent.com/pw/AM-JKLWJL3dgteCBfIGV_JhzC-ITVo-WvLOSi3pTyWawRGMXdXZhHwNM0AVVFLTYNfGQRYpw38FZdL-0D44XMKzSRX3D1ZgYeZZVE6nXZU7Uju2YtSRuDIMbFzgeiIfO6z2ZCxja_xGiZ57Hinj8hRZ2j48r=w868-h1300-no?authuser=0', 
 'https://lh3.googleusercontent.com/pw/AM-JKLVHRSjbBrGhC9YNX4OIkxsuvB1Yk7yV4aUQBbyfR-SVOVOoaCkJXwunPnVhxIQf3mYxhoGJaHHAPLwcUVaC73k2CvBWuMgugEijevlK_L84nbubex8wNb34cSdnpsoH1JhYY_aU-1sWRuXUjjF3sbjF=w1950-h1300-no?authuser=0',
 'https://lh3.googleusercontent.com/pw/AM-JKLXABtHBGaUGnjj43rgjuOVmSJtBQwy8aTfyMid1OmnRgdmpDCU8UXYn1t3crwzMwQc7mFqeSEPpA9LGG6OPXySjzRGxjVgYcwPMKVzm369u2rV_ijJY1JvBH9qTXKcFiUq--FyAwq2pL1k46DCodJBo=w2162-h1300-no?authuser=0', 
 'https://lh3.googleusercontent.com/pw/AM-JKLUI1baxjJ7Ut93aqDKKRzuxEZTlhRHLaYrRlUUWTs0xU1BVYsYm5bmVkarFqYaBf9dZidLPfrx7DaL8ooU_54X4FB3q9NLz_Gj-7VvzgRxtRwyE7PCKMYErQOA86RtfEY8zlMMKEjR9oxfhEK7Beo_J=w1950-h1300-no?authuser=0',
 ]

skateboarding = ['https://lh3.googleusercontent.com/pw/AM-JKLXw0QkJnmnHeuhyl_wQ3_Vl57RQZDjhx8KU5FZQXUjZCV7vkMJCMkdOkRkhKtsCOE3_MnPxYHjFUdSa9BwH6cjCLm3pRWMAZLPogyHPBr0bIeDj_JHCi1RVQ8yeqwkhN_gTdoOkJwl0o0AmbtVKAPEL=w1950-h1300-no?authuser=0',
                 'https://lh3.googleusercontent.com/pw/AM-JKLVwmCHCS78P8urOgxNiNHQwhRioDu3RsvcZXpaXmDLuJ36M6cd8tc2LV6ZH5T48MwlX34EBC4B4_l33__lNg0OFvdBAOQ7x6TRAy7MdafLnmnAcJaP5-pQFNeihbb1JlNQVlymVh_nwCLBB5czHTA72=w1950-h1300-no?authuser=0',
                 'https://lh3.googleusercontent.com/pw/AM-JKLUW9SP2hJYdkX0owX-OAJC05U7O6rw_FdWIa5xUSYDcqyyz_8BF4WMgFFI8CCrVhdK-MQXHuabaYKx7AFPaNWXrVP2Q6dGVBlqEd4Mq_h4GdKzmm_Y68jkf-npCv4HZzARc9f8GUwo8MOZGUD5Cs5FZ=w1950-h1300-no?authuser=0',
                 'https://lh3.googleusercontent.com/pw/AM-JKLWu48FteNqNECmjExa4J4yMGpsvM9byyH6bwcGc2Z72utab-c2iJUZA890uqoI_vf__PMx0lGeWJ8LFoOLa3nGnw95LHGqS2lwO5gp6pTtbED7XEZ1jxsCDlrR_zWOYPwuevFo8qAG9TKXdVqrHUVeD=w1950-h1300-no?authuser=0',
                 'https://lh3.googleusercontent.com/pw/AM-JKLWzLyxr2rUmSVYltFFDwLyZAeEQ4jRViNT_rqw11xvmfFU6jKvoSwqxVYnVDCp3raAz5vKAy35hGusMH7nGykyLUJx7l6MCxJjQR9Bhg432HLp2L4BcF5ySMFS_CKZvWYfox3tb_fgcG3_RTfs-BfDK=w1954-h1300-no?authuser=0',
                 'https://lh3.googleusercontent.com/pw/AM-JKLVE53zDv66BzPahrcXwLz0QNaiJTqv2HY6thwpRqQ-8QsXX2P5VU4x-yEXaUOpPARzlO66IzvI8XjTggv-VuE5w5r29-AQZVRG8PZGArWN8uuoqAMDTdcROWdQ5bHWb_VzwySEuEMs8gm4ZlJLbOA3B=w1978-h1300-no?authuser=0',
                #  'https://lh3.googleusercontent.com/pw/AM-JKLUC_v0FobAw8epbZtEUN7W2uT3Y4TpRBd6UhlGECuYP3Ar3FcaZZj-R81WGf2maz-NVjJox2WrE5A7lSex4xqtVOVSiMXFjsa5uMLPNaSKdXIe-b5HZ0Totxd5UeiTageXe5NOnr-LmNIqvgOkHk8Jo=w1958-h1300-no?authuser=0',
                 'https://lh3.googleusercontent.com/pw/AM-JKLX72TqjF3F4EjUc_zVjYuqXU_L3Z01ShYv7_EOh4RQWqMGA1ihcYGx_2aNuuj6j6MsXybPn0yGudhwUzgm5gz18oIpIGO67ejTgzx2U9vD4wjZol5Wd0Bv6NRocH7VKrWfnPSHrQxyxlUGa4lVCq9R8=w1950-h1300-no?authuser=0',
                 'https://lh3.googleusercontent.com/pw/AM-JKLUq92b3PUu9lXx7xDV9qhJv-a3oPhN5zQX7wZz3nkBfxLZRpdL5heZkbpfTABaInkIT2fInuSeO1Rf7a1U26N6EcKhngqK3Yx4z9WayFWNM3c12mZJYvk7d-MAbkYmGpjPD1dLeBFmXQKVPhjwPaGvu=w1950-h1300-no?authuser=0',
                 'https://lh3.googleusercontent.com/pw/AM-JKLWS_2ZvShmGs50yR_IRjwQUuPXQAwRDMAGHqrBnvp5xaBpn2mst883swMmvDffptX9t_aGaYxEm-02ltcZkaDDnljKkZIVJUUN425jSa4zQc2EIxnnXq2-tpnEPO6wS9qpHZFDEU-EhJVgoev4CpVH8=w1964-h1300-no?authuser=0',
                 'https://lh3.googleusercontent.com/pw/AM-JKLV5E_kquM5pOmX-6SBxKSY0Zvvy76ydo_G91IgXUKOAKNCEvoGRJQMtEbtLeuN7E6OHjxRKVzRMRbSPwWfnnbRFL3EUbnJKlpkjs-a818B0MguXKpmFulXgTlxB4miAM_ncJo0Y10ZX_uiCnmsesJ9I=w2160-h1300-no?authuser=0'
                 ]
chandos = ['https://lh3.googleusercontent.com/pw/AM-JKLW9MQrTzLuvTPXtasEg9xiPj7TlpC1K3NbiM3Ak0sLav42P2U6nPH8uwaREU3Gv4n7dXCTWDWfaGb8MuW4yAzWY7a0jQuSmWTTQba46y632xWfAJuXEaH_aCDBnZamrn8SMuTtTkQ7MCHpwhkdJ3zhs=w1950-h1300-no?authuser=0',
           'https://lh3.googleusercontent.com/pw/AM-JKLVom-SxRpQStxKffaCQeBNNIY5BbjWS-sXNJRmsdeQzl-FTjfabUSvF5SpwNgbA6ftko5Th1C_ku1r6nVfWeygUOBVREK0A-DRoW6YuTKfopXU1MC5wydg1R75QzGtg_UZWdY7zbA3QgWFxocfwqNHm=w868-h1300-no?authuser=0',
           'https://lh3.googleusercontent.com/pw/AM-JKLU2wCeA_HiAGTKziL_B6SHPKFGKNqVc6O6TJMKWt_0dcdYQNd-2R-F9iD7PJZ1Z2QwkG4QRdRl1uCWwVmlswxThyZqVpl7OCSkDNgi2fq5FeWykN5Id1M4RNAr98FEsrhJ8Cri0ddt2JpLWucp6xDZK=w1950-h1300-no?authuser=0',
           'https://lh3.googleusercontent.com/pw/AM-JKLVg3fIjX4XRB1n_BJKMlFuCnqUrh1-E2hrVgoVmfTwhSdrix0s74idDaWXE4MwSozQDQN7mFrvNyAwNlJTFL-qrF4_VnhNoSY_-jRSEOQ8BqllcSGrzWM4rY2wAWAddbhWqKPK3Clzw4-5jgOpPHnx7=w1950-h1300-no?authuser=0',
           'https://lh3.googleusercontent.com/pw/AM-JKLVvzbQlLyMQSqmW1JBLpHYEM1tnjqjkApOdz9IjDWkRYAv7HkG7o4h7f7MCkFRKsqo988C75tyMV617DJwaKko8Lt4yr0ATac7sihl7B9MB_XPkK988JIqaiV0f6DAFJrCUJ9s1IY1nkzO96i83SVrV=w1950-h1300-no?authuser=0',
           'https://lh3.googleusercontent.com/pw/AM-JKLV69msf9-MKqYuXNodwRaPe5S-lEmMrPxzNijgLsN8W0SiHnjOLKBWRUJGOLNsODlO2SKBMwQ9cn0nbw1bt45Na6lpHphcqe0vS70veIpc4b95DOvwWmQtW0jc8_2SwiW8tinD2KufnYhbM1mx_HwGI=w1950-h1300-no?authuser=0',
        #    'https://lh3.googleusercontent.com/pw/AM-JKLXgsgqXPlr6N7sJJNMNZiAUwOAY8L1xrZms5QKqh8_yU6MtlbI1ezJ42mH_H_oT0CbEusIjNc6OcGu21Il4MKiZ0Bql5PH2yz8w1XapIESRWz937xYbgAqWetMS99JF1kSWnU0_YQeKdKoJSbWryySG=w1950-h1300-no?authuser=0',
           'https://lh3.googleusercontent.com/pw/AM-JKLWI6k7Hz2hbnwVuV3EkBqyfvKP5AWq9BRtnwGvowosnM6jtIPgGxgeaBmwWk7KV3nJc0f80Vw0_-tXMKZZRaqV0inAToaOsMsybYwx2FFlgAmelCx4zNCjb4qwpMBBfj6CfSp4TOnHuON9ma-bkdWMu=w868-h1300-no?authuser=0',
           'https://lh3.googleusercontent.com/pw/AM-JKLVlZvYb6BfLl5dKyYoiwitNQT1vXC8JzjpQckzSXQs6AQ3Bp2jcw9nn91E8wG7TaZHzLJhK5SM3c9QqvSozeocU9lwwc6VGVQoYBNe8RL3_09vqJIeiQWpOR_yXL7IaHXieZy9gVZqQiRltg5nbkzHx=w1950-h1300-no?authuser=0']

film = ['https://lh3.googleusercontent.com/pw/AM-JKLVTn6tQS6jCtwU2r7MaPnWgdIB0cxx6bFwbZT19b4ZTtcnpAFzMYK1Ytbwus2FAapHJnhy7qs4r5emhaasJMKeFFFRFS4RV1VdjRoSI4faty0kUSdAOg9EyHiVVLw4xEgjmY6p7WP6b52t2wVfCSKNu=w1936-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLWyiilp2LOjSVmhZOlbqkIrRVgYXYeneXew0cWVqpbkq_vIKpL7MiLBMHUUdnCOdAao8A-lIdIMUxJ00vzXXGz51nTeolFaEAeL8_8rjXi98nXo-1pUGXkS--BTFWqtG0DCS0RJhI3l69q_-Vf-5sKz=w1980-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLW4uDETzSHssZsvY50kRI2a7KZDnKhum3a-waDy-46FpoOWrQ8dCeZUuK9kcwONIQeATZghX89FM5zlb0rzC-BUrC0J8WZrbLqj6IrLy1kK7QbOAVizE3fPCPtf0kn3cGCKLSMLQW6R7H_yehEGadtg=w1958-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLW1R822RgoRc-VppW2Ty1EKfOSrkphXeeBiJfRXOMfI-TdA0gvqFZEWYV70vxV_uB7RnSsSpXxjNcrTZsHrfKzOHU4ak7sWDPLXE4Q6rvW0qmJLGVZ2JgsJgNFnJ755fXFWjRba8_s6mrPdShZThrF_=w1932-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLW-t--y52S5Z7BcBpF-FOkMcUps4QnpZDIWRbthml8mG0V6L_gMnGB-v1Js3Vgq4RkXS5v_BpikxOhGI0MFOEgH23hlrqPjUPOxND9Jn3Ykt-tloDM1wo-FYzEuuUxTzTiH1tpkV17o6stBGfUVVlq2=w2030-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLXZiD1l6hMaFD1U-vWGzw_eqBWDcCglx9jNiBef0Bfx92026AmJN8nhcSS-qJ6WwkpCKV0Ql7SwgK1ZSnbBjqN--gpceHU43IFMu-g8P2AUyotcnUdSncwYYk9f41-dwGWppZbkijutrlkFE8CqdKHL=w1996-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLXobuP21BBdFZS2KAUFku0moE3EueVMAdvdb8ZdRe1sJTOwyeMBU4l68Np_UXKi77psvqgEVD30Ggjt1iMrpGgzrHXFceJElWhuNdSCG5I-kXyXWlHIDtzXO-ORWxK7RPbhe86hS3RYjzKnMsVQeYLn=w1996-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLV4qNhHS1mRtFtc18JPP0CSbFwEci53tC-TR3KtbjSe1_CewmEFI5hGKnk32KCl60SdZ89XDsW3unhvAZYwfIcpQeVgFraBdSRaHLEYcTex4OEZFqmvIhb4Zpc4S_yxjVfM4CQ4G2ksgETtKAVn2HyD=w2014-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLXzYuKvwXXi3BeCfyjnJ-9SUlVDKQluS9C3pWVcuSHH64FDu0406wBdS5ZZRzBr5N4jIlbAwtzYc55O6Nle5JFlFGl9Ai7_i4ITAiI54f6YRMW7Pbk-j0JCEOiUCx_MN0ttru3MWe39dF06tGKpP4TJ=w2012-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLU0qZnfAqfz0l3waYMDD7cmrJKKgycAW2VnvevxCr86A-X1ormLxr_Rs6GMoAj1KSb3oj4ELi2tOpcwi_7X2IStoMVro4dMv9jIm1cE-NVmcXve1on-r-aoHP4SFdU5YOIeyduT3IlQRVbhskgbfBHz=w1984-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLUW99vjSUGfTTRmjB6otOVCwN3WbSHtVbwDkUmB2c2SfteMjkSw2ZstMLam2o4OoFarH46tXsTLFYkzjKL03kXQF9fGXXVhcO-bb6QhXQSD3OStDdPRO-_eQ84Ld0R_5khwm5d1LHyuN9lck20pbWj2=w1998-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLXM54VFiBEpyioZWJF9MKOZJHzqMbVGDCUNXTJd4OnE6vBnbQKz09Fn3ciH1weCU8yGTpjATfm8gm3ErT3JNPpvWF03HdpsWPSBn7eyu6Yy8iciIf6o9CJ-h5iTnc4IrZHN9MZ6A_pXOypWyaJO8pmv=w1964-h1300-no?authuser=0']

fabi = ['https://lh3.googleusercontent.com/pw/AM-JKLWyl2oqVj_KYJaQzBeeelk80SUr3xGEHk27xbeRTZ3nyxSMjbFkikW2fhad4HwzWVq7BOM9lYnAqDdxjvocw3V5Cno-rGeN8Jt4MZorUvYc_gZ6VB9AQC-ta1AEVL2U6AnW8DACCgKWOe8jlz_WNxM_=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLW83aBt3tuxBNjLO1srvJno1TXSuWD7l9HIzWZ3QwHa6zi8Moppi8KjWv1SL2jX5XNUH84Xhdb8gh3vvV0DG-SiwFOCBoWGcFv4PwPkRMdgQi6VbHURIBIBxf2hVAYnaAoDs9IK94dqdyU2d9aJyaXX=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLWC_U7uTa4sGUBpnz2yOrH7QlCklokt4btTucmgahJA-hbM5VvI0kxxAJqpNwBwXln3BY-gQkbVQFg9GmdfNbVZPrt3DjcFG5ZuyISIl2YfWYFjbXtCnWy6I4zkHyz82O-ycbPZLqwukN7llbcgkCd5=w1952-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLVu0MGBaGwigo5T6hxN8Sg-JzVylVKKFXxdIlhrk-yLP0FpRaUHeOoUpAEYnAEL9KKZ_PA3i95In-bTNhrGvX0s_O4xqLYpuHnkqkM_5SbSFZR52ZtbA2NWr8m5lyVKng2n0ZqI-ypu66tZS32ft4fA=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLWZLWQW7nEem1Z2jBGdTlvJ-kLah1aOIf_dObtxN20C2u0j_Y6bVSjoO7RRVyB_-NGIEuVSruzpySYqNz-ZeG5zGVD4km981Wb1zB1uj2vzYMQjhslh_v8eucnz-jBiPY9faffpJkBGCkFRKneiF_HC=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLW6IHVA-PWhtTrV9b6-eoGlh-NdGJRTuyClpu0j8ydjOWTDt7dQk4cfkEB101xv8q-st5qZLcgckF_lgqfHvkebUYQgyNehft4cRLq3e6WHirKKFTfRfr-pfB5GWsc2_Yt9ML1p8gTKQp8-zARtz0g3=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLVfJLVsVOcVzTCu51meKGlgNRLgxIzKu-dhoL2nfVUJib_w9QUKnxNO18UklKC9IbvL4cHZN3vordWAGtKlLdj9xmnmez83NllzsbLgTus82GuwWL-DeTilAHPQSYhz9ts-DtIRaUhHkPer8_dFK7Ta=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLV8N2H8Kg_1O-0RtirObDEUBBZoX8i9vywQ5akyNmCNbbA1IGUTeJz_N4wHmYocNnt-ZlXRmfkbYp9Cgupzq1GUxFhw6CTtC_POrnwUOM1_vNmopvH_GC6gCM3LEvcz7JsAqPinEH8j7qNALvXL-JlD=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLUOfKPIer2arbzE6mAbxBzx3S84hcUdBq-bxr3c-C2Z32f-C2c2SeGs4KLiAiMFRIjYY4Ou791n25oGv21UL2VCICWsv_aXHP0xXdztDNo3FKnaNXEA-qPN0xPql-yD1f5vt_PamcPTNQuEeiEsdqqz=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLUuNKvOM1kq5KdtceNmxswc1Qy7aBO9HHcRBlHNeSmWQhi1R21Fr_hK4X0ZdI748JOO-w3hc1nO0P1XTg_YCp1Uoz1yIEqMPzSsN26-Qx5Dtx-4D0iGWp1DtmGQdHdu9Lj8WoRVCOda6A5OPSwG-bIW=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLVnpFWaf89p9g5aju-XJh4nN9C35E8WLJGR_2lA40ybAaUSWR2UgO1zg-Xl7ljgv9X1Gae7gDzI3mXg-PGYGT8gEhzPudiWU2QtiJ00nukPR8jmTstKhxFF97VDjA1ucdHr7fpnNyPuDanJiZecG7yI=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLVpWGys9Hl7I6iZ2Xq1frtVBsxMDx73iOm5WUvx-2rJkC05KVogx29nihfCQ3LrpinF1Rr9CsWhomYlAF0f5zDg2i2G4ae6uQ3wPW6cKDn6PznGTGQZF35XtYtzjLBTqHz0SC0U4TCiLyDeZOwvjP_t=w1950-h1300-no?authuser=0']

pets_yoga = ['https://lh3.googleusercontent.com/pw/AM-JKLWBjbC5MdGI5wWqoEqP5jsNImNz_b2jr8cHGKJOKyCtj1NLdFua9eJt0gCNQ6yXeVHeLZffibDmKR6g9JTa1OeOMmq6Wi3K0wtcitIxhEmJYsnng7xzccK04uGUF7MsXmr8R2h7eY7fw2QaMxrVdV1Z=w868-h1300-no?authuser=0',
        
        'https://lh3.googleusercontent.com/pw/AM-JKLUkjRU-Y_cxv0_50J6keAV7WcjRXDlWad9r2ClC__dex4HFwm3BEBwU1gqtwvY48zM9DIjyrVFkQ9w6aI2zxpUNFgBQAw5PAVyS-QOHBF7L_NZIvT86v4V_wKYIQ3rcr-WWTy4c0kEruvXDp27DfUgU=w868-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLUwNJa2pVnTja8FYEMWXkbGt2Kdb87VBwhm3aVooEAABbHSG51JrybJYg5q5iwDt72bScZlXmh3iv2lcdunG-y4OTqm3MelqTB1ZOG4UDV0Bcd6YxYaQ3CZ_kE2qYZMcdlr2c0uBZfHR2uUod7w6JjZ=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLXeQzphaZmCfh-8hOy-TCp7xcJ_wmPAJUg2kkP_qtG2DQIaZRtJjIB6wGGdGMEMf_tIO1utLnV3LdCoakgrwnSKuIGSSylp6Dd8fRO3bAVkog1qOIsRax9qCr_UufCw1xPKYKM1xYQ4NyrCNT4kssHS=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLUUxuT71qKGp0i3SVT5UyZbkq0M0r4WhP8kENWoTAQAyj_-IpFmffkWgyazKXryJORYOCYd9tj6U1d71ftGWaX2Uh07clTAiDxSx9mn21jL377OYH2Ik2NHMqh7IzCLnVI4X-fvdccFz9edyQDUxoBm=w868-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLXSFJXXrricFbwrYjwZ8hkkgP0cSw_ZxKAAlDE7Tst5DJ_i76qoeC2AgVdCrJZTu5eqtDAFHS7o0faXO4RFOj3p9K2M4fBKnieypCYsYmcs6hvvvC8HBhSLahh0i3nsAMfzv9Jf4-q6oI74JGOoxKVw=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLXX6xKDqwPYyCljforA8x6X9LdCcEIbcwvWguKK53unz2H7ejyr2BGa1jwqpssG3VILtS-isrpgNbUx--uVdnhqwYhjIbVaJ3eQ3pGXCXbpjf-sSfeujnGQCOPYOYs2LEwDjfaQJyu0pS_LMRNUla0G=w868-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLUDwYbfteQ2AmKxGiDz8p39loC5XWYgZ88XNidBBqElng13D9-rIGsUiaJPEXAJhd9xLtJLuhmA5emOCnhNP7xL1kryMAZ9nRLlkHoup1CigImzo7Xt3WyqnXTIMIEOa-eDACiKVqtOS2jF0e4ITzM6=w1950-h1300-no?authuser=0']

julia = ['https://lh3.googleusercontent.com/pw/AM-JKLW8oc9xwbu9EgYCkb4bieEcvRc2H100qq9pj3-iBkdkMcKZm0U-fu9Sre1SC6TEOS7rbnqvLIhQGFv2pcF_u393nxEOde9lj8Z1O9pVBY6aMQK97zksy4czudllVEtPdkqQAIcI3dHkaRBCZMK1JiIt=w1950-h1300-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLVa1p7613fKNiYRM0ZAADzFtkLDukVqzt4kAOcSMCHpYVVBqm5oRar93b_bAXBOCtCuCAN3mdfyF7DLV67BJSKve6OMNsoEXgEzwAEsI3tN4UcTH85pv0k_7yFmDE9790MdHzj4QthmcqHko4gBCYxC=w868-h1300-no?authuser=0',
         
         'https://lh3.googleusercontent.com/pw/AM-JKLVtkKhhovczTBN6lnl9ule3AbA2e68pl-O8HwczCI8_GazFknQv-unVaA5jgieqsCPdWAx9Nxv7ZZ0IwNujXRbzwVSu3lsJxGyt3F93Ad8nnMbtliCmU2AJkHbD5REZbSoVTMOvZ_pClczu6SHRFL2K=w1950-h1300-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLXbnfgK6gftAhFKPJLorF_X3NuWLO1SPzDK7xo4vkR2Pj2KD0aZoOB6fweTqmnmG-bWvgwENmj23ISryOmbasV6ymwdyfJTX3MmaEePVLQDLdpJ1nOoiSHJyoAH_v9nJbniOX0XgpF4dXn5F1ErYZ9K=w1950-h1300-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLUcihiqbYlySO8kyKpM-hlOGxmqRY1bFvOp_H0GwglZgqTMJ8czjv3vvjLeYU3Z8Lb53lw58NXlzUusyF4P_HSTRqh-GnRYCDhE_JZixWE8urL6oOmkSiwA-QoxKDKj9MQwCAlB9hPGO_f06cMENCcr=w1950-h1300-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLWRZIcMqAKQaO2Ars6xwcXO4L2i6C5aoeLdbNiDcde3eq3tDsVor00wl506mbc2ApRNdvsiaFgRLLx-HXIx8GB4poBrX0tqDBcte5uSdnkgg6Kl0Q3hiy1cjLC7qzj-sPkjGeSvkFJlR1GJXymrM0zA=w1950-h1300-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLUp6AtcHd7O8eWsFb3NcpLBdBXTaLkcj1wgJj-NG243Z-16vLZSYEsMDjzsM8Vtq9tvz2--R2oyitiQb6OFOpvoUCnOaB3YWpl2ImtKWA_73iGWaVCrk6CqRql9QNvEpWohR72iSPusBuTIXiQm8fjW=w868-h1300-no?authuser=0',
         'https://lh3.googleusercontent.com/pw/AM-JKLVkcCH9mB-s6HrdkHb257on9ynXyJggBSR7h0KJd9JCrmPlc-q4o0iOXPG69H0YheN8p4jQ-rJpSrS0d_nX8KTjBR4HgqFmjS81jW1vTQZgxkthGSfogtZPEBZRHvaELPH_SeeIvCnIdW-TtbaEMJE1=w1950-h1300-no?authuser=0']

joy = ['https://lh3.googleusercontent.com/pw/AM-JKLXY4kec1kxSppMIUlpNz6tu93yViXjaxdZB3Y4G7xMzWC1KUT2tRc0QiMbgD_1JsfZvfnbTP4ZZtJfxzvR91JGoee-hTxbOOkoweUFNjVInp3WFkO8NYJvvlcOdZ9vbdCra_UnjpznGpkq9HrHY2YvB=w1950-h1300-no?authuser=0',
       'https://lh3.googleusercontent.com/pw/AM-JKLWsxyzWQaTWPNZ4W_UYQ8GcMaXyjL3l7LCsl4nBPPw6ioOz00kempv34JBJ8n0z5DBz6f6Nz3S7qx2SXqbkGV9JQlQKdPNEW-rW_7l6cHTrGZ3co9oWErk7SjsqyHuuy-xg2XDy6TP4QaUEKJfedNkt=w1950-h1300-no?authuser=0',
       'https://lh3.googleusercontent.com/pw/AM-JKLWXku16dYdnsYgzoCz_pTsrNzHCzEzpJxJtHTT0L8ft9lsat8qPid351GB5v79n6XrIMzq_HcVn1NlZ7KnMsljgS8thZabpO5BT85OJheZx8X0OD1HC8LeGPk0x4y0_azSA1scBM9hM8vXiDBwnestA=w1950-h1300-no?authuser=0',
       'https://lh3.googleusercontent.com/pw/AM-JKLW5WaklGmmQnKQFJCAHUSFayfL4EM2M0j3bL6WGexZBQVLanNJkT6euvte2ZbeeC8KBSf2OIzyXpyg5-hZGtCKck36OABtSO33ZPgGHocuy5Hw1guVzwEiLb1mHbZhFMyxm8Zb_9Uu5w5tNDeVY-AB5=w1950-h1300-no?authuser=0',
       'https://lh3.googleusercontent.com/pw/AM-JKLUdilkuK_q9JqlNb_2VyTkjN4yeuzbR1N5ieVbXybXA33ldLq0TMFmHPx9CWjae34eDWaBhagrWeYncJy9f-ZaTu33iqMa7AHDAwj6n0YnVHHOMsdriq0fP0ntYhtzkohDA9kYeNnlrxrAcs_wu-dOe=w1950-h1300-no?authuser=0',
       'https://lh3.googleusercontent.com/pw/AM-JKLX_AstKD_eSCnSPByFjl6nWH9hu4W8lLjPR1DuyuXi2zbA2vlAZASyRpozgMD9yDq88GmOebj4vVm_SICY3UCb2sVq8P1u4vjjapdp8IY9ogPsZe9M2J1NGOR2dJ9QYZKTAhBdNHZjAvftD8ZdyYCy9=w1950-h1300-no?authuser=0',
       'https://lh3.googleusercontent.com/pw/AM-JKLU-Gfhy0yB4m6t1Mx2EEsXGxmLMbSMweKEytDUXiJYBFNBBSE4Yt9oJ2guDEfQIB0V3sS_ijboJ-oDlW9Kmg56MBOmpZMbWf6umHeOBQ7bdHHX12nCj2tX00Zh6ZkNmlg7kfEuGpQD_ACFBg4sv1PIG=w1950-h1300-no?authuser=0',
       'https://lh3.googleusercontent.com/pw/AM-JKLX792gFIAAVBr5zCa07PZb3HfRMhuaWQw9qyajifQzS5l_c7Pa4VLc52Dx3QF7yZgo81IcxzG834b4dDUGYhsOqi1Rb73KYzrS9POGrcOY1YkF-p782F4fRBRL3z3O8BZY_JHUVf6H3osLu6aoFt3RE=w1950-h1300-no?authuser=0',
       'https://lh3.googleusercontent.com/pw/AM-JKLVfnioSEBcZtNezWx9xffO6pVzLy8561UvHOvTK1vn8f6CvJVpFK_6eq1AMqC_hHNmBTUkntplTgHUfxetG3_neRe6IpLd8I4TmQj8OVIlLey__zeE_8RrFW2e4ACIGI17yhVqhZeaDnU3Nz5r1YK2c=w1950-h1300-no?authuser=0',
       'https://lh3.googleusercontent.com/pw/AM-JKLUr3n6R1lqSRMrvFkBLcL2nPtoAA1Ijkq0BK_-emw4YDtg8cJnqzR4_Eg8Vd7Gj54KXMfzHQ8l4_6qqsc4deojWA7GKIRAqASmOiIGMV63woDxg_31P4GhKfdkAr6H0smJwYXFi7cBRNCBB3Y3Fot6-=w1950-h1300-no?authuser=0',
       'https://lh3.googleusercontent.com/pw/AM-JKLVKjhHR-fwQSSFWcFDl5t3xt8zAk0ZCzWyUSbJ0ddTQlIJqqxxdVW2aO6afLN8faCnUjPHUEOqSLXvFsc3dth9G7EKFLeIq-OuAY5yK7YZobiX7Ul7TXgHM-tqJjz5JCm3J09s2huxW3CANMMJkYY15=w1950-h1300-no?authuser=0',
       'https://lh3.googleusercontent.com/pw/AM-JKLWf-lvakpBAe2EiQ4IjrXHDFPEGLxSvb474b7gYMg1t4LSvGMm8XOYojWTmOjYabIAF9CbD0pf0MCB9chYvORbocogFVtL2IPCwuLsGgaL1RL-1eOs9TFxRpcs4je3p4IXOlh_zBf93Y94DGnEaQU9X=w1950-h1300-no?authuser=0']

pets = ['https://lh3.googleusercontent.com/pw/AM-JKLXDhse0e4VNOr3x2NAURByASJcP8vnKL9TU3Mh4AxVAF5OEJf9gpne3XDHTkQ6dMxUAvPfo6ZFhOPi8BT7b6IF3uOsmIxz088uDwipKPjMr19SAbhgFYQpq-DpRyCOIqtLlkO40ysxv9Ierg5YND1uD=w868-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLX_ty13na9W5mU6tfvUQl2w7eMx-OGzyzctKhU3SKu-cbtBgf8IxHEXamICZ8qt6T0hUqNETVCFhaLCQ4trk5PCE2yVqh8tHSGl4WiFV6ORo1Q5H4RI2EgOMQgPcheqo823JsixNBWK14A0p85gupEj=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLUelJ7UEolv4jPYC4cnrzyyIRwEc6alk-d1TBsQIWzNpVk0bLW5gEhD_HRcvPBCGzo2pqrBhwhumqskuHrbVt1INH0QBs3VzROYSCtVwd9AVT5Kshd7bFh-nWnNJCagAFabG-Z74nS7piZafzYHq6cS=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLXKlTFpHpmaOxDs_AiOmAyKMy1g9UUV3MWuXkn1s6--Ey7t7UIScXV6v8xM1J1pZl26ayWPSnd0VdPkYJY_IBYIhblPqWWNX0lXgewSC6kSME1a7Tx3klPUOu_V30fVGa9VW9CVdH_7pLoOKDiXPhOt=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLW61mosmOWJIYwN6-o555GWifYkIIMlN1K58xuCD8KXuFaDX-VhfKLTdzNFy5TWm4mkMMK1RQcIGkWWCSUB8kCLADsyuhoBesBhfuC0mAn1ijG0vLTjrUaov5JbRNAnykeCIkb_DdLHXXRmA6RZt7L0=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLXaw2uxAb00rw1kgjWFnHwhS2B8PtyW-yjeU7o_LFKMlcnbTf7bq8iWi0cqOB_bTRdFoxlfHDSDzL2j85MaIatmY9RNwa8JIw2kCWMkBHCxfBuZKW3H2FcrkLupy4iRDp_3SC9SBEtl3ErI4btwAdQa=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLVk8hC3QTu7mJ-e1KsDVGCnZALoeIbPdoYmDYslGxZ0I-vG-3annuKP_qCF3tVCGr4pE21gGmwft8ACF7cwzIBgyFwTOTiDD1jtWpKvShGRRt8weh1ytsZr2AD2hbZTOSA2KOSsRhDP-NHDNEwrB55X=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLVUDruOTlmGmfPZHGgn39TN4rLknEBYG_UPKWV3xVsaFUwiJbr9AKNSoXPUBwXZ_eg-s2s183rynwxMnOYEVJ7PqDhnto1xYmjsdJXCivmiPBYpK2FhUS6WKAlQ6NJW9l7oB5esE0KFeRFI-3Yi3i5N=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLW_IMHq1dFYL5GcWpKzoWOxtr0hxFhGENge4dShRihJjMo8vaPP5kJPN31qdroWuiVweVoFSUZsxDUvAdi-_N0NQ9kH3nM4xlk6FlgVVLk4EWZlr9FzZSlO3OP7YjHI76UUdsgcz-uHzemiZfF8n4uV=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLUUCARNMN-Xn0nPNWcBxYMF2YpElwHZ0ythz_VUP0xgOk6p6s8ZAVtfLxsp8-ahI7Np2XVtrjag5XpJPiLxheBWr7taDEH48fgVIwsLgedqlZQypWDc9KJhB2JI_qAaz7fmcB7XghYob7NrbWMes79Y=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLXfMwn6b6ReKw4oN5R7crF0jUl4hpM80iRStcKAycQ1Wq39SRlZisUlO2ANGgaqdjg9fSMoxI_sV28RLEuQTzGdJShdcBlcz2Uk7W-jK5EK-wixzhjZfsYFN942z6c64mx7pyN2N3ExKYqyUO4yMfvK=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLXDsoBSOSpMJkpJRNLK0Jxl2HzGbeMGJYo6X_VptSQ0xi8gFw50XmWKER0CG9dBMomK3VmFUBT2uxzDS8uo_3H4d4eegObtov8OwaMd8l6UzRXPtZy58ZNeg5DuL-DndGvi6IJfI_5ohR0FfzIYjOy3=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLU1mqR7aHuslyTUYIUfAAp3OHqqwbXy0Efq8rFIyfnDkfXrU8H7gqYOuaryyRXCEw2o92C3Ns8Ud5BLZWtBsw7UL9y-4q94E_Y6GsMPQO9ewMtNfE837OyVUkV8G26Rkcb2VQ0Tn54Isd8ItsPAeuYa=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLVzJitpNnK-wZ9vNyAdmlZNLu_tb1hah_sm3EdUefciheMA6f6h0a_iOuCeV7dqXdLAhzmVxWwuUkZe618y267_T4t7ZNEW6E3OoYy1WWVwhPpEXMHSrhA77hD6CjJhSTHd_8-dXLSwafY8q71DFciD=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLUt5fi_V6thV5hhJpOF2nIdy5LW4eiGMlSL_-EUlALFfvGalr1LDRr_H3E-iGXCPgEE-RZM6YSG0hxgprp8jnDfco5H-vRqjEF9cREVe67_Hou8INLa3zaYDIsSPToVqJxL2jv7ZuNvWk1PBVZcORPD=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLUmkl8sECwMSIWyWxFuc7Bi1-WoxB7PGEI0sOC9v2pzjVPseGSzVxERujXjkE7yf7aWeFwdSytWfPa92PNegUYMvYD1cgfN6KnGpvyZzGZ2SmB7M1DY5OmWy8rBF4xw8M9fyCf1dOpWQFAWkoh1LBuy=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLUMfLWtQnKeRVKJPmyJSBdexlWt7vHs2pW0wseh4FXyFQlLVEPzK3SOkN8KSWnRp_0eL1mSiv1hLL30u8vVjZhN1WjsXp9eJcjQLEjrihilEtoH6lgnitmZnQ3yLrjRKqrM33Y-tU7_G9Tj3J0mdU5Z=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLWLZ1MnNknqMyddh-sVUek7yeOIDDquC1BWgWRRbsBwnyBaHpg3Dk_L779sP38vxS97dw2EhVyS8vcpWhs2djD7YKPcuAbvMwXpzVcLSIEfL6Y1Gtfvbe0E9ajbAvgHF6ejtZWAkH96N8qKAcf2gXz5=w868-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLX7EnrDBt4h6NjfLOpPUyQV0KB4ql_3f0aee6alVyrlfVdmaGkP4ZoTANsXOL9J0fOOUV48Wz9Qf_NhaNdbgnAMgZUzK72EWx3FTQb3NQwzcG_CiKu6UBL9L7CuUkIXEPgug6hw2vMPpSTZmsYVP6YW=w1950-h1300-no?authuser=0',
        'https://lh3.googleusercontent.com/pw/AM-JKLWTmxs49Dvh39GGQvIF1Yy0yqwPOAHJ4vJdgs1Ld43onYvDC31cHy_pXGJaqVuaeqVds2YlOIXvoJHeS1Ghqfv4IwzvrBN-mwNcuMVipGxM8H_HMsyBFM1k4QLTBi3HbpEyiGkejGrDPUdaD_X2a06a=s1300-no?authuser=0']

nature = ['https://lh3.googleusercontent.com/pw/AM-JKLUmdyOyC8VggTDZ7Fta2IZhZBC9PnuAzUTnHj92MsN_1EDOuExZP5lQm6y61SK8GgLlXOD8sWBgdClqKF05unJ9l6KANMqhAW-Ct4jnFaAg1otBtrATgOnbYxc1lUEL3pdYvs6LkkipwQISAhfnIXuF=w1950-h1300-no?authuser=0',
          'https://lh3.googleusercontent.com/pw/AM-JKLUt7WUal8dfpfkwa7dFtkJBeRxLJaHfXIMYycQU0TBDlFs1KMlWv9CvUKG9G97ZxeMTuzTO9ydQ4Eh4x-uRLBqqvIcqDpvd7CdbZuYfUqaXro2q98tQJ5Y66-QSDjd7R-Rixg7DioMUleSvpIB_Q_2o=w1950-h1300-no?authuser=0',
          'https://lh3.googleusercontent.com/pw/AM-JKLVrZ4lw1J-NO_GFFrLT_Rn5zo0Ug3jGW8VYgxGx4_SFm2Ayu_N-trJQwjfEWcM0Q0uAFXp2KLPC3Y1MP5Rf-Pja1Vby_EkKiYUyrFgPjQ_ixaTvy-fXNbX8imbUtOK6B3m_5ArYWeEPrzie0uGd2yfB=w1950-h1300-no?authuser=0',
          'https://lh3.googleusercontent.com/pw/AM-JKLWSMx5dA_KmtZVOluqY8EVZTiReQzQL-wiCijaAZjGDZqOJM8SdTrn6T39AoZfvPezsl0x14lyy4g6tPvL92RQReg2N1rakp5m_5vZGFE9WBExImWXCBRpGfh4ODYT7QLozwOqyr-rsudC_F1qrlGNE=w1950-h1300-no?authuser=0',
          'https://lh3.googleusercontent.com/pw/AM-JKLVgzrjfO12ztTKdBOmVA19GGkgKy9f5_3XHEEh1dmRbAavSbrIcLp4avXZmWSguVUMpRE9ppmabNZZIAGhfBYf3P2lC6Qv46tpUeoUNvT6rg6u5JF7XB708KegAe9zwxSXWpU6X483tjiXV456_8-Mb=w1950-h1300-no?authuser=0',
          'https://lh3.googleusercontent.com/pw/AM-JKLVOnXMIS6xRi6JGr3T5QA-sLSKkMCLpmojF5C2OXYxnxU6sECdJbo2N5BI2oNs_rU78IghKPcB1JLlF92GubnEI_-qK8an_6f4Ym3ZQQrEJLnwGUwG5JDW735W5Gns1ATi9KceRH-OS73xJ75U8LW2l=w1950-h1300-no?authuser=0',
          'https://lh3.googleusercontent.com/pw/AM-JKLU_Gihdm0x8XBPyi2ITcE_gGQNLJqoE5AY4zJy9NTDE-uPWRbehPzxaEwBYeMyq_2lDrhG64X72CGgIKH2agT8SCI9adFpI9tqGC3FIfwhv5TcRHfhsVNLd1r8uz7opoIWS04nFeyWiXzIqZrAYRnRp=w1950-h1300-no?authuser=0',
          'https://lh3.googleusercontent.com/pw/AM-JKLWi9fyrDWv26Uk0y_klkg1RRBtjApReKMv5XFv8aqRgqd_2J0tRqtq3b1x7qkF36CHw7Wz8wNVB6VmK-4Vf1lM5eBDLm-LIgs-wZbochHBoff3wE_OE4m28FVWsrewQ7BF5ELprFz5iOzzVxvsCCded=w1950-h1300-no?authuser=0',
          'https://lh3.googleusercontent.com/pw/AM-JKLUwrBFMP3V8t5FUdvuUQhl-9_fDcwLQn6eS2IwpPDbHjkqIqbInCCfAcaCC6GTVILyCmXuazV1mOD6sANA37JTkgM-e2RfnYN7SFalAco1LJuOd05RRDnCiFBc73mGvQuFqQ-3uyLFYT0-OalOaUhDk=w1950-h1300-no?authuser=0',
        #   'https://lh3.googleusercontent.com/pw/AM-JKLXBZKvFuVCQxTVg_pRp2gBw1P-bntrsIOmAIkICY-GVMYde5xWTqu8h8MJpW5CKooDoMdNFI0ERqnA2FSop3TV_FEJ1j4dpauo5WoRmGKv50eJlxARSLzqpUrrYFMBrXmavfLDRKLETzr3fJZj6_lEr=w1950-h1300-no?authuser=0',
          'https://lh3.googleusercontent.com/pw/AM-JKLVNUWYgMmrrdmfWmFPQu7erlJ7RfLuBh5sVdWxQPm3FaOSGekonI_zan2eXcQdayaVH_Kg8qpgAz2Sd72iA9xIkw_9TuaSk_bmPEl_UvELEsPhcXW-FZPaT8vuCpwzcAlQBv8SEUZLViF7aYTCNfeLW=w1950-h1300-no?authuser=0']

dartmoor = ['https://lh3.googleusercontent.com/pw/AM-JKLVUfXkAt7hgW01M47LaRGmbnWwz13a91uc2bDafYE4p-YdkxDdT0pqQoEEML7Z-z3ExDqhuKlvPxs_0xMdghPdrRGs2XfylorUKlmYCq0szWGoucXM7XLWQo-8-e4Z_swEw-g8TYhSCuIQUzK_ZZ8PC=w1950-h1300-no?authuser=0',
            'https://lh3.googleusercontent.com/pw/AM-JKLWCoXtRnq_CfF4uWVl6gr3kg9VKFQlF5lybpZR4w9ROhAiFPPqL6MzkXleUEBl1BRT92XZlfrPk0z0J8ZeF02JIeaqJSTTgffMbr9pPM9VC6T3TiS5rOWmEvMOTJtrd1K44xz4G_eBRO5pBkjPMvJgE=w1950-h1300-no?authuser=0',
            'https://lh3.googleusercontent.com/pw/AM-JKLXqTFrczKlk3iWceGwo-4_u9PE2wVsajomcJIzMd4fj6fBC36_eSHsLmYtn9_ZJvBrzh9TFg4GvopjjKFQjfHW-EOwxy_Zw4VClbswDTceMJcxEsrLvWkP8EfC35drso0KuBm1Av8DI_4AyPpl1rO1K=w1950-h1300-no?authuser=0',
            'https://lh3.googleusercontent.com/pw/AM-JKLXojjye5IVlMlG3zuwLCXPJ9HV8FmDQPdKBe40X7KSK8OWd2ZK9wzaFk8TN9ZTQsdoOAn-lupmP5eD6ieFJ3hQTAoF00229B82lM6pgvtAu4w-rK0cbrAsH0mHkZHPkwmw7ZBO8MGgoz5A2vZk1jIFa=w868-h1300-no?authuser=0']

cornwal = ['https://lh3.googleusercontent.com/pw/AM-JKLXWEewp7f6lwZzsMifgwgw5c7ezpEMb8r42KIAPXC-wgVQGLp9gI4_AUjd2F7TErvXsfOquEZoZMY5pjwPmpEfcOET2NtlSwDrfCA90yWQJslo2Vx5kFDLfRNnGwCiXrz-X7vsJ5VrO5V7Ag4Eh8WAg=w1950-h1300-no?authuser=0',
           'https://lh3.googleusercontent.com/pw/AM-JKLVhkeCpn5sUlDUJ76vqGdprhIwJVaCkjT5BI8qUMCHCwHxmwMLGpgDiTPIEQvKgBtKu7mbuFztUfkOd_2n3q7aOMpENLy6omPGPcdK3zrJy7-1u3n2as8dV-PKy7R2E8Kr7EOwpugYnfHMxuPMdvUYw=w1950-h1300-no?authuser=0',
           'https://lh3.googleusercontent.com/pw/AM-JKLUVtZwDpGuNlfrmgY76_KjT6pdrI6MmiokUNuiHUtl-FV4LZ-k_IaUlQc1TrfFP3EwtHZ5zzGV2KI-Iq1ftZIdGaj-LlRHMo0Zt_K6OwRZ8Ep5AojA2AmAfdbD-iI86G-Bey5-dQUBiSadYEu4XxMfp=w1950-h1300-no?authuser=0',
           'https://lh3.googleusercontent.com/pw/AM-JKLUqRx_T_TYLYihYERkJNapUQQVtrPBPFApYAB5mH-KfAFjKpIXkEyFvLgbOyI3Qx2D42nvnFN1mzFIqSVS1tAu_llvS3Y0NtP3Ja4k0qjtiaJS5-OuogKpg_MX0JzI20ZksV7l_p7pHR1jVVMh6sNl9=w1950-h1300-no?authuser=0',
           'https://lh3.googleusercontent.com/pw/AM-JKLUyNW69KGiLtFpsX1o-uqiuB-DVkHtPoIDMpCQ27Gr3nYO-MsH2eTa95dOLX9tLrb_G8lfJqwtPw952nUbA2Q7M2-i_-54dn4jCXgXGw0zS7Icn58ZLZADVpnL5f6ciwMqLisfzKIGvKX0B3CpaTGdl=w1950-h1300-no?authuser=0']

portfolio = [('portraits', 'https://lh3.googleusercontent.com/pw/AM-JKLWHkgQMLCGC6GW2km9vWIPf7L-GJ8uqtKrP4uzDQIq6HD4AxicWsm0WvVyMRq5z8Xmh3g1PUhCgh0_YsdhQP8poZJOoDaa6yUZMd3heh7O3k92wxQq2imWna0MNP6qxTD9dwS3ejCzCxrLj8OjXSOxW=w1950-h1300-no?authuser=0'),
           ('nature', 'https://lh3.googleusercontent.com/pw/AM-JKLXQzGWjExkBU4G9_0oJXAdyJ4JjVf1THVPIn7D-Fw1i-0UFvEUs3EMrTAfu0h-UWESCdZOkMFcaPnUIEiXXA4WJ4BkVYELlaEzMFYo3MedEDMOdc4TgCCK18dfagrDhqK5dASZHfhDWJM15h69bmUTn=w1950-h1300-no?authuser=0'),
           ('film', 'https://lh3.googleusercontent.com/pw/AM-JKLUHyv7459xI_TYRZt95QoHIwyc3nWfaHGxjJDI5sgmnGqRcS7cST4zcpjd38YPsDmtLuGjO06E0dmrkdt2-XfnbcD6HYlrKe13wegLlQ7nGCKEdwf0vvnDTbBczl-6Uq2lKQaS2KqTkDnTJ3foO6QGZ=w1964-h1300-no?authuser=0')]

commissions = [('skateboarding', 'https://lh3.googleusercontent.com/pw/AM-JKLW5csjbCv8gBGL8NZXpVP_JhmSA2OPPZbG99VNnAcXiHBnJf18iP-a9K1VXa6Icn2kTXKKeBvHrXWnEVgGpiRkHzG8p8L0CXJfbzhyHhePkiN7dffiTy-w4ekOsltITtiPLOj3DMp059iQrk5FV7Ulw=w1950-h1300-no?authuser=0'),
              ('fashion', 'https://lh3.googleusercontent.com/pw/AM-JKLUvQcOhnh-6T3bn2M4OfSmZ5apMMNQ-NCMb5I9Sy5vwPbwJIHrvsr8gfWcRw8TtMAwVEvUX4HOZ07k8gT27XPXYKEuK92symEaRPULUOHIQpbtZ-XDugYZvb9qosveDbI0WV6WegkqvGj0nTlvq3ev3=w1950-h1300-no?authuser=0'),
              ('pets', 'https://lh3.googleusercontent.com/pw/AM-JKLXApCIuOsry8EO1otqgHWhiMFivzk6FDKnZ4F5T_47VSPvBL2uiPnud-u_Mkl8XywxfDYTDZH6Lb2v_Lhin8AOF2qA8o3WV-ibKIl-Dbq2lpqktrUCDqanwhGgDjdOS3ojCTdzNOTqEKVMmbZRvbZxV=w1950-h1300-no?authuser=0'),
              ('chandos deli', 'https://lh3.googleusercontent.com/pw/AM-JKLUManjFqTmVAtNjqJzdDerfGEOLzz6PKkZh9aNxTdUH-vhGakSb6i8iwyZ0eeDIkGMhdEQg1BJ7Utrz4ssPyskdo89ULSTVY-iSSUpM1yQPOaG1CSZ_Bc9AzLOQVqQfMfvwsgkgNjL9Fv8cQW5xolZ3=w1950-h1300-no?authuser=0'),
              ('joy', 'https://lh3.googleusercontent.com/pw/AM-JKLXUw5e4PYBzr93wSQooCBGUsBpBByvRW-UyPpMmImttYTBFFvzqtthSgE7kuTWHuYE6Aw9rC-PJwq4Dh8PzTQWbkgoIDGVQk_IylO000KRyS3JNFhcwp3VJt-w-POmva22QzXzyR_1GzCBNcJ5ukc3a=w1950-h1300-no?authuser=0'),
              ('julia', 'https://lh3.googleusercontent.com/pw/AM-JKLXbHNRa4ox5UqWtaXLsxS5jpjqg9KiIXFaP6KqpDt3-KFQ65OzLKLpO7J8iON_N91GLsBlNza-HOI4c1osdEM__hoXW-q1ZDHT8UNXiYBCC2kWrKJN0jEJ5rPxdmRN48s8RMOdYErpg-Sg77oOBpmnq=w1950-h1300-no?authuser=0'),
              ('pets yoga', 'https://lh3.googleusercontent.com/pw/AM-JKLUe6a1R9YF7Pf611QO99UJz08O4ZGEcJtWXMNEr__gX9fKPDdG4kNpIRXcvCXeO6pqetrFH9hUBk4n2je9IgOgpaVid-wpjhLMJD_i9FvxKx9GkzVYA6Cx34_rHRE5cxpw9kH4IwHlQrQuXaiD1HaHB=w1950-h1300-no?authuser=0'),
              ('baked by fabi', 'https://lh3.googleusercontent.com/pw/AM-JKLX_3jzyJdHTnVX7-SM5NfX8TCiDpkNmGLGz78OCKG1bM4OtOqnpeKIIC0Vt1DbRNSsJl_ugXa1Rx3wbH8NUtieioSxRa1IHyiemA84h1BEVCULRfIXdYGTodjJt3h0Iub5ECjVYDE8ww9Ip2QC46Jfe=w1950-h1300-no?authuser=0')]

pages = {'fashion': fashion, 
         'skateboarding': skateboarding, 
         'chandos deli': chandos,
         'film': film,
         'baked by fabi': fabi,
         'pets yoga': pets_yoga,
         'pets': pets,
         'julia': julia,
         'joy': joy,
         'nature': nature,
         'portraits': portraits}

menus = {'portfolio': portfolio, 'commissions': commissions}