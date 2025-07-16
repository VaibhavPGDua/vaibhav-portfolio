import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev_secret_key_change_in_production")

# Configure database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Initialize database
db.init_app(app)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)

# Create database tables
with app.app_context():
    # Import models here to ensure they're registered
    import models
    db.create_all()

@app.route('/')
def index():
    """Main portfolio page"""
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submission"""
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        if not all([name, email, subject, message]):
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('index') + '#contact')
        
        # Import the model
        from models import ContactMessage
        
        # Save to database
        contact_message = ContactMessage(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        db.session.add(contact_message)
        db.session.commit()
        
        # Send email (optional - requires mail configuration)
        try:
            if app.config.get('MAIL_USERNAME'):
                msg = Message(
                    subject=f"Portfolio Contact: {subject}",
                    recipients=['vaibhavd881@gmail.com'],
                    body=f"""
                    New message from your portfolio website:
                    
                    Name: {name}
                    Email: {email}
                    Subject: {subject}
                    
                    Message:
                    {message}
                    """
                )
                mail.send(msg)
        except Exception as mail_error:
            app.logger.warning(f"Email sending failed: {str(mail_error)}")
        
        flash('Thank you for your message! I will get back to you soon.', 'success')
        
    except Exception as e:
        app.logger.error(f"Error processing contact form: {str(e)}")
        flash('There was an error sending your message. Please try again or contact me directly.', 'error')
    
    return redirect(url_for('index') + '#contact')

@app.route('/admin/messages')
def admin_messages():
    """Admin route to view contact messages"""
    from models import ContactMessage
    
    # Get all messages ordered by creation date (newest first)
    messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
    
    return render_template('admin_messages.html', messages=messages)

@app.route('/admin/messages/<int:message_id>/mark_read', methods=['POST'])
def mark_message_read(message_id):
    """Mark a message as read"""
    from models import ContactMessage
    
    message = ContactMessage.query.get_or_404(message_id)
    message.is_read = True
    db.session.commit()
    
    flash('Message marked as read.', 'success')
    return redirect(url_for('admin_messages'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
