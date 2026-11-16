from django.shortcuts import render

def booking(request):

    doctor = request.GET.get('doctor')

    slots = [
        '10:00 AM',
        '11:00 AM',
        '12:00 PM',
        '02:00 PM',
        '04:00 PM'
    ]

    return render(
        request,
        'appointments/booking.html',
        {
            'doctor': doctor,
            'slots': slots
        }
    )