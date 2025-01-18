from django.db import models
import ast


class PluginManager(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, default=None)
    active = models.BooleanField(default=False)
    identifier = models.CharField(max_length=100, unique=True)
    configuration = models.JSONField(blank=True, null=True, default=dict)

    # def save(self,*args, **kwargs):
    #     if self.configuration is None:


class BasePlugin:
    PLUGIN_NAME = ""

    PLUGIN_CONFIGURATION = {}

    CONFIGURATION_DEFAULT = {}

    def load_configuration(self):
        """
        Loads the configuration of the plugin from DB
        If the plugin is not found in DB, then create it in DB
        """
        plugin_model = PluginManager.objects.filter(identifier=self.PLUGIN_NAME)
        if plugin_model:
            config = plugin_model.first().configuration
            db_config_key = config.keys()
            self_config_key = self.CONFIGURATION_DEFAULT.keys()
