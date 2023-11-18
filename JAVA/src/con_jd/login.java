package con_jd;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;

import java.awt.BorderLayout;
import java.awt.GridLayout;
//import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.*;

public class login { 
	private static Connection connection;
	private static Statement statement;
	public static void main(String[] args) { 
		con();  
		LogSign();  
    }
	
	
	public static void con() {
		String records = "";
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			connection = DriverManager.getConnection("jdbc:mysql://localhost:3307/epiz_32083127_traffic", "amshuandroid", "amshuandroid");
	        System.out.println(connection);
		}
		catch (SQLException exception){
            records = "error : "+exception.toString();
        }
        catch (ClassNotFoundException ex){
            records = "@@@@"+ex.toString();
        }
        catch (Exception e){
            records = "#####"+e.toString();
        }
		System.out.println(records);
	}

	private static void LogSign() {

        JFrame frame = new JFrame("Plate Watch - Login or Signup");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 350);    
        // Center the frame on the screen
        frame.setLocationRelativeTo(null);
        // Make the frame not resize
        frame.setResizable(false);

        JPanel panel = new JPanel();  
        panel.setLayout(null);  
        JButton loginButton = new JButton("Login"); 
        loginButton.setBounds(100, 100, 300, 30); 
        JButton signupButton = new JButton("Signup"); 
        signupButton.setBounds(100, 150, 300, 30); 

        panel.add(loginButton);
        panel.add(signupButton);
        // Add panel to frame
        frame.add(panel);
         
//        frame.revalidate();
//        frame.repaint();
         
        frame.setVisible(true);

        // Add ActionListener for the "Login" button
        loginButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Replace this with your login logic 
                frame.setVisible(false);
                LogIn();
            }
        });
 
        signupButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) { 
            	frame.setVisible(false);
            	SignUp();
            }
        });
    }
	 
    private static void LogIn() {
        JFrame frame = new JFrame("Plate Watch - Log In");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        // Center the frame on the screen
        frame.setLocationRelativeTo(null);
        // Make the frame not resize
        frame.setResizable(false);

        JPanel panel = new JPanel();
        panel.setLayout(null); // Use null layout for absolute positioning

        JLabel emailLabel = new JLabel("Email");
        emailLabel.setBounds(50, 20, 300, 30);
        // Create JTextFields
        JTextField emailField = new JTextField();
        emailField.setBounds(50, 50, 300, 30);

        JLabel passwordLabel = new JLabel("Password");
        passwordLabel.setBounds(50, 80, 300, 30);
        JPasswordField passwordField = new JPasswordField();
        passwordField.setBounds(50, 110, 300, 30);

        // Create JButton
        JButton loginButton = new JButton("Log In");
        loginButton.setBounds(50, 160, 300, 30); 

        // Create JLabel
        JButton signUpLabel = new JButton("Don't have an account? Sign Up");
        signUpLabel.setBounds(50, 200, 300, 30);  

        // Add components to the panel
        panel.add(emailLabel);
        panel.add(passwordLabel);
        panel.add(emailField); 
        panel.add(passwordField);
        panel.add(loginButton);
        panel.add(signUpLabel); 
        frame.add(panel);
        frame.setVisible(true);
        
        signUpLabel.addActionListener(new ActionListener() { 
            public void actionPerformed(ActionEvent e) {
            	frame.setVisible(false);
            	SignUp();
            }
        });
        
     // Add an ActionListener to the loginButton
        loginButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Retrieve the text entered in the fields
                String email = emailField.getText(); 
                char[] passwordChars = passwordField.getPassword();
                String password = new String(passwordChars);
                String qu = "SELECT * FROM users WHERE email = '"+email+"' and password ='"+password+"'";
                try {
            		statement = connection.createStatement();
        	        ResultSet resultSet = statement.executeQuery(qu);
        	        if(resultSet.next()) {
	        	        do { 
	        	        	frame.setVisible(false);
	        	        	Main_Page(email);
	        	        }
	        	        while (resultSet.next());
        	        }else { 
        	        	JOptionPane.showMessageDialog(null, "Log In Failed!", "Could not Log In User !", JOptionPane.WARNING_MESSAGE);
        	        }
                }
                catch (SQLException exception){ 
                    JOptionPane.showMessageDialog(null, "Log In Failed!", "Could not Log In User !", JOptionPane.WARNING_MESSAGE);
                    System.out.println("error : "+exception.toString());
                } 
                catch (Exception ex){
                	JOptionPane.showMessageDialog(null, "Log In Failed!", "Could not Log In User !", JOptionPane.WARNING_MESSAGE);
                	System.out.println("#####"+ex.toString());
                } 
            }
        });
        
    }
    
    private static void SignUp() {
        JFrame frame = new JFrame("Plate Watch - Sign UP");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 500);
        // Center the frame on the screen
        frame.setLocationRelativeTo(null);
        // Make the frame not resize
        frame.setResizable(false);
        
        JPanel panel = new JPanel();
        panel.setLayout(null); // Use null layout for absolute positioning
 
        JLabel emailLabel = new JLabel("Email");
        emailLabel.setBounds(50, 20, 300, 30); 
        JTextField emailField = new JTextField();
        emailField.setBounds(50, 50, 300, 30);

        JLabel numberPlateLabel = new JLabel("Number Plate");
        numberPlateLabel.setBounds(50, 80, 300, 30);
        JTextField numberPlateField = new JTextField();
        numberPlateField.setBounds(50, 110, 300, 30);

        JLabel phoneLabel = new JLabel("Phone Number");
        phoneLabel.setBounds(50, 140, 300, 30);
        JTextField phoneField = new JTextField();
        phoneField.setBounds(50, 170, 300, 30);
        
        JLabel passwordLabel = new JLabel("Password");
        passwordLabel.setBounds(50, 200, 300, 30);
        JPasswordField passwordField = new JPasswordField();
        passwordField.setBounds(50, 230, 300, 30);

        // Create JButton
        JButton regButton = new JButton("Register");
        regButton.setBounds(50, 280, 300, 30);

        // Create JLabel
        JButton alreadyLabel = new JButton("Already have an account? Log In");
        alreadyLabel.setBounds(50, 320, 300, 30); 

        // Add components to the panel
        panel.add(emailField);
        panel.add(emailLabel);
        panel.add(passwordField);
        panel.add(passwordLabel);
        panel.add(phoneLabel);
        panel.add(numberPlateField);
        panel.add(numberPlateLabel);
        panel.add(phoneField);
        panel.add(regButton);
        panel.add(alreadyLabel); 

        frame.add(panel);
        frame.setVisible(true);
     // Add an ActionListener to the loginButton
        
        alreadyLabel.addActionListener(new ActionListener() { 
            public void actionPerformed(ActionEvent e) {
            	frame.setVisible(false);
            	LogIn();
            }
        });
        
        regButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Retrieve the text entered in the fields
                String email = emailField.getText();
                String numberPlate = numberPlateField.getText();
                String phone = phoneField.getText();
                char[] passwordChars = passwordField.getPassword();
                String password = new String(passwordChars);
                String qu = "SELECT * FROM users WHERE email = '"+email+"' and numberPlate ='"+numberPlate+"' and phone ='"+phone+"'";
                try {
            		statement = connection.createStatement();
        	        ResultSet resultSet = statement.executeQuery(qu); 
        	        if(resultSet.next()) {    
        	        	String que = "UPDATE users SET password = '"+password+"' WHERE email = '"+email+"' and numberPlate ='"+numberPlate+"' and phone ='"+phone+"'";
        	        	int resultS = statement.executeUpdate(que);
        	        	if(resultS > 0) {   
        	        		frame.setVisible(false);
        	        		LogIn(); 
        	        	}else { 
            	        	JOptionPane.showMessageDialog(null, "SignUp Failed!", "Could not Register User !", JOptionPane.WARNING_MESSAGE);
            	        }  
        	        }
        	        else { 
        	        	JOptionPane.showMessageDialog(null, "SignUp Failed!", "User Not Found !", JOptionPane.WARNING_MESSAGE);
        	        }
                }
                catch (SQLException exception){
                	JOptionPane.showMessageDialog(null, "SignUp Failed!", "Could not Register User !", JOptionPane.WARNING_MESSAGE);
                    System.out.println("error : "+exception.toString());
                } 
                catch (Exception ex){
                	JOptionPane.showMessageDialog(null, "SignUp Failed!", "Could not Register User !", JOptionPane.WARNING_MESSAGE);
                	System.out.println("#####"+ex.toString());
                }   
            }
        });
    }
    
    private static void Main_Page(String email) { 
    	JFrame frame = new JFrame("Plate Watch - Main");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 400);
        // Center the frame on the screen
        frame.setLocationRelativeTo(null);  

        JMenuBar menuBar = new JMenuBar();
        JMenuItem fineMenu = new JMenuItem("My Fines");
        JMenuItem infoMenu = new JMenuItem("My Information"); 

        menuBar.add(fineMenu);
        menuBar.add(infoMenu);

        frame.setJMenuBar(menuBar);
        
     
        JPanel contentPanel = new JPanel();
        frame.add(contentPanel, BorderLayout.PAGE_START);
        
        DefaultTableModel model = new DefaultTableModel();
		JTable table = new JTable();
    	table.setModel(model);
        JScrollPane scrollPane = new JScrollPane(table); 
        contentPanel.add(scrollPane);  
		model.addColumn("ID");
//		model.addColumn("Name"); 
		model.addColumn("Type");
		model.addColumn("Amount");
		model.addColumn("Date");
    	String query = "SELECT * FROM fines WHERE email = '" + email + "'";

		Timer timer = new Timer(1000, (e) -> {
	    	try { 
	    		statement = connection.createStatement(); 
	    		model.setRowCount(0);
	    		ResultSet rs = statement.executeQuery(query);
	    		// add other column names
	    		int id = 1;  
	    		while (rs.next()) { 
//	    		  String name = rs.getString("name");
	    		  String type = rs.getString("type");
	    		  String amount = rs.getString("amount");  
	    		  String date = rs.getString("date");  
	    		  Object[] row = {id, type, amount, date}; 
	    		  model.addRow(row); 
	    		  id++;
	    		} 	    		
	    	}
	    	catch (SQLException exception){
	    		JOptionPane.showMessageDialog(null, "Data Loading Failed !", "Could not Load Records !", JOptionPane.WARNING_MESSAGE);
	            System.out.println("error : "+exception.toString());
	        } 
	        catch (Exception ex){
	        	JOptionPane.showMessageDialog(null, "Data Loading Failed !", "Could not Load Records !", JOptionPane.WARNING_MESSAGE);
	        	System.out.println("#####"+ex.toString());
	        } 
		}); 
	    timer.start();
	    
	    
	    JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(4, 1, 20, 20)); // Use null layout for absolute positioning

        JLabel usernameLabel = new JLabel("User Name"); 
        
        JLabel emailLabel = new JLabel("Email"); 

        JLabel numberPlateLabel = new JLabel("Number Plate");  

        JLabel phoneLabel = new JLabel("Phone Number");

        JLabel addLabel = new JLabel("Address");
        
        String que = "SELECT * FROM users WHERE email = '" + email + "'";
        try { 
    		statement = connection.createStatement(); 
    		model.setRowCount(0);
    		ResultSet rs = statement.executeQuery(que);
    		// add other column names 
    		while (rs.next()) {  
    		  String name = rs.getString("name");
    		  usernameLabel.setText("Username: " + name); 
    		  emailLabel.setText("Email: " + email);
    		  String numberplate = rs.getString("numberplate"); 
    		  numberPlateLabel.setText("Number Plate: " + numberplate);
    		  String phone = rs.getString("phone"); 
    		  phoneLabel.setText("Phone Number: " + phone);
    		  String address = rs.getString("address"); 
    		  addLabel.setText("Address: " + address);
    		} 	    		
    	}
    	catch (SQLException exception){
    		JOptionPane.showMessageDialog(null, "Data Loading Failed !", "Could not Load Records !", JOptionPane.WARNING_MESSAGE);
            System.out.println("error : "+exception.toString());
        } 
        catch (Exception ex){
        	JOptionPane.showMessageDialog(null, "Data Loading Failed !", "Could not Load Records !", JOptionPane.WARNING_MESSAGE);
        	System.out.println("#####"+ex.toString());
        } 

        
        panel.add(usernameLabel);// Add components to the panel 
        panel.add(emailLabel); 
        panel.add(phoneLabel); 
        panel.add(numberPlateLabel);
        panel.add(addLabel); 
	    
	    
	    
	    
	    
	 // Add action listeners to the menu items
	    fineMenu.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
            	contentPanel.removeAll();
        	    contentPanel.add(scrollPane); 
        	    contentPanel.revalidate();
        	    contentPanel.repaint();
            }
        });

	    infoMenu.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) { 
            	contentPanel.removeAll();
        	    contentPanel.add(panel);
        	    contentPanel.revalidate();
        	    contentPanel.repaint();
            }
        });
	    
	    
    	frame.setVisible(true); 
    } 
 

}
 
