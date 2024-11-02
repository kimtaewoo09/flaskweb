from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, length

class BoardForm(FlaskForm):
    title=StringField(
        "제목",
        validators=[
            DataRequired(message='제목은 필수입니다'),
            length(max=30, message='30자 이내로 입력해주세요')
        ]
    )

    content=StringField(
        '내용',
        validators=[
            DataRequired(message='내용는 필수입니다'),
        ]
    )


    submit=SubmitField('신규등록')