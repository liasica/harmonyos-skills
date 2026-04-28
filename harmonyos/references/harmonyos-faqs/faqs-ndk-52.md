---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-52
title: Native侧如何获取ArkTS侧的Uint8Array实例
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何获取ArkTS侧的Uint8Array实例
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b0d064ca25879171d454e76611fc5af747cf3cf53214eeb8602f68ecd98f0252
---

ArkTS Uint8Array的传递方式与其他类型相同。

```
1. // ArkTS passes Uint8Array parameter
2. import testNapi from 'libentry.so';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';

9. build() {
10. Row() {
11. Column() {
12. Text(this.message)
13. .fontSize(50)
14. .fontWeight(FontWeight.Bold)
15. .onClick(() => {
16. let temp = new Uint8Array(2);
17. temp[0] = 1;
18. temp[1] = 2;
19. console.info(`Pure inputBuffer length: ${temp.length}`);
20. let res = testNapi.uintArr(temp);
21. console.info(`Pure outputBuffer: ${res}`);
22. })
23. }
24. .width('100%')
25. }
26. .height('100%')
27. }
28. }
```

[UintArr.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/ets/pages/UintArr.ets#L19-L46)

Native侧使用napi\_get\_typedarray\_info方法获取Uint8Array的详细信息。

```
1. // Native side obtains Uint8Array parameter and returns it to ArkTS side
2. #include "UintArr.h"
3. napi_value Demo1::UintArr(napi_env env, napi_callback_info info) {
4. size_t requireArgc = 1;
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};

8. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

10. napi_value inputArray = args[0];

12. // Get the ArrayBuffer type
13. napi_typedarray_type type;
14. napi_value inArrayBuffer;
15. size_t byteOffset;
16. size_t length;
17. napi_get_typedarray_info(env, inputArray, &type, &length, nullptr, &inArrayBuffer, &byteOffset);
18. if (type != napi_uint8_array) {
19. return nullptr;
20. }

22. // Retrieve information from the ArrayBuffer
23. void *data = nullptr;
24. size_t byte_length;
25. napi_get_arraybuffer_info(env, inArrayBuffer, &data, &byte_length);

27. // Construct an ArrayBuffer and assign a value
28. napi_value output_buffer;
29. void *output_ptr = nullptr;
30. napi_create_arraybuffer(env, byte_length, &output_ptr, &output_buffer);
31. napi_value outputArray;
32. napi_create_typedarray(env, type, length, output_buffer, byteOffset, &outputArray);
33. uint8_t *input_bytes = (uint8_t *)(data) + byteOffset;
34. uint8_t *array = (uint8_t *)(output_ptr);
35. for (size_t idx = 0; idx < length; idx++) {
36. array[idx] = 3;
37. }

39. return outputArray;
40. }
```

[UintArr.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/cpp/UintArr/UintArr.cpp#L19-L58)

index.d.ts声明接口。

```
1. export const uintArr: (a: Uint8Array) => object;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/cpp/types/libentry/Index.d.ts#L19-L19)
