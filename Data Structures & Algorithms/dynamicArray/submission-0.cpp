class DynamicArray {
public:
    //member functions
    DynamicArray(int capacity) {
      myarr = new int[capacity];
      m_capacity = capacity;
      m_size = 0;  
    }

    int get(int i) {
        //assuming validity of index
        return myarr[i];
    }

    void set(int i, int n) {
        //assuming validity of index
        myarr[i] = n;
    }

    void pushback(int n) {
        if(m_size >= m_capacity){ 
            /*if size is greater than or equal to
            capacity the array is full so we resize the array*/
            resize();
        }
        //setting array values
        myarr[m_size] = n;
        m_size++;
    }

    int popback() {
        //setting the
        int poppedItem = myarr[m_size - 1];
        myarr[m_size - 1] = 0; 
        m_size--;
        return poppedItem;
    
    }

    void resize() {
        m_capacity = m_capacity * 2; 
        int * newArr = new int[m_capacity];
        for(int i = 0; i < m_size; i++){ 
            //copying items in old array into the new one
            newArr[i] = myarr[i];
        }
        delete [] myarr; 
        //setting array to the new array of doubled capacity
        myarr = newArr;
    }

    int getSize() {
        return m_size;
    }

    int getCapacity() {
        return m_capacity;
    }
    //member variables
    private: 
    int * myarr; 
    int m_capacity;
    int m_size; 

};
