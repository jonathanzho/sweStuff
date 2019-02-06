public class Pegasus extends Animal implements ICanRunAnimal, ICanFlyAnimal {
    public Pegasus(String name) {
	super(name);
	System.out.println("[D] Pegasus::Pegasus: name=[" + name + "]");
    }

    public void fly() {
	System.out.println("[D] Pegasus::fly with 2 wings and 4 legs");
    }

    public void run() {
	System.out.println("[D] Pegasus::run with 4 legs and 2 wings");
    }
}

