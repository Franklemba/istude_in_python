from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.messages import Message


# create a blueprint for contact routes
contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact')
def contact():
    return render_template('contact.html')


@contact_bp.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message_text = request.form.get('message')
    
    
    
    # Use the model to add a message to the database
    Message.create_message(name, email, message_text)
    
    flash('Thank you for your message! we will get back to you soon.')
    
    return redirect(url_for('contact.contact'))

@contact_bp.route('/messages')
def view_messages():
    # Get all messages from the database
    messages = Message.get_all_messages()
    return render_template('messages.html', messages= messages)
 
