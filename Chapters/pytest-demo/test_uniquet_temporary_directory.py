
def test_needsfiles(tmp_path):
    # print(temp_path)
    # assert 0

    temp_file = tmp_path/"sample.txt"
    temp_file.write_text("Hello, pytest!")
    print(f"Temporary file is located at: {temp_file}")
    assert temp_file.read_text() == "Hello, pytest!"





'''
tmp_path is a built-in fixture provided by pytest.
When tmp_path is included as an argument in your test function, pytest automatically supplies it before running the test.
This fixture creates a unique temporary directory for each test run and passes the path to this directory as a pathlib.Path object to the test function.
The temporary directory will be automatically cleaned up after the test completes, so you don't have to worry about manually cleaning up temporary files or directories.

'''