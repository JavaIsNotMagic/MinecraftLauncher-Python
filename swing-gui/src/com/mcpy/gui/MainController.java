package com.mcpy.gui;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.stage.Window;

import com.mcpy.LoginHandler;
import com.mcpy.Play;
import com.mcpy.AccountHandler;
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
        LoginHandler.login();
    };
    
    @FXML    
    protected void create_accountButtonEvent(ActionEvent cabe) {
        AccountHandler.new();
    };
    
    @FXML    
    protected void playButtonActionEvent(ActionEvent pbae) {
        boolean authenticated = AccountHandler.login();
        if(authenticated) {
            Play.play_mc();
        } else {
            System.out.println("ERROR: Authentication Failed!");
        }
    }
}
