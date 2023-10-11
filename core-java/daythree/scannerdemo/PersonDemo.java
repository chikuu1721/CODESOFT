package com.tns.daythree.scannerdemo;
import java.util.*;
public class PersonDemo {

	public static void main(String[] args) {
		
		Scanner ob= new Scanner(System.in);
		
		String name;
		System.out.println("Enter Person name:");
		name=ob.nextLine();
		
		System.out.println("Enter age:");
		int age=ob.nextInt();
		
		System.out.println("Enter Gender:");
		String gender=ob.next();
		
		System.out.println("Enter Taxable Income:");
		int income=ob.nextInt();
		
		
		Person person= new Person();
		person.setName(name);
		person.setAge(age);
		person.setGender(gender);
		person.setIncome(income);
		
		System.out.println(person);
		
		TaxCalculation calc= new TaxCalculation();
		calc.calculateTax(person);
		
		System.out.println("After Calculatin tax:");
		
		System.out.println(person);
		
		ob.close();
		
	}

}
