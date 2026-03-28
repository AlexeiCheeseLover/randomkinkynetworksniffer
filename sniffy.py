#!/usr/bin/python

import struct
import socket
#import scapy.all

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
		print('Destination: {}, source: {}, protocol: {}, data: {}'.format(d_mac , s_mac , eth_proto , data) ) #yes I know I should make data readable, go fuck yourself

# WE MAKING THE DATA READABLE
def packet(data):
	vsl = data[0] #version header length
	version = vsl >> 4 #shifts brotien by bits to the right, somehow giving the result of left. yea i dont really get it
	headerL = (vsl & 15) * 4 #so anyways where bro ends is where data starts. dont ask me what the fuck happening here
	ttl , proto , src , target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
	return  ttl , ipv4(proto) , ipv4(src) , target, version, headerL, data[headerL:]

#get the damn protocol and source readable, spoiled fucking children
def ipv4(addr):
	return '.'.join(map(str, addr))



try:
	main()
except KeyboardInterrupt:
	exit()