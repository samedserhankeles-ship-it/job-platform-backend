from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        
        # SADECE izin verilen alanları listeliyoruz.
        # id, user, created_at gibi otomatik veya hassas alanları ÇIKARIYORUZ.
        fields = [
            'id', 
            'user', # Görüntüleme (GET) için user'ı dahil etmeliyiz.
            'title', 
            'description', 
            'location_city'
        ]
        
        # Bu alanlar sadece kullanıcıya gösterilir, kullanıcı bunları değiştiremez/gönderemez.
        read_only_fields = [
            'id', 
            'user', 
            'created_at' # created_at'ı da buraya ekliyoruz (eğer GET'te göstermek isterseniz)
        ]
        
        # Eğer created_at ve id'yi GET isteklerinde göstermek istiyorsanız fields'a ekleyin.
        # title, description ve location_city yazma (POST/PUT) iznine sahip olur.
