"""
Command to wait for the availability of the database before connecting.
"""
import time

from psycopg2 import OperationalError as PsycopgError

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Command to wait for database."""

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Waiting for database...'))
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (PsycopgError, OperationalError):
                self.stdout.write(self.style.WARNING('Database unavailable, waiting 1 second.'))
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Database available.'))
