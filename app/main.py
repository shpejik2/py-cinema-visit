from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str
) -> None:
    clients = []
    for client in customers:
        clients.append(Customer(client["name"], client["food"]))
    cleaning_staff = Cleaner(cleaner)
    hall1 = CinemaHall(hall_number)
    for client in clients:
        CinemaBar.sell_product(client.food, client)
    hall1.movie_session(movie, clients, cleaning_staff)
