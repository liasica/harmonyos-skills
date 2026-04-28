---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-58
title: 在ArkTS侧如何引用Native侧使用napi_create_buffer接口构造的对象
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 在ArkTS侧如何引用Native侧使用napi_create_buffer接口构造的对象
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:06fc783403af83f685c910eaf7e3ef1be22afed1800c4857a521c72a89b5570a
---

**问题现象**

使用napi\_create\_buffer接口创建缓冲区，并在ArkTS与Native之间传递构建结果的步骤如下：

**解决措施**

可以参考以下代码示例：

1. Native侧构造buffer并写入数据。

   ```
   1. #include "CreateBuffer.h"
   2. napi_value CreateBuffer::TestBuffer(napi_env env, napi_callback_info) {
   3. size_t length = 100;
   4. char *data = nullptr;
   5. napi_value result = nullptr;
   6. napi_create_buffer(env, length, reinterpret_cast<void **>(&data), &result);

   9. char buf[50] = {0};
   10. for (int i = 0; i < 50; i++) {
   11. buf[i] = i + 2;
   12. }
   13. napi_create_buffer_copy(env, 50, buf, reinterpret_cast<void **>(&data), &result);
   14. return result;
   15. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/ArkTSCallNativeNapiCreateBuffer/src/main/cpp/napi_init.cpp#L22-L36)
2. index.d.ts文件中声明接口。

   ```
   1. export const testBuffer: () => ArrayBuffer;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/ArkTSCallNativeNapiCreateBuffer/src/main/cpp/types/libarktscallnativenapicreatebuffer/Index.d.ts#L20-L20)
3. ArkTS侧获取buffer信息。

   ```
   1. import testNapi from 'libentry.so';

   4. @Entry
   5. @Component
   6. struct Index {
   7. @State message: string = 'Hello World';

   10. build() {
   11. Row() {
   12. Column() {
   13. Text(this.message)
   14. .fontSize(50)
   15. .fontWeight(FontWeight.Bold)
   16. .onClick(() => {
   17. let arr = testNapi.testBuffer();
   18. let result = new Uint8Array(arr);
   19. for (let index = 0; index < result.byteLength; index++) {
   20. console.info(`res[${index}] = ${result[index]}`)
   21. }
   22. })
   23. }
   24. .width('100%')
   25. }
   26. .height('100%')
   27. }
   28. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/ArkTSCallNativeNapiCreateBuffer/src/main/ets/pages/Index.ets#L20-L47)
