from pathlib import Path

import pytest

from vcs.errors import VCSError
from vcs.repository import Repository


def test_init_creates_repository_structure(tmp_path: Path) -> None:
    repository = Repository.init(tmp_path)

    assert repository.meta_dir.is_dir()
    assert repository.objects_dir.is_dir()
    assert repository.heads_dir.is_dir()
    assert repository.head_file.is_file()
    assert (repository.heads_dir / "main").is_file()