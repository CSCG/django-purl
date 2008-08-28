from purl.purl.models import Profile, StepTwo, StepThree
from django.shortcuts import render_to_response
from purl.purl.forms import *
from django.http import HttpResponseRedirect
import datetime
import string

def main(request):
	profile = Profile()
	if request.method == "POST":
		pform = MainForm(request.POST, instance=profile)
		if pform.is_valid():
			cform = pform.cleaned_data
			first = cform['first_name']
			last = cform['last_name']
			stripped_fn = ""
			for f in first:
				if f in string.punctuation:
					f = ""
				stripped_fn += f
			stripped_ln = ""
			for l in last:
				if l in string.punctuation:
					l = ""
				stripped_ln += l
			cform['email'] = ''
			cform['phone'] = '' 
			pname = '%s%s' % (stripped_fn, stripped_ln)
			plower = pname.lower()
			try:
				test = Profile.objects.get(purl_name=plower)
			except Profile.DoesNotExist:
				pform.save()
			return HttpResponseRedirect('%s' % (plower))
	else:
		main_form = MainForm(instance=profile)
	return render_to_response('purl_user/main.html', { 'profile' : profile, 'main_form' : main_form })

def step_one(request, purl_id):
	pid = purl_id.lower()
	try:
		profile = Profile.objects.get(purl_name=pid)
	except Profile.DoesNotExist:
		return HttpResponseRedirect('../')
	if request.method == "POST":
		step_one_form = StepOneForm(request.POST, error_class=DivErrorList, instance=profile)
		if step_one_form.is_valid():
			step_one_form.save()
			return HttpResponseRedirect('2/')
		else:
			return render_to_response('purl_user/step_one.html', { 'profile' : profile, 'step_one_form' : step_one_form })
	else:
		step_one_form = StepOneForm(instance=profile)
		profile.visited = True
		profile.date_visited = datetime.datetime.now()
		profile.save()
	return render_to_response('purl_user/step_one.html', { 'profile' : profile, 'step_one_form' : step_one_form })
	
def step_two(request, purl_id):
	pid = purl_id.lower()
	profile = Profile.objects.get(purl_name=pid)
	
	if request.method == "POST":
		steptwo = StepTwo.objects.get(steptwo_user=profile)
		step_two_form = StepTwoForm(request.POST, instance=steptwo)
		if step_two_form.is_valid():
			step_two_form.save()
			return HttpResponseRedirect('../3/')
		else:
			return render_to_response('purl_user/step_two.html', { 'profile' : profile, 'step_two_form' : step_two_form })
	else:
		try:
			steptwo = StepTwo.objects.get(steptwo_user=profile)
			step_two_form = StepTwoForm(instance=steptwo)
		except StepTwo.DoesNotExist:
			steptwo = StepTwo()
			step_two_form = StepTwoForm(instance=steptwo)
			steptwo.steptwo_user = profile
			steptwo.visited = True
			steptwo.date_visited = datetime.datetime.now()
			steptwo.save()
	return render_to_response('purl_user/step_two.html', { 'profile' : profile, 'step_two_form' : step_two_form })
	
def step_three(request, purl_id):
	pid = purl_id.lower()
	profile = Profile.objects.get(purl_name=pid)

	if request.method == "POST":
		stepthree = StepThree.objects.get(stepthree_user=profile)
		step_three_form = StepThreeForm(request.POST, instance=stepthree)
		if step_three_form.is_valid():
			step_three_form.save()
			return HttpResponseRedirect('../3/')
		else:
			return render_to_response('purl_user/step_two.html', { 'profile' : profile, 'step_two_form' : step_two_form })
	else:
		try:
			stepthree = StepThree.objects.get(stepthree_user=profile)
			step_three_form = StepThreeForm(instance=stepthree)
		except StepThree.DoesNotExist:
			stepthree = StepThree()
			step_three_form = StepThreeForm(instance=stepthree)
			stepthree.stepthree_user = profile
			stepthree.visited = True
			stepthree.date_visited = datetime.datetime.now()
			stepthree.save()
	return render_to_response('purl_user/step_three.html', { 'profile' : profile, 'step_three_form' : step_three_form })
