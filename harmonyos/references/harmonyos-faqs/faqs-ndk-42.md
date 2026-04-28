---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-42
title: Native侧如何获取ArkTS侧Object对象及其成员变量
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何获取ArkTS侧Object对象及其成员变量
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8f08cc9850cb205eddaa088f18bea7137659d8d403e81fc25fed812212ea9b84
---

在ArkTS侧定义类，传递类到Native侧调用类函数。详情见示例代码。

ArkTS侧

```
1. // index.ets
2. import testNapi from 'libentry.so';
3. import { PromptAction } from '@kit.ArkUI';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

7. class A {
8. name: string = 'username'

10. onCall() {
11. try {
12. new PromptAction().showToast({
13. message: 'Message Info',
14. duration: 2000
15. });
16. } catch (err) {
17. hilog.error(0x0000, 'testTag', `showToast undefined, code is ${err.code}, message is ${err.message}`);
18. }
19. }
20. }

22. @Entry
23. @Component
24. struct NativeGetArkTSObject {
25. build() {
26. Button()
27. .onClick(() => {
28. testNapi.callFunction(new A());
29. })
30. }
31. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/NativeGetArkTSObject/src/main/ets/pages/Index.ets#L21-L52)

```
1. // index.d.ts
2. export const callFunction: (a:object) => void;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/NativeGetArkTSObject/src/main/cpp/types/libnativegetarktsobject/Index.d.ts#L20-L21)

Native侧

```
1. // Pass in an instance object and call functions in the object on the C++side
2. #include "napi/native_api.h"
3. static napi_value CallFunction(napi_env env, napi_callback_info info) {
4. // Get instance object
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, NULL, NULL);
8. // Method for obtaining objects
9. napi_value onCall;
10. napi_get_named_property(env, args[0], "onCall", &onCall);
11. // Call functions in the object
12. napi_value res;
13. napi_call_function(env, args[0], onCall, 0, nullptr, &res);
14. return onCall;
15. }
16. EXTERN_C_START
17. static napi_value Init(napi_env env, napi_value exports) {
18. napi_property_descriptor desc[] = {
19. {"callFunction", nullptr, CallFunction, nullptr, nullptr, nullptr, napi_default, nullptr}};
20. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
21. return exports;
22. }
23. EXTERN_C_END
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/NativeGetArkTSObject/src/main/cpp/napi_init.cpp#L20-L42)
