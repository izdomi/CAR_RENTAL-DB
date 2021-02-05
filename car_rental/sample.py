from sqlalchemy import func
from .db import Base, Session, engine, Location, Car, Client, Car_type,Reservation

def populate_db():
    Base.metadata.create_all()

    session = Session()

    existing_category_count = session.query(func.count(Client.id)).scalar()

    if existing_category_count > 0:
        return

    clients = [
        Client(first_name="John", last_name="Lennon",license_number="12340987", phone="098-23-54-654"),
        Client(first_name="Mark", last_name="Zukemberg", license_number="5678342134", phone="888-889-800"),
        Client(first_name="Arthur", last_name="Schopenhauer", license_number="0983657313", phone="290-098-789"),
        Client(first_name="Sigmund", last_name="Freud", license_number="8764589809", phone="904-890-888"),
        Client(first_name="Bill", last_name="Gates", license_number="9043876572", phone="657-890-098"),
        Client(first_name="Bill", last_name="Clinton", license_number="8974658909", phone="094-987-789"),
        Client(first_name="Billie", last_name="Eilish", license_number="9087654678", phone="789-098-677"),
        Client(first_name="Bruno", last_name="Mars", license_number="2456980978", phone="080-098-321"),
        Client(first_name="Adriano", last_name="Celentano", license_number="9076325632", phone="908-908-789"),
        Client(first_name="Edith", last_name="Piaf", license_number="0912679854", phone="099-800-766"),
        Client(first_name="Alessandro", last_name="Botticeli", license_number="9809321475", phone="456-899-098"),
        Client(first_name="John", last_name="Johnson", license_number="7654890954", phone="890-098-765"),
        Client(first_name="George", last_name="Bush", license_number="9087213356", phone="234-564=321"),
        Client(first_name="Caterina", last_name="Firenze", license_number="9876902134", phone="290-098-789"),
        Client(first_name="Ismail", last_name="Kadare", license_number="8976523332", phone="988-098-345")
    ]
    session.add_all(clients)

    reservation = [
        Reservation(amount=5900, pickup_date='2021-08-17', return_date='2021-10-26',return_location_id="tirane"),
        Reservation(amount=4000, pickup_date='2021-10-10', return_date='2021-12-18', return_location_id="shkoder"),
        Reservation(amount=8900, pickup_date='2021-11-06', return_date='2021-12-25', return_location_id="kukes"),
        Reservation(amount=7900, pickup_date='2021-01-08', return_date='2021-04-04', return_location_id="korce"),
        Reservation(amount=5500, pickup_date='2021-03-06', return_date='2021-07-09', return_location_id="elbasan"),
        Reservation(amount=10000, pickup_date='2021-08-19', return_date='2021-09-30', return_location_id="milano"),
        Reservation(amount=6700, pickup_date='2021-06-06', return_date='2021-06-23', return_location_id="firenze"),
        Reservation(amount=8700, pickup_date='2021-07-23', return_date='2021-10-22', return_location_id="sarande"),
        Reservation(amount=9700, pickup_date='2021-05-09', return_date='2021-06-22', return_location_id="vlore"),
        Reservation(amount=5690, pickup_date='2021-07-06', return_date='2021-08-15', return_location_id="astir"),
        Reservation(amount=6000, pickup_date='2021-10-14', return_date='2021-12-29', return_location_id="21dhjetori"),
        Reservation(amount=6500, pickup_date='2021-05-01', return_date='2021-05-18', return_location_id="alidemi"),
        Reservation(amount=3500, pickup_date='2021-02-12', return_date='2021-04-16', return_location_id="tirane"),
        Reservation(amount=4450, pickup_date='2021-03-03', return_date='2021-04-20', return_location_id="durres")
    ]

    session.add_all(reservation)

    car = [
        Car(
            name="Mercedes-Benz",
            description="The Mercedes-Benz S-Class, formerly known as Sonderklasse (German for special class, abbreviated as S-Class), is a series of full-size luxury sedans, limousines and armored sedans produced by the German automaker Mercedes-Benz, a division of German company Daimler AG.",
            model="S-Class",
            year=2017,
            color="black",
            capacity=5,
            rate=4.7,
            currentlocation_id=1,
            car_type_id=2,
        ),
        Car(
            name="Audi",
            description="The Audi A6 is an executive car made by the German automaker Audi. ... All generations of the A6 have offered either front-wheel-drive or Torsen-based four-wheel-drive, marketed by Audi as their quattro system",
            model="A6",
            year=2012,
            color="white",
            capacity=5,
            rate=4.1,
            currentlocation_id=1,
            car_type_id=2,
        ),

        Car(
            name="BMW",
            description="The BMW 7 Series is a full-size luxury sedan produced by the German automaker BMW since 1977.",
            model="Series 7",
            year=2014,
            color="grey",
            capacity=5,
            rate=4.3,
            currentlocation_id=1,
            car_type_id=2,
        ),

        Car(
            name="Toyota",
            description="The Toyota RAV4 is a compact crossover SUV (sport utility vehicle) produced by the Japanese automobile manufacturer Toyota.",
            model="Rav4",
            year=2015,
            color="red",
            capacity=5,
            rate=4.3,
            currentlocation_id=2,
            car_type_id=1,
        ),

        Car(
            name="Hyundai",
            description="The 2018 Hyundai Tucson ranks near the top of the compact SUV class. It has a stellar predicted reliability rating, lots of available safety features, and a quiet cabin with plenty of space.",
            model="Tucson",
            year=2018,
            color="grey",
            capacity=5,
            rate=4.3,
            currentlocation_id=2,
            car_type_id=1,
        )
    ]

    session.add_all(car)

    session.commit()
