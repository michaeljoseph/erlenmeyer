from app import app
app.template_folder = 'drain/templates'
app.run(debug=app.config['DEBUG'])
