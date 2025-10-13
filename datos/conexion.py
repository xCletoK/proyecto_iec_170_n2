from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# pip install sqalchemy
# pip install mysql-connector-python

# definir cadena de conexión
# mysql+mysqlconnector://usuario:contraseña@host:puerto/nombre_base_datos

DATABASE_URL = "mysql+mysqlconnector://root:@localhost:localhost/iec_170_n2"

motor_db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=motor_db)