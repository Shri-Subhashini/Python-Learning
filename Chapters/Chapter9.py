#  classes themselves are objects. This provides semantics for importing and renaming -
# When you import a module, you are essentially importing a namespace containing objects, including classes.
# You can rename a class during import using the as keyword, which allows you to refer to the class by a different name within your current scope. 
# import my_module  ; from my_module import MyClass as RenamedClass
'''
In C++,

virtual - In C++, declaring all member functions as virtual, or making a class abstract by having pure virtual functions, enables polymorphism, allowing derived classes to override base functions and ensuring correct implementation.

class Base {
public:
    virtual void someFunction() {
        // Base class implementation
    }
};

class Derived : public Base {
public:
    void someFunction() override {
        // Derived class implementation
    }
};
'''

