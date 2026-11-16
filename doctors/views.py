from django.shortcuts import render


def hospital_list(request):

    district = request.GET.get('district')

    hospitals = {

        'Chennai':[
            'Apollo Hospital',
            'MIOT Hospital',
            'Global Hospital'
        ],

        'Coimbatore':[
            'Ganga Hospital',
            'KMCH Hospital'
        ],

        'Madurai':[
            'Meenakshi Mission',
            'Apollo Madurai'
        ],

        'Salem':[
            'SKS Hospital',
            'Neuro Foundation'
        ]

    }

    hospital_data = hospitals.get(district, [])

    return render(
        request,
        'doctors/hospital_list.html',
        {
            'district': district,
            'hospitals': hospital_data
        }
    )



def doctor_list(request):

    hospital = request.GET.get('hospital')

    doctors = {

        'Apollo Hospital':[
            'Dr Arjun',
            'Dr Priya',
            'Dr Karthik'
        ],

        'MIOT Hospital':[
            'Dr Ram',
            'Dr Vignesh'
        ],

        'Global Hospital':[
            'Dr Surya',
            'Dr Meena'
        ]

    }

    doctor_data = doctors.get(hospital, [])

    return render(
        request,
        'doctors/doctor_list.html',
        {
            'hospital': hospital,
            'doctors': doctor_data
        }
    )