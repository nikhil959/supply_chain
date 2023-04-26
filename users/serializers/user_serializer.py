from rest_framework import serializers
from ..models import Users, BasicAddress, BasicBranch, BasicPhoneDetails

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicAddress
        fields = '__all__'

class UserBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicBranch
        fields = '__all__'

class UserPhoneNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicPhoneDetails
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True)
    phone_no = UserPhoneNoSerializer()
    branch = UserBranchSerializer()
    class Meta:
        model = Users
        fields = '__all__'

    def create(self, validated_data):  
        """ 
        Create and return a new `Students` instance, given the validated data. 
        """  
        branch_data = validated_data.pop("branch")
        branch = BasicBranch.objects.create(**branch_data)
        address_data = validated_data.pop("address")
        phone_no_data = validated_data.pop("phone_no")
        phone_no = BasicPhoneDetails.objects.create(**phone_no_data)
        user_res = Users.objects.create(branch=branch, phone_no=phone_no, **validated_data)  
        for item in address_data:
            address = BasicAddress.objects.create(**item)
            user_res.address.add(address)
        return user_res