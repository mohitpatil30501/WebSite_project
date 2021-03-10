from django.contrib import admin

from .models import *
from .forms import UserChoiceField


@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id', 'name',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(SubjectOfInterest)
class SubjectOfInterestAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Academics)
class AcademicsAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(ProfessionalMembership)
class ProfessionalMembershipAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(TeachingExperience)
class TeachingExperienceAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(AdministrativeExperience)
class AdministrativeExperienceAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(IndustrialExperience)
class IndustrialExperienceAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(FacultyDevelopment)
class FacultyDevelopmentAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(PublicationsBook)
class PublicationsBookAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(PublicationsJournal)
class PublicationsJournalAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(PublicationsPaper)
class PublicationsPaperAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(ShortTermsTrainingProgram)
class ShortTermsTrainingProgramAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Workshops)
class WorkshopsAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(OtherInstituteInteractions)
class OtherInstituteInteractionsAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Consultancy)
class ConsultancyAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(AwardReceived)
class AwardReceivedAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(ProjectGuided)
class ProjectGuidedAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(ExtraCurricularActivities)
class ExtraCurricularActivitiesAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    readonly_fields = ('id',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            return UserChoiceField(queryset=Teacher.objects.filter())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
