class Microwave {
    String brand;
    String powerrating;
    boolean turned_on;
    public Microwave(String brand, String powerrating) {
        this.brand = brand;
        this.powerrating = powerrating;
        this.turned_on = false;
    }
    public void turn_on() {
        if (turned_on) {
            System.out.println("Microwave is turned on");
        } else {
            turned_on = true;
            System.out.println("Microwave is already turned on");
        }
    }
    public void turn_off() {
        if (turned_on) {
            turned_on = false;
            System.out.println("Microwave is turned off");
        } else {
            System.out.println("Microwave is already turned off");
        }
    }
    public void run(int seconds) {
        if (turned_on) {
            System.out.println("Running " + brand + " for " + seconds + " seconds");
        } else {
            System.out.println("Microwave is not turned on");
        }
    }

    public String toString() { // dunder method
        return brand + " " + powerrating;
    }
}

class Main{
    public static void main(String[] args){
        Microwave smeg = new Microwave("Smeg", "B");
        System.out.println(smeg);
        smeg.turn_on();
        smeg.run(10);
        smeg.turn_off();
    }
}