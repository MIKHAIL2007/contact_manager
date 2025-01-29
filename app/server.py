from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from logger import Logger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
logger = Logger()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/<name>')
def home(name='Guest'):
    logger.info(f'Visited home page by {name}')
    return render_template('index.html', name=name)

@app.route('/contacts/<int:contact_id>')
def get_contact(contact_id):
    contact = Contact.query.get(contact_id)
    if contact:
        logger.info(f'Viewed contact: {contact.name}')
        return jsonify({
            'id': contact.id,
            'name': contact.name,
            'phone': contact.phone,
            'email': contact.email,
        })
    logger.warning(f'Attempted to view invalid contact ID: {contact_id}')
    return 'The contact ID is invalid', 404

@app.route('/contacts')
def get_contacts():
    logger.info('Visited contacts page')
    contacts = Contact.query.all()
    return render_template('contacts.html', contacts=contacts)

@app.route('/contacts/add', methods=['GET', 'POST'])
def add_contact():
    logger.info('Visited add contact page')
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        new_contact = Contact(name=name, phone=phone, email=email)
        db.session.add(new_contact)
        db.session.commit()
        logger.info(f'Added new contact: {name}')
        return redirect(url_for('get_contacts'))

    return render_template('add_contact.html')

@app.route('/contacts/edit/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    logger.info(f'Visited edit contact page for {contact.name}')
    if request.method == 'POST':
        contact.name = request.form['name']
        contact.phone = request.form['phone']
        contact.email = request.form['email']
        db.session.commit()
        logger.info(f'Edited contact: {contact.name}')
        return redirect(url_for('get_contacts'))
    return render_template('edit_contact.html', contact=contact)

@app.route('/contacts/delete/<int:contact_id>', methods=['POST'])
def delete_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    logger.info(f'Visited delete contact page for {contact.name}')
    db.session.delete(contact)
    db.session.commit()
    logger.info(f'Deleted contact: {contact.name}')
    return redirect(url_for('get_contacts'))

if __name__ == '__main__':
    app.run(port=8080)