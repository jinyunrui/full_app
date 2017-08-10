from app import db

class FileNames(db.Model):

    __tablename__ = 'image_to_text'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String)
    
    def __init__(self, filename):
        self.filename = filename
        
