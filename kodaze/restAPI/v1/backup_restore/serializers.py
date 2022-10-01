from rest_framework import serializers
from backup_restore.models import BackupAndRestore
from restAPI.core import DynamicFieldsCategorySerializer

class BackupAndRestoreSerializer(DynamicFieldsCategorySerializer):
    class Meta:
        model = BackupAndRestore
        fields = "__all__"