from django.contrib import admin
from django.urls import path
from adherents.views import index, list_adherents, send_notification_email, enregistrer_presences, list_presences, save_selected_adherents, update_presence
from adherents.views import LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/adherents/', list_adherents, name='list_adherents'),
    path('api/adherents/<int:adherent_id>/send_notification/', send_notification_email, name='send_notification_email'),
    path('api/presences/', enregistrer_presences, name='enregistrer_presences'),
    path('api/presences/list/', list_presences, name='list_presences'),
    path('api/save-selected-adherents/', save_selected_adherents, name='save_selected_adherents'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/adherents/<int:adherent_id>/', update_presence, name='update_presence'),  # Correction ici
]
