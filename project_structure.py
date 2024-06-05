import os

# List of folders to be created
folders = [
    "todo-list-web-app/backend",
    "todo-list-web-app/backend/templates",
    "todo-list-web-app/backend/templates/partials",
    "todo-list-web-app/backend/static",
    "todo-list-web-app/backend/static/css",
    "todo-list-web-app/backend/static/js",
    "todo-list-web-app/backend/static/img",
    "todo-list-web-app/backend/static/vendor",
    "todo-list-web-app/backend/static/vendor/bootstrap/css",
    "todo-list-web-app/backend/static/vendor/bootstrap/js",
    "todo-list-web-app/backend/static/vendor/chart.js",
    "todo-list-web-app/frontend",
    "todo-list-web-app/frontend/public",
    "todo-list-web-app/frontend/src",
    "todo-list-web-app/frontend/src/components",
    "todo-list-web-app/db"
]

# List of files to be created
files = [
    "todo-list-web-app/backend/__init__.py",
    "todo-list-web-app/backend/config.py",
    "todo-list-web-app/backend/models.py",
    "todo-list-web-app/backend/routes.py",
    "todo-list-web-app/backend/templates/index.html",
    "todo-list-web-app/backend/templates/login.html",
    "todo-list-web-app/backend/templates/register.html",
    "todo-list-web-app/backend/templates/profile.html",
    "todo-list-web-app/backend/templates/tasks.html",
    "todo-list-web-app/backend/templates/base.html",
    "todo-list-web-app/backend/templates/partials/header.html",
    "todo-list-web-app/backend/templates/partials/footer.html",
    "todo-list-web-app/backend/static/css/style.css",
    "todo-list-web-app/backend/static/js/script.js",
    "todo-list-web-app/backend/static/img/logo.png",
    "todo-list-web-app/backend/static/vendor/bootstrap/css/bootstrap.min.css",
    "todo-list-web-app/backend/static/vendor/bootstrap/js/bootstrap.bundle.min.js",
    "todo-list-web-app/backend/static/vendor/bootstrap/js/bootstrap.min.js",
    "todo-list-web-app/backend/static/vendor/bootstrap/js/popper.min.js",
    "todo-list-web-app/backend/static/vendor/chart.js/Chart.min.js",
    "todo-list-web-app/backend/static/vendor/chart.js/Chart.bundle.min.js",
    "todo-list-web-app/backend/static/vendor/chart.js/Chart.min.js.map",
    "todo-list-web-app/frontend/public/index.html",
    "todo-list-web-app/frontend/public/favicon.ico",
    "todo-list-web-app/frontend/public/manifest.json",
    "todo-list-web-app/frontend/public/robots.txt",
    "todo-list-web-app/frontend/src/App.css",
    "todo-list-web-app/frontend/src/App.js",
    "todo-list-web-app/frontend/src/index.css",
    "todo-list-web-app/frontend/src/index.js",
    "todo-list-web-app/frontend/src/logo.svg",
    "todo-list-web-app/frontend/src/components/TaskList.js",
    "todo-list-web-app/frontend/src/components/TaskItem.js",
    "todo-list-web-app/frontend/src/components/AddTaskForm.js",
    "todo-list-web-app/frontend/src/components/Navbar.js",
    "todo-list-web-app/frontend/src/components/Footer.js",
    "todo-list-web-app/db/schema.sql",
    "todo-list-web-app/.gitignore",
    "todo-list-web-app/requirements.txt",
    "todo-list-web-app/README.md"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file in files:
    with open(file, 'w') as f:
        pass

print("Folder structure created successfully.")
