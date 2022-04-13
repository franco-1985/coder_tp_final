from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "tp_final_coder.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import tp_final_coder.users.signals  # noqa F401
        except ImportError:
            pass
