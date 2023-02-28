from django.db import models
from django.contrib.auth.models import User 


class SaccoAdmin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Member(models.Model):
	STATUS = (
		('ACTIVE','ACTIVE'),
		('PENDING', 'PENDING'),
		)

	ID_TYPE = (
		('NATIONAL ID', 'NATIONAL ID'),
		('PASSPORT', 'PASSPORT'),
	    )

	GENDER = (
		('MALE','MALE'),
		('FEMALE', 'FEMALE'),
		)

	DISTRICTS = (
		('1' ,  'Mombasa'),
		('2' ,  'Kwale'),
		('3' ,  'Kilifi'),
		('4' ,  'Tana River'),
		('5' ,  'Lamu'),
		('6' ,  'Taita/Taveta'),
		('7' ,  'Garissa'),
		('8' ,  'Wajir'),
		('9' ,  'Mandera'),
		('10',  'Marsabit'),
		('11',  'Isiolo'),
		('12',  'Meru'),
		('13',  'Tharaka-Nithi'),
		('14',  'Embu'),
		('15',  'Kitui'),
		('16',  'Machakos'),
		('17',  'Makueni'),
		('18',  'Nyandarua'),
		('19',  'Nyeri'),
		('20',  'Kirinyaga'),
		('21',  'Murang"a'),
		('22',  'Kiambu'),
		('23',  'Turkana'),
		('24',  'West Pokot'),
		('25',  'Samburu'),
		('26',  'Trans Nzoia'),
		('27',  'Uasin Gishu'),
		('28',  'Elgeyo/Marakwet'),
		('29',  'Nandi'),
		('30',  'Baringo'),
		('31',  'Laikipia'),
		('32',  'Nakuru'),
		('33',  'Narok'),
		('34',  'Kajiado'),
		('35',  'Kericho'),
		('36',  'Bomet'),
		('37',  'Kakamega'),
		('38',  'Vihiga'),
		('39',  'Bungoma'),
		('40',  'Busia'),
		('41',  'Siaya'),
		('42',  'Kisumu'),
		('43',  'Homa Bay'),
		('44',  'Migori'),
		('45',  'Kisii'),
		('46',  'Nyamira'),
		('47',  'Nairobi City'),
		)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	firstname = models.CharField(max_length=200, null=True)
	lastname = models.CharField(max_length=200, null=True)
	id_type = models.CharField(max_length=200, null=True, choices=ID_TYPE)
	id_number = models.CharField(max_length=200, null=True)
	gender = models.CharField(max_length=200, null=True, choices=GENDER)
	date_of_birth = models.DateField(auto_now_add=False, null=True)
	district = models.CharField(max_length=200, null=True, choices=DISTRICTS)
	county = models.CharField(max_length=200, null=True,  choices=DISTRICTS)
	subcounty = models.CharField(max_length=200, null=True)
	parish = models.CharField(max_length=200, null=True)
	village = models.CharField(max_length=200, null=True)
	account_number = models.CharField(max_length=200, null=True)
	opening_balance = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	next_of_keen_first_name = models.CharField(max_length=200, null=True)
	next_of_keen_last_name = models.CharField(max_length=200, null=True)
	next_of_keen_phone = models.CharField(max_length=200, null=True)
	next_of_keen_relationship = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	# member_photo = models.ImageField(upload_to='uploads/memberPhotos/' )
	# member_id_att = models.ImageField(upload_to='uploads/memberIDs/' )
	# next_of_keen_id = models.ImageField(upload_to='uploads/nextofKeenIDs/' )



	def __str__(self):
		return self.firstname + " " + self.lastname


class Deposit(models.Model):
	STATUS = (
		('COMPLETE','COMPLETE'),
		('PENDING', 'PENDING'),
		)
	member_name = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
	account_number = models.CharField(max_length=200, null=True)
	amount = models.IntegerField(null=True)
	date_of_transaction = models.DateTimeField(auto_now=True, null=True)
	deposited_by = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, choices=STATUS)

	def __str__(self):
		return self.member_name.firstname + " " + self.member_name.lastname + " " + str(self.amount) + " UGX" + " " + str(self.date_of_transaction)


class Withdraw(models.Model):
	STATUS = (
		('COMPLETE','COMPLETE'),
		('PENDING', 'PENDING'),
		)
	member_name = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
	account_number = models.CharField(max_length=200, null=True)
	amount = models.IntegerField(null=True)
	date_of_transaction = models.DateTimeField(auto_now=True, null=True)
	withdrawn_by = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, choices=STATUS)

	def __str__(self):
		return self.member_name.firstname + " " + self.member_name.lastname + " " + str(self.amount) + " UGX" + " " + str(self.date_of_transaction)



class Loan(models.Model):
		STATUS = (
		('COMPLETE','COMPLETE'),
		('PENDING', 'PENDING'),
		)

		REPAY_PERIOD = (
		('DAYS','DAYS'),
		('MONTHS', 'MONTHS'),
		('YEARS', 'YEARS'),
		)

		member_name = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
		account_number = models.CharField(max_length=200, null=True)
		amount = models.CharField(max_length=200, null=True)
		date_of_loan_application = models.DateTimeField(auto_now=True, null=True)
		date_of_repayemnt = models.DateField(auto_now=False,auto_now_add=False,null=True)
		intrest_rate = models.CharField(max_length=200, null=True)
		repay_in = models.CharField(max_length=200, choices=REPAY_PERIOD)
		status = models.CharField(max_length=200, choices=STATUS)
		collateral1 = models.CharField(max_length=200, null=True)
		collateral2 = models.CharField(max_length=200, null=True)
		reason = models.TextField(max_length=1000, null=True)
		# collateral1_attachements = models.ImageField(upload_to='uploads/Collatreals/' )
		# collateral2_attachements = models.ImageField(upload_to='uploads/Collatreals/' )
		

		def __str__(self):
			return self.member_name.firstname + " " + self.member_name.lastname + " " + str(self.amount) + " UGX" + " " + str(self.date_of_loan_application)


	
class RepayLoan(models.Model):
		STATUS = (
		('COMPLETE','COMPLETE'),
		('PENDING', 'PENDING'),
		)

		member_name = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
		account_number = models.CharField(max_length=200, null=True)
		amount = models.CharField(max_length=200, null=True)
		date_of_loan_repayment = models.DateTimeField(auto_now=True, null=True)
		repay_in = models.CharField(max_length=200, null=True)
		paid_by = models.CharField(max_length=200, null=True)
		status = models.CharField(max_length=200, choices=STATUS)

		def __str__(self):
			return self.member_name.firstname + " " + self.member_name.lastname + " " + str(self.amount) + " UGX" + " " + str(self.date_of_loan_repayment)


	
