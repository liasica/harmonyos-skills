---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-53
title: Native侧如何获取ArkTS侧类实例
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何获取ArkTS侧类实例
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:da70ea2ea8c61530ab2d59bc97a7374c3cb16ebd68523bf607994881b7899a97
---

在ArkTS创建一个类并传递给Native侧，Native侧通过napi\_call\_function接口调用ArkTS侧的类函数。

```
1. // Declare Demo class
2. class Demo {
3. add(a: number, b: number): number {
4. return a + b;
5. }

7. sub(a: number, b: number): number {
8. return a - b;
9. }
10. }

12. export default new Demo();
```

[ClassDemo1.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/ets/pages/interface/ClassDemo1.ets#L19-L30)

ArkTS侧：

```
1. // Pass the parameters to the native side
2. import testNapi from 'libentry.so';
3. import demo from './interface/ClassDemo1'

5. @Entry
6. @Component
7. struct Index {
8. @State message: string = 'Hello World';

10. build() {
11. Row() {
12. Column() {
13. Text(this.message)
14. .fontSize(50)
15. .fontWeight(FontWeight.Bold)
16. .onClick(() => {
17. let flag:Boolean = false;
18. console.info(`Test NAPI Result is ${testNapi.cal(2, 3, demo, true)}`)
19. console.info(`Num is  ${demo.add(3,2)}`)
20. })
21. }
22. .width('100%')
23. }
24. .height('100%')
25. }
26. }
```

[CGetArkTSObject.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/ets/pages/CGetArkTSObject.ets#L19-L44)

Native侧：

```
1. // Get class information and call class functions
2. #include "CGetArkTSObject.h"
3. napi_value CGetArkTSObject::Cal(napi_env env, napi_callback_info info) {
4. size_t argc = 4;
5. napi_value args[4] = {nullptr};
6. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

8. double value0;
9. napi_get_value_double(env, args[0], &value0);

11. double value1;
12. napi_get_value_double(env, args[1], &value1);

14. // Construct class instances
15. napi_value demo;
16. napi_create_object(env, &demo);
17. napi_coerce_to_object(env, args[2], &demo);

19. bool flag;
20. napi_get_value_bool(env, args[3], &flag);

22. // Obtain the add and sub functions of the class instance
23. napi_value add, sub, num;
24. napi_get_named_property(env, demo, "add", &add);
25. napi_get_named_property(env, demo, "sub", &sub);

27. // Call the ArkTS function
28. napi_value result;
29. if (flag) {
30. napi_call_function(env, nullptr, add, 2, args, &result);
31. } else {
32. napi_call_function(env, nullptr, sub, 2, args, &result);
33. }

35. return result;
36. }
```

[CGetArkTSObject.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/cpp/CGetArkTSObject/CGetArkTSObject.cpp#L20-L55)
