from test_purl.purl.models import *
from django import forms
from django.forms.util import ErrorList

class MainForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ( 'full_name',
        			'address1',
        			'address2',
        			'city',
        			'state',
        			'zipcode',
        			'phone',
        			'email',
                    'purl_name',
                    'purl',
                    'qpath',
                    'visited',
                    'date_created',
                    'date_visited')

class DivErrorList(ErrorList):
	def __unicode__(self):
		return self.as_divs()
	def as_divs(self):
		if not self: return u''
		return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="error">%s</div>' % e for e in self])

class StepOneForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ( 'full_name',
        			'first_name',
                    'last_name',
        			'purl_name',
                    'purl',
                    'qpath',
                    'visited',
                    'date_created',
                    'date_visited')
                    
class StepTwoForm(forms.ModelForm):
    class Meta:
        model = StepTwo
        exclude = ( 'steptwo_user',
        			'visited',
                    'date_visited')

class StepThreeForm(forms.ModelForm):
    class Meta:
        model = StepThree
        exclude = ( 'stepthree_user',
        			'visited',
                    'date_visited')

