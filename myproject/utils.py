import os
from uuid import uuid4
from django.utils import timezone

# uuid를 통한 파일명 정하기
def uuid_name_upload_to(instance, filename):
    app_label = instance.__class__._meta.app_label  # 앱 별로
    cls_name = instance.__class__.__name__.lower()  # 모델 별로
    ymd_path = timezone.now().strftime('%Y/%m/%d')  # 업로드 하는 년/월/일 뱌럴
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()  # 확장자 추출 및 소문자 변환
    return '/'.join([
        app_label,
        cls_name,
        ymd_path,
        uuid_name[:2],
        uuid_name + extension,   
    ])