from flask import Flask, render_template, request, redirect, url_for, flash,session, jsonify
 
import mysql.connector
import hashlib
import os
from werkzeug.utils import secure_filename
import streamlit as st
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
import psycopg2
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///complaints.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# # Define the Student model
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    registration_no = db.Column(db.String(100), unique=True, nullable=False)
    email_id = db.Column(db.String(100), unique=True, nullable=False)
    phoneno = db.Column(db.String(15), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100))
    password = db.Column(db.String(255), nullable=False)

# Define the Faculty model
class Faculty(db.Model):
    __tablename__ = 'faculty'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    employee_id = db.Column(db.String(100), unique=True, nullable=False)
    email_id = db.Column(db.String(100), unique=True, nullable=False)
    phoneno = db.Column(db.String(15), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)

# Define the Admin model
class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

# FacultyComplaint Model
class FacultyComplaint(db.Model):
    __tablename__ = 'faculty_complaints'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    complaint_type = db.Column(db.String(100), nullable=False)
    faculty_name = db.Column(db.String(100), nullable=False)
    complaint_details = db.Column(db.Text, nullable=False)
    evidence = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(50), nullable=False)

# AdminComplaint Model
class AdminComplaint(db.Model):
    __tablename__ = 'admin_complaints'
    id = db.Column(db.Integer, primary_key=True)
    complaint_type = db.Column(db.String(100), nullable=False)
    faculty_name = db.Column(db.String(100), nullable=False)
    complaint_details = db.Column(db.Text, nullable=False)
    evidence = db.Column(db.String(255), nullable=True)

# Complaint Model
class Complaint(db.Model):
    __tablename__ = 'complaints'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    complaint_type = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    faculty_name = db.Column(db.String(100), nullable=True)
    complaint_details = db.Column(db.Text, nullable=False)
    evidence = db.Column(db.String(255), nullable=True)
    details = db.Column(db.Text, nullable=False)
    votes = db.relationship('Vote', backref='complaint', lazy=True)
    poll_votes = db.relationship('PollVote', backref='complaint', lazy=True)

# Vote Model
class Vote(db.Model):
    __tablename__ = 'votes'
    id = db.Column(db.Integer, primary_key=True)
    vote = db.Column(db.String(50), nullable=False)  # 'support' or 'against'
    complaint_id = db.Column(db.Integer, db.ForeignKey('complaints.id'), nullable=False)

# PollVote Model
class PollVote(db.Model):
    __tablename__ = 'poll_votes'
    id = db.Column(db.Integer, primary_key=True)
    vote = db.Column(db.String(50), nullable=False)  # 'support' or 'against'
    complaint_id = db.Column(db.Integer, db.ForeignKey('complaints.id'), nullable=False)

with app.app_context():
    db.create_all()

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

# Route for the student login page
# Route for the student login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Query the 'student' table
        student = Student.query.filter_by(username=username).first()

        if student:
            # Compare the hashed password
            if hashed_password == student.password:
                session['username'] = username  # Store username in session
                flash('Login successful as Student!', 'success')
                return redirect(url_for('student_dashboard'))  # Redirect to student dashboard
            else:
                flash('Incorrect password for Student!', 'danger')
        else:
            flash('User not found! Please <a href="/student_register">register</a>.', 'danger')

    return render_template('login.html')





# Route for the faculty login page
@app.route('/faculty_login', methods=['GET', 'POST'])
def faculty_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Query the 'faculty' table
        faculty = Faculty.query.filter_by(username=username).first()

        if faculty:
            # Compare the hashed password
            if hashed_password == faculty.password:
                flash('Login successful as Faculty!', 'success')
                session['username'] = username  # Store username in session
                return redirect(url_for('faculty_dashboard'))  # Redirect to faculty dashboard
            else:
                flash('Incorrect password for Faculty!', 'danger')
        else:
            flash('User not found! Please <a href="/faculty_register">register</a>.', 'danger')

    return render_template('faculty_login.html')

# Route for the admin login page
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Query the 'admin' table
        admin = Admin.query.filter_by(username=username).first()

        if admin:
            # Compare the hashed password
            if hashed_password == admin.password:
                flash('Login successful as Admin!', 'success')
                session['username'] = username  # Store username in session
                return redirect(url_for('admin_dashboard'))  # Redirect to admin dashboard
            else:
                flash('Incorrect password for Admin!', 'danger')
        else:
            flash('User not found! Please <a href="/admin_register">register</a>.', 'danger')

    return render_template('admin_login.html')


# Route for the student dashboard
@app.route('/student_dashboard')
def student_dashboard():
    return render_template('home.html')

# Route for the faculty dashboard
@app.route('/faculty_dashboard')
def faculty_dashboard():
    # Query the faculty_complaints table using SQLAlchemy
    complaints_data = FacultyComplaint.query.all()

    # Pass complaints data to the template
    return render_template('faculty_complaint.html', complaints=complaints_data)


@app.route('/admin_dashboard')
def admin_dashboard():
    # Query all admin complaints using SQLAlchemy
    admin_complaints = AdminComplaint.query.all()

    # Render the admin complaints in the template
    return render_template('admin_complaint_view.html', admin_complaints=admin_complaints)


# Route for the student registration page
import hashlib
@app.route('/student_register', methods=['GET', 'POST'])
def student_register():
    if request.method == 'POST':
        try:
            # Retrieve form data
            username = request.form['username']
            registration_no = request.form['registration_no']
            email_id = request.form['email_id']
            phoneno = request.form['phoneno']
            department = request.form['department']
            specialization = request.form.get('specialization')  # specialization can be NULL
            password = request.form['password']
            
            # Ensure no empty or duplicate data for required fields
            if not username or not registration_no or not email_id or not phoneno or not department or not password:
                flash('All required fields must be filled!', 'danger')
                return redirect(request.url)

            # Hash the password before storing it
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # Check if the username, registration_no, or email_id already exists using SQLAlchemy
            existing_student = Student.query.filter(
                (Student.username == username) | 
                (Student.registration_no == registration_no) | 
                (Student.email_id == email_id)
            ).first()

            if existing_student:
                flash('Username, Registration No., or Email ID already exists. Please use unique values.', 'danger')
                return redirect(request.url)

            # Create a new student instance
            new_student = Student(
                username=username,
                registration_no=registration_no,
                email_id=email_id,
                phoneno=phoneno,
                department=department,
                specialization=specialization,
                password=hashed_password
            )

            # Add the new student to the session and commit
            db.session.add(new_student)
            db.session.commit()

            flash('Student registered successfully!', 'success')
            return redirect(url_for('login'))

        except Exception as e:
            flash('An error occurred. Please try again.', 'danger')

    return render_template('student_registration.html')






# Route for the faculty registration page
@app.route('/faculty_register', methods=['GET', 'POST'])
def faculty_register():
    if request.method == 'POST':
        username = request.form['username']
        employee_id = request.form['employee_id']
        email_id = request.form['email_id']
        phoneno = request.form['phoneno']
        department = request.form['department']
        password = request.form['password']

        # Hash the password before storing it
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Check if the faculty already exists using SQLAlchemy
        existing_faculty = Faculty.query.filter(
            (Faculty.username == username) | 
            (Faculty.employee_id == employee_id) | 
            (Faculty.email_id == email_id)
        ).first()

        if existing_faculty:
            flash('Username, Employee ID, or Email ID already exists. Please use unique values.', 'danger')
            return redirect(request.url)

        # Create a new faculty instance
        new_faculty = Faculty(
            username=username,
            employee_id=employee_id,
            email_id=email_id,
            phoneno=phoneno,
            department=department,
            password=hashed_password
        )

        # Add the new faculty to the session and commit
        db.session.add(new_faculty)
        db.session.commit()

        flash('Faculty registration successful!', 'success')
        return redirect(url_for('faculty_login'))

    return render_template('faculty_registration.html')


@app.route('/logout')
def logout():
     # Clear the session
    return redirect(url_for('login'))



# Email credentials
sender_email = "your_email@gmail.com"
sender_password = "your_password"  # Use an App Password if 2FA is enabled
recipient_email = "recipient_email@gmail.com"

# Email content
subject = "Test Email from Python"
body = """\
Hello,

This is a test email sent using Python. Have a great day!

Best regards,
Your Python Script
"""

# Create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Send the email
try:
    # Connect to Gmail SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Start TLS encryption
        server.login(sender_email, sender_password)
        server.send_message(message)
        print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")


UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp3', 'mp4', 'mov', 'wav'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if a file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/lodge_complaint', methods=['GET', 'POST'])
def lodge_complaint():
    if 'username' not in session:  # Ensure user is logged in
        flash('You need to log in to lodge a complaint.', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        try:
            # Retrieve form data
            complaint_type = request.form['comment']
            category = request.form['comment1']
            faculty_name = request.form['comment2']
            complaint_details = request.form['complaint_details']
            evidence = request.files.get('evidence')

            # Retrieve username from session
            username = session['username']

            # Handle file upload
            evidence_filename = None
            if evidence and allowed_file(evidence.filename):
                filename = secure_filename(evidence.filename)
                evidence_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                evidence.save(evidence_filename)
            elif evidence and evidence.filename != '':
                flash('Unsupported file type. Please upload valid audio, video, or image files.', 'danger')
                return redirect(request.url)

            # Insert complaint into the database using SQLAlchemy
            if complaint_type.strip().lower() == 'personal':
                # Directly insert into admin_complaints table for personal complaints
                new_complaint = AdminComplaint(
                    complaint_type=complaint_type,
                    faculty_name=faculty_name or 'N/A',
                    complaint_details=complaint_details,
                    evidence=evidence_filename
                )
                db.session.add(new_complaint)
                db.session.commit()

            else:
                # Insert into complaints table for other types of complaints
                new_complaint = Complaint(
                    username=username,
                    complaint_type=complaint_type,
                    category=category,
                    faculty_name=faculty_name,
                    complaint_details=complaint_details,
                    evidence=evidence_filename
                )
                db.session.add(new_complaint)
                db.session.commit()

                # Additional logic for faculty or admin complaints
                if category.strip().lower() == 'faculty':
                    new_faculty_complaint = FacultyComplaint(
                        username=username,
                        complaint_type=complaint_type,
                        faculty_name=faculty_name,
                        complaint_details=complaint_details,
                        evidence=evidence_filename
                    )
                    db.session.add(new_faculty_complaint)
                    db.session.commit()

                elif category.strip().lower() == 'admins':
                    new_admin_complaint = AdminComplaint(
                        complaint_type=complaint_type,
                        faculty_name=faculty_name or 'N/A',
                        complaint_details=complaint_details,
                        evidence=evidence_filename
                    )
                    db.session.add(new_admin_complaint)
                    db.session.commit()

                    # Send email notification to admin
                    send_complaint_email(complaint_type, faculty_name, complaint_details, evidence_filename)

            flash('Complaint submitted successfully!', 'success')
            return redirect(url_for('view_complaints'))

        except Exception as e:
            flash(f'Error: {e}', 'danger')

    return render_template('lodge_complaint.html')

def send_complaint_email(complaint_type, faculty_name, complaint_details, evidence_filename):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    # Email configuration
    smtp_server = "smtp.gmail.com"  # Update as per your email provider
    smtp_port = 587
    sender_email = "yenapoyayenapoya@gmail.com"  # Replace with your email
    sender_password = "sfai iqpi yiav hvfn"  # Replace with your email password
    receiver_email = "adithya.regunath@gmail.com"  # Replace with the recipient's email

    # Create email message
    subject = "New Complaint Submission"
    body = f"""
    Dear Admin,

    A new complaint has been submitted. Below are the details:

    Complaint Type: {complaint_type}
    Faculty Name: {faculty_name}
    Complaint Details: {complaint_details}

    Evidence: {evidence_filename if evidence_filename else 'No evidence provided'}

    Please take appropriate action.

    Best regards,
    Automated System
    """

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Sending the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


import subprocess
from flask import flash, redirect, url_for

@app.route('/open_streamlit', methods=['POST'])
def open_streamlit():
    try:
        # Try to launch Streamlit in the background
        result = subprocess.Popen(
            ['streamlit', 'run', 'encrypt12.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        
        # Capture output and errors
        stdout, stderr = result.communicate()
        
        if result.returncode != 0:
            flash(f"Error launching Streamlit: {stderr.decode()}", 'danger')
        else:
            flash('Streamlit app is now running!', 'success')
    
    except Exception as e:
        flash(f'Error: {e}', 'danger')
    
    # Redirect or render the lodge_complaint page after launching Streamlit
    return redirect(url_for('lodge_complaint'))

@app.route('/open_streamlit1', methods=['POST'])
def open_streamlit1():
    try:
        # Try to launch Streamlit in the background
        result = subprocess.Popen(
            ['streamlit', 'run', 'decrypt12.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        
        # Capture output and errors
        stdout, stderr = result.communicate()
        
        if result.returncode != 0:
            flash(f"Error launching Streamlit: {stderr.decode()}", 'danger')
        else:
            flash('Streamlit app is now running!', 'success')
    
    except Exception as e:
        flash(f'Error: {e}', 'danger')
    
    # Redirect or render the admin dashboard page after launching Streamlit
    return redirect(url_for('admin_dashboard'))


@app.route('/poll_complaint')
def poll_complaint():
    # Get the complaint type from the query parameter
    complaint_type = request.args.get('complaint_type')

    # Fetch complaints of the selected type and their vote counts using SQLAlchemy
    complaints = Complaint.query.filter_by(complaint_type=complaint_type).all()

    complaint_data = []
    for complaint in complaints:
        # Aggregate votes
        total_votes = len(complaint.votes)
        support_votes = sum(1 for vote in complaint.votes if vote.vote == 'support')
        
        support_percentage = (support_votes / total_votes * 100) if total_votes > 0 else 0
        
        complaint_data.append({
            "id": complaint.id,
            "details": complaint.details,
            "total_votes": total_votes,
            "support_votes": support_votes,
            "support_percentage": round(support_percentage, 2)
        })

    return render_template('poll_complaint.html', complaints=complaint_data, complaint_type=complaint_type)


@app.route('/submit_poll', methods=['POST'])
def submit_poll():
    try:
        # Loop through each vote
        for complaint_id in request.form:
            support_value = request.form[complaint_id]
            # Insert vote into PollVote table
            poll_vote = PollVote(complaint_id=complaint_id.split('_')[1], vote=support_value)  # Extract complaint_id
            db.session.add(poll_vote)

        db.session.commit()
        flash('Your votes have been submitted!', 'success')

    except Exception as e:
        db.session.rollback()
        flash(f"An error occurred: {e}", 'danger')

    return redirect(url_for('student_dashboard'))  # Redirect back to dashboard after voting

@app.route('/view_complaints', methods=['GET', 'POST'])
def view_complaints():
    complaints = Complaint.query.all()

    if request.method == 'POST':
        try:
            for complaint in complaints:
                complaint_id = complaint.id
                vote = request.form.get(f'vote_{complaint_id}')

                if vote:
                    # Insert the vote into the PollVote table
                    poll_vote = PollVote(complaint_id=complaint_id, vote=vote)
                    db.session.add(poll_vote)

            db.session.commit()
            flash('Your vote has been submitted!', 'success')

        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred: {e}", 'danger')

        return redirect(url_for('view_vote_status'))

    return render_template('view_complaint.html', complaints=complaints)


@app.route('/view_vote_status', methods=['GET'])
def view_vote_status():
    try:
        # Using SQLAlchemy to query and calculate the votes and support percentage
        complaints_with_support = db.session.query(
            Complaint.id,
            Complaint.complaint_type,
            Complaint.complaint_details,
            db.func.sum(db.case([(PollVote.vote == 'support', 1)], else_=0)).label('support_count'),
            db.func.count(PollVote.id).label('total_votes')
        ).outerjoin(PollVote, Complaint.id == PollVote.complaint_id) \
         .group_by(Complaint.id) \
         .all()

        return render_template('view_vote_status.html', complaints_with_support=complaints_with_support)

    except Exception as e:
        flash(f"An error occurred: {e}", 'danger')
        return redirect(url_for('student_dashboard'))


@app.route('/track', methods=['GET'])
def track_complaints():
    try:
        # Fetch all admin complaints
        admin_complaints = AdminComplaint.query.all()

        # Fetch all faculty complaints
        faculty_complaints = FacultyComplaint.query.all()

        # Pass both data sets to the template
        return render_template(
            'track_complaints.html',
            complaints=admin_complaints,
            faculty_complaints=faculty_complaints
        )

    except Exception as e:
        flash(f"An error occurred: {e}", 'danger')
        return "An error occurred while fetching complaints."







@app.route('/complaint', methods=['GET'])
def complaint_history():
    try:
        # Fetch complaints from the Complaint model
        complaints = Complaint.query.all()

        return render_template('complaint_history.html', complaints=complaints)

    except Exception as e:
        flash(f"An error occurred: {e}", 'danger')
        return render_template('complaint_history.html', complaints=[])

@app.route('/update_complaint_status', methods=['POST'])
def update_complaint_status():
    complaint_id = request.form.get('complaint_id')
    status = request.form.get('status')

    try:
        # Fetch the complaint by ID and update the status
        complaint = FacultyComplaint.query.get(complaint_id)
        
        if complaint:
            complaint.status = status
            db.session.commit()

            # Return a success response with the updated status
            return jsonify({'success': True, 'status': status})
        else:
            return jsonify({'success': False, 'message': 'Complaint not found.'})

    except Exception as e:
        # Log the error for debugging
        return jsonify({'success': False, 'message': str(e)})



@app.route('/update_complaint_status1', methods=['POST'])
def update_complaint_status1():
    complaint_id = request.form.get('complaint_id')
    status = request.form.get('status')

    try:
        # Fetch the complaint by ID and update the status
        complaint = AdminComplaint.query.get(complaint_id)
        
        if complaint:
            complaint.status = status
            db.session.commit()

            return jsonify({'success': True, 'status': status})
        else:
            return jsonify({'success': False, 'message': 'Complaint not found.'})

    except Exception as e:
        # Log the error for debugging
        return jsonify({'success': False, 'message': str(e)})


 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
