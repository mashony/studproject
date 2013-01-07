# -*- coding: utf-8 -*-
from optparse import make_option
from django.core.management.base import BaseCommand,CommandError
from app.models import Student

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--delete', dest='delete_group', action='store_true',
            default=False, help="Delete a group."),
        make_option('--add', dest='add_group',action='store_true',
            default=False, help="Add a group."),
        make_option('--students',dest='print_students',action='store_true',
            default=False, help="Print students of the group."),
    )
    args = "<group_name>"
    help = "Echo all positional arguments."

    def handle(self, *args, **options):
        def delete_group(group_name):
            self.stdout.write("Delete group %s" % group_name)
        def add_group(group_name):
            self.stdout.write("Add group %s" % group_name)
        def print_students(group_name):
            try:
                students = Student.objects.get_query_set().filter(group_id__exact=group_name)
            except Student.DoesNotExist:
                raise CommandError("There aren't students in this group")
            lines = []
            for student in students:
                lines += ["%s %s %s %s" % (student.id,
                                          student.first_name,
                                          student.second_name,
                                          student.date_of_birth)]
            self.stdout.write("\n".join(lines))

        try:
            group_name = args[0]
        except IndexError:
            raise CommandError('You must write a group name')
        if options['delete_group']:
            delete_group(group_name)
        if options['add_group']:
            add_group(group_name)
        if options['print_students']:
            print_students(group_name)


