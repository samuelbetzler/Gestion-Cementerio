from django.db import models

class AuditLog(models.Model):
    table_name = models.CharField(max_length=50)
    operation = models.CharField(max_length=50)
    old_data = models.JSONField(null=True, blank=True)
    new_data = models.JSONField(null=True, blank=True)
    changed_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'audit_log' # Nombre de la tabla en la base de datos
        
class QueryHistory(models.Model):
    query_sql = models.TextField()
    result = models.TextField()
    executed_at = models.DateTimeField(auto_now_add=True)
