from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

class MyForm(FlaskForm):
    has_pet = BooleanField('Czy masz zwierze?')
    pet_name = StringField('Jak sie nazywa zwierze?')
    like_pet = BooleanField('Czy je lubisz?')
    submit = SubmitField('Wyslij')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        has_pet = form.has_pet.data
        pet_name = form.pet_name.data
        like_pet = form.like_pet.data
        # Dane które wyœwietlane s¹ na 2 karcie, po wys³aniu
        if has_pet and like_pet:
            return f'<h1>Czyli masz zwierze, ktore nazywa sie {pet_name} i go lubisz</h1>'
        if has_pet  and not like_pet:
            return f'<h1>Czyli masz zwierze, ktore nazywa sie {pet_name} i go nie lubisz</h1>'
        else:
            return f'<h1>Czyli nie masz zwierzecia :c</h1>'
    return render_template('index.html', form=form)


if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)