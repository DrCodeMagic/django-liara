from django.db import models



# =========================
# اطلاعات شخصی
# =========================
from django.db import models

# =========================
# اطلاعات شخصی دو زبانه
# =========================
from django.db import models

class Profile(models.Model):
    # اسم
    full_name_fa = models.CharField(max_length=100, verbose_name="نام کامل فارسی", default="علی رضایی")
    full_name_en = models.CharField(max_length=100, verbose_name="Full Name English", default="Ali Rezaei")
    
    # عنوان شغلی فقط انگلیسی
    job_title = models.CharField(max_length=150, verbose_name="Job Title", default="Full-Stack Developer")
    
    # درباره من دو زبانه
    about_me_fa = models.TextField(verbose_name="درباره من فارسی", default="من توسعه‌دهنده وب هستم و در Django و React تخصص دارم.")
    about_me_en = models.TextField(verbose_name="About Me English", default="I am a web developer specializing in Django and React.")

    # تصویر پروفایل
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    
    # اطلاعات تماس
    email = models.EmailField(default="hello@example.com")
    phone = models.CharField(max_length=20, blank=True, default="+98 912 345 6789")
    github = models.URLField(blank=True, default="https://github.com/username")
    linkedin = models.URLField(blank=True, default="https://www.linkedin.com/in/username/")
    website = models.URLField(blank=True, default="https://example.com")

    def __str__(self):
        return f"{self.full_name_en} / {self.full_name_fa}"



# =========================
# خدمات
# =========================
class Service(models.Model):
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(
        max_length=50,
        help_text="مثلاً: fa-code , fa-laptop"
    )
    price = models.CharField(
        max_length=100,
        blank=True,
        help_text="مثلاً: شروع از 5 میلیون"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# =========================
# دسته‌بندی نمونه‌کار
# =========================
class ProjectCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# =========================
# نمونه‌کارها
# =========================
class Project(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(
        ProjectCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='projects'
    )
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    project_url = models.URLField(blank=True)
    technologies = models.CharField(
        max_length=255,
        help_text="مثلاً: Django, React, Tailwind"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# =========================
# پیام‌های تماس
# =========================
class ContactMessage(models.Model):
    STATUS_CHOICES = (
        ('new', 'جدید'),
        ('read', 'خوانده شده'),
        ('answered', 'پاسخ داده شده'),
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"


# =========================
# بلاگ (اختیاری)
# =========================


