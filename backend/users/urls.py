from django.urls import include, path, re_path
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView, UserDetailsView
from users.views import *

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),    
    path('auth/register/', include('dj_rest_auth.registration.urls')),
    path('registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view(),), # Needs to be defined before the registration path
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('delete/user', RemoveUserView.as_view(), name='remove_user'), # redundant if we use HTTP method on /auth/user?


    # Parking Spaces
    
    path('provider/parking', CreateParkingSpace.as_view(), name='create_parking_space'),
    path('provider/parking/<int:parkingID>', ParkingSpaceView.as_view(), name='modify_parking_space'),
    path('provider/parking/images/<int:parkingID>', ImageList.as_view(), name='list_images'),
    path('provider/parking/reviews/<int:parkingID>', ReviewList.as_view(), name='list_reviews'),
    path('provider/parking/favourites/<int:parkingID>', FavouriteList.as_view(), name='list_favourites'),
    path('provider/parking/bookings/<int:parkingID>', BookingList.as_view(), name='list_bookings'),
    path('provider/parking/all', ParkingSpaceList.as_view(), name='list_parking_space'),

    # Booking

    path('consumer/book', CreateBooking.as_view(), name='create_booking'),
    path('consumer/book/<int:bookingID>', BookingView.as_view(), name='modify_booking'),

    #History

    path('provider/history', ProviderBookingHistory.as_view(), name='provider_history'),
    path('consumer/history', ConsumerBookingHistory.as_view(), name='consumer_history'),

    # Images 

    path('provider/image/<int:parkingID>', CreateImage.as_view(), name='create_image'),
    path('provider/image/<int:imgID>', ImageView.as_view(), name='modify_image'),
    

    # Reviews

    path('consumer/review', CreateReview.as_view(), name='create_review'),
    path('consumer/review/<int:reviewID>', ReviewView.as_view(), name='modify_review'),
 

    # Favourites

    path('consumer/favourite', CreateFavourite.as_view(), name='create_favourite'),
    path('consumer/favourite/<int:favID>', FavouriteView.as_view(), name='modify_favourite'),

    # Vehicle

    path('consumer/vehicle', CreateVehicle.as_view(), name='create_vehicle'),
    path('consumer/vehicle/<int:vehicleID>', VehicleView.as_view(), name='modify_vehicle'),
    path('consumer/vehicle/all', VehicleList.as_view(), name='list_vehicle'),


]