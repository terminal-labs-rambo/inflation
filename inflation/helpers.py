
def _get_github_repo(url, target, filename, extract):
    zipname = filename.replace(".zip", "-master")
    url = url + "/archive/master.zip"
    if not exists(target):
        with urllib.request.urlopen(url) as response, open(filename, "wb") as out_file:
            shutil.copyfileobj(response, out_file)
        zipfile = filename
        with ZipFile(zipfile) as zf:
            zf.extractall(path=extract)
