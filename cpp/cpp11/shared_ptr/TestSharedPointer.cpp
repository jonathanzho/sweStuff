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
    cout << "TestSharedPointer: start" << endl;

    Node* pNode = new Node(123);
    int id1 = pNode->mId;
    cout << "id1=[" << id1 << "]" << endl;    // 123

    {
        shared_ptr<Node> sp1Node(pNode);
        int id2 = sp1Node->mId;
        cout << "id2=[" << id2 << "]" << endl;    // 123

        shared_ptr<Node> sp2Node(sp1Node);
        int id3 = sp2Node->mId;
        cout << "id3=[" << id3 << "]" << endl;    // 123

        // sp1Node goes out of scope, pNode is deleted.
    }

    int id4 = pNode->mId;
    cout << "id4=[" << id4 << "]" << endl;    // undefined behavior, most likely 0, or 123, or even a crash

    cout << "TestSharedPointer: end" << endl;

    return 0;
}
 
