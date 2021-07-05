from rest_framework import serializers
from core.models import Libro
class LibroSerializer(serializers.ModelSerializers):
    class Meta:
        model = Libro
        fields = ['isbn','nombre_libro','autor','categoria','descripcion']