from django.db import models

class Character(models.Model):
    character_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.character_name

class Move(models.Model):
    move_name = models.CharField(max_length=255)
    startup_frames = models.CharField(max_length=255)
    active_frames = models.CharField(max_length=255)
    recovery_frames = models.CharField(max_length=50)
    on_hit = models.CharField(max_length=255)
    on_block = models.CharField(max_length=255)
    cancel = models.CharField(max_length=255)
    damage = models.CharField(max_length=255)
    scaling = models.CharField(max_length=255)
    drive_increase = models.CharField(max_length=255)
    drive_decrease = models.CharField(max_length=255)
    drive_decrease_pc = models.CharField(max_length=255)
    sa_increase = models.CharField(max_length=255)
    high_low = models.CharField(max_length=255)
    misc = models.TextField()
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return self.move_name, self.character