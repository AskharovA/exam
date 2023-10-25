from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path('update_post/<int:post_id>', views.update_post, name='update_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('api_page/', views.api_page, name='api_page'),
    path('about/', views.about, name='about'),
    path('<slug:category_slug>/', views.post_list, name='select_category'),
    path('tag/<slug:tag_slug>/', views.post_list, name='posts_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('', views.post_list, name='post_list'),
]
