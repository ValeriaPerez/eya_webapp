# -*- coding: utf-8 -*-

from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q

class Command(BaseCommand):
    help = 'Create groups for managers'

    def handle(self, *args, **options):
        # Create group Super Admin
        try:
            super_admin = Group.objects.get(name='Super Admin')
            for perm in super_admin.permissions.all():
                super_admin.permissions.remove(perm)
        except Exception:
            super_admin = Group.objects.create(name='Super Admin')
        # Create group Trader
        try:
            admin = Group.objects.get(name='Trader')
            for perm in admin.permissions.all():
                admin.permissions.remove(perm)
        except Exception:
            admin = Group.objects.create(name='Trader')

        # Create group Provider
        try:
            staff = Group.objects.get(name='Provider')
            for perm in staff.permissions.all():
                staff.permissions.remove(perm)
        except Exception:
            staff = Group.objects.create(name='Provider')
        # Create group Provider
        try:
            staff = Group.objects.get(name='Billing')
            for perm in staff.permissions.all():
                staff.permissions.remove(perm)
        except Exception:
            staff = Group.objects.create(name='Billing')