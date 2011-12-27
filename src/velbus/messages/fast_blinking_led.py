"""
@author: Thomas Delaet <thomas@delaet.org>
"""
import velbus

COMMAND_CODE = 0xf8

class FastBlinkingLedMessage(velbus.Message):
	"""
	send by: VMB4RYLD
	received by: VMB6IN
	"""	
	def __init__(self):
		velbus.Message.__init__(self)
		self.leds = []
		
	def populate(self, priority, address, rtr, data):
		"""
		@return ""
		"""
		assert isinstance(data, str)
		self.needs_low_priority(priority)
		self.needs_no_rtr(rtr)
		self.needs_data(data, 1)
		self.set_attributes(priority, address, rtr)
		self.leds = self.byte_to_channels(data[0])
			
	def data_to_binary(self):
		"""
		@return: str
		"""
		return chr(COMMAND_CODE) + \
			self.channels_to_byte(self.leds)
					
velbus.register_command(COMMAND_CODE, FastBlinkingLedMessage)