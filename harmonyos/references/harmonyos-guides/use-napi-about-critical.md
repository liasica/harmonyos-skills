---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-critical
title: 使用扩展的Node-API接口创建和销毁临界区作用域及访问字符串内容
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用扩展的Node-API接口创建和销毁临界区作用域及访问字符串内容
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:11+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f80de86d50f06df0eedaff0aefbde4ec62eb99d6ae53a1822141756469e04f98
---

Node-API扩展接口napi\_open\_critical\_scope用于打开临界区作用域，napi\_close\_critical\_scope用于关闭临界区作用域。

注意

非临界接口不能在临界区作用域使用，且同一执行环境中只能打开一个临界区作用域。建议仅在需要临界接口时打开临界区作用域，使用后应及时关闭。

## 场景介绍

调用临界接口前，必须通过napi\_open\_critical\_scope打开临界区作用域，并在临界区作用域内进行调用。

关闭临界区作用域后，请勿使用临界接口及其返回结果，否则可能导致程序崩溃或数据损坏。

## 临界区作用域的打开、关闭及临界接口的使用

| 接口 | 描述 | 临界区作用域外执行的状态码 |
| --- | --- | --- |
| napi\_open\_critical\_scope | 打开临界区作用域 | NA |
| napi\_close\_critical\_scope | 关闭临界区作用域 | napi\_generic\_failure |
| napi\_get\_buffer\_string\_utf16\_in\_critical\_scope | 获取ArkTS String的UTF-16编码内存缓冲区数据 | napi\_generic\_failure |

注意

1.当ArkTS String以UTF-16编码存储时，napi\_get\_buffer\_string\_utf16\_in\_critical\_scope才能正确获取其内存缓冲区，否则该函数返回错误。

2.napi\_create\_string\_utf16和napi\_create\_string\_utf8的功能是将输入数据以指定编码传递给虚拟机。这些函数不控制字符串在虚拟机的内部存储编码方式。

## 示例代码

* 模块注册

  ```
  1. // napi_init.cpp
  2. #include <string>
  3. #include <string_view>
  4. #include <vector>

  6. #include "napi/native_api.h"

  8. // 使用C++的RAII机制管理临界区作用域，避免遗漏关闭
  9. // 仅用作示例，也可以通过其他方式进行封装，或直接使用原始接口
  10. class MyCriticalScope
  11. {
  12. napi_env env_{};
  13. napi_critical_scope scope_{};

  15. public:
  16. explicit MyCriticalScope(napi_env env) : env_(env)
  17. {
  18. if (napi_open_critical_scope(env, &scope_) != napi_ok)
  19. {
  20. // 失败时，进行一些必要的错误处理，或维护信息补充，此处省略。
  21. // 常见失败原因：env不是有效的Node-API执行上下文（如：env参数为nullptr）
  22. }
  23. }
  24. ~MyCriticalScope()
  25. {
  26. Close();
  27. }
  28. inline void Close()
  29. {
  30. if (scope_ == nullptr)
  31. {
  32. return;
  33. }
  34. // 在析构函数中，关闭临界区作用域
  35. if (napi_close_critical_scope(env_, scope_) != napi_ok)
  36. {
  37. // 失败时，进行一些必要的错误处理，或维护信息补充，此处省略。
  38. // 常见失败原因：
  39. // 1. 重复关闭临界区作用域。
  40. // 2. env不是有效的Node-API执行上下文（如：空指针）。
  41. // 3. scope不是有效的临界区作用域句柄（如：空指针）。
  42. }
  43. scope_ = nullptr;
  44. }
  45. };

  47. // 二次封装的方法，用于在获取ArkTS字符串底层缓冲区失败时，回落到拷贝
  48. static std::vector<char16_t> GetValueStringUtf16(napi_env env, napi_value value)
  49. {
  50. size_t strLength{};
  51. if (napi_get_value_string_utf16(env, value, nullptr, 0, &strLength) != napi_ok) {
  52. return {};
  53. }
  54. /* Node-API接口要求缓冲区长度大于字符串内容长度，用于写入c字符串结束标记。
  55. 因此，需要获取完整字符串内容时，缓冲区大小应为字符串长度 + 1。 */
  56. std::vector<char16_t> result(strLength + 1);
  57. if (napi_get_value_string_utf16(env, value, result.data(), result.size(), &strLength) != napi_ok) {
  58. return {};
  59. }
  60. return result;
  61. }

  63. static napi_value NAPI_Global_getBufferStringUtf16(napi_env env, napi_callback_info info)
  64. {
  65. napi_value args[1]{};
  66. size_t argc = 1;
  67. napi_get_cb_info(env, info, &argc, args, /* thisVar */ nullptr, /* data */ nullptr);
  68. // 传入参数小于要求的最低参数数量
  69. if (argc < 1) {
  70. return nullptr;
  71. }
  72. napi_valuetype argType;

  74. // 传入参数类型不是字符串
  75. if (napi_typeof(env, args[0], &argType) != napi_ok || argType != napi_string) {
  76. return nullptr;
  77. }

  79. uint32_t returnCode = 0;
  80. {
  81. [[maybe_unused]] MyCriticalScope scope(env);
  82. size_t bufSize{};
  83. const char16_t *buf{};
  84. std::vector<char16_t> copied{}; // 预留，用以获取缓冲区失败时回落
  85. std::u16string_view str;

  87. if (napi_get_buffer_string_utf16_in_critical_scope(env, args[0], &buf, &bufSize) == napi_ok)
  88. {
  89. str = std::u16string_view(buf, bufSize);
  90. } else {
  91. scope.Close();
  92. copied = GetValueStringUtf16(env, args[0]);
  93. str = std::u16string_view(copied.data(), copied.size());
  94. returnCode |= (1 << 1);
  95. }

  97. // do something with str
  98. if (str == u"测试字符串") {
  99. returnCode |= 1;
  100. }
  101. }

  103. napi_value returnResult{};
  104. napi_create_int32(env, returnCode, &returnResult);
  105. return returnResult;
  106. }

  108. // 模块注册
  109. EXTERN_C_START
  110. static napi_value Init(napi_env env, napi_value exports)
  111. {
  112. std::vector<napi_property_descriptor> desc{{"getBufferStringUtf16", nullptr, NAPI_Global_getBufferStringUtf16,
  113. nullptr, nullptr, nullptr, napi_default, nullptr}};
  114. napi_define_properties(env, exports, desc.size(), desc.data());
  115. return exports;
  116. }
  117. EXTERN_C_END

  119. static napi_module demoModule = {
  120. .nm_version = 1,
  121. .nm_flags = 0,
  122. .nm_filename = nullptr,
  123. .nm_register_func = Init,
  124. .nm_modname = "entry",
  125. .nm_priv = ((void *)0),
  126. .reserved = {0},
  127. };

  129. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
  130. {
  131. napi_module_register(&demoModule);
  132. }
  ```
* 接口声明

  ```
  1. // index.d.ts
  2. export const getBufferStringUtf16: (str: string) => number;
  ```
* ArkTS代码示例

  ```
  1. // index.ets
  2. import testNapi from "libentry.so"

  4. const makeTest = (str: string) => {
  5. console.info(`status code of get buffer on "${str}": ${testNapi.getBufferStringUtf16(str)}`);
  6. }

  8. makeTest("hello world"); // 预期结果: 2或0
  9. makeTest("你好");        // 预期结果: 0或2
  10. makeTest("测试字符串");   // 预期结果: 1或3
  ```
