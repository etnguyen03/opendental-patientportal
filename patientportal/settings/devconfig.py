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

COMPANY_NAME = "Fictional Dental Company"
MAIN_PAGE_DOMAIN = "example.com"
DOMAIN = "patientportal.example.com"
SECRET_KEY = (
    "5k9v(zqt9-s45*-kr1o@2gf2b&c=%2#&38es)ci-395o=ytc=0"  # DO NOT USE IN PRODUCTION
)

DEBUG = True

OPENDENTAL_MYSQL_SERVER = "localhost"
OPENDENTAL_MYSQL_USER = "root"
OPENDENTAL_MYSQL_PASSWORD = ""
OPENDENTAL_MYSQL_DATABASE = "opendental"
