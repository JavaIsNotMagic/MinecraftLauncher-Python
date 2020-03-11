import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.control.PasswordField;

//import com.mcpy.gui.Hash;
import com.mcpy.gui.AccountHandler;

public class LoginController {

    @FXML
    private TextField username;

    @FXML
    private PasswordField password;

    @FXML
    private Button submit;

    @FXML
    protected void submitActionEvent(ActionEvent sae) {
        AccountHandler.authUser(username.getText(), password.getText());
    }

}
