#ifndef PYBIND11_FUNSET_HPP_
#define PYBIND11_FUNSET_HPP_

#include <string>

#define PYBIND11_API __attribute__((visibility ("default")))

PYBIND11_API int get_random_number(int min, int max);

struct PYBIND11_API Pet {
    Pet(const std::string& name) : name_(name) { }
    void setName(const std::string& name) { name_ = name; }
    const std::string& getName() const { return name_; }

    static int getAge() { return 18; }

    std::string name_;
};

struct Dog : Pet {
    Dog(const std::string& name) : Pet(name) { }
    std::string bark() const { return "woof!"; }
};

struct PolymorphicPet {
    virtual ~PolymorphicPet() = default;
};

struct PolymorphicDog : PolymorphicPet {
    std::string bark() const { return "woof!"; }
};

struct Pet2 {
    Pet2(const std::string& name, int age) : name_(name), age_(age) { }

    void set(int age) { age_ = age; }
    void set(const std::string& name) { name_ = name; }
    int getAge() const { return age_; }
    const std::string& getName() const { return name_; }

    std::string name_;
    int age_;
};

struct Widget {
    int foo(int x, float y) { return 0; };
    int foo(int x, float y) const { return 1; };
};

struct Pet3 {
    enum Kind {
        Dog = 0,
        Cat
    };

    struct Attributes {
        float age = 0;
    };

    Pet3(const std::string& name, Kind type) : name_(name), type_(type) { }

    std::string name_;
    Kind type_;
    Attributes attr_;
};

#endif // PYBIND11_FUNSET_HPP_