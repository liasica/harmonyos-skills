---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-77
title: 如何在ArkTS侧管理Native侧的C++对象
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在ArkTS侧管理Native侧的C++对象
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:987e2d24695e73387ed08a5231711fd6db377220f94a58ee6fd2e33b9f7e6eab
---

**问题现象**

在ArkTS层管理C++层分配的对象，并通过接口访问C++层的业务。

**解决措施**

C++层分配一个类对象，返回该对象的地址给ArkTS层。ArkTS层通过自定义类对象的number属性存储C++层返回的地址。后续涉及对C++层对象的业务处理时，ArkTS层调用接口将地址传递到C++层处理。

声明TestClass：

```
1. class TestClass {
2. public:
3. int GetValue() {
4. return this->value;
5. }
6. void SetValue(int value) {
7. this->value = value;
8. }
9. private:
10. int value = 999;
11. };
```

[TestClass.h](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/ArkTSManageCObjects/src/main/cpp/TestClass.h#L21-L31)

C++层将定义的对象地址返回到ArkTS层：

```
1. #include "napi/native_api.h"
2. #include "TestClass.h"
3. #include "hilog/log.h"
4. #define LOG_TAG "MY_TAG"

6. static napi_value DefineObject(napi_env env, napi_callback_info info) {
7. OH_LOG_INFO(LOG_APP, "enter DefineObject");

9. napi_value result;
10. auto a = new TestClass();
11. int64_t addrValue = (int64_t)a;
12. napi_create_bigint_int64(env, addrValue, &result);
13. OH_LOG_INFO(LOG_APP, "end DefineObject, addrValue:%{public}ld", addrValue);
14. return result;
15. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/ArkTSManageCObjects/src/main/cpp/napi_init.cpp#L19-L33)

C++层接收ArkTS层传递过来的对象地址完成业务：

```
1. static napi_value CallObject(napi_env env, napi_callback_info info) {
2. OH_LOG_INFO(LOG_APP, "enter CallObject");
3. size_t argc = 1;
4. napi_value args[1] = {nullptr};
5. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
6. int64_t addrValue = 0;
7. bool flag = false;
8. napi_get_value_bigint_int64(env, args[0], &addrValue, &flag);
9. TestClass *a = (TestClass *)addrValue;
10. OH_LOG_INFO(LOG_APP, "CallObject, addrValue:%{public}ld", addrValue);
11. OH_LOG_INFO(LOG_APP, "CallObject, value:%{public}d", a->GetValue());
12. a->SetValue(888);
13. return nullptr;
14. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/ArkTSManageCObjects/src/main/cpp/napi_init.cpp#L37-L50)

ArkTS侧调用接口：

```
1. import testNapi from 'libentry.so';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'DefineObject';
7. @State message2: string = 'CallObject';
8. addr: number = 0;

10. build() {
11. Column() {
12. Button(this.message)
13. .fontSize(16)
14. .fontWeight(FontWeight.Bold)
15. .onClick(() => {
16. this.addr = testNapi.defineObject();
17. console.log('testTag:' + this.addr.toString());
18. })
19. Button(this.message2)
20. .fontSize(16)
21. .fontWeight(FontWeight.Bold)
22. .onClick(() => {
23. if (this.addr != 0) {
24. testNapi.callObject(this.addr);
25. this.message2 = 'CallObject';
26. } else {
27. this.message2 = 'want define Object';
28. }
29. })
30. }
31. .justifyContent(FlexAlign.Center)
32. .height('100%')
33. .width('100%')
34. }
35. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/ArkTSManageCObjects/src/main/ets/pages/Index.ets#L19-L53)
