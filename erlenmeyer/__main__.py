from app import app
app.template_folder = 'erlenmeyer/templates'
app.run(debug=app.config['DEBUG'])
