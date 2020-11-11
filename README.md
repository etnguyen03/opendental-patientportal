# opendental-patientportal

![Django CI](https://github.com/etnguyen03/opendental-patientportal/workflows/Django%20CI/badge.svg) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/ddf35206d7a74342b11d95b61ad4e36d)](https://www.codacy.com/manual/etnguyen03/opendental-patientportal?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=etnguyen03/opendental-patientportal&amp;utm_campaign=Badge_Grade) [![Codacy Badge](https://app.codacy.com/project/badge/Coverage/ddf35206d7a74342b11d95b61ad4e36d)](https://www.codacy.com/manual/etnguyen03/opendental-patientportal?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=etnguyen03/opendental-patientportal&amp;utm_campaign=Badge_Coverage) [![GitHub license](https://img.shields.io/github/license/etnguyen03/opendental-patientportal)](https://github.com/etnguyen03/opendental-patientportal)

A patient portal written in Django for Open Dental.

Please note that this project has absolutely no affiliation with Open Dental. It just interfaces with the MySQL database.

This is still a work in progress, and is definitely not ready for any production usage.

## Development Environment Setup

```bash
git clone https://github.com/etnguyen03/opendental-patientportal
cd opendental-patientportal
```

Now, you will want to copy `patientportal/settings/config.sample.py` to `patientportal/settings/config.py`
and fill in the details.

Then,

```bash
pipenv install --dev
pipenv run python3 manage.py collectstatic
pipenv run python3 manage.py migrate
pipenv run gunicorn patientportal.wsgi
```

## Production Setup

I assume that you have a reverse proxy and a Postgres database set up.

```bash
git clone https://github.com/etnguyen03/opendental-patientportal
cd opendental-patientportal
```

Now, you will want to copy `patientportal/settings/config.sample.py` to `patientportal/settings/config.py`
and fill in the details. Ensure `DEBUG` is set to `False`.

Then,

```bash
pipenv install
pipenv run python3 manage.py collectstatic
pipenv run python3 manage.py migrate
pipenv run gunicorn patientportal.wsgi
```

A `systemd` service will be created in the future.

---

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
