from django.db import models
import datetime
import string

class Profile(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	full_name = models.CharField(max_length=200, blank=True, editable=False)
	purl_name = models.CharField(max_length=200, blank=True)
	address1 = models.CharField(max_length=250)
	address2 = models.CharField(max_length=250, blank=True)
	city = models.CharField(max_length=100)
	state = models.USStateField()
	zipcode = models.CharField(max_length=10)
	phone = models.PhoneNumberField()
	email = models.EmailField()
	purl = models.CharField(max_length=250, blank=True)
	qpath = models.CharField(max_length=1, blank=True)
	visited = models.BooleanField()
	date_created = models.DateTimeField(default=datetime.datetime.now)
	date_visited = models.DateTimeField(null=True)
	
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)
		
	def save(self):
		self.full_name = u'%s %s' % (self.first_name, self.last_name)
		stripped_fn = ""
		for f in self.first_name:
			if f in string.punctuation:
				f = ""
			stripped_fn += f
		stripped_ln = ""
		for l in self.last_name:
			if l in string.punctuation:
				l = ""
			stripped_ln += l
		pn = u'%s%s' % (stripped_fn, stripped_ln)
		self.purl_name = pn.lower()
		super(Profile, self).save()
		
class StepTwo(models.Model):
	steptwo_user = models.ForeignKey(Profile, unique=True)
	
	NEW_HOME_CHOICES = (
		('Next 30 days', 'Next 30 days'),
		('1-3 Months', '1-3 Months'),
		('3-6 Months', '3-6 Months'),
		('6-9 Months', '6-9 Months'),
		('12+ Months', '12+ Months'),
	)
	new_home = models.CharField(max_length=12, choices=NEW_HOME_CHOICES)
	
	OWN_RENT_CHOICES = (
		('Own', 'Own'),
		('Rent', 'Rent'),
	)
	own_rent = models.CharField(max_length=4, choices=OWN_RENT_CHOICES)
	
	COUNTY_CHOICES = (
		('Lee', 'Lee'),
		('Collier', 'Collier'),
		('Charlotte', 'Charlotte'),
	)
	county = models.CharField(max_length=9, choices=COUNTY_CHOICES)
	
	BEDROOM_CHOICES = (
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
	)
	bedrooms = models.CharField(max_length=1, choices=BEDROOM_CHOICES)
	
	BATHROOM_CHOICES = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
	)
	bathrooms = models.CharField(max_length=1, choices=BATHROOM_CHOICES)
	
	PRICE_RANGE_CHOICES = (
		('$150,000 - $199,999', '$150,000 - $199,999'),
		('$200,000 - $249,999', '$200,000 - $249,999'),
		('$250,000 - $299,999', '$250,000 - $299,999'),
		('$300,000 - $349,999', '$300,000 - $349,999'),
	)
	price_range = models.CharField(max_length=20, choices=PRICE_RANGE_CHOICES)
	visited = models.BooleanField()
	date_visited = models.DateTimeField(null=True)
	
class StepThree(models.Model):
	stepthree_user = models.ForeignKey(Profile, unique=True)
	callback = models.BooleanField()
	visited = models.BooleanField()
	date_visited = models.DateTimeField(null=True)