from django.db import models
from django.utils.translation import gettext_lazy as _


class Keyword(models.Model):

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Faction(models.Model):

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class StatCard(models.Model):

    name = models.CharField(max_length=50, unique=True)
    card_front = models.ImageField(upload_to='stat_cards')
    card_back = models.ImageField(upload_to='stat_cards')

    def __str__(self):
        return self.name


class Trigger(models.Model):

    name = models.CharField(max_length=50, unique=True)
    suit = models.CharField(max_length=6)
    description = models.TextField()

    def __str__(self):
        return self.name


class Action(models.Model):

    class ActionType(models.TextChoices):
        ATTACK_ACTION = 'AA', _('Attack Action')
        TACTICAL_ACTION = 'TA', _('Tactical Action')

    name = models.CharField(max_length=50, unique=True)
    action_type = models.CharField(max_length=2, choices=ActionType.choices)
    range_type = models.CharField(max_length=50, blank=True)
    range = models.CharField(max_length=2)
    stat = models.CharField(max_length=50)
    resist = models.CharField(max_length=50)
    target_number = models.CharField(max_length=2)
    description = models.TextField()
    triggers = models.ManyToManyField(Trigger, blank=True)
    bonus_action = models.BooleanField()

    def __str__(self):
        return self.name


class Ability(models.Model):

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Characteristic(models.Model):

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class MalifauxModel(models.Model):

    class FactionType(models.TextChoices):
        GUILD = 'G', _('Guild')
        RESURRECTIONISTS = 'R', _('Resurrectionists')
        NEVERBORN = 'N', _('Neverborn')
        ARACANISTS = 'A', _('Arcanists')
        OUTCASTS = 'O', _('Outcasts')
        BAYOU = 'B', _('Bayou')
        TEN_THUNDERS = 'T', _('Ten Thunders')
        EXPLORERS_SOCIETY = 'E', _('Explorer\'s Society')

    stat_card = models.ForeignKey(StatCard, on_delete=models.CASCADE)

    # front of card
    name = models.CharField(max_length=50, unique=True)
    faction = models.CharField(max_length=1, choices=FactionType.choices)
    cost = models.IntegerField()
    characteristics = models.ManyToManyField(Characteristic)
    keywords = models.ManyToManyField(Keyword)
    defence = models.CharField(max_length=2)
    willpower = models.CharField(max_length=2)
    movement = models.CharField(max_length=2)
    size = models.CharField(max_length=2)
    abilities = models.ManyToManyField(Ability, blank=True)
    health = models.IntegerField()

    # back of card
    actions = models.ManyToManyField(Action)
    base_size = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def characteristic_string(self):
        return ', '.join(characteristic.name for characteristic in self.characteristics.all())

    @property
    def keyword_string(self):
        return ', '.join(keyword.name for keyword in self.keywords.all())
