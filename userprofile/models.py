from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	foretag = models.CharField('Company name', max_length=50, blank=True)
	stad = models.CharField('City', max_length=50, blank=True)
	
	
	
#-------------------Machining-------------------------------------
	bol1=models.BooleanField('Boring',default=False)
	bol2=models.BooleanField('Broaching & Splining',default=False)
	bol3=models.BooleanField('Drilling',default=False)
	bol4=models.BooleanField('Drilling, CNC',default=False)
	bol5=models.BooleanField('Drilling, Deep Hole',default=False)
	bol6=models.BooleanField('Engraving',default=False)
	bol7=models.BooleanField('Etching',default=False)
	bol8=models.BooleanField('Flat bed turning',default=False)
	bol9=models.BooleanField('Gear Cutting',default=False)
	bol10=models.BooleanField('Grinding',default=False)
	bol11=models.BooleanField('Honing',default=False)
	bol12=models.BooleanField('Vertical Milling',default=False)
	bol13=models.BooleanField('Lapping',default=False)
	bol14=models.BooleanField('Machining with Fabrication',default=False)
	bol15=models.BooleanField('Machining, CNC',default=False)
	bol16=models.BooleanField('Machining, CNC Centres',default=False)
	bol17=models.BooleanField('Machining, Conventional',default=False)
	bol18=models.BooleanField('Machining, High Precision',default=False)
	bol19=models.BooleanField('Machining, Large 1m Plus',default=False)
	bol20=models.BooleanField('Machining, Multi-Axis',default=False)
	bol21=models.BooleanField('Machining, Plastics',default=False)
	bol22=models.BooleanField('Machining, Prototyping',default=False)
	bol23=models.BooleanField('Milling, CNC',default=False)
	bol24=models.BooleanField('Milling, Conventional',default=False)
	bol25=models.BooleanField('Multi Spindle',default=False)
	bol26=models.BooleanField('Planing',default=False)
	bol27=models.BooleanField('Saw Cutting',default=False)
	bol28=models.BooleanField('Spark Erosion',default=False)
	bol29=models.BooleanField('Special Purpose Machines',default=False)
	bol30=models.BooleanField('Tapping',default=False)
	bol31=models.BooleanField('Thread Cutting',default=False)
	bol32=models.BooleanField('Turning Auto',default=False)
	bol33=models.BooleanField('Turning CNC',default=False)
	bol34=models.BooleanField('Turning, Conventional',default=False)
	bol35=models.BooleanField('Vertical Boring',default=False)
	bol36=models.BooleanField('Wire Erosion',default=False)
	
	#-------------------Tool Making-------------------------------------	
	bol37=models.BooleanField('Blanking Tools',default=False)
	bol38=models.BooleanField('Cutting Tools',default=False)
	bol39=models.BooleanField('Dies',default=False)
	bol40=models.BooleanField('Jigs & Fixtures',default=False)
	bol41=models.BooleanField('Mould Tools',default=False)
	bol42=models.BooleanField('Pattern & Model Making',default=False)
	bol43=models.BooleanField('Press Tools',default=False)
	
	#-------------------Casting------------------------------------------
	bol44=models.BooleanField('Chill casting',default=False)
	bol45=models.BooleanField('Cire perdue',default=False)
	bol46=models.BooleanField('Continuous casting',default=False)
	bol47=models.BooleanField('Die Casting, Gravity',default=False)
	bol48=models.BooleanField('Die Casting, Pressure',default=False)
	bol49=models.BooleanField('Extrusion',default=False)
	bol50=models.BooleanField('Forging',default=False)
	bol51=models.BooleanField('Ingot casting',default=False)
	bol52=models.BooleanField('Metal Injection Moulding',default=False)
	bol53=models.BooleanField('Precision Casting',default=False)
	bol54=models.BooleanField('Sand Casting',default=False)
	bol55=models.BooleanField('Shell Moulding',default=False)
	
	#-------------------Plastic & Rubber---------------------------------
	bol56=models.BooleanField('3D Printing',default=False)
	bol57=models.BooleanField('Bonding',default=False)
	bol58=models.BooleanField('Clean Room Moulding',default=False)
	bol59=models.BooleanField('Compression moulding',default=False)
	bol60=models.BooleanField('Dip Moulding',default=False)
	bol61=models.BooleanField('GRP Moulding',default=False)
	bol62=models.BooleanField('Injection Moulding',default=False)
	bol63=models.BooleanField('Insert Moulding',default=False)
	bol64=models.BooleanField('Plastic & rubber extrusion',default=False)
	bol65=models.BooleanField('Plastic Fabrication',default=False)
	bol66=models.BooleanField('Prototyping',default=False)
	bol67=models.BooleanField('Rotational Moulding',default=False)
	bol68=models.BooleanField('Rubber Moulding',default=False)
	bol69=models.BooleanField('Vacuum Forming',default=False)
	
	#-------------------Finishing----------------------------------------
	bol70=models.BooleanField('Anodizing',default=False)
	bol71=models.BooleanField('Case hardening',default=False)
	bol72=models.BooleanField('Cleaning',default=False)
	bol73=models.BooleanField('Heat Treatment',default=False)
	bol74=models.BooleanField('Laserfinishing',default=False)
	bol75=models.BooleanField('Metal Spraying',default=False)
	bol76=models.BooleanField('Nitriding',default=False)
	bol77=models.BooleanField('Nitrocarburizing',default=False)
	bol78=models.BooleanField('Pickling',default=False)
	bol79=models.BooleanField('Plastic Coating',default=False)
	bol80=models.BooleanField('Plating',default=False)
	bol81=models.BooleanField('Polishing',default=False)
	bol82=models.BooleanField('Powder Coating',default=False)
	bol83=models.BooleanField('Precision Cleaning',default=False)
	bol84=models.BooleanField('Shot Blasting',default=False)
	bol85=models.BooleanField('Silk Screening',default=False)
	bol86=models.BooleanField('Spray Painting',default=False)
	bol87=models.BooleanField('Other coating',default=False)
	bol88=models.BooleanField('Stress relieving',default=False)
	bol89=models.BooleanField('Tempering',default=False)
	bol90=models.BooleanField('Wet painting',default=False)
	bol91=models.BooleanField('Zinc plating',default=False)
	
	#-------------------Fabrication----------------------------------------
	bol92=models.BooleanField('Architectural Steelwork',default=False)
	bol93=models.BooleanField('Brazing',default=False)
	bol94=models.BooleanField('Deep Drawing',default=False)
	bol95=models.BooleanField('Enclosures',default=False)
	bol96=models.BooleanField('Excenter pressing',default=False)
	bol97=models.BooleanField('Fabrication with Machining',default=False)
	bol98=models.BooleanField('Forging',default=False)
	bol99=models.BooleanField('Gas Cutting',default=False)
	bol100=models.BooleanField('General Fabrication 6-15mm',default=False)
	bol101=models.BooleanField('General Heavy Fabrication 15mm Plus',default=False)
	bol102=models.BooleanField('General Sheet Metal Under 6mm',default=False)
	bol103=models.BooleanField('Guillotine',default=False)
	bol104=models.BooleanField('Laser Cutting',default=False)
	bol105=models.BooleanField('Laser cutting, tube',default=False)
	bol106=models.BooleanField('Laser welding',default=False)
	bol107=models.BooleanField('Metal Spinning',default=False)
	bol108=models.BooleanField('Nibbling',default=False)
	bol109=models.BooleanField('Perforation',default=False)
	bol110=models.BooleanField('Pipework',default=False)
	bol111=models.BooleanField('Plasma Cutting',default=False)
	bol112=models.BooleanField('Press brake work',default=False)
	bol113=models.BooleanField('Pressure & Vacuum Vessels',default=False)
	bol114=models.BooleanField('Presswork',default=False)
	bol115=models.BooleanField('Presswork, Hydralic',default=False)
	bol116=models.BooleanField('Presswork, Hot',default=False)
	bol117=models.BooleanField('Prototyping',default=False)
	bol118=models.BooleanField('Punching',default=False)
	bol119=models.BooleanField('Robotic Welding',default=False)
	bol120=models.BooleanField('Roll Bending',default=False)
	bol121=models.BooleanField('Rolling',default=False)
	bol122=models.BooleanField('Spring Manufacturing',default=False)
	bol123=models.BooleanField('Stamping',default=False)
	bol124=models.BooleanField('Strip forming',default=False)
	bol125=models.BooleanField('Tube Bending & Manipulation',default=False)
	bol126=models.BooleanField('Water Cutting',default=False)
	bol127=models.BooleanField('Welding',default=False)	
	bol128=models.BooleanField('Wire Forming',default=False)
	
	

	def __unicode__(self):
		return self.user.username
	
	
	User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])