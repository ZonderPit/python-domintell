"""
@author: Thomas Delaet <thomas@delaet.org>
"""
import velbus
import struct

COMMAND_CODE = 0xfb

CHANNEL_NORMAL = 0x00

CHANNEL_INHIBITED = 0x01

CHANNEL_FORCED_ON = 0x02

CHANNEL_DISABLED = 0x03

RELAY_ON = 0x01

RELAY_OFF = 0x00

INTERVAL_TIMER_ON = 0x03

LED_OFF = 0

LED_ON = 1 << 7

LED_SLOW_BLINKING = 1 << 6

LED_FAST_BLINKING = 1 << 5

LED_VERY_FAST_BLINKING = 1 << 4

class RelayStatusMessage(velbus.Message):
	#pylint: disable-msg=R0904
	"""
	send by: VMB4RYLD
	received by:
	"""	
	def __init__(self):
		velbus.Message.__init__(self)
		self.channel = 0
		self.disable_inhibit_forced = 0
		self.status = 0
		self.led_status = 0
		self.delay_time = 0

		
	def populate(self, priority, address, rtr, data):
		"""
		@return ""
		"""
		assert isinstance(data, str)
		self.needs_low_priority(priority)
		self.needs_no_rtr(rtr)
		self.needs_data(data, 7)
		self.set_attributes(priority, address, rtr)
		self.channel = self.byte_to_channel(data[0])
		self.needs_valid_channel(self.channel, 5)
		self.disable_inhibit_forced = ord(data[1])
		self.status = ord(data[2])
		self.led_status = ord(data[3])
		(self.delay_time,) = struct.unpack('>L', chr(0) + data[4:])
	
	def is_normal(self):
		"""
		@return: bool
		"""
		return self.disable_inhibit_forced == CHANNEL_NORMAL
	
	def is_inhibited(self):
		"""
		@return: bool
		"""
		return self.disable_inhibit_forced == CHANNEL_INHIBITED
	
	def is_forced_on(self):
		"""
		@return: bool
		"""
		return self.disable_inhibit_forced == CHANNEL_FORCED_ON
	
	def is_disabled(self):
		"""
		@return: bool
		"""
		return self.disable_inhibit_forced == CHANNEL_DISABLED
	
	def is_on(self):
		"""
		@return: bool
		"""
		return self.status == RELAY_ON
	
	def is_off(self):
		"""
		@return: bool
		"""
		return self.status == RELAY_OFF
	
	def has_interval_timer_on(self):
		"""
		@return: bool
		"""
		return self.status == INTERVAL_TIMER_ON
		
	def data_to_binary(self):
		"""
		@return: str
		"""
		return chr(COMMAND_CODE) + self.channels_to_byte([self.channel]) + \
				chr(self.disable_inhibit_forced) + \
				chr(self.status) + \
				chr(self.led_status) + \
				struct.pack('>L', self.delay_time)[-3:]
					
velbus.register_command(COMMAND_CODE, RelayStatusMessage)