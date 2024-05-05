from core import models
>>> models.Disease.objects.all()
<QuerySet [<Disease: Грипп>, <Disease: Туберкулез>, <Disease: ВИЧ>, <Disease: Ковид>, <Disease: Пневмомикоз>, <Disease: Аскаридоз>, <Disease: Гепатит А>]>
>>> models.Patient.objects.filter(first_name__contains='Василиса').dates('date_of_birth', 'year')
<QuerySet [datetime.date(1999, 1, 1)]>
>>> models.Patient.objects.dates('date_of_birth', 'year')
<QuerySet [datetime.date(1976, 1, 1), datetime.date(1999, 1, 1)]>
>>> models.Disease.objects.filter(name__startswith='ВИЧ')
<QuerySet [<Disease: ВИЧ>]>
>>> models.Disease.objects.filter(name__startswith='ВИЧ').values()
<QuerySet [{'id': 3, 'name': 'ВИЧ', 'type': 'viral', 'information': 'Инфекционное хроническое заболевание, передающееся контактным путем, медленно прогрессирующее и характеризующееся поражением иммунной системы с развитием синдрома приобретенного иммунодефицита.', 'infected': 300, 'is_cure': True}]>
>>>models.Disease.objects.values_list('id').order_by('id')  
<QuerySet [(1,), (2,), (3,), (4,), (5,), (6,), (7,)]>
>>> models.Disease.objects.values_list('id', 'name', named=True)
<QuerySet [Row(id=1, name='Грипп'), Row(id=2, name='Туберкулез'), Row(id=3, name='ВИЧ'), Row(id=4, name='Ковид'), Row(id=5, name='Пневмомикоз'), Row(id=6, name='Аскаридоз'), Row(id=7, name='Гепатит А')]>
>>> models.Disease.objects.only('name')
<QuerySet [<Disease: Грипп>, <Disease: Туберкулез>, <Disease: ВИЧ>, <Disease: Ковид>, <Disease: Пневмомикоз>, <Disease: Аскаридоз>, <Disease: Гепатит А>]>
>>> models.Disease.objects.latest('type')
<Disease: Гепатит А>
>>> models.Disease.objects.earliest('name')
<Disease: Аскаридоз>
>>> models.Disease.objects.get(id__exact=3)
<Disease: ВИЧ>
>>> models.Disease.objects.filter(id__gt=2)
<QuerySet [<Disease: ВИЧ>, <Disease: Ковид>, <Disease: Пневмомикоз>, <Disease: Аскаридоз>, <Disease: Гепатит А>]>
>>>




