public class Bird extends Animal implements ICanFlyAnimal {
    public Bird(String name) {
	super(name);
	System.out.println("[D] Bird::Bird: name=[" + name + "]");
    }

    public void fly() {
	System.out.println("[D] Bird::fly with 2 wings and 2 legs");
    }

    public void run() {
	System.out.println("[D] Bird::run with 2 legs and 2 wings");
    }
}

