from django.conf import settings

from ..apps.users.models import Patient

import pymysql.cursors


def get_connection() -> pymysql.Connection:
    """
    Get a pymysql.Connection

    :return: pymysql.Connection
    """
    return pymysql.connect(host=settings.OPENDENTAL_MYSQL_SERVER,
                           user=settings.OPENDENTAL_MYSQL_USER,
                           password=settings.OPENDENTAL_MYSQL_PASSWORD,
                           db=settings.OPENDENTAL_MYSQL_DATABASE,
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)


def lookup_patient(connection, ssn: str) -> Patient:
    """
    Given a SSN, lookup the patient in the Opendental DB and return a Patient object.

    :param connection: Connection object to Opendental DB
    :param ssn: Social Security Number, with or without dashes
    :return: a newly created Patient object, or a Patient object if one already exists with the SSN given.
    """
    # Strip dashes from SSN
    ssn = ssn.replace("-", "")
    with connection.cursor() as cursor:
        cursor.execute("SELECT `PatNum`, `LName`, `FName` FROM `patient` WHERE `SSN`=%s", (ssn,))
        rows = cursor.fetchall()
        if len(rows) != 1:
            raise ValueError(f"{len(rows)} patients matching this SSN were found, expecting only one.")

    patient_object = Patient.objects.update_or_create(opendental_patient_id=rows[0]["PatNum"],
                                                      defaults={"ssn": ssn, "first_name": rows[0]["FName"],
                                                                "last_name": rows[0]["LName"]})
    return patient_object
