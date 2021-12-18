from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('lang', views.lang_list),
    path('lang/create', views.LanguageCreate.as_view()),
    path('class/<int:id>/update', views.LanguageUpdate.as_view(), name='lang_update'),
    path('class/<int:id>/delete', views.LanguageDelete.as_view(), name='lang_delete'),
    path('library', views.library_list),
    path('library/create', views.LibraryCreate.as_view()),
    path('library/<int:id>/update', views.LibraryUpdate.as_view(), name='library_update'),
    path('library/<int:id>/delete', views.LibraryDelete.as_view(), name='library_delete'),
    path('report', views.report)
]