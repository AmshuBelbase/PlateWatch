package com.example.platewatch;
//import java.sql.*;

import androidx.appcompat.app.AppCompatActivity;
import java.lang.*;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Handler;
import android.os.StrictMode;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class MainActivity extends AppCompatActivity {
    TextView dis;
    String records;
    Button show;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        dis = (TextView) findViewById(R.id.dis);
        show = (Button) findViewById(R.id.button);

        show.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view){
                String records = "";
                dis.setText("here");
                Task task = new Task();
                task.execute();
            }
        });
    }

    class Task extends AsyncTask<Void, Void, Void>{
        String records = "";

        @Override
        protected Void doInBackground(Void... voids) {
            try {
//                    StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
//                    StrictMode.setThreadPolicy(policy);
                Class.forName("com.mysql.cj.jdbc.Driver");
                Connection connection = DriverManager.getConnection("jdbc:mysql://192.168.66.29:3307/epiz_32083127_traffic", "amshuandroid", "amshuandroid");
                Statement statement = connection.createStatement();
                if(connection==null){
                    records = "FAiled";
                }
                else {
                    ResultSet resultSet = statement.executeQuery("SELECT * FROM users");
                    while (resultSet.next()) {
                        records += resultSet.getString(1) + "" + resultSet.getString(2) + "" + resultSet.getString(3) + "\n";
                    }
                }
                connection.close();
                statement.close();
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
            return null;
        }

        @Override
        protected void onPostExecute(Void aVoid) {
            dis.setText(records);
            super.onPostExecute(aVoid);
        }
    }
}