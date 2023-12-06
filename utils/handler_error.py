from flask import render_template

class HandlerError:
    def not_found_error(self, error):
        return render_template('errors/404.html'), 404

    def internal_error(self, error):
        return render_template('errors/500.html'), 500
