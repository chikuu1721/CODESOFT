package com.tns.dayone;

public class PrimitiveDataTypesDemo {

	public static void main(String[] args) {
		
		byte byteMax=127;
		byte byteMin=-128;
		
		System.out.println("Min range of byte is "+byteMin+" Max range of byte is "+byteMax);
		
		short shortMax = 32767;
		short shortMin = -32768;
		
		System.out.println("Minshort range of byte is "+shortMin+" Maxshort range of byte is"+shortMax);
		
		int maxInt = 2147483647;
		int minInt = -2147483648;
		
		System.out.println("MinInt range of byte is "+minInt+" MaxInt range of byte is "+maxInt);
		
		long maxlong= 9223362036854775807L;
		long minlong= -9223372036854775808L;
		
		System.out.println("Minlong range of byte is"+minlong+" Maxlong range of byte is "+maxlong);
		
		float f=3234.14124512345678902345678914f;
		double d=3456.14124512345678902345678914f;
		
		System.out.println("float value is "+f+" double value is "+d);
		
		boolean flag= false;
		System.out.println("boolean value is "+flag);
	}

}
