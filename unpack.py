import gzip
import tarfile
import zipfile
import os
import sys
import progressbar

target = "packages"

def un_gz(filename):
    """unzip the gzip file"""

    name = filename.replace(".gz", "")

    # create the gzip object
    try:
        gzipFile = gzip.GzipFile(filename)
        with open(name, "w+") as f:
            f.write(gzipFile.read())
        #os.remove(filename)
        gzipFile.close()
        return 1

    except:
        return 0




def un_tar(filename):
    """untar the tar file"""
    try:
        # dirname = filename.replace(".tar", "")
        tar = tarfile.open(filename)
        names = tar.getnames()
        # there are many fiels in tar file, mkdir the same name dir first
        if os.path.isdir(target):
            pass
        else:
            os.mkdir(target)
        for name in names:
            tar.extract(name, target)
        tar.close()
        return 1

    except:
        return 0




def un_tgz(filename):
    """unpack the tgz file"""

    if(un_gz(filename)):
        name = filename.replace(".gz", "")
        un_tar(name)
        os.remove(name)




def un_zip(filename):

    """unpack the zip file"""
    # name = filename.replace(".zip", "")

    try:
        zip_file = zipfile.ZipFile(filename)
        if os.path.isdir(target):
            pass

        else:
            os.mkdir(target)

        for file in zip_file.namelist():
            zip_file.extract(file, target)

        zip_file.close()
        return 1

    except:
        return 0



def un_pack(dir):
    """unpack all file"""

    num = len(os.listdir(dir))

    count = 1

    for name in os.listdir(dir):

        progressbar.bar(count, num)
        file = os.path.join(dir, name)
        split = os.path.splitext

        name_end = split(file)

        # check the .tar.gz file
        if (name_end[-1] == ".gz" and split(name_end[0])[-1] == '.tar') or name_end[-1] == ".tgz":
            un_tgz(file)

        # check the .tar file
        elif name_end[-1] == '.tar':
            un_tar(file)

        elif name_end[-1] == '.zip':
            un_zip(file)

        count += 1


