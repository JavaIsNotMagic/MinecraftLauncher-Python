package com.mcpy.gui;
import java.sql.*;
public class AccountHandler {
	public static boolean accountCreate(String username, String password, String email){
    		try {
        		Class.forName("com.mysql.jdbc.Driver");
   			Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/PYMCAUTH?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC", "ctozer", "password");
   			Statement mystatement = con.createStatement();
   			ResultSet codespeedy=mystatement.executeQuery("insert into users(username, password, email) values(username, password, email)");
      			while(codespeedy.next())
      			{
         	 		System.out.println(codespeedy.getString("username")+"  "+codespeedy.getString("password")+"  "+codespeedy.getString("email"));  
          
      			}
			return true;	
      
          
        	} catch (Exception e) {
			return false;
    		}
  	}
	
	public static boolean authUser(String username, String password) {
    		try {
        		Class.forName("com.mysql.jdbc.Driver");
   			Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/PYMCAUTH?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC", "ctozer", "password");
   			Statement mystatement = con.createStatement();
   			ResultSet codespeedy=mystatement.executeQuery("select * from users");
      			while(codespeedy.next()) {
				if(username.equals(codespeedy.getString("username"))) {         	 		
					if(password.equals(codespeedy.getString("password"))) {
						return true;
					} else {
						System.out.println("LOGIN FAILED");
						return false;  
          				}
				} else {
					break;
				}
			}
			return false;
        	} catch (Exception e){
			return false;
    		}
  	}
}
