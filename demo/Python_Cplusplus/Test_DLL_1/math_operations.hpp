#ifndef TEST_DLL_1_MATH_OPERATIONS_HPP_
#define TEST_DLL_1_MATH_OPERATIONS_HPP_

#ifdef __linux__
	#define FBC_EXPORTS __attribute__((visibility("default")))
#else
	#define FBC_EXPORTS __declspec(dllexport)
#endif

#ifdef __cplusplus
extern "C" {
#endif

FBC_EXPORTS int add_(int a, int b);
FBC_EXPORTS int sub_(int a, int b);
FBC_EXPORTS int mul_(int a, int b);
FBC_EXPORTS int div_(int a, int b);

#ifdef __cplusplus
}
#endif

#endif // TEST_DLL_1_MATH_OPERATIONS_HPP_
