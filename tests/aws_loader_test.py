from hepbackends import AWSBackend

aws_storage = AWSBackend(endpoint_url='https://storage.yandexcloud.net' ,
               bucket='cern-net')

aws_storage.copy_from_backend("file.txt", "file.txt")