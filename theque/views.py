from django.shortcuts import render, get_object_or_404, redirect
from .models import Book,Comment
from .forms import CommentForm

# Create your views here.
def index(request):
    return render(request, 'theque/index.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'theque/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    rating_list = range(book.rating)
    comments = book.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = CommentForm()
    return render(request, 'theque/book_detail.html', {'book': book, 'rating_list': rating_list, 'comments': comments, 'form': form})
