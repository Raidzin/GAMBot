from modules.db.models import Base, engine

Base.metadata.create_all(engine)
print('База данных успешно записана!')
