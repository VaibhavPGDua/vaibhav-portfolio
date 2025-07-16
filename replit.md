# Vaibhav Dua Portfolio Website

## Overview

This is a personal portfolio website for Vaibhav Dua, a Data & Business Analyst. The application is built using Flask (Python web framework) with PostgreSQL database integration and features a modern, responsive design showcasing skills, projects, and contact information. The website includes a contact form with database storage and email functionality powered by Flask-Mail.

## User Preferences

Preferred communication style: Simple, everyday language.

## Recent Changes (Updated: July 16, 2025)

✓ Integrated PostgreSQL database for contact message storage
✓ Added real profile picture (profile.jpg) replacing placeholder SVG
✓ Removed phone number from contact information
✓ Updated education section to show BCA degree as completed
✓ Enhanced animations with smoother transitions and better performance
✓ Added admin panel (/admin/messages) to view and manage contact messages
✓ Improved profile image styling with better object-fit and hover effects
✓ Reverted from overly advanced presentation back to modest, authentic representation
✓ Removed certifications section and advanced analytics claims
✓ Restored original projects (Blinkit Dashboard, Sales Forecasting) with realistic metrics
✓ Adjusted skill levels to reflect actual experience as a fresher analyst
✓ Maintained professional design while keeping claims authentic and achievable

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 (Flask's default templating engine)
- **Styling Framework**: Bootstrap 5.3.0 for responsive design
- **CSS Architecture**: Custom CSS with CSS variables for consistent theming
- **JavaScript**: Vanilla JavaScript for interactive components including:
  - Navigation scroll effects
  - Smooth scrolling
  - Skill bar animations
  - Typewriter effects
  - Contact form handling

### Backend Architecture
- **Web Framework**: Flask (Python micro-framework)
- **Application Structure**: Single-file Flask application (app.py) with a separate entry point (main.py)
- **Email Service**: Flask-Mail integration with Gmail SMTP for contact form functionality
- **Session Management**: Flask's built-in session handling with secret key configuration

## Key Components

### 1. Main Application (app.py)
- Flask application initialization and configuration
- Email configuration for Gmail SMTP
- Route handlers for main page and contact form
- Error handling and form validation

### 2. Templates
- **index.html**: Main portfolio page with sections for:
  - Hero/landing section
  - About section
  - Projects showcase
  - Skills display
  - Contact form

### 3. Static Assets
- **CSS**: Custom styling with modern design patterns, CSS variables, and responsive layouts
- **JavaScript**: Interactive functionality for enhanced user experience

### 4. Email Integration
- Gmail SMTP configuration for sending contact form submissions
- Environment variable-based configuration for security

## Data Flow

1. **User Visit**: User accesses the main route ('/') which renders the index.html template
2. **Contact Form Submission**: 
   - User fills out contact form and submits via POST to '/contact'
   - Server validates form data
   - Email is composed and sent via Flask-Mail to the portfolio owner
   - User receives feedback via flash messages
   - User is redirected back to the contact section

## External Dependencies

### Python Packages
- **Flask**: Core web framework
- **Flask-Mail**: Email sending functionality

### Frontend Libraries
- **Bootstrap 5.3.0**: CSS framework for responsive design
- **Font Awesome 6.4.0**: Icon library
- **Google Fonts (Inter)**: Typography

### External Services
- **Gmail SMTP**: Email delivery service for contact form

## Environment Configuration

The application requires the following environment variables:
- `SESSION_SECRET`: Flask session secret key (falls back to dev key)
- `MAIL_USERNAME`: Gmail username for SMTP authentication
- `MAIL_PASSWORD`: Gmail app password for SMTP authentication

## Deployment Strategy

### Development
- Application runs on localhost:5000 with debug mode enabled
- Uses main.py as entry point for development server

### Production Considerations
- Environment variables must be properly configured
- Debug mode should be disabled
- Session secret should use a secure random key
- Email credentials should be stored securely

### Server Configuration
- Application is configured to bind to all interfaces (0.0.0.0)
- Port 5000 is the default serving port
- Static files are served by Flask (suitable for small-scale deployment)

## Security Features

- Form validation to prevent empty submissions
- Environment variable-based configuration for sensitive data
- Flash messaging for user feedback
- CSRF protection through Flask's built-in mechanisms

## Responsive Design

The website implements a mobile-first responsive design approach:
- Bootstrap grid system for layout
- Custom CSS media queries for fine-tuned responsiveness
- Mobile-friendly navigation with collapsible menu
- Optimized typography and spacing for different screen sizes