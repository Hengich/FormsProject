import re
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FormTemplate


class FormAPIView(APIView):
    """
    Обработчик POST-запросов для определения шаблона формы.
    """

    def post(self, request, *args, **kwargs):
        data = request.data
        templates = FormTemplate.objects.all()

        matched_template = self.find_matching_template(data, templates)

        if matched_template:
            return Response({'template_name': matched_template.name},
                            status=status.HTTP_200_OK)
        else:
            validated_fields = self.validate_fields(data)
            return Response(validated_fields, status=status.HTTP_200_OK)

    def find_matching_template(self, data, templates):
        """
        Находит подходящий шаблон формы по переданным данным.
        """
        for template in templates:
            template_fields = template.fields
            if all(
                key in data and
                self.determine_field_type(data[key]) == template_fields[key]
                for key in template_fields
            ):
                return template
        return None

    def validate_fields(self, data: dict) -> dict:
        """
        Определяет типы полей на основе переданных данных.
        """
        validated_fields = {}
        for key, value in data.items():
            field_type = self.determine_field_type(value)
            validated_fields[key] = field_type
        return validated_fields

    def determine_field_type(self, value: str) -> str:
        """
        Определяет тип переданного значения: дата, телефон, email или текст.
        """
        date_formats = ['%d.%m.%Y', '%Y-%m-%d']
        for fmt in date_formats:
            try:
                datetime.strptime(value, fmt)
                return "date"
            except ValueError:
                pass

        phone_pattern = r'^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$'
        if re.match(phone_pattern, value):
            return "phone"

        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(email_pattern, value):
            return "email"

        return "text"
