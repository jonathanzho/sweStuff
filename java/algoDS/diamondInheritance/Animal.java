public class Animal {
    private String mName;

    public Animal(String name) {
	System.out.println("[D] Animal::Animal: name=[" + name + "]");
	mName = name;
    }

    public String getName() {
	System.out.println("[D] Animal::getName: mName=[" + mName + "]");
	return mName;
    }

    public void setName(String name) {
	System.out.println("[D] Animal::setName: name=[" + name + "]");
	mName = name;
    }
}

