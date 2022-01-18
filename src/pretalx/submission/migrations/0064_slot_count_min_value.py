# Generated by Django 3.2.10 on 2022-01-04 21:32

from django.db import migrations


def fix_min_value(apps, schema_editor):
    Submission = apps.get_model("submission", "Submission")
    TalkSlot = apps.get_model("schedule", "TalkSlot")

    for submission in Submission.objects.all().filter(slot_count=0):
        submission.slot_count = 1
        submission.save()
        TalkSlot.objects.create(
            submission=submission,
            schedule=submission.event.schedules.all().get(version__isnull=True),
        )


class Migration(migrations.Migration):

    dependencies = [
        ("submission", "0063_submission_pending_state"),
    ]

    operations = [
        migrations.RunPython(fix_min_value, migrations.RunPython.noop),
    ]