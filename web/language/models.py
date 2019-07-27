from django.contrib.auth.models import User

from django.contrib.gis.db import models

class BaseModel(models.Model):
    name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class LanguageFamily(BaseModel):
    pass


class LanguageSubFamily(BaseModel):
    family = models.ForeignKey(LanguageFamily, on_delete=models.SET_NULL, null=True)


class Language(BaseModel):
    other_names = models.TextField(default="")
    fv_archive_link = models.URLField(max_length=255, blank=True, default="")
    color = models.CharField(max_length=31, default="")
    sub_family = models.ForeignKey(
        LanguageSubFamily, on_delete=models.SET_NULL, null=True
    )
    notes = models.TextField(default="")
    fluent_speakers = models.IntegerField(
        default=0
    )  # sum of field_tm_lna2_on_fluent_sum_value
    some_speakers = models.IntegerField(default=0)  # field_tm_lna2_on_some_sum_value
    learners = models.IntegerField(default=0)  # sum of field_tm_lna2_on_lrn_sum_value
    pop_total_value = models.IntegerField(
        default=0
    )  # sum of field_tm_lna2_pop_total_value

    color = models.CharField(max_length=31)
    geom = models.PolygonField(null=True, default=None)
    bbox = models.PolygonField(null=True, default=None)



class LanguageLink(models.Model):
    url = models.URLField(max_length=255, default=None, null=True)
    title = models.CharField(max_length=255)
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, null=True, default=None
    )


class Community(BaseModel):
    notes = models.TextField(default="")
    point = models.PointField(null=True, default=None)
    english_name = models.CharField(max_length=255, default="")
    other_names = models.CharField(max_length=255, default="")
    internet_speed = models.CharField(max_length=255, default="")
    population = models.IntegerField(default=0)
    languages = models.ManyToManyField(Language)
    email = models.EmailField(max_length=255, default=None, null=True)
    website = models.URLField(max_length=255, default=None, null=True)
    phone = models.CharField(max_length=255, default="")
    alt_phone = models.CharField(max_length=255, default="")
    fax = models.CharField(max_length=255, default="")


class CommunityLink(models.Model):
    url = models.URLField(max_length=255, default=None, null=True)
    title = models.CharField(max_length=255)
    community = models.ForeignKey(
        Community, on_delete=models.CASCADE, null=True, default=None
    )


class LanguageMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class PlaceName(BaseModel):
    point = models.PointField(null=True, default=None)
    other_name = models.CharField(max_length=255, default="")
    kind = models.CharField(max_length=15, default="")


class Champion(BaseModel):
    bio = models.TextField(default="")
    job = models.CharField(max_length=255, default="")
    community = models.ForeignKey(
        Community, on_delete=models.SET_NULL, null=True, default=None
    )
    language = models.ForeignKey(
        Language, on_delete=models.SET_NULL, null=True, default=None
    )


class Dialect(BaseModel):
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, null=True, default=None
    )


class LNA(BaseModel):
    year = models.IntegerField(default=1970)
    language = models.ForeignKey(
        Language, on_delete=models.SET_NULL, null=True
    )  # field_tm_lna1_lang_target_id
    # nations = models.ManyToManyField(Community)  # field_tm_lna1_comms_servd_target_id
    # Held in LNAData model.


class LNAData(BaseModel):
    lna = models.ForeignKey(
        LNA, on_delete=models.SET_NULL, null=True
    )  # field_tm_lna2_lna_target_id
    community = models.ForeignKey(Community, on_delete=models.SET_NULL, null=True)
    fluent_speakers = models.IntegerField(
        default=0
    )  # field_tm_lna2_on_fluent_sum_value
    some_speakers = models.IntegerField(default=0)  # field_tm_lna2_on_some_sum_value
    learners = models.IntegerField(default=0)  # field_tm_lna2_on_lrn_sum_value
    pop_off_res = models.IntegerField(default=0)  # field_tm_lna2_pop_off_res_value
    pop_on_res = models.IntegerField(default=0)  # field_tm_lna2_pop_on_res_value
    pop_total_value = models.IntegerField(default=0)  # field_tm_lna2_pop_total_value


class Art(BaseModel):
    point = models.PointField(null=True, default=None)
    art_type = models.CharField(max_length=10, default="")
    title = models.CharField(max_length=255)
    node_id = models.IntegerField()

