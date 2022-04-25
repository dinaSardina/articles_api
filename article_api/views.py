from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Article, User
from .serializers import ArticleSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .permissions import IsOwnerOrReadOnly, IsAuthorOrReadOnly


class ArticleView(CreateAPIView, ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        """
        This view return a list of all articles for authenticated users,
        and list of only public articles for any other users
        """
        if self.request.user.is_authenticated:
            return Article.objects.all()
        else:
            return Article.objects.filter(public=True)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class SingleArticleView(RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Article.objects.all()
        else:
            return Article.objects.filter(public=True)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

