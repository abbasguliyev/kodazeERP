from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from product.models import (
    Mehsullar, 
)
from company.models import (
    Shirket,
)
from restAPI.company.serializers import ShirketSerializer


class MehsullarSerializer(serializers.ModelSerializer):
    shirket = ShirketSerializer(read_only = True)
    shirket_id = serializers.PrimaryKeyRelatedField(
        queryset = Shirket.objects.all(), source = "shirket", write_only= True
    )
    class Meta:
        model = Mehsullar
        fields = "__all__"

    def create(self, validated_data):
        mehsulun_adi = validated_data.get('mehsulun_adi')
        validated_data['mehsulun_adi'] = mehsulun_adi.upper()
        shirket = validated_data['shirket']
        print(f"{shirket=}")
        try:
            mehsul = Mehsullar.objects.filter(mehsulun_adi=mehsulun_adi.upper(), shirket=shirket)
            print(f"{mehsul=}")
            if len(mehsul)>0:
                raise ValidationError
            return super(MehsullarSerializer, self).create(validated_data)
        except:
            raise ValidationError({"detail" : 'Bu ad ilə məhsul artıq əlavə olunub'})
