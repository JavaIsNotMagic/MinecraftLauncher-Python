package com.mcpy.gui;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.stage.Window;

import com.mcpy.gui.Play;
import com.mcpy.gui.Login;
import com.mcpy.gui.CreateAccount;
/* Logic for the main gui. DO NOT EDIT. */

public class MainController {

    @FXML
    private static Button login;
    
    @FXML
    private static Button create_account;

    @FXML 
    private static Button play;

    @FXML
    protected void loginButtonEvent(ActionEvent lbe) {
        String[] args = (null);        
        Login.main(args);
    };
    
    @FXML    
    protected void create_accountButtonEvent(ActionEvent cabe) {
        String[] args = (null);          
        CreateAccount.main(args);
    };
    
    @FXML    
    protected void playButtonActionEvent(ActionEvent pbae) {       
        Play.play_mc();
    }
}
