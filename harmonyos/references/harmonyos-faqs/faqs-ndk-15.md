---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-15
title: 如何将Native侧的函数封装到类中导出到ArkTS侧使用
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何将Native侧的函数封装到类中导出到ArkTS侧使用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:675e0bf11ee540bc5ec06c622afeca5b45fe0d34261a083ee897ab0457803700
---

**问题详情**

现有一个C++库，提供的接口以类方法形式提供。Native侧可以封装成普通函数的形式供上层调用，也可以保持原有类方法的形式。

**解决措施**

Native侧提供以下类方法供上层调用。

具体代码如下：

1. Native侧封装类方法。

   ```
   1. #include "napi/native_api.h"
   2. #include <string>

   4. static napi_value Sub(napi_env env, napi_callback_info info) {
   5. size_t requireArgc = 2;
   6. size_t argc = 2;
   7. napi_value args[2] = {nullptr};
   8. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   9. napi_valuetype valuetype0;
   10. napi_typeof(env, args[0], &valuetype0);
   11. napi_valuetype valuetype1;
   12. napi_typeof(env, args[1], &valuetype1);
   13. double value0;
   14. napi_get_value_double(env, args[0], &value0);
   15. double value1;
   16. napi_get_value_double(env, args[1], &value1);
   17. napi_value sub;
   18. napi_create_double(env, value0 - value1, &sub);
   19. return sub;
   20. }
   21. static napi_value Sum(napi_env env, napi_callback_info info) {
   22. size_t requireArgc = 2;
   23. size_t argc = 2;
   24. napi_value args[2] = {nullptr};
   25. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   26. napi_valuetype valuetype0;
   27. napi_typeof(env, args[0], &valuetype0);
   28. napi_valuetype valuetype1;
   29. napi_typeof(env, args[1], &valuetype1);
   30. double value0;
   31. napi_get_value_double(env, args[0], &value0);
   32. double value1;
   33. napi_get_value_double(env, args[1], &value1);
   34. napi_value sum;
   35. napi_create_double(env, value0 + value1, &sum);
   36. return sum;
   37. }
   38. napi_value Constructor(napi_env env, napi_callback_info info) { return nullptr; }
   39. EXTERN_C_START
   40. static napi_value Init(napi_env env, napi_value exports) {
   41. std::string class_name = "TestEntryA";
   42. napi_property_descriptor desc[] = {{"sub", nullptr, Sub, nullptr, nullptr, nullptr, napi_static, nullptr},
   43. {"sum", nullptr, Sum, nullptr, nullptr, nullptr, napi_static, nullptr}};
   44. napi_value defined_class = nullptr;
   45. napi_define_class(env, class_name.c_str(), class_name.length(), Constructor, nullptr, 2, desc, &defined_class);
   46. const napi_property_descriptor exports_desc[] = {
   47. {class_name.c_str(), nullptr, nullptr, nullptr, nullptr, defined_class, napi_default, nullptr},
   48. };
   49. napi_define_properties(env, exports, 2, exports_desc);
   50. return exports;
   51. }
   52. EXTERN_C_END
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/FuncEncapsulation/src/main/cpp/napi_init.cpp#L19-L70)
2. 在Index.d.ts文件中导出类及其方法。

   ```
   1. export declare class TestEntryA {
   2. static sub (a: number, b: number) : number;
   3. static sum (a: number, b: number) : number;
   4. }
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/FuncEncapsulation/src/main/cpp/types/libfuncencapsulation/Index.d.ts#L19-L22)
3. 在ArkTS侧通过类调用方法。

   ```
   1. import { TestEntryA } from 'libfuncencapsulation.so';

   3. @Entry
   4. @Component
   5. struct Index {
   6. @State message: string = 'Function Encapsulation';

   8. build() {
   9. Row() {
   10. Column() {
   11. Text(this.message)
   12. .fontSize(50)
   13. .fontWeight(FontWeight.Bold)
   14. .onClick(() => {
   15. console.info(`Test NAPI 2 + 3 = ${TestEntryA.sum(2, 3)}`);
   16. console.info(`Test NAPI 2 - 3 = ${TestEntryA.sub(2, 3)}`);
   17. })
   18. }
   19. .width('100%')
   20. }
   21. .height('100%')
   22. }
   23. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/FuncEncapsulation/src/main/ets/pages/Index.ets#L19-L41)
