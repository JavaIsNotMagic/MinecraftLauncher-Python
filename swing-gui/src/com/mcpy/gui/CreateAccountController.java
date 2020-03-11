import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.control.PasswordField;
import javafx.stage.Window;

import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.IOException;

//import com.mcpy.gui.Hash;
import com.mcpy.gui.AccountHandler;

public class CreateAccountController {

    @FXML
    private TextField username;

    @FXML
    private PasswordField password;
    
    @FXML
    private TextField email;

    @FXML
    private Button submit;

    @FXML
    protected void submitActionEvent(ActionEvent sae) {
        AccountHandler.accountCreate(username.getText(), password.getText(), email.getText());
   }
}   
