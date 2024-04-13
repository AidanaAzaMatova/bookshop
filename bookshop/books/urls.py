from django.urls import path
from .views import BookListCreate, BookRetrieveUpdateDelete, ProfileListCreate, ProfileRetrieveUpdateDelete, ProfileVisibleFalse, ProfileVisibleTrue

urlpatterns = [
    path('books', BookListCreate.as_view(), name="Create-Book-List"),
    path('profiles', ProfileListCreate.as_view(), name="Create-Profile-List"),
    path('profile/visible/false', ProfileVisibleFalse.as_view(), name="Visible-Profile-List"),
    path('profile/visible/true', ProfileVisibleTrue.as_view(), name="Visible-Profile-List"),
    path('book/<int:pk>/', BookRetrieveUpdateDelete.as_view(), name="books-Details"),
    path('profile/<int:pk>/', ProfileRetrieveUpdateDelete.as_view(), name="profiles-Details")
]