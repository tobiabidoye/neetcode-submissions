class DynamicArray {
public:

    DynamicArray(int capacity):size(0),cap(capacity){
        myarr = new int[capacity];
    }

    int get(int i) {
        return myarr[i];
    }

    void set(int i, int n) {
        myarr[i] = n;
    }

    void pushback(int n) {
        if(size >= cap){
            resize();
        }
        myarr[size] = n;
        size++;
    }

    int popback() {
        int poppedItem = myarr[size - 1];
        myarr[size-1] = 0; 
        size --;
        return poppedItem;
    }

    void resize() {
        cap = cap*2; 
        int * newarr = new int[cap];
        for(int i = 0; i < size; i++){ 
            newarr[i] = myarr[i];
        }
        delete [] myarr; 
        myarr = newarr;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return cap;
    }
    private: 
    int * myarr; 
    int size; 
    int cap;
};
