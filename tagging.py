import os
import subprocess  # nosec
import sys
import urllib.parse
from pathlib import Path

import git
import requests
from dotenv import load_dotenv

import mermaid

ROOT = Path(__file__).parent
load_dotenv()
GITEA_API_TOKEN = os.environ["GITEA_API_TOKEN"]


def create_release(version: str, body: str) -> None:
    print("Creating Release")
    file_name = f"mermaid-{mermaid.__version__}-py3-none-any.whl"
    query_args = urllib.parse.urlencode({"token": GITEA_API_TOKEN})
    resp = requests.post(
        f"http://gitea.matthew-hamilton.com/api/v1/repos/gitea/mermaid/releases?{query_args}",
        json={"tag_name": version, "name": version, "body": body},
        timeout=15,
    )
    release_id = resp.json()["id"]
    assert resp.ok

    query_args = urllib.parse.urlencode({"name": file_name, "token": GITEA_API_TOKEN})
    resp = requests.post(
        f"http://gitea.matthew-hamilton.com/api/v1/repos/gitea/mermaid/releases/{release_id}/assets?{query_args}",
        files={"attachment": (ROOT / "dist" / file_name).read_bytes()},
        timeout=60,
    )
    assert resp.ok


current_version = "v" + mermaid.__version__
repo = git.Repo(".")
if current_version not in repo.tags:
    tag = repo.create_tag(current_version)
    repo.remote().push(tag.name)

    subprocess.Popen(["python", "-m", "build", "--wheel"], stdout=sys.stdout, stderr=sys.stderr).communicate()  # nosec
    create_release(current_version, str(repo.head.commit.message))
