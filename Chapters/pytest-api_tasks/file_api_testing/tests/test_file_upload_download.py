import requests
import pytest
import os
from time import sleep

# UPLOAD_URL = "https://file.io/"
UPLOAD_URL = "https://gofile.io"

# Upload small file test
def test_upload_files(sample_file):
    with open(sample_file, "rb") as f:
        files = {"file": f}
        response = requests.post(UPLOAD_URL, files = files)
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "link" in data
    print(f"File uploaded successfully: {data['link']}")

"""
JSON Response Example:

{
  "success": true,
  "link": "https://file.io/abc123",
  "expiry": "14 days"
}

"""

def test_download_file(sample_file):
    # Uploading file
    with open(sample_file, "rb") as f:  # binary read mode; File upload APIs expect binary data, not plain text, because files can contain images, PDFs, etc.
        files = {"file": f}
        response = requests.post(UPLOAD_URL, files = files)
    link = response.json()["link"]

    # Downloading file
    r = requests.get(link)  # opening the shared file link in your browser
    assert r.status_code == 200
    assert r.content == open(sample_file, "rb").read()


# Upload multiple files test
def test_upload_multiple_files(sample_file, large_file):
    upload_links = []
    for fpath in [sample_file, large_file]:
        with open(fpath , "rb") as f:
            files = {"file": f}
            response = requests.post(UPLOAD_URL, files = files)
            data = response.json()
            assert data.get("success") is True
            upload_links.append(data.get("link"))
    assert len(upload_links) == 2
    print(f"Files uploaded successfully: {upload_links}")


# Upload withot file 
# 400 Bad Request; 422 Unprocessable Entity (Content doesn't match)

def test_upload_no_file():
    response = requests.post(UPLOAD_URL, files = {})
    assert response.status_code in [400, 422]



# Validate multipart content type

def test_multipart_headers(sample_file):
    with open(sample_file, "rb") as f:
        files = {"file": f}
        response = requests.post(UPLOAD_URL, files = files)
    assert "multipart/form-data" in response.requests.headers["Content-Type"]


# Invalid download link
# 410 Gone (Existed bt its deleted or expired)

def test_invalid_download_link():
    link = requests.get("https://file.io/invalid-link")
    assert link.status_code in [404, 410]


# Remove temp files

def test_cleanup_temp_files(sample_file, large_file):
    for fpath in [sample_file, large_file]:
        assert os.path.exist(fpath) # checks whether the file actually exists on disk at that path.


# Retry download mechanism
def test_retry_download(sample_file):
    with open(sample_file, "rb") as f:
        files = {"file": f}
        response = requests.post(UPLOAD_URL, files = files)
    link = response.json()["link"]

    attempts = 0
    while attempts < 3:
        r = requests.get(link)
        if r.status_code == 200:
            break
        attempts += 1
        sleep(2)
    assert r.status_code == 200
    
