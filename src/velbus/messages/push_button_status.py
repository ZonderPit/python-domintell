"""
@author: Thomas Delaet <thomas@delaet.org>
"""
import velbus

COMMAND_CODE = 0x00

class PushButtonStatusMessage(velbus.Message):
	"""
	send by: VMB6IN, VMB4RYLD
	received by: VMB4RYLD
	"""	
	def __init__(self):
		velbus.Message.__init__(self)
		self.closed = []
		self.opened = []
		self.closed_long = []
		
	def populate(self, priority, address, rtr, data):
		"""
		@return ""
		"""
		assert isinstance(data, str)
		self.needs_high_priority(priority)
		self.needs_no_rtr(rtr)
		self.needs_data(data, 3)
		self.set_attributes(priority, address, rtr)
		self.closed = self.byte_to_channels(data[0])
		self.opened = self.byte_to_channels(data[1])
		self.closed_long = self.byte_to_channels(data[2])
		
	def get_channels(self):
		"""
		@return: list
		"""
		return self.closed + self.opened	
	
	def data_to_binary(self):
		"""
		@return: str
		"""
		return chr(COMMAND_CODE) + self.channels_to_byte(self.closed) + \
			self.channels_to_byte(self.opened) + \
			self.channels_to_byte(self.closed_long)
					
velbus.register_command(COMMAND_CODE, PushButtonStatusMessage)