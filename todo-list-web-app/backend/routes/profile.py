from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user, logout_user
from backend.models import db

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@profile_bp.route('/logout_profile')  # Rename to avoid route conflict
@login_required
def logout_profile():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('index.home'))