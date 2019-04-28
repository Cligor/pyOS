import os
import curses
import pycfg
from pyarch import load_binary_into_memory
from pyarch import cpu_t

class os_t:
	def __init__ (self, cpu, memory, terminal):
		self.cpu = cpu
		self.memory = memory
		self.terminal = terminal

		self.terminal.enable_curses()

		self.console_str = ""
		self.terminal.console_print("this is the console, type the commands here\n")

	def printk(self, msg):
		self.terminal.kernel_print("kernel: " + msg + "\n")

	def panic (self, msg):
		self.terminal.end()
		self.terminal.dprint("kernel panic: " + msg)
		self.cpu.cpu_alive = False
		#cpu.cpu_alive = False

	def interrupt_keyboard(self):
		key = self.terminal.get_key_buffer()

		if ((key >= ord('a')) and (key <= ord('z'))) or ((key >= ord('A')) and (key <= ord('Z'))) or ((key >= ord('0')) and (key <= ord('9'))) or (key == ord(' ')) or (key == ord('-')) or (key == ord('_')) or (key == ord('.')):
			strchar = chr(key)
			self.console_str += strchar
			self.terminal.console_print(strchar)
			return 

		elif key == curses.KEY_BACKSPACE:
			self.console_str = self.console_str[0: len(self.console_str) - 1  ]
			self.terminal.console_print("\r" + self.console_str)

			
		elif (key == curses.KEY_ENTER) or (key == ord('\n')):
			self.commands()
			self.terminal.console_print("\n")
			self.console_str = ""


	def interrupt_timer(self):
		self.syscall()

	def interrupt_memory_protection(self):
		self.syscall()

	def handle_interrupt (self, interrupt):
		if interrupt == pycfg.INTERRUPT_KEYBOARD:
			self.interrupt_keyboard()
		elif interrupt == pycfg.INTERRUPT_TIMER:
			self.interrupt_timer()
			self.terminal.kernel_print("kernel: interrupt timer\n")
		elif interrupt == pycfg.INTERUPT_MEMORY_PROTECTION_FAULT:
			self.interrupt_memory_protection()
			self.terminal.kernel_print("kernel: interrupt memory\n")
		

	def commands(self):
		command = self.console_str
 
		if command == "exit":
			self.terminal.console_print("\nExiting...");
			self.cpu.cpu_alive = False;
			self.terminal.end();
			# self.terminal.console_print(command)

		elif (command[:2] == "./"):
			self.terminal.console_print("\nYou doesn't have permission to execute a file");

		else:
			self.terminal.console_print("\nCommand not found");

	def syscall (self):
		msg = "Not implemented\n";
		self.terminal.app_print(msg)
		return
