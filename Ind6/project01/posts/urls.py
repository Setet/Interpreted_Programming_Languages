from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('getInfo', views.getInfo),
    path('InsertFolder/insert_author', views.insertAuthor),
    path('InsertFolder/insert_picture', views.insertPicture),
    path('InsertFolder/insert_gallery', views.insertGallery ),

    path('EditFolder/edit_author/', views.editAuthor),
    path('EditFolder/edit_author/deleteAuthor/<int:id_del>/', views.deleteAuthor),
    path('EditFolder/edit_author/editAuthor/<int:id_del>/', views.editAuthorF),
    
    path('EditFolder/edit_picture/', views.editPicture),
    path('EditFolder/edit_picture/deletePicture/<int:id_pic>/', views.deletePicture),
    path('EditFolder/edit_picture/editPicture/<int:id_pic>/', views.editPicturebt),

    path('EditFolder/edit_gallery/', views.editGallery),
    path('EditFolder/edit_gallery/deleteGallery/<int:id_gal>/', views.deleteGallery),
    path('EditFolder/edit_gallery/editGallery/<int:id_gal>/', views.editGalleryt),
]
