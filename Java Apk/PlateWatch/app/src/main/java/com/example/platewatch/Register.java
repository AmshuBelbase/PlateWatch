package com.example.platewatch;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;

public class Register extends AppCompatActivity {

    EditText email, numplate, phone;
    Button regBtn;
    TextView login;
    ProgressBar progressBar;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        email = findViewById(R.id.email);
        numplate = findViewById(R.id.numberplate);
        phone = findViewById(R.id.phone);
        regBtn = findViewById(R.id.regButton);
        login = findViewById(R.id.already);

        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(getApplicationContext(), LogIn.class));
            }
        });

        regBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String uemail = email.getText().toString().trim();
                String unumplate = numplate.getText().toString().trim();
                String uphone = phone.getText().toString().trim();
                if(TextUtils.isEmpty(uemail)){
                    email.setError("Email is required");
                    return;
                }
                if(TextUtils.isEmpty(unumplate)){
                    numplate.setError("Number Plate is required");
                    return;
                }
                if(TextUtils.isEmpty(uphone)){
                    phone.setError("Phone Number is required");
                    return;
                }
                if(!TextUtils.isDigitsOnly(uphone)){
                    phone.setError("Only Numbers are Allowed");
                    return;
                }
                if(!uemail.contains("@") || !uemail.contains(".com")){
                    email.setError("Please enter your correct Email");
                    return;
                }
                progressBar.setVisibility(view.VISIBLE);
                // This code is for establishing connection with MySQL
                // database and retrieving data
                // from db Java Database connectivity

                /*
                 *1. import --->java.sql
                 *2. load and register the driver ---> com.jdbc.
                 *3. create connection
                 *4. create a statement
                 *5. execute the query
                 *6. process the results
                 *7. close
                 */



            }
        });
    }


}