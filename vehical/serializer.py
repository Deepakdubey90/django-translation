from rest_framework import serializers
from models import VehicalParking


class VehicalParkingSerializer(serializers.ModelSerializer):
    """
    Vehical parking seruializer.
    """
    class Meta:
        model = VehicalParking
        fields = ('vehical_name', 'vehical_number', 'vehical_type',
                  'vehical_intime', 'vehical_outtime', 'park_fare'
        )
