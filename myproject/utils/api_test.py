import requests
from django.http import JsonResponse

def make_get_request(request):
    # Buat permintaan GET ke URL yang ditentukan
    url = 'https://api.publicapis.org/entries'
    response = requests.get(url)

    # Periksa apakah permintaan berhasil
    if response.status_code == 200:
        # Jika berhasil, tampilkan respons JSON
        return JsonResponse(response.json())
    else:
        # Jika gagal, tampilkan pesan kesalahan
        return JsonResponse({'error': 'Failed to make GET request'}, status=500)
