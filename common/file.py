from common.string import String

class File:
    def migration(self, class_name):
        table = String(class_name).transform_class_name()
        return f"""
from config.config import Config

class {class_name}:
    def __init__(self):
        self.connection = Config().get_connection()
        self.cursor = self.connection.cursor()
        self.table = '{table}'
    
    def up(self):
        query = f'''CREATE TABLE {{self.table}} (
          id INT AUTO_INCREMENT PRIMARY KEY
        )'''
        self.cursor.execute(query)
        self.connection.commit()
        print(f"Table {{self.table}} created")
    
    def down(self):
        query = f"DROP TABLE {{self.table}}"
        self.cursor.execute(query)
        self.connection.commit()
        print(f"Table {{self.table}} dropped")
    
    def __del__(self):
        Config().close_connection()
"""

    def seeder(self, class_name):
        table = String(class_name).transform_class_name()
        return f"""
from config.config import Config

class {class_name}:
    def __init__(self):
        self.connection = Config().get_connection()
        self.cursor = self.connection.cursor()
        self.table = '{table}'
    
    def run(self):
        data = {{ 
            'id': 1,
         }}
        query = f"INSERT INTO {{self.table}} ({{', '.join(data.keys())}}) VALUES ({{', '.join(data.values())}})"
        self.cursor.execute(query)
        self.connection.commit()
        print(f"Seeder {{self.table}} created")
    
    def __del__(self):
        Config().close_connection()
"""

    def model(self, class_name):
        table = String(class_name).transform_class_name()
        return f"""
from config.config import Config

class {class_name}:
    def __init__(self):
        self.connection = Config().get_connection()
        self.cursor = self.connection.cursor()
        self.table = '{table}'
        self.column_names = []
    
    def findAll(self, data):
        column = ', '.join(data) if data else '*'
        query = f"SELECT {{column}} FROM {{self.table}}"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def findById(self, id, data):
        column = ', '.join(data) if data else '*'
        query = f"SELECT {{column}} FROM {{self.table}} WHERE id = {{id}}"
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def create(self, data):
        query = f"INSERT INTO {{self.table}} ({{', '.join(data.keys())}}) VALUES ({{', '.join(data.values())}})"
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.lastrowid
    
    def update(self, id, data):
        query = f"UPDATE {{self.table}} SET {{', '.join([f'{{key}} = {{value}}' for key, value in data.items()])}} WHERE id = {{id}}"
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.rowcount
    
    def delete(self, id):
        query = f"DELETE FROM {{self.table}} WHERE id = {{id}}"
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.rowcount
    
    def __del__(self):
        Config().close_connection()
"""

    def controller(self, class_name, model_name, args=None):
        class_model = model_name
        module_model_name = String(model_name).camelcase_to_underscore()
        model_instance = String(model_name).lowercase_first_letter()
        route_name = String(model_name).transform_class_name()
        if args == 'y':
            return f"""
from flask import render_template, request, redirect, session, flash
import pandas as pd
import numpy as np
from app.models.{module_model_name} import {class_model}

class {class_name}:
    def __init__(self):
        self.{model_instance} = {class_model}()
    
    def index(self):
        try:
            data = {{ 
                'title': '{class_name}',
                'data': self.{model_instance}.findAll(),
             }}
            return render_template('pages/{route_name}/index.html', data=data)
        except Exception as e:
            return str(e)
    
    def create(self):
        try:
            return render_template('pages/{route_name}/create.html')
        except Exception as e:
            return str(e)
    
    def store(self):
        try:
            data = request.form.to_dict()
            self.{model_instance}.create(data)
            return redirect('/{route_name}')
        except Exception as e:
            return str(e)
    
    def show(self, id):
        try:
            data = self.{model_instance}.findById(id)
            return render_template('pages/{route_name}/show.html', data=data)
        except Exception as e:
            return str(e)

    def edit(self, id):
        try:
            data = self.{model_instance}.findById(id)
            return render_template('pages/{route_name}/edit.html', data=data)
        except Exception as e:
            return str(e)

    def update(self, id):
        try:
            data = request.form.to_dict()
            self.{model_instance}.update(id, data)
            return redirect('/{route_name}')
        except Exception as e:
            return str(e)
    
    def destroy(self, id):
        try:
            self.{model_instance}.delete(id)
            return redirect('/{route_name}')
        except Exception as e:
            return str(e)
"""
        else:
            return f"""
from flask import render_template, request, redirect, session, flash
import pandas as pd
import numpy as np
from app.models.{module_model_name} import {class_model}

class {class_name}:
    def __init__(self):
        self.{model_instance} = {class_model}()
    
"""

    