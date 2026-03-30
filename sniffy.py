#!/usr/bin/python

import struct
import socket
#import scapy.all

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

DATA_TAB_1 = '\t  '
DATA_TAB_2 = '\t\t '
DATA_TAB_3 = '\t\t\t '
DATA_TAB_4 = '\t\t\t\t '

#unpack ethernet frame
def unpack_frame(data):
	d_mac , s_mac , proto = struct.unpack('! 6s 6s H', data[:14])
	return get_addr(d_mac), get_addr(s_mac),socket.htons(proto), data[14:]

#make mac readable again :3
def get_addr(bytes_addr): #we got data in the form of bytes from unpacking
	byte_str = map('{:02x}'.format, bytes_addr)
	mac_addr = ':'.join(byte_str).upper() # join the DAMN address
	return mac_addr

def main():
	s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
	while True: #creates an infinite loop where brosynthesis gets data from uhh wherever (internet ofc) and then displays it :>
		raw_data , addr = s.recvfrom(65536)
		d_mac , s_mac , eth_proto , data = unpack_frame(raw_data)
		print('\nEthernet frame')
		print(TAB_1 + 'Destination: {}, source: {}, protocol: {}, data: {}'.format(d_mac , s_mac , eth_proto , data) ) #yes I know I should make data readable, go fuck yourself
		
		if (eth_proto == 8):
			(target, version, headerL, ttl, src, data, proto) = packet(data)		
			print(TAB_1 + 'IPv4')
			print(TAB_2 + 'version: {}, Header Length: {}, TTL: {}, source: {}, protocol: {}, target: {}'.format(version, headerL, ttl, src, proto, target))

			if (proto == 1):
				print("sup twin")

				#icmp
			elif (proto == 2):
				#good question
				print("hi again")


# WE MAKING THE DATA READABLE
def packet(data):
	vsl = data[0] #version header length
	version = vsl >> 4 #shifts brotien by bits to the right, somehow giving the result of left. yea i dont really get it
	headerL = (vsl & 15) * 4 #so anyways where bro ends is where data starts. dont ask me what the fuck happening here
	ttl , proto , src , target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
	return  ttl , proto , src , target, version, headerL, data[headerL:]

#get the damn protocol and source readable, spoiled fucking children
def ipv4(addr):
	return '.'.join(map(str, addr))

def icmp_packet(data):
	itype, code, checksum = struct.unpack('1 B B H', data[:4])
	return itype, code, checksum, data[4:]

def tcp_packet(data):
	src_port, dest_port, sequence, aknowledge, reserved_fags = struct.unpack('! H H L L H', data[:14])
	offset = (reserved_fags >> 12) * 4
	fag_urg = (reserved_fags & 32) >> 5
	fag_ack = (reserved_fags & 32) >> 4
	fag_psh = (reserved_fags & 8) >> 3
	fag_syn = (reserved_fags & 2) >> 1
	fag_fin = reserved_fags & 1
	fag_rst = (reserved_fags & 4) >> 2
	return src_port, dest_port, sequence, aknowledge, reserved_fags, fag_urg, fag_ack, fag_psh, fag_syn, fag_fin, fag_rst, data[offset:]

def udp_packet(data):
	src_port, dest_port, size = struct.unpack('! H H 2x H', data[:8])
	return src_port, dest_port, size, data[8:]

# multi-line data? think again
def multi_nolonger(prefix, string, size=80):
	size -= len(prefix)
	if isinstance(string, bytes):
		string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
		if size % 2:
			size -= 1
	return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])


try:
	main()
except KeyboardInterrupt:
	exit()
