from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL

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