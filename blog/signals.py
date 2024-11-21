from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Reclamation
import json
from datetime import datetime

def update_reclamations_json():
    """ Helper function to update the reclamations.json file. """
    # Get all reclamations
    reclamations = Reclamation.objects.all()

    # Convert them to a list of dictionaries (this excludes fields like 'id', etc.)
    reclamations_list = list(reclamations.values())

    # Convert datetime fields to string format to avoid JSON serialization errors
    for reclamation in reclamations_list:
        if 'created_date' in reclamation:
            reclamation['created_date'] = reclamation['created_date'].strftime('%Y-%m-%d %H:%M:%S')
        if 'published_date' in reclamation:
            reclamation['published_date'] = reclamation['published_date'].strftime('%Y-%m-%d %H:%M:%S')

    # Save the data to a JSON file
    with open('reclamations.json', 'w') as json_file:
        json.dump(reclamations_list, json_file, indent=4)


@receiver(post_save, sender=Reclamation)
def save_reclamations_to_json(sender, instance, created, **kwargs):
    """ Save or update reclamations in the JSON file when a reclamation is created or updated. """
    update_reclamations_json()


@receiver(post_delete, sender=Reclamation)
def delete_reclamation_from_json(sender, instance, **kwargs):
    """ Remove the deleted reclamation from the JSON file. """
    update_reclamations_json()
