from django.conf.urls import url

from . import views


urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^books/$',views.BookListView.as_view(), name = 'books'),
               url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
			   url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
			   ]
urlpatterns += [   
    url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [  
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]