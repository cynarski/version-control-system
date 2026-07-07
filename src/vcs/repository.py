import json
import os


class Repository:
    
    DEFAULT_BRANCH = "master"

    
    def __init__(self, path: str = ".") -> None:
        self.path = os.path.abspath(path or ".")
        self.repo_path = os.path.join(self.path, ".vcs")

        self.index_file = os.path.join(self.repo_path, "index")
        self.objects_path = os.path.join(self.repo_path, "objects")
        self.branches_path = os.path.join(self.repo_path, "branches")
        self.head_file = os.path.join(self.repo_path, "HEAD")
        self.ignore_file = os.path.join(self.path, ".vcsignore")

    def init(self) -> None:
        if os.path.exists(self.repo_path):
            raise RuntimeError("Repository already exists")

        os.makedirs(self.objects_path, exist_ok=True)
        os.makedirs(self.branches_path, exist_ok=True)

        with open(self.head_file, "w", encoding="utf-8") as file:
            file.write(self.DEFAULT_BRANCH)

        with open(self.index_file, "w", encoding="utf-8") as file:
            json.dump({}, file)