import pandas as pd
from django.core.management.base import BaseCommand
from stats.models import Circuit, Constructor, Driver, Standing
from datetime import datetime

class Command(BaseCommand):
    help = 'Cargar datos desde los archivos CSV a la base de datos'

    def handle(self, *args, **kwargs):
        path = 'C:\\Users\\fedef\\.cache\kagglehub\\datasets\\rohanrao\\formula-1-world-championship-1950-2020\\versions\\23\\'  # Ajusta esta ruta a la ubicación de tus CSV

        # Borrar datos actuales de la base de datos
        self.stdout.write('Borrando datos actuales...')
        Circuit.objects.all().delete()
        Constructor.objects.all().delete()
        Driver.objects.all().delete()
        Standing.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Datos borrados exitosamente.'))

        # Cargar datos de Circuitos
        self.stdout.write('Cargando datos de circuitos...')
        circuits_data = pd.read_csv(path + 'circuits.csv')
        for _, row in circuits_data.iterrows():
            circuit = Circuit.objects.create(
                name=row['name'],
                location=row['location'],
                country=row['country'],
                length_km=row.get('length_km', None)
            )
            self.stdout.write(f"Circuito {row['name']} creado.")

        # Cargar datos de Constructores
        self.stdout.write('Cargando datos de constructores...')
        constructors_data = pd.read_csv(path + 'constructors.csv')
        for _, row in constructors_data.iterrows():
            constructor = Constructor.objects.create(
                name=row['name'],
                nationality=row['nationality']
            )
            self.stdout.write(f"Constructor {row['name']} creado.")

        # Cargar datos de Pilotos
        self.stdout.write('Cargando datos de pilotos...')
        drivers_data = pd.read_csv(path + 'drivers.csv')
        for _, row in drivers_data.iterrows():
            date_of_birth = datetime.strptime(row['date_of_birth'], '%Y-%m-%d')
            driver = Driver.objects.create(
                name=row['name'],
                nationality=row['nationality'],
                date_of_birth=date_of_birth
            )
            self.stdout.write(f"Piloto {row['name']} creado.")

        # Cargar datos de Standings
        self.stdout.write('Cargando datos de standings...')
        standings_data = pd.read_csv(path + 'driver_standings.csv')
        for _, row in standings_data.iterrows():
            driver = Driver.objects.get(name=row['driver_name'])  # Asegúrate que el nombre coincida
            standing = Standing.objects.create(
                driver=driver,
                season=row['season'],
                points=row['points'],
                position=row['position']
            )
            self.stdout.write(f"Standing para {row['driver_name']} en la temporada {row['season']} creado.")

        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente.'))
