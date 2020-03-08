import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Textfield;
import javafx.scene.control.PasswordField;
import javafx.stage.Window;

import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.IOException;

import com.mcpy.gui.Hash;

public class LoginController {

    @FXML
    private TextField username;

    @FXML
    private PasswordField password;

    @FXML
    private Button submit;

    @FXML
    protected void submitActionEvent(ActionEvent sae) {
        BufferedWriter writer = new BufferedWriter(new FileWriter("data/user_info.txt");
        try {
            writer.write(username.getText() + ":" + Hash.main(password.getText()));
            writer.close()
         } catch(IOException io) {
            io.printStackTrace();
      }
   }
}   
