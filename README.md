from core import models
>>> models.Disease.objects.all()
<QuerySet [<Disease: Грипп>, <Disease: Туберкулез>, <Disease: ВИЧ>, <Disease: Ковид>, <Disease: Пневмомикоз>, <Disease: Аскаридоз>, <Disease: Гепатит А>]>
>>> models.Disease.objects.first()
<Disease: Грипп>
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
>>> models.Disease.objects.count()
7
>>> models.Disease.objects.filter(name__contains='в') 
<QuerySet [<Disease: Ковид>, <Disease: Пневмомикоз>]>
>>> models.Disease.objects.filter(id=10).exists()
False
>>> models.Disease.objects.create(name='СПИД',infected=85)
<Disease: СПИД>
>>> models.Patient.objects.dates('date_of_birth','day').reverse()  
<QuerySet [datetime.date(1999, 6, 5), datetime.date(1976, 5, 5)]>
>>> models.Disease.objects.values('name','type')
<QuerySet [{'name': 'Грипп', 'type': 'viral'}, {'name': 'Туберкулез', 'type': 'bacterial'}, {'name': 'ВИЧ', 'type': 'viral'}, {'name': 'Ковид', 'type': 'viral'}, {'name': 'Пневмомикоз', 'type': 'fungal'}, {'name': 'Аскаридоз', 'type': 'viral'}, {'name': 'Гепатит А', 'type': 'Вирусные'}, {'name': 'СПИД', 'type': 'Вирусные'}]>
>>> models.Disease.objects.values_list('name',flat=True)
<QuerySet ['Грипп', 'Туберкулез', 'ВИЧ', 'Ковид', 'Пневмомикоз', 'Аскаридоз', 'Гепатит А', 'СПИД']>
>>> models.Disease.objects.exclude(name__contains='о')  
<QuerySet [<Disease: Грипп>, <Disease: Туберкулез>, <Disease: ВИЧ>, <Disease: Гепатит А>, <Disease: СПИД>]>
>>> models.Disease.objects.order_by('name').order_by('information') 
<QuerySet [<Disease: Гепатит А>, <Disease: СПИД>, <Disease: Пневмомикоз>, <Disease: ВИЧ>, <Disease: Грипп>, <Disease: Аскаридоз>, <Disease: Туберкулез>, <Disease: Ковид>]>
>>> models.Disease.objects.filter(infected=85).delete()
(1, {'core.Disease': 1})
>>> print(models.Disease.objects.filter(name='СПИД').explain())
2 0 0 SCAN core_disease
>>> models.Disease.objects.filter(name__endswith='А')
<QuerySet [<Disease: Гепатит А>]>





