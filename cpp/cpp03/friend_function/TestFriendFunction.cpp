#include <iostream>

using namespace std;

class Node {
public:
   int mPublicInt;
protected:
   int mProtectedInt;
private:
   int mPrivateInt;
public:
    Node(int publicInt, int protectedInt, int privateInt) :
        mPublicInt(publicInt),
        mProtectedInt(protectedInt),
        mPrivateInt(privateInt)
    {
        cout << "Node::Node: mPublicInt=[" << mPublicInt << "], mProtectedInt=[" << mProtectedInt << "], mPrivateInt=[" << mPrivateInt << "]" << endl;
    }
public:
    ~Node()
    {
        cout << "Node::~Node" << endl;
    }
    friend void myFriendFunction(const Node& node);
};

void myFriendFunction(const Node& node)
{   
    int publicInt = node.mPublicInt;
    int protectedInt = node.mProtectedInt;
    int privateInt = node.mPrivateInt;
         
    cout << "myFriendFunction: publicInt=[" << publicInt << "], protectedInt=[" << protectedInt << "], privateInt=[" << privateInt << "]" << endl;
}

int main(int argc, char** argv)
{
    cout << "TestFriendFunction: start" << endl;

    Node node(123, 456, 789);

    myFriendFunction(node);

    cout << "TestFriendFunction: end" << endl;

    return 0;
}
  
