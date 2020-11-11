# Copyright (c) 2020 Ethan Nguyen. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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

# Remove for testing (to use an SQLite3 DB in testing).
# Fill in for production usage.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]  # Allowed hosts, see Django docs
DEBUG = False  # Set to False in production
