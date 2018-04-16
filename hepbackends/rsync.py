import os
from sh import rsync, ssh
from .base import BackendBase


class RsyncBackend(BackendBase):
    def copy_from_backend(self, src_path, dst_path):
        rsync("-razvP", src_path, dst_path)

    def copy_to_backend(self, src_path, dst_path):
        rsync("-razvP", src_path, dst_path)

    def list_uploaded(self, path):
        host, path_on_host = path.split(":")
        files = ssh(host, "ls -1", path_on_host).split("\n")
        files = list(filter(None, files))
        return [os.path.join(path, f) for f in files]
