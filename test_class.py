class TestBase:

    def setup_class(self):
        print("\nCreating base setup.")

    def teardown_class(self):
        print("\nDeleting the setup.")

    def test_login(self):
        print("Login page...")

    def test_add_device(self):
        print("Adding new device")