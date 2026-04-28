---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-jsvm-5
title: 如何正确使用OH_JSVM_GetValueStringUtf8获取字符串
breadcrumb: FAQ > 应用框架开发 > NDK开发 > JSVM > 如何正确使用OH_JSVM_GetValueStringUtf8获取字符串
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:58+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:178ddb1ab05f5591d845aa0bb41e61ed0afa8b7e561bf943463d2676725c4423
---

**问题现象**

1. OH\_JSVM\_GetValueStringUtf8 中传入的缓冲区大小不确定。
2. 使用 OH\_JSVM\_GetValueStringUtf8 获取超长字符串时可能会导致崩溃。

**解决措施**

函数 OH\_JSVM\_GetValueStringUtf8 的第三个参数用于指定字符串写入的内存地址。如果传入空指针，接口会通过最后一个参数 result 返回字符串的长度（不包含终止符）。

```
1. JSVM_EXTERN JSVM_Status OH_JSVM_GetValueStringUtf8(JSVM_Env env,
2. JSVM_Value value,
3. char* buf,
4. size_t bufsize,
5. size_t* result);
```

[Jsvm\_test.cpp](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Jsvm/entry/src/main/cpp/Jsvm_test.cpp#L31-L35)

获取字符串可分为以下三步：

1. 调用接口获取字符串长度；
2. 申请buffer内存空间；
3. 调用接口获取字符串。

   ```
   1. std::string GetValueString(JSVM_Env env, JSVM_Value value) {
   2. constexpr size_t PREALLOC_SIZE = 256;
   3. char preallocMemory[PREALLOC_SIZE];

   6. char *buff = preallocMemory;

   8. // Obtain length
   9. size_t totalLen = 0;
   10. OH_JSVM_GetValueStringUtf8(env, value, nullptr, 0, &totalLen);
   11. size_t needed = totalLen + 1;

   14. if (needed > PREALLOC_SIZE) {
   15. // Allocate space, size must include termination character
   16. buff = new char[needed];
   17. }
   18. // get string
   19. OH_JSVM_GetValueStringUtf8(env, value, buff, needed, nullptr);

   22. std::string ret(buff, totalLen);

   25. if (needed > PREALLOC_SIZE) {
   26. delete[] buff;
   27. }
   28. return ret;
   29. }
   ```

   [Jsvm\_test.cpp](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Jsvm/entry/src/main/cpp/Jsvm_test.cpp#L39-L67)

说明

1. 分配的 buffer 大小必须大于字符串长度，因为字符串长度不包含最后的终止字符。如果 buffer 的大小等于字符串长度，字符串的最后一个字符将被终止字符覆盖。
2. 不建议直接在栈上使用 `char buff[totalLen + 1]` 分配空间，因为当字符串长度过大时，可能会导致栈溢出，从而引发应用崩溃。
