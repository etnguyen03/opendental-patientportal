COMPANY_NAME = ""  # Company name used for notices and welcome
MAIN_PAGE_DOMAIN = ""  # Domain of public main page
SECRET_KEY = ""  # Django secret key
DOMAIN = ""  # Domain of patient portal page

OPENDENTAL_MYSQL_SERVER = ""  # Opendental MySQL Server host
OPENDENTAL_MYSQL_USER = (
    ""  # Opendental MySQL Server username (Opendental default is 'root')
)
OPENDENTAL_MYSQL_PASSWORD = ""  # Opendental MySQL Server password
OPENDENTAL_MYSQL_DATABASE = (
    ""  # Opendental MySQL Server DB name (Opendental default is "opendental")
)

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]  # Allowed hosts, see Django docs
DEBUG = False  # Set to False in production
