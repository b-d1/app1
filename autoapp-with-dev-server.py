# -*- coding: utf-8 -*-
"""Create an application instance."""
from app1.app import create_app

app = create_app()
app.run(host='0.0.0.0', port=5000)
