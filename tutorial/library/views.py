from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Client, Book
from django.http import HttpResponse
import json
class books_views(View):
    def get(self, request):
        id_book_query = request.GET.get('id_book')
        if id_book_query:
            
            book_object = get_object_or_404(Book, id_book=request.GET.get('id_book'))
            data = {
            'id_book': book_object.id_book,
            'book_name': book_object.book_name,
            'id_user': book_object.id_user
        }
        else:
            book_all = Book.objects.all()
            data = []
            for book in book_all:
                data.append({
                    'id_book': book.id_book,
                    'book_name': book.book_name,
                    'id_user': book.id_user
                })
    # Converter o objeto JSON em uma string
        json_data = json.dumps(data)
    # Definir o tipo de resposta como application/json
        response = HttpResponse(json_data, content_type='application/json')
        return response
    def post(self, request):
        json_data = json.loads(request.body)
        book = Book()
        book.book_name = json_data.get('book_name')
        book.save()
        return HttpResponse("Livro salvo com sucesso!")
        
# Create your views here.
