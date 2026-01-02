from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    icon = models.ImageField(
        upload_to="apps/icons/",
        blank=True,
        null=True
    )

    icon_url = models.URLField(
        blank=True,
        null=True,
        help_text="Optional external icon URL"
    )

    icon_font = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Optional use fa or bi"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Folder(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class SubFolder(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    folder = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
        related_name="subfolders"
    )

    class Meta:
        unique_together = ("title", "folder")
        ordering = ["title"]

    def __str__(self):
        return f"{self.folder.title} → {self.title}"


class App(models.Model):

    STATUS_CHOICES = (
        ("working", "Working"),
        ("need_key", "Needs API Key"),
        ("not_installed", "Not Installed"),
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    # FIXED FIELD NAME
    categories = models.ManyToManyField(
        Category,
        related_name="apps",
        blank=True
    )

    icon = models.ImageField(
        upload_to="apps/icons/",
        blank=True,
        null=True
    )

    icon_url = models.URLField(
        blank=True,
        null=True,
        help_text="Optional external icon URL"
    )

    folders = models.ManyToManyField(
        Folder,
        related_name="apps",
        blank=True
    )

    sub_folder = models.ForeignKey(
        SubFolder,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text='Leave empty only if folder is "Other"'
    )

    description = models.TextField(default="<p>  </p>    <p>  </p>    <div class='list-title'></div>     <ul class='list px-3'><li> </li>    <li> </li>      </ul>")

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="need_key"
    )

    use = models.TextField(
        help_text="What this app is used for"
    )

    cost_usd = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


    def next_id(self):
        n_id = self.id + 1
        if App.objects.count() == n_id:
            return False
        else:
            return n_id


    def previous_id(self):
        p_id = self.id - 1
        if 0 == p_id:
            return False
        else:
            return p_id
