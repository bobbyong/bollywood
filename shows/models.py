# encoding: utf-8
from django.db import models
from django.utils.translation import ugettext as _

# http://xml.coverpages.org/country3166.html
COUNTRIES = (
	('AD', _('Andorra')),
	('AE', _('United Arab Emirates')),
	('AF', _('Afghanistan')),
	('AG', _('Antigua & Barbuda')),
	('AI', _('Anguilla')),
	('AL', _('Albania')),
	('AM', _('Armenia')),
	('AN', _('Netherlands Antilles')),
	('AO', _('Angola')),
	('AQ', _('Antarctica')),
	('AR', _('Argentina')),
	('AS', _('American Samoa')),
	('AT', _('Austria')),
	('AU', _('Australia')),
	('AW', _('Aruba')),
	('AZ', _('Azerbaijan')),
	('BA', _('Bosnia and Herzegovina')),
	('BB', _('Barbados')),
	('BD', _('Bangladesh')),
	('BE', _('Belgium')),
	('BF', _('Burkina Faso')),
	('BG', _('Bulgaria')),
	('BH', _('Bahrain')),
	('BI', _('Burundi')),
	('BJ', _('Benin')),
	('BM', _('Bermuda')),
	('BN', _('Brunei Darussalam')),
	('BO', _('Bolivia')),
	('BR', _('Brazil')),
	('BS', _('Bahama')),
	('BT', _('Bhutan')),
	('BV', _('Bouvet Island')),
	('BW', _('Botswana')),
	('BY', _('Belarus')),
	('BZ', _('Belize')),
	('CA', _('Canada')),
	('CC', _('Cocos (Keeling) Islands')),
	('CF', _('Central African Republic')),
	('CG', _('Congo')),
	('CH', _('Switzerland')),
	('CI', _('Ivory Coast')),
	('CK', _('Cook Iislands')),
	('CL', _('Chile')),
	('CM', _('Cameroon')),
	('CN', _('China')),
	('CO', _('Colombia')),
	('CR', _('Costa Rica')),
	('CU', _('Cuba')),
	('CV', _('Cape Verde')),
	('CX', _('Christmas Island')),
	('CY', _('Cyprus')),
	('CZ', _('Czech Republic')),
	('DE', _('Germany')),
	('DJ', _('Djibouti')),
	('DK', _('Denmark')),
	('DM', _('Dominica')),
	('DO', _('Dominican Republic')),
	('DZ', _('Algeria')),
	('EC', _('Ecuador')),
	('EE', _('Estonia')),
	('EG', _('Egypt')),
	('EH', _('Western Sahara')),
	('ER', _('Eritrea')),
	('ES', _('Spain')),
	('ET', _('Ethiopia')),
	('FI', _('Finland')),
	('FJ', _('Fiji')),
	('FK', _('Falkland Islands (Malvinas)')),
	('FM', _('Micronesia')),
	('FO', _('Faroe Islands')),
	('FR', _('France')),
	('FX', _('France, Metropolitan')),
	('GA', _('Gabon')),
	('GB', _('United Kingdom (Great Britain)')),
	('GD', _('Grenada')),
	('GE', _('Georgia')),
	('GF', _('French Guiana')),
	('GH', _('Ghana')),
	('GI', _('Gibraltar')),
	('GL', _('Greenland')),
	('GM', _('Gambia')),
	('GN', _('Guinea')),
	('GP', _('Guadeloupe')),
	('GQ', _('Equatorial Guinea')),
	('GR', _('Greece')),
	('GS', _('South Georgia and the South Sandwich Islands')),
	('GT', _('Guatemala')),
	('GU', _('Guam')),
	('GW', _('Guinea-Bissau')),
	('GY', _('Guyana')),
	('HK', _('Hong Kong')),
	('HM', _('Heard & McDonald Islands')),
	('HN', _('Honduras')),
	('HR', _('Croatia')),
	('HT', _('Haiti')),
	('HU', _('Hungary')),
	('IN', _('India')),
	('ID', _('Indonesia')),
	('IE', _('Ireland')),
	('IL', _('Israel')),
	('IO', _('British Indian Ocean Territory')),
	('IQ', _('Iraq')),
	('IR', _('Islamic Republic of Iran')),
	('IS', _('Iceland')),
	('IT', _('Italy')),
	('JM', _('Jamaica')),
	('JO', _('Jordan')),
	('JP', _('Japan')),
	('KE', _('Kenya')),
	('KG', _('Kyrgyzstan')),
	('KH', _('Cambodia')),
	('KI', _('Kiribati')),
	('KM', _('Comoros')),
	('KN', _('St. Kitts and Nevis')),
	('KP', _('Korea, Democratic People\'s Republic of')),
	('KR', _('Korea, Republic of')),
	('KW', _('Kuwait')),
	('KY', _('Cayman Islands')),
	('KZ', _('Kazakhstan')),
	('LA', _('Lao People\'s Democratic Republic')),
	('LB', _('Lebanon')),
	('LC', _('Saint Lucia')),
	('LI', _('Liechtenstein')),
	('LK', _('Sri Lanka')),
	('LR', _('Liberia')),
	('LS', _('Lesotho')),
	('LT', _('Lithuania')),
	('LU', _('Luxembourg')),
	('LV', _('Latvia')),
	('LY', _('Libyan Arab Jamahiriya')),
	('MA', _('Morocco')),
	('MC', _('Monaco')),
	('MD', _('Moldova, Republic of')),
	('MG', _('Madagascar')),
	('MH', _('Marshall Islands')),
	('ML', _('Mali')),
	('MN', _('Mongolia')),
	('MM', _('Myanmar')),
	('MO', _('Macau')),
	('MP', _('Northern Mariana Islands')),
	('MQ', _('Martinique')),
	('MR', _('Mauritania')),
	('MS', _('Monserrat')),
	('MT', _('Malta')),
	('MU', _('Mauritius')),
	('MV', _('Maldives')),
	('MW', _('Malawi')),
	('MX', _('Mexico')),
	('MY', _('Malaysia')),
	('MZ', _('Mozambique')),
	('NA', _('Namibia')),
	('NC', _('New Caledonia')),
	('NE', _('Niger')),
	('NF', _('Norfolk Island')),
	('NG', _('Nigeria')),
	('NI', _('Nicaragua')),
	('NL', _('Netherlands')),
	('NO', _('Norway')),
	('NP', _('Nepal')),
	('NR', _('Nauru')),
	('NU', _('Niue')),
	('NZ', _('New Zealand')),
	('OM', _('Oman')),
	('PA', _('Panama')),
	('PE', _('Peru')),
	('PF', _('French Polynesia')),
	('PG', _('Papua New Guinea')),
	('PH', _('Philippines')),
	('PK', _('Pakistan')),
	('PL', _('Poland')),
	('PM', _('St. Pierre & Miquelon')),
	('PN', _('Pitcairn')),
	('PR', _('Puerto Rico')),
	('PT', _('Portugal')),
	('PW', _('Palau')),
	('PY', _('Paraguay')),
	('QA', _('Qatar')),
	('RE', _('Reunion')),
	('RO', _('Romania')),
	('RU', _('Russian Federation')),
	('RW', _('Rwanda')),
	('SA', _('Saudi Arabia')),
	('SB', _('Solomon Islands')),
	('SC', _('Seychelles')),
	('SD', _('Sudan')),
	('SE', _('Sweden')),
	('SG', _('Singapore')),
	('SH', _('St. Helena')),
	('SI', _('Slovenia')),
	('SJ', _('Svalbard & Jan Mayen Islands')),
	('SK', _('Slovakia')),
	('SL', _('Sierra Leone')),
	('SM', _('San Marino')),
	('SN', _('Senegal')),
	('SO', _('Somalia')),
	('SR', _('Suriname')),
	('ST', _('Sao Tome & Principe')),
	('SV', _('El Salvador')),
	('SY', _('Syrian Arab Republic')),
	('SZ', _('Swaziland')),
	('TC', _('Turks & Caicos Islands')),
	('TD', _('Chad')),
	('TF', _('French Southern Territories')),
	('TG', _('Togo')),
	('TH', _('Thailand')),
	('TJ', _('Tajikistan')),
	('TK', _('Tokelau')),
	('TM', _('Turkmenistan')),
	('TN', _('Tunisia')),
	('TO', _('Tonga')),
	('TP', _('East Timor')),
	('TR', _('Turkey')),
	('TT', _('Trinidad & Tobago')),
	('TV', _('Tuvalu')),
	('TW', _('Taiwan, Province of China')),
	('TZ', _('Tanzania, United Republic of')),
	('UA', _('Ukraine')),
	('UG', _('Uganda')),
	('UM', _('United States Minor Outlying Islands')),
	('US', _('United States of America')),
	('UY', _('Uruguay')),
	('UZ', _('Uzbekistan')),
	('VA', _('Vatican City State (Holy See)')),
	('VC', _('St. Vincent & the Grenadines')),
	('VE', _('Venezuela')),
	('VG', _('British Virgin Islands')),
	('VI', _('United States Virgin Islands')),
	('VN', _('Viet Nam')),
	('VU', _('Vanuatu')),
	('WF', _('Wallis & Futuna Islands')),
	('WS', _('Samoa')),
	('YE', _('Yemen')),
	('YT', _('Mayotte')),
	('YU', _('Yugoslavia')),
	('ZA', _('South Africa')),
	('ZM', _('Zambia')),
	('ZR', _('Zaire')),
	('ZW', _('Zimbabwe')),
	('ZZ', _('Unknown or unspecified country')),
)


class Actor(models.Model):
	actor_name = models.CharField(max_length=200)
	actor_slug_name = models.SlugField(unique=True,
										help_text=u'This is a permalink for Actor. Ensure name is unique.')
	

	def __unicode__(self):
		return self.actor_name


class Director(models.Model):
	director_name = models.CharField(max_length=200)
	director_slug_name = models.SlugField(unique=True,
										help_text=u'This is a permalink for Director. Ensure name is unique.')
	
	def __unicode__(self):
		return self.director_name


class Genre(models.Model):
	genre_type = models.CharField(max_length=200)
	genre_slug_type = models.SlugField(unique=True,
										help_text=u'This is a permalink for Genre. Ensure name is unique.')
	
	def __unicode__(self):
		return self.genre_type

class Network(models.Model):
	network_name = models.CharField(max_length=100)
	network_slug_name = models.SlugField(unique=True,
										help_text=u'This is a permalink for Network. Ensure name is unique.')
	
	def __unicode__(self):
		return self.network_name


class Production_House(models.Model):
	production_house_name = models.CharField(max_length=100)
	production_house_slug_name = models.SlugField(unique=True,
										help_text=u'This is a permalink for Production House. Ensure name is unique.')
	
	class Meta:
	    verbose_name = u'Production House'
	    verbose_name_plural = u'Production Houses'

	def __unicode__(self):
		return self.production_house_name


class Episode(models.Model):
	episode_number = models.IntegerField()
	episode_name = models.CharField(max_length=200)
	episode_slug_name = models.SlugField(unique=True,
										help_text=u'This is a permalink for Episode. Ensure name is unique.')
	episode_duration = models.IntegerField(blank=True, null=True, 
											help_text=u'Duration of episode in minutes')
	episode_trailer = models.CharField(max_length=11, 
									blank=True, 
									help_text=u'Key in the 11 characters Youtube ID. Eg M0jmSsQ5ptw',
									verbose_name='Episode link')
	episode_startdate = models.DateField(blank=True, null=True)
	
	###Mayank: added the MTV link to support MTV video embedding which is differenct from Youtube
	episode_mtv_link=models.TextField(max_length=6000,
									blank=True,
									help_text=u'Copy and paste the embed video option from MTV website')

	def __unicode__(self):
		return self.episode_name


class Show(models.Model):
	show_name = models.CharField(max_length=200)
	show_slug_name = models.SlugField(unique=True,
										help_text=u'This is a permalink for Show. Ensure name is unique.')
	show_abbrev = models.CharField(max_length=10,
										help_text=u'Choose a unique abbreviation. Max length 10 characters.')
	show_pix1 = models.CharField(max_length=200,
									blank=True, null=True, 
									help_text=u'Insert picture URL here. Max length 200 characters. If longer use bit.ly to shorten')
	show_pix2 = models.CharField(max_length=200,
									blank=True, null=True, 
									help_text=u'Insert picture URL here. Max length 200 characters. If longer use bit.ly to shorten')
	show_pix3 = models.CharField(max_length=200,
									blank=True, null=True, 
									help_text=u'Insert picture URL here. Max length 200 characters. If longer use bit.ly to shorten')
	show_startdate = models.DateField(blank=True, null=True)
	show_current_episode = models.IntegerField(blank=True, null=True)
	show_official_site = models.URLField(blank=True)
	show_rating = models.IntegerField(blank=True, null=True)
	show_trailer = models.CharField(max_length=11, 
									blank=True, 
									help_text=u'Key in the 11 characters Youtube ID. Eg M0jmSsQ5ptw')
	show_storyline = models.TextField(blank=True)
	show_country = models.CharField(max_length=50,
									blank=True)
	show_network = models.ManyToManyField(Network, blank=True, null=True)
	show_actor = models.ManyToManyField(Actor, blank=True, null=True)
	show_director = models.ManyToManyField(Director, blank=True, null=True)
	show_genre = models.ManyToManyField(Genre, blank=True, null=True)
	show_episode = models.ManyToManyField(Episode, blank=True, null=True)
	###Mayank: added the MTV link to support MTV video embedding which is differenct from Youtube
	show_mtv_link = models.TextField(max_length=6000,
									blank=True,
									help_text=u'Copy and paste the embed video option from MTV website')

	def __unicode__(self):
		return self.show_name



class Movie(models.Model):
	movie_name = models.CharField(max_length=200)
	movie_slug_name = models.SlugField(unique=True,
										help_text=u'This is a permalink for Show. Ensure name is unique.')
	movie_abbrev = models.CharField(max_length=10, unique=True,
										help_text=u'Choose a unique abbreviation. Max length 10 characters.')
	movie_pix1 = models.CharField(max_length=200,
									blank=True, null=True, 
									help_text=u'Insert picture URL here. Max length 200 characters. If longer use bit.ly to shorten')
	movie_pix2 = models.CharField(max_length=200,
									blank=True, null=True, 
									help_text=u'Insert picture URL here. Max length 200 characters. If longer use bit.ly to shorten')
	movie_pix3 = models.CharField(max_length=200,
									blank=True, null=True, 
									help_text=u'Insert picture URL here. Max length 200 characters. If longer use bit.ly to shorten')
	movie_startdate = models.DateField(blank=True, null=True)
	movie_official_site = models.URLField(blank=True)
	movie_rating = models.IntegerField(blank=True, null=True)
	movie_trailer = models.CharField(max_length=11, 
									blank=True, 
									help_text=u'Key in the 11 characters Youtube ID. Eg M0jmSsQ5ptw')
	movie_storyline = models.TextField(blank=True)
	movie_country = models.CharField(max_length=50,
									blank=True)
	movie_language = models.CharField(max_length=50,
									blank=True)
	movie_production_house = models.ManyToManyField(Production_House, blank=True, null=True)
	movie_actor = models.ManyToManyField(Actor, blank=True, null=True)
	movie_director = models.ManyToManyField(Director, blank=True, null=True)
	movie_genre = models.ManyToManyField(Genre, blank=True, null=True)

	def __unicode__(self):
		return self.movie_name


class MTV(models.Model):
	mtv_name = models.CharField(max_length=100)
	mtv_slug_name = models.SlugField(unique=True,
										help_text=u'This is a permalink for MTV. Ensure name is unique.')
	mtv_embed_code = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.mtv_name