import os
from flask import Flask, render_template, request

app = Flask(
    __name__,
    template_folder='.',
    static_folder='assets',
    static_url_path='/assets'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forms/contact.php', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')
    
    # Basic validation
    if not all([name, email, subject, message]):
        return 'All fields are required.', 400
        
    # Log the message details to the console
    print(f"\n[Contact Form Submission]")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Subject: {subject}")
    print(f"Message: {message}\n")
    
    # Save the submission locally
    try:
        messages_dir = os.path.join(app.root_path, 'messages')
        os.makedirs(messages_dir, exist_ok=True)
        message_file = os.path.join(messages_dir, 'contact_messages.txt')
        with open(message_file, 'a', encoding='utf-8') as f:
            f.write(f"--- Contact Form Submission ---\n")
            f.write(f"Name: {name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Subject: {subject}\n")
            f.write(f"Message: {message}\n\n")
    except Exception as e:
        print(f"Error saving message to file: {e}")
        
    # 'OK' is required by validate.js to show success message
    return 'OK'

if __name__ == '__main__':
    print("Starting AgriVision India Flask Server on http://localhost:5000")
    app.run(debug=True, port=5000)
