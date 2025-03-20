from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # Temps d'attente entre les tâches (entre 1 et 3 secondes)
    wait_time = between(1, 3)

    @task(3)  # Cette tâche est exécutée 3 fois plus souvent que les autres
    def load_index(self):
        # Teste le temps de chargement de la page d'accueil
        with self.client.get("/", catch_response=True) as response:
            if response.elapsed.total_seconds() > 5:  # Temps maximal de 5 secondes
                response.failure("Temps de chargement de la page d'accueil trop long")
            else:
                response.success()

    @task(2)
    def show_summary(self):
        # Teste le temps de réponse de la route /showSummary
        email = "clubA@example.com"  # Remplacez par un email valide de votre clubs.json
        with self.client.post("/showSummary", data={"email": email}, catch_response=True) as response:
            if response.elapsed.total_seconds() > 2:  # Temps maximal de 2 secondes
                response.failure("Temps de réponse de /showSummary trop long")
            else:
                response.success()

    @task(1)
    def purchase_places(self):
        # Teste le temps de réponse de la route /purchasePlaces
        competition = "Competition 1"  # Remplacez par une compétition valide de competitions.json
        club = "Club A"  # Remplacez par un club valide de clubs.json
        places_required = 1  # Nombre de places à réserver

        with self.client.post(
            "/purchasePlaces",
            data={
                "competition": competition,
                "club": club,
                "places": places_required,
            },
            catch_response=True,
        ) as response:
            if response.elapsed.total_seconds() > 2:  # Temps maximal de 2 secondes
                response.failure("Temps de réponse de /purchasePlaces trop long")
            else:
                response.success()