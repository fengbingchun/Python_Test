#ifndef TEST_DLL_1_MATH_OPERATIONS_HPP_
#define TEST_DLL_1_MATH_OPERATIONS_HPP_

#define FBC_EXPORTS extern "C" __declspec(dllexport)

//namespace fbc {

extern "C" FBC_EXPORTS int add_(int a, int b);
extern "C" FBC_EXPORTS int sub_(int a, int b);
extern "C" FBC_EXPORTS int mul_(int a, int b);
extern "C" FBC_EXPORTS int div_(int a, int b);

//} // namespace fbc

#endif // TEST_DLL_1_MATH_OPERATIONS_HPP_
