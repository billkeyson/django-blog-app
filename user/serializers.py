from rest_framework import serializers
# from rest_framework
from django.contrib.auth import get_user_model,authenticate
from django.utils.translation import ugettext_lazy as _

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email','password','username')
        extra_kwargs =  {'password':{'write_only':True,'min_length':8}}

    def create(self, validated_data):
        print(validated_data)
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace = False
    )

    def validate(self, attrs):
        print("validate")
        email = attrs.get('email')
        password = attrs.get('password')
        # print('serial context',dir(self.context.get('request')))
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password = password
        )
        if not user:
            msg = _('Invalid credenial provided')
            raise serializers.ValidationError(msg,code='authentication')
        attrs['user'] = user
        return attrs
    