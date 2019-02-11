public class Horse extends Animal implements ICanRunAnimal {
    public Horse(String name) {
	super(name);
	System.out.println("[D] Horse::Horse: name=[" + name + "]");
    }

    public void run() {
	System.out.println("[D] Horse::run with 4 legs");
    }
}

