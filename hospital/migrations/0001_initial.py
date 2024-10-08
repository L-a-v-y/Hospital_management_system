from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("patientId", models.PositiveIntegerField(null=True)),
                ("doctorId", models.PositiveIntegerField(blank=True, null=True)),
                ("patientName", models.CharField(max_length=40, null=True)),
                ("doctorName", models.CharField(blank=True, max_length=40, null=True)),
                ("appointmentTime", models.DateTimeField(null=True)),
                ("description", models.TextField(max_length=500)),
                ("status", models.BooleanField(default=False)),
                ("prescription", models.TextField(max_length=500)),
                (
                    "priority",
                    models.IntegerField(
                        choices=[(1, "Regular"), (2, "Emergency")], null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile_pic",
                    models.ImageField(
                        blank=True, null=True, upload_to="profile_pic/DoctorProfilePic/"
                    ),
                ),
                ("address", models.CharField(max_length=40)),
                ("mobile", models.CharField(max_length=10, null=True)),
                (
                    "department",
                    models.CharField(
                        choices=[
                            ("Cardiologist", "Cardiologist"),
                            ("Dermatologists", "Dermatologists"),
                            (
                                "Emergency Medicine Specialists",
                                "Emergency Medicine Specialists",
                            ),
                            ("Allergists/Immunologists", "Allergists/Immunologists"),
                            ("Anesthesiologists", "Anesthesiologists"),
                            ("Colon and Rectal Surgeons", "Colon and Rectal Surgeons"),
                        ],
                        default="Cardiologist",
                        max_length=50,
                    ),
                ),
                ("status", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(default=None, max_length=40)),
                ("last_name", models.CharField(default=None, max_length=40)),
                (
                    "profile_pic",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profile_pic/PatientProfilePic/",
                    ),
                ),
                ("address", models.CharField(max_length=40)),
                ("mobile", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=254)),
                ("symptoms", models.CharField(max_length=100)),
                ("assignedDoctorId", models.PositiveIntegerField(null=True)),
                ("admitDate", models.DateField(auto_now=True, null=True)),
                ("dischargeDate", models.DateField(auto_now=True, null=True)),
                ("status", models.PositiveIntegerField(default=0)),
                ("room", models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="PatientDischargeDetails",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("patientId", models.PositiveIntegerField(null=True)),
                ("patientName", models.CharField(max_length=40)),
                ("assignedDoctorName", models.CharField(max_length=40)),
                ("address", models.CharField(max_length=40)),
                ("mobile", models.CharField(max_length=10, null=True)),
                ("symptoms", models.CharField(max_length=100, null=True)),
                ("admitDate", models.DateField()),
                ("releaseDate", models.DateField()),
                ("daySpent", models.PositiveIntegerField()),
                ("roomCharge", models.PositiveIntegerField()),
                ("medicineCost", models.PositiveIntegerField()),
                ("doctorFee", models.PositiveIntegerField()),
                ("OtherCharge", models.PositiveIntegerField()),
                ("total", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Procedure",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("cost", models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "number",
                    models.PositiveIntegerField(primary_key=True, serialize=False),
                ),
                ("room_type", models.CharField(max_length=40)),
                ("cost", models.PositiveIntegerField()),
                ("max_capacity", models.PositiveIntegerField(default=1)),
                ("occupied_capacity", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Undergoes",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                (
                    "doctorId",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="hospital.doctor",
                        verbose_name="id",
                    ),
                ),
                (
                    "patientId",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="hospital.patient",
                        verbose_name="id",
                    ),
                ),
                (
                    "procedureId",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="hospital.procedure",
                        verbose_name="id",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Test",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("doctername", models.CharField(max_length=40)),
                ("procedurename", models.CharField(max_length=40)),
                ("description", models.TextField(max_length=500, null=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="testimages/"),
                ),
                (
                    "patientId",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="hospital.patient",
                        verbose_name="id",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FrontDeskOperator",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile_pic",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profile_pic/FrontDeskOperatorProfilePic/",
                    ),
                ),
                ("address", models.CharField(max_length=40)),
                ("mobile", models.CharField(max_length=10, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DataEntryOperator",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile_pic",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profile_pic/DataEntryOperatorProfilePic/",
                    ),
                ),
                ("address", models.CharField(max_length=40)),
                ("mobile", models.CharField(max_length=10, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Admin",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(max_length=40)),
                ("mobile", models.CharField(max_length=10, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
