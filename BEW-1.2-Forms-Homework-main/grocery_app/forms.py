from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import GroceryItem, GroceryStore, ItemCategory, User

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField('Store Title', validators=[DataRequired(), Length(min=1, max=80)])
    address = StringField('Store Address', validators=[DataRequired(), Length(min=1, max=80)])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""
    name = StringField('Item Name', validators=[DataRequired(), Length(min=1, max=80)])
    price = FloatField('Item Price', validators=[DataRequired()])
    category = SelectField('Category', choices = ItemCategory.choices(), validators=[DataRequired()])
    photo_url = StringField('Photo URL', validators=[URL()])
    store = QuerySelectField('Store', query_factor=lambda: GroceryStore.query)
    submit = SubmitField('Submit')

# forms.py
class SignUpForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class AddItemForm(FlaskForm):
    submit = SubmitField('Add to Shopping List')