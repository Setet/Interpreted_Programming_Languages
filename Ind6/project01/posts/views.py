from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound

# Create your views here.
from .forms import AuthorForm, PictureForm, GalleryForm
from .models import Picture, Author, Gallery


def index(request):
    return render(request, 'index.html')


def getInfo(request):
    dataPicture = Picture.picture_obj.order_by('id')
    dataAuthor = Author.author_obj.order_by('id')
    dataGallery = Gallery.gallery_obj.order_by('id')
    return render(request, 'getInfo.html',
                  {'dataPicture': dataPicture, 'dataAuthor': dataAuthor, 'dataGallery': dataGallery})


def insertAuthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            aut = Author()
            aut.first_name = request.POST.get("first_name")
            aut.second_name = request.POST.get("second_name")
            aut.pseudonym = request.POST.get("pseudonym")
            aut.date_birth = request.POST.get("date_birth")
            aut.save()
        return redirect('home')
    form = AuthorForm()
    dataAuthor = Author.author_obj.all()
    return render(request, 'InsertFolder/insert_author.html',
                  {'title': 'Add New Author', 'dataAuthor': dataAuthor, 'form': form})


def insertGallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST)
        if form.is_valid():
            gal = Gallery()
            gal.name = request.POST.get("name")
            gal.address = request.POST.get("address")
            gal.save()
        return redirect('home')
    form = GalleryForm()
    dataGallery = Gallery.gallery_obj.all()
    return render(request, 'InsertFolder/insert_gallery.html',
                  {'title': 'Add New Gallery', 'dataGallery': dataGallery, 'form': form})


def insertPicture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            picture = Picture()
            picture.name = request.POST.get("name")
            picture.id_author = Author.author_obj.get(pk=request.POST.get("id_author"))
            picture.genre = request.POST.get("genre")
            picture.id_gallery = Gallery.gallery_obj.get(pk=request.POST.get("id_gallery"))
            picture.timestamp = request.POST.get("timestamp")
            picture.save()
        return redirect('home')
    form = PictureForm()
    dataPicture = Picture.picture_obj.all()
    return render(request, 'InsertFolder/insert_picture.html',
                  {'title': 'Add New Picture', 'dataPicture': dataPicture, 'form': form})


def deleteAuthor(reqiest, id_del):
    try:
        aut = Author.author_obj.get(pk=id_del)
        aut.delete()

        return HttpResponseRedirect("/EditFolder/edit_author")
    except Author.author_obj.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")


def editAuthor(request):
    dataAuthor = Author.author_obj.order_by('id')
    return render(request, 'EditFolder/author.html', {'dataAuthor': dataAuthor})


def editAuthorF(request, id_del):
    try:
        aut = Author.author_obj.get(pk=id_del)

        if request.method == "POST":
            aut.first_name = request.POST.get("first_name")
            aut.second_name = request.POST.get("second_name")
            aut.pseudonym = request.POST.get("pseudonym")
            aut.date_birth = request.POST.get("date_birth")
            aut.save()
            return HttpResponseRedirect("/EditFolder/edit_author")
        else:
            return render(request, "EditFolder/edit_author.html", {'dataAut': aut})
    except Author.author_obj.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")


def deletePicture(request, id_pic):
    try:
        picture = Picture.picture_obj.get(pk=id_pic)
        picture.delete()
        return HttpResponseRedirect("/EditFolder/edit_picture")
    except Picture.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")


def editPicture(request):
    dataPicture = Picture.picture_obj.order_by('id')
    return render(request, 'EditFolder/picture.html', {'dataPicture': dataPicture})


def editPicturebt(request, id_pic):
    try:
        picture = Picture.picture_obj.get(pk=id_pic)

        if request.method == "POST":
            picture.name = request.POST.get("name")
            picture.id_author = Author.author_obj.get(pseudonym=request.POST.get("id_author"))
            picture.genre = request.POST.get("genre")
            picture.timestamp = request.POST.get("timestamp")
            picture.save()
            return HttpResponseRedirect("/EditFolder/edit_picture")
        else:
            dataAuthor = Author.author_obj.all()
            dataGallery = Gallery.gallery_obj.all()
            return render(request, "EditFolder/edit_picture.html",
                          {'dataAuthor': dataAuthor, 'dataGallery': dataGallery, 'dataPicture': picture})
    except Picture.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")


def deleteGallery(request, id_gal):
    try:
        gal = Gallery.gallery_obj.get(pk=id_gal)
        gal.delete()
        return HttpResponseRedirect("/EditFolder/edit_gallery")
    except Gallery.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")


def editGallery(request):
    dataGallery = Gallery.gallery_obj.order_by('id')
    return render(request, 'EditFolder/gallery.html', {'dataGallery': dataGallery})


def editGalleryt(request, id_gal):
    try:
        gal = Gallery.gallery_obj.get(pk=id_gal)

        if request.method == "POST":
            gal.name = request.POST.get("name")
            gal.address = request.POST.get("address")
            gal.save()
            return HttpResponseRedirect("/EditFolder/edit_gallery")
        else:
            return render(request, "EditFolder/edit_gallery.html", {'dataGallery': gal})
    except Gallery.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")
