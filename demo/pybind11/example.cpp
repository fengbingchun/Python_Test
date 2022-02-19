#include <pybind11/pybind11.h>
#include <funset.hpp>

// reference: https://pybind11.readthedocs.io/en/stable/

namespace py = pybind11;

// If you prefer the py::overload_cast syntax but have a C++11 compatible compiler only,
// you can use py::detail::overload_cast_impl with an additional set of parentheses
template <typename... Args>
using overload_cast_ = pybind11::detail::overload_cast_impl<Args...>;

// #define PYBIND11_MODULE(name, variable): name: module name; variable: a variable of type `py::module_` which can be used to initialize the module
PYBIND11_MODULE(example, m) {
	m.doc() = "pybind11 example plugin"; // optional module docstring

	// 1. bindings for a simple function
	m.def("get_random_number", &get_random_number, "A function that get random number", py::arg("min"), py::arg("max"));

	// 2. bindings for a custom C++ data structure: class or struct
	// class_ creates bindings for a C++ class or struct-style data structure
	py::class_<Pet>(m, "Pet")
		 // init() is a convenience function that takes the types of a constructor’s parameters as template arguments and wraps the corresponding constructor
		.def(py::init<const std::string &>())
		.def("setName", &Pet::setName)
		.def("getName", &Pet::getName)

		// Static member functions can be bound in the same way using class_::def_static()
		.def_static("getAge", &Pet::getAge)

		// 3. Binding lambda functions
		.def("__repr__",
			[](const Pet &a) {
				return "<example.Pet named '" + a.name_ + "'>";
			}
		)

		// We can also directly expose the name_ field using the class_::def_readwrite() method.
		// A similar class_::def_readonly() method also exists for const fields
		.def_readwrite("name", &Pet::name_);

	// 4. class inheritance
	// There are two different ways of indicating a hierarchical relationship to pybind11:
	// the first specifies the C++ base class as an extra template parameter of the class_:
	py::class_<Dog, Pet /* <- specify C++ parent type */>(m, "Dog")
		.def(py::init<const std::string &>())
		.def("bark", &Dog::bark);

	// // Alternatively, we can also assign a name to the previously bound Pet class_ object and reference it when binding the Dog class
	// py::class_<Pet> pet(m, "Pet");
	// pet.def(py::init<const std::string &>())
   	// 	.def_readwrite("name", &Pet::name);

	// // Method 2: pass parent class_ object:
	// py::class_<Dog>(m, "Dog", pet /* <- specify Python parent type */)
	// 	.def(py::init<const std::string &>())
	// 	.def("bark", &Dog::bark);

	// 5. class polymorphic
	// In C++, a type is only considered polymorphic if it has at least one virtual function and pybind11 will automatically recognize this
	py::class_<PolymorphicPet>(m, "PolymorphicPet");
	py::class_<PolymorphicDog, PolymorphicPet>(m, "PolymorphicDog")
		.def(py::init<>())
		.def("bark", &PolymorphicDog::bark);

	// Again, return a base pointer to a derived instance
	// Given a pointer to a polymorphic base, pybind11 performs automatic downcasting to the actual derived type
	m.def("pet_store2", []() { return std::unique_ptr<PolymorphicPet>(new PolymorphicDog); });

	// 6. Overloaded methods
	py::class_<Pet2>(m, "Pet2")
		.def(py::init<const std::string &, int>())
		.def("set", static_cast<void (Pet2::*)(int)>(&Pet2::set), "Set the pet's age")
		.def("set", static_cast<void (Pet2::*)(const std::string &)>(&Pet2::set), "Set the pet's name")
		.def("getAge", &Pet2::getAge)
		.def("getName", &Pet2::getName);

	// If you have a C++14 compatible compiler, you can use an alternative syntax to cast the overloaded function
	// py::class_<Pet2>(m, "Pet2")
	// 	.def("set", py::overload_cast<int>(&Pet2::set), "Set the pet's age")
	// 	.def("set", py::overload_cast<const std::string &>(&Pet2::set), "Set the pet's name");

	// If a function is overloaded based on constness, the py::const_ tag should be used
	py::class_<Widget>(m, "Widget")
		.def("foo_mutable", overload_cast_<int, float>()(&Widget::foo))
		.def("foo_const",   overload_cast_<int, float>()(&Widget::foo, py::const_));

	// 7. Enumerations and internal types: nested types
	py::class_<Pet3> pet(m, "Pet3");

	pet.def(py::init<const std::string &, Pet3::Kind>())
		.def_readwrite("name", &Pet3::name_)
		.def_readwrite("type", &Pet3::type_)
		.def_readwrite("attr", &Pet3::attr_);

	py::enum_<Pet3::Kind>(pet, "Kind")
		.value("Dog", Pet3::Kind::Dog)
		.value("Cat", Pet3::Kind::Cat)
		.export_values();

	py::class_<Pet3::Attributes>(pet, "Attributes")
		.def(py::init<>())
		.def_readwrite("age", &Pet3::Attributes::age);
}
