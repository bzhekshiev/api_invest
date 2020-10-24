from django.db import models


def get_upload_path(instance, filename):
    return f'uploads/{instance.client.pk}/{filename}'


class ClientInfo(models.Model):
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    middle_name = models.CharField(verbose_name='Отчество', max_length=50)
    birth_date = models.DateField(
        verbose_name='Дата рождения', auto_now=False, auto_now_add=False)
    doc_num = models.CharField(verbose_name='Серия и номер', max_length=20)
    birth_place = models.CharField(
        verbose_name='Место рождения', max_length=100)
    issue_date = models.DateField(
        verbose_name='Дата выдачи', auto_now=False, auto_now_add=False)
    division_code = models.CharField(
        verbose_name='Код подразделения', max_length=10)
    issue_by = models.CharField(verbose_name='Кем выдан', max_length=200)
    reg_address = models.CharField(
        verbose_name='Адрес регистрации', max_length=200)

    class Meta:
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name})'


class ClientPersDoc(models.Model):
    client = models.ForeignKey(
        ClientInfo, on_delete=models.CASCADE, related_name='client_pers_doc', unique=True)
    doc_first_page = models.FileField(
        verbose_name='Разворот с фото', upload_to=get_upload_path, max_length=100)
    doc_second_page = models.FileField(
        verbose_name='Разворот с регистрацией', upload_to=get_upload_path, max_length=100)

    class Meta:
        verbose_name_plural = "Документы клиента"


class PlatformRule(models.Model):
    client = models.ForeignKey(
        ClientInfo, on_delete=models.CASCADE, related_name='client_rule', unique=True)
    is_read_rule = models.BooleanField(
        verbose_name='Ознакомился с правилами', default=False)
    is_ru_tax_resident = models.BooleanField(
        verbose_name='Налоговый резидент РФ', default=False)
    consent_to_use_auto_completion = models.BooleanField(
        verbose_name='Согласие использовать автопополнение', default=False)

    class Meta:
        verbose_name_plural = "Правила платформы"


class Qualification(models.Model):
    client = models.ForeignKey(
        ClientInfo, on_delete=models.CASCADE,
        related_name='client_qualification', unique=True)
    is_economist = models.FileField(
        verbose_name='Высшее экономическое', upload_to=get_upload_path,
        null=True, blank=True)
    total_cost_more_six_ml = models.FileField(
        verbose_name='Общая стоимость более 6 млн',
        upload_to=get_upload_path, null=True, blank=True)
    experience_in_fintech = models.FileField(
        verbose_name='Опыт работы в финансовой компании',
        upload_to=get_upload_path, null=True, blank=True)
    deposit_more_six_ml = models.FileField(
        verbose_name='Депозит более 6 млн', upload_to=get_upload_path,
        null=True, blank=True)
    active_trade_more_six_ml = models.FileField(
        verbose_name='Активная торговля более 6 млн',
        upload_to=get_upload_path, null=True, blank=True)
    already_qualified = models.FileField(
        verbose_name='Уже квалифицирован', upload_to=get_upload_path,
        null=True, blank=True)

    class Meta:
        verbose_name_plural = "Квалификация"


class ClientState(models.Model):
    client = models.ForeignKey(ClientInfo, on_delete=models.CASCADE,
                               related_name='client_state', unique=True)
    is_qualified = models.BooleanField(
        verbose_name='Квалифицирован', default=False)
