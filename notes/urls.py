from django.urls import path

from .views import Notes, Each_Note, Add_Note

app_name = "notes"
urlpatterns = [
    path('', Notes.as_view(), name="all_notes"),
    path('note/<int:pk>', Each_Note.as_view(), name="note"),
    path('add', Add_Note.as_view(), name="add"),
]
