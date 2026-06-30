#include <vector>
struct Node{ 
    int m_data; 
    Node * m_next; 
    Node(int data):m_data(data),m_next(nullptr){}
};
class LinkedList {
private:
    Node * m_head; 
    Node * m_tail; 
    int m_size;
public:
    LinkedList():m_head(nullptr),m_tail(nullptr),m_size(0){}

    int get(int index) {
        if(index >= m_size){ 
            return -1;
        }else{ 
            int count = 0;
            Node * temp = m_head;
            while(count != index){ 
                temp = temp -> m_next;
                count++;
            }
            return temp -> m_data; 
        }
    }

    void insertHead(int val){
        Node * newnode = new Node(val);
        if(m_head == nullptr){
            m_head = newnode; 
            m_tail = newnode;
        }else{ 
            newnode -> m_next = m_head; 
            m_head = newnode;
        }
        m_size++;
    }
    
    void insertTail(int val) {
        Node * newnode = new Node(val);
        if(m_tail == nullptr){ 
            m_head = newnode; 
            m_tail = newnode; 
        }else{ 
            m_tail -> m_next = newnode; 
            m_tail = newnode; 
        }
        m_size++;
    }

    bool remove(int index) {
        if(index >= m_size || index < 0){ 
            return false;
        }   
        if(index == 0){ 
            //edge case of removing the head
            Node * temp = m_head; 
            m_head = m_head -> m_next; 
            delete temp; 
            temp = nullptr; 
            m_size--; 
            return true; 
        }
        Node * temp = m_head; 
        Node * prev = nullptr; 
        int count = 0;
        while(count != index){ 
            prev = temp;
            temp = temp -> m_next; 
            count++;
        }
        prev -> m_next = temp -> m_next; 
        if(prev -> m_next == nullptr){ 
            m_tail = prev; 
        }
        delete temp; 
        temp = nullptr; 
        m_size--;
        return true;
    }

    vector<int> getValues() {
        vector <int> myvec;
        Node * temp = m_head; 
        while(temp != nullptr){ 
            myvec.push_back(temp -> m_data);
            temp = temp -> m_next;
        }
        return myvec;
    }
    
};
