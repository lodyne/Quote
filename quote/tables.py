import django_tables2 as tables
from .models import Quote

class MyTable(tables.Table):
    class Meta:
        model = Quote
        fields = ("quote","author",)