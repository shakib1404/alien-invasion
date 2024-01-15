class Settings:
	"""docstring for settings:"""
	def __init__(self):
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(0,0,230)
		self.ship_speed=1.5

		#bullet settings
		self.bullet_speed=1.0
		self.bullet_width=6
		self.bullet_height=25
		self.bullet_color=(230,0,0)
		self.bullet_allowed=3