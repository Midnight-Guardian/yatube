from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
urlpatterns = [

    path('', (views.PostsList.as_view()), name="index"),
    path('group/<slug>/', views.PostsList.as_view(), name="group_list"),
    path('new/', views.NewPost.as_view(), name="new_post"),
    path('<str:username>/', views.Profile.as_view(), name='profile'),
    path("<username>/<int:post_id>/comment", views.AddComment.as_view(), name="add_comment"),
]

urlpatterns += [
    path('<str:username>/<int:post_id>/', views.Post_View.as_view(), name='post'),
    path(
    '<str:username>/<int:post_id>/edit/',
    views.Post_Edit.as_view(),
    name='post_edit'
),
    ]