#include <iostream>
#include <memory>

using namespace std;

struct Node {
    int mId;
    Node(int id) : 
        mId(id)
    {
        cout << "Node::Node: mId=[" << mId << "]" << endl;
    }
    ~Node() 
    {
        cout << "Node::~Node" << endl;
    }
};

int main(int argc, char** args)
{
    cout << "TestUniquePointer: start" << endl;

    Node* pNode = new Node(123);
    int id1 = pNode->mId;
    cout << "id1=[" << id1 << "]" << endl;    // 123

    {
        unique_ptr<Node> upNode(pNode);
        int id2 = upNode->mId;
        cout << "id2=[" << id2 << "]" << endl;    // 123
        // upNode goes out of scope, pNode is deleted
    }

    int id3 = pNode->mId;
    cout << "id3=[" << id3 << "]" << endl;    // undefined behavior, most likely 0, or 123, or even a crash

    cout << "TestUniquePointer: end" << endl;

    return 0;
}
 
