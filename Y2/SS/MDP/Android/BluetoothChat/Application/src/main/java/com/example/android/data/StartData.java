package com.example.android.data;

public class StartData {
    private Integer ID,x,y;
    private String z,imageID;

    public StartData (Integer ID, Integer x, Integer y, String z, String imageID){
        this.ID = ID;
        this.x = x;
        this.y = y;
        this.z = z;
        this.imageID = imageID;
    }

    public Integer getID(){ return  ID;}

    public Integer getX(){ return x; }

    public Integer getY(){ return y; }

    public String getZ(){ return z; }

    public String getImageID(){ return imageID;}

    public void setImageID( String imageID ){ this.imageID = imageID; }

    public String toString(){
        return String.valueOf(x) + "," + String.valueOf(y) + "," + z;
    }
}
