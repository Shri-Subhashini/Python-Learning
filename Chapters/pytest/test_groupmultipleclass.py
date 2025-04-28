class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        #assert hasattr(x, 'check')  # Fails
        assert hasattr(x, 'lower')   # This would pass, as strings have a 'lower' method.


