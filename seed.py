import pandas as pd
from database import SessionLocal, engine, Base
from models import Stable

Base.metadata.create_all(bind=engine)

df = pd.read_csv("stables.csv", encoding="utf-8").fillna("")

db = SessionLocal()
db.query(Stable).delete()

for _, row in df.iterrows():
    db.add(Stable(
        name=row["name"],
        address=row["address"],
        lat=float(row["lat"]),
        lon=float(row["lon"]),
        price_board=int(row["price_board"] or 0),
        price_training=int(row["price_training"] or 0),
        discipline=row["discipline"],
        description=row["description"],
        contact=row["contact"],
        has_warm_wash=str(row["has_warm_wash"]).lower() in ["1", "true", "да"],
        has_summer_wash=str(row["has_summer_wash"]).lower() in ["1", "true", "да"],
        has_summer_stables=str(row["has_summer_stables"]).lower() in ["1", "true", "да"],
        has_solarium=str(row["has_solarium"]).lower() in ["1", "true", "да"],
        has_indoor_arena=str(row["has_indoor_arena"]).lower() in ["1", "true", "да"],
        has_levalds=str(row["has_levalds"]).lower() in ["1", "true", "да"],
        has_vet=str(row["has_vet"]).lower() in ["1", "true", "да"],
    ))

db.commit()
db.close()
print(f"Загружено конюшен: {len(df)}")