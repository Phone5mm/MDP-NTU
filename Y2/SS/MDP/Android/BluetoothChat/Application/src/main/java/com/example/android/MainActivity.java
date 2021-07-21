/*
 * Copyright 2013 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


package com.example.android;

import android.app.AlertDialog;
import android.content.ClipData;
import android.content.Intent;
import android.content.res.ColorStateList;
import android.icu.text.CaseMap;
import android.os.Build;
import android.os.Bundle;
import android.util.TypedValue;
import android.view.DragEvent;
import android.view.Gravity;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.ImageView;
import android.widget.Switch;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.ToggleButton;

import androidx.annotation.RequiresApi;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.constraintlayout.widget.ConstraintSet;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentTransaction;

import com.example.android.bluetoothchat.BluetoothChatFragment;
import com.example.android.bluetoothchat.R;
import com.example.android.common.activities.SampleActivityBase;
import com.example.android.data.StartData;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 * A simple launcher activity containing a summary sample description, sample log and a custom
 * {@link Fragment} which can display a view.
 * <p>
 * For devices with displays with a width of 720dp or greater, the sample log is always visible,
 * on other devices it's visibility is controlled by an item on the Action Bar.
 */
public class MainActivity extends SampleActivityBase implements View.OnClickListener{

    StartData ROBOT_START_POS = new StartData(0000,0,0,"0","-");
    String AUTO_MANUAL = "MANUAL";

    BluetoothChatFragment fragment;

    TextView textViewInfo;
    ImageView robotImage;
    Button buttonObs;
    Button buttonRbt;
    Button buttonStart;
    Button buttonCam;
    ToggleButton autoManual;

    TextView popUpTextViewImageID;
    TextView popUpTextViewPos;
    ImageView popUpImage;
    Button popUpButton;

    List<StartData> startDataList = new ArrayList<StartData>();
    StartData coordinate;
    StartData robotPos;

    Integer idNum;
    String robotMode;


    private AlertDialog.Builder dialogBuilder;
    private AlertDialog dialog;

    public static final String TAG = "MainActivity";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button buttonUp = findViewById(R.id.buttonUp);
        Button buttonDown = findViewById(R.id.buttonDown);
        Button buttonLeft = findViewById(R.id.buttonLeft);
        Button buttonRight = findViewById(R.id.buttonRight);

        buttonObs = findViewById(R.id.buttonObs);
        buttonRbt = findViewById(R.id.buttonRobot);
        buttonStart = findViewById(R.id.buttonStart);
        buttonCam = findViewById(R.id.buttonCam);

        autoManual = findViewById(R.id.autoManual);

        robotImage = findViewById(R.id.robotImage);

        buttonUp.setOnClickListener(this);
        buttonDown.setOnClickListener(this);
        buttonLeft.setOnClickListener(this);
        buttonRight.setOnClickListener(this);
        buttonObs.setOnClickListener(this);
        buttonRbt.setOnClickListener(this);
        buttonStart.setOnClickListener(this);
        buttonCam.setOnClickListener(this);

        buttonObs.setOnLongClickListener(longClickListener);
        buttonRbt.setOnLongClickListener(longClickListener);

        robotPos = ROBOT_START_POS;
        robotMode = AUTO_MANUAL;

        populateMap();

        if (savedInstanceState == null) {
            FragmentTransaction transaction = getSupportFragmentManager().beginTransaction();
            fragment = new BluetoothChatFragment();
            transaction.replace(R.id.sample_content_fragment, fragment);
            transaction.commit();
        }

        autoManual.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked) {
                    robotMode = "AUTO";
                    robotImage.requestLayout();
                    robotImage.getLayoutParams().height = 108;
                    robotImage.getLayoutParams().width = 108;
                } else {
                    robotMode = "MANUAL";
                    robotImage.requestLayout();
                    robotImage.getLayoutParams().height = 72;
                    robotImage.getLayoutParams().width = 72;
                }
            }
        });


    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    public void updateStatus(String statusMsg){
        textViewInfo = findViewById(R.id.textViewInfo);

        textViewInfo.setText(statusMsg);
    }

    public void populateMap(){

        TableLayout tableLayout = findViewById(R.id.mapLayout);

        for (int i = 0; i < 21; i++) {
            TableRow tableRow = new TableRow(this);

            TextView textView = new TextView(this);
            if(i==20){
                textView.setText("");
            }
            else{
                textView.setText(Integer.toString(19 - i));
            }
            textView.setGravity(Gravity.TOP);

            tableRow.addView(textView, new TableRow.LayoutParams(0, 36, 1f));

            if (i == 20) {
                for (int k = 0; k < 20; k++) {
                    TextView textView1 = new TextView(this);
                    textView1.setText(Integer.toString(k));
                    textView.setGravity(Gravity.CENTER);

                    tableRow.addView(textView1, new TableRow.LayoutParams(0, TableRow.LayoutParams.WRAP_CONTENT, 1f));
                }
            } else {
                Button button;
                for (int j = 0; j < 20; j++) {
                    int l = 19 - i;
                    int idNum = ((j * 100) + l);
                    button = new Button(this);
                    button.setId(idNum);
                    button.setOnClickListener(this);
                    button.setOnDragListener(dragListener);
                    button.setOnLongClickListener(longClickListener);
                    button.setBackgroundTintList(
                            ColorStateList.valueOf(getResources().getColor(R.color.colorGray)));
                    tableRow.addView(button, new TableRow.LayoutParams(0, 36, 1f));

                }
            }
            tableLayout.addView(tableRow, i);
        }
    }

    @RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
    public void incomingMessage(String readMsg) {

        if(readMsg.length()>0){
            String message[];
            // - delimiter for imgReg, : delimiter for everything else
            if(readMsg.contains(":")) {
                message = readMsg.split(":");
            }else{
                message = readMsg.split("-");
            }

            switch (message[0]) {
                case "M":
                    switch (message[1]) {
                        case "F":
                            updateStatus((String) getText(R.string.mvgF));
                            updateRobotPos("MOVE FWR");
                            break;
                        case "L":
                            updateStatus((String) getText(R.string.mvgL));
                            updateRobotPos("MOVE LFT");
                            break;
                        case "B":
                            updateStatus((String) getText(R.string.mvgB));
                            updateRobotPos("MOVE BKR");
                            break;
                        case "R":
                            updateStatus((String) getText(R.string.mvgR));
                            updateRobotPos("MOVE RGT");
                            break;
                        case "SI":
                            updateStatus((String) getText(R.string.scanI));
                            break;
                        case "DONE":
                            updateStatus((String) getText(R.string.doneM));
                            break;
                    }
                    break;
                case "I":
                    String messageImg[];
                    String messageImgID = "";

                    messageImg = message[1].split(",");

                    if(robotMode.equals("AUTO")) {
                        Button buttonImg = findViewById(Integer.parseInt(messageImg[0]));

                        messageImgID = ((Integer.valueOf(messageImg[0]))/100) + ", "+((Integer.valueOf(messageImg[0]))%100);

                        buttonImg.setText(messageImg[1]);
                        //dropButton.setBackgroundColor(getResources().getColor(R.color.colorAccent));
                        buttonImg.setBackgroundTintList(ColorStateList.valueOf(getResources().getColor(R.color.colorPrimary)));

                        for (int i=0; i < startDataList.size(); i++){
                            StartData sd = startDataList.get(i);
                            if (sd.getID() == buttonImg.getId()){

                                sd.setImageID(messageImg[1]);

                            }
                        }


                    }

                    TextView imageResult = findViewById(R.id.imageResult);

                    imageResult.append("Obs "+ messageImgID+ ": " + messageImg[1] + "\t");

                    break;
                default:
                    updateStatus("Invalid Message");
                    break;
            }
        }
    }

    public void outgoingMessage(String sendMsg) {
        fragment.sendMsg(sendMsg);
        //Toast.makeText(getApplicationContext(),sendMsg,Toast.LENGTH_SHORT).show();
    }

    public void updateRobotPos(String action){
        int x1 = robotPos.getX();
        int y1 = robotPos.getY();
        String z1 = robotPos.getZ();

        int cons2 = 36;

        switch(action) {
            case "MOVE FWR":

                ConstraintLayout constraintLayoutF = findViewById(R.id.constraintLayOut);
                ConstraintSet constraintSetF = new ConstraintSet();

                constraintSetF.clone(constraintLayoutF);

                switch (z1) {
                    case "0":
                        y1 = y1 + 1;
                        break;
                    case "1":
                        x1 = x1 + 1;
                        break;
                    case "2":
                        y1--;
                        break;
                    case "3":
                        x1--;
                        break;
                    default:
                        break;
                }

                if(x1>10){
                    cons2 = 38;
                }
                if(x1>14){
                    cons2 = 42;
                }

                constraintSetF.connect(R.id.robotImage, ConstraintSet.LEFT,
                        R.id.mapLayout, ConstraintSet.LEFT, cons2 + (35 * (x1)));
                constraintSetF.connect(R.id.robotImage, ConstraintSet.BOTTOM,
                        R.id.mapLayout, ConstraintSet.BOTTOM, 26 + (36 * (y1)));

                constraintSetF.applyTo(constraintLayoutF);

                robotPos = new StartData(idNum, x1, y1 , z1, "-");

                break;
            case "MOVE BKR":

                ConstraintLayout constraintLayoutB = findViewById(R.id.constraintLayOut);
                ConstraintSet constraintSetB = new ConstraintSet();

                constraintSetB.clone(constraintLayoutB);

                switch (z1) {
                    case "0":
                        y1 = y1 - 1;
                        break;
                    case "1":
                        x1 = x1 - 1;
                        break;
                    case "2":
                        y1++;
                        break;
                    case "3":
                        x1++;
                        break;
                    default:
                        break;
                }

                if(x1>10){
                    cons2 = 38;
                }
                if(x1>14){
                    cons2 = 42;
                }

                constraintSetB.connect(R.id.robotImage, ConstraintSet.LEFT,
                        R.id.mapLayout, ConstraintSet.LEFT, cons2 + (35 * (x1)));
                constraintSetB.connect(R.id.robotImage, ConstraintSet.BOTTOM,
                        R.id.mapLayout, ConstraintSet.BOTTOM, 26 + (36 * (y1)));

                constraintSetB.applyTo(constraintLayoutB);

                robotPos = new StartData(idNum, x1, y1 , z1, "-");

                break;
            case "MOVE LFT":

                robotImage.setRotation(robotImage.getRotation()-90);

                if(z1.equals("0")){
                    z1="3";
                } else if(z1.equals("1")){
                    z1="0";
                } else if(z1.equals("2")){
                    z1="1";
                } else if(z1.equals("3")){
                    z1="2";
                }

                robotPos = new StartData(idNum,x1,y1,z1,"-");

                break;

            case "MOVE RGT":

                robotImage.setRotation(robotImage.getRotation()+90);

                if(z1.equals("0")){
                    z1="1";
                } else if(z1.equals("1")){
                    z1="2";
                } else if(z1.equals("2")){
                    z1="3";
                } else if(z1.equals("3")){
                    z1="0";
                }

                robotPos = new StartData(idNum,x1,y1,z1,"-");

                break;

            default:
                break;

        }

    }

    @RequiresApi(api = Build.VERSION_CODES.N)
    public void onClick(View v) {
        String cmdText = null;
        switch (v.getId()) {
            case R.id.buttonUp:
                cmdText = "w";
                outgoingMessage(cmdText);
                //updateRobotPos("MOVE FWR");
                break;
            case R.id.buttonDown:
                cmdText = "s";
                outgoingMessage(cmdText);
                //updateRobotPos("MOVE BKR");
                break;
            case R.id.buttonLeft:
                cmdText = "a";
                outgoingMessage(cmdText);
                //updateRobotPos("MOVE LFT");
                break;
            case R.id.buttonRight:
                cmdText = "d";
                outgoingMessage(cmdText);
                //updateRobotPos("MOVE RGT");
                break;
            case R.id.buttonStart:
                //cmdText = startDataList .toString();
                outgoingMessage(robotMode);
                if(robotMode.equals("AUTO")){
                    cmdText = startDataList.stream().map(Object::toString)
                            .collect(Collectors.joining(","));
                    outgoingMessage(cmdText);
                }
                break;
            case R.id.buttonObs:
                if(buttonObs.getText().equals("O")){
                    buttonObs.setText("N");
                    buttonObs.setTag("0");
                }
                else if(buttonObs.getText().equals("N")){
                    buttonObs.setText("E");
                    buttonObs.setTag("1");
                }
                else if(buttonObs.getText().equals("E")){
                    buttonObs.setText("S");
                    buttonObs.setTag("2");
                }
                else if(buttonObs.getText().equals("S")){
                    buttonObs.setText("W");
                    buttonObs.setTag("3");
                }
                else if(buttonObs.getText().equals("W")){
                    buttonObs.setText("N");
                    buttonObs.setTag("0");
                }
                break;
            case R.id.buttonRobot:
                if(buttonRbt.getText().equals("R")){
                    buttonRbt.setText("N");
                    buttonRbt.setTag("0");
                }
                else if(buttonRbt.getText().equals("N")){
                    buttonRbt.setText("E");
                    buttonRbt.setTag("1");
                }
                else if(buttonRbt.getText().equals("E")){
                    buttonRbt.setText("S");
                    buttonRbt.setTag("2");
                }
                else if(buttonRbt.getText().equals("S")){
                    buttonRbt.setText("W");
                    buttonRbt.setTag("3");
                }
                else if(buttonRbt.getText().equals("W")){
                    buttonRbt.setText("N");
                    buttonRbt.setTag("0");
                }
                break;
            case R.id.buttonCam:
                cmdText = "c";
                outgoingMessage(cmdText);
                break;


            default:

                //cmdText = Integer.toString(v.getId());

                for (int i=0; i < startDataList.size(); i++){
                    StartData sd = startDataList.get(i);
                    if (sd.getID() == v.getId()){

                    createNewContactDialog(sd.getID(), sd.getZ(), sd.getImageID());

                    }
                }



                //startActivity(new Intent(MainActivity.this, Pop.class));
                break;
        }
        // Send command to Arduino board
        //connectedThread.write(cmdText);
        //Toast.makeText(getApplicationContext(),cmdText,Toast.LENGTH_SHORT).show();
    }

    View.OnLongClickListener longClickListener = new View.OnLongClickListener(){
        @Override
        public boolean onLongClick(View v) {

            for (int i=0; i < startDataList.size(); i++){
                StartData sd = startDataList.get(i);
                if (sd.getID() == v.getId()){
                    startDataList.remove(i);

                    Button buttonTemp = findViewById(v.getId());
                    buttonTemp.setBackgroundTintList(ColorStateList.valueOf(getResources().getColor(R.color.colorGray)));
                    buttonTemp.setText("");

                }
            }

            ClipData data = ClipData.newPlainText("","");
            View.DragShadowBuilder myShadowBuilder = new View.DragShadowBuilder(v);
            v.startDrag(data,myShadowBuilder,v, 0);
            return true;
        }
    };

    View.OnDragListener dragListener = new View.OnDragListener(){

        @RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
        @Override
        public boolean onDrag(View v, DragEvent event) {

            int dragEvent = event.getAction();
            final View view = (View) event.getLocalState();

            switch (dragEvent){
                case DragEvent.ACTION_DRAG_ENTERED:
                    int dragArea = v.getId();
                    int x1 = dragArea/100;
                    int y1 = dragArea%100;
                    updateStatus("Map Location " + x1 + ", " + y1);
                    break;

                case DragEvent.ACTION_DRAG_EXITED:
                    updateStatus("");
                    break;

                case DragEvent.ACTION_DROP:
                    int dropArea = v.getId();
                    int x = dropArea/100;
                    int y = dropArea%100;
                    String z;

                    Button dropButton = findViewById(v.getId());
                    if (view.getId() == R.id.buttonObs){
                        if (buttonObs.getText().equals("O")) {

                            Toast.makeText(getApplicationContext(), "Please select orientation",Toast.LENGTH_SHORT).show();

                        } else {
                            dropButton.setText(buttonObs.getText());
                            //dropButton.setBackgroundColor(getResources().getColor(R.color.colorAccent));
                            dropButton.setBackgroundTintList(ColorStateList.valueOf(getResources().getColor(R.color.colorAccent)));
                            dropButton.setAutoSizeTextTypeUniformWithConfiguration(1, 17, 1, TypedValue.COMPLEX_UNIT_DIP);

                            idNum = dropButton.getId();

                            z = buttonObs.getTag().toString();

                            coordinate = new StartData(idNum,x,y,z,"-");
                            startDataList.add(coordinate);

                        }
                    }
                    else if (view.getId() == R.id.buttonRobot){
                        if (buttonRbt.getText().equals("R")) {

                            Toast.makeText(getApplicationContext(), "Please select orientation",Toast.LENGTH_SHORT).show();

                        }
                        else {

                            ConstraintLayout constraintLayout = findViewById(R.id.constraintLayOut);
                            ConstraintSet constraintSet = new ConstraintSet();


                            constraintSet.clone(constraintLayout);

                            constraintSet.clear(R.id.robotImage, ConstraintSet.TOP);
                            constraintSet.clear(R.id.robotImage, ConstraintSet.LEFT);
                            constraintSet.clear(R.id.robotImage, ConstraintSet.RIGHT);
                            constraintSet.clear(R.id.robotImage, ConstraintSet.BOTTOM);

                            int cons1 = 36;
                            if(x>10){
                                cons1 = 38;
                            }
                            if(x>14){
                                cons1 = 42;
                            }
                            constraintSet.connect(R.id.robotImage, ConstraintSet.LEFT,
                                    R.id.mapLayout, ConstraintSet.LEFT, cons1 + (35 * (x)));
                            constraintSet.connect(R.id.robotImage,ConstraintSet.BOTTOM,
                                    R.id.mapLayout,ConstraintSet.BOTTOM,26 + (36 * (y)));

                            constraintSet.applyTo(constraintLayout);

                            z = buttonRbt.getTag().toString();

                            robotPos = new StartData(idNum,x,y,z,"-");

                            switch (z) {
                                case "0":
                                    robotImage.setRotation(180);
                                    break;
                                case "1":
                                    robotImage.setRotation(270);
                                    break;
                                case "2":
                                    robotImage.setRotation(0);
                                    break;
                                case "3":
                                    robotImage.setRotation(90);
                                    break;
                                default:
                                    break;
                            }
                        }
                    }
                    break;
            }
            return true;
        }
    };

    public void  createNewContactDialog(int ID, String face, String imageResultID){
        dialogBuilder = new AlertDialog.Builder(this);
        final View contactPopupView = getLayoutInflater().inflate(R.layout.popup,null);

        popUpImage = contactPopupView.findViewById(R.id.popUpObs);
        popUpTextViewImageID = contactPopupView.findViewById(R.id.popUpTextID);
        popUpTextViewPos = contactPopupView.findViewById(R.id.popUpTextPos);

        dialogBuilder.setView(contactPopupView);
        dialog = dialogBuilder.create();
        dialog.show();

        popUpTextViewPos.setText("Position \t : " + "x: "+(ID/100)+" y: "+(ID%100));
        popUpTextViewImageID.setText("Image ID\t : "+ imageResultID);

        if(face.equals("0")){
            popUpImage.setRotation(0);
        } else if(face.equals("1")){
            popUpImage.setRotation(90);
        } else if(face.equals("2")){
            popUpImage.setRotation(180);
        } else if(face.equals("3")){
            popUpImage.setRotation(270);
        }


    }

}