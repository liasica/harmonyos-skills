---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-1
title: 在Native侧如何精准获取ArkTS侧传入的字符串长度
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 在Native侧如何精准获取ArkTS侧传入的字符串长度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:92097e16b4bc9c680480ad30e6ca71dbf3043020a7d174d245e90e0914358eec
---

**问题现象**

在Native侧，转换ArkTS侧的字符串到char[]数组时无法准确获取字符串长度。频繁使用NAPI\_AUTO\_LENGTH宏定义会增加内存开销，影响性能。

**解决措施**

使用napi\_get\_value\_string\_utf8的第五个参数获取ArkTS层传入字符串的长度。此参数是一个指向size\_t类型的变量，函数调用成功后，该变量会被赋值为字符串的长度。根据这个长度分配合适大小的char数组。具体操作如下：先调用napi\_get\_value\_string\_utf8获取字符串的长度，然后根据长度分配char数组的内存空间。再次调用napi\_get\_value\_string\_utf8获取字符串的内容。分配内存时，长度加 1，以便为字符串添加终止符\0。

参考代码如下：

```cpp
static napi_value TestFunc(napi_env env, napi_callback_info info) 
{ 
    size_t argc = 1; 
    napi_value args[1] = {nullptr}; 
    napi_get_cb_info(env, info, &argc, args , nullptr, nullptr); 
     
    size_t len = 0; 
    napi_get_value_string_utf8(env, args[0], nullptr, 0, &len);    // Get string length to len 
    char* buf = new char[len+1];                                   // Allocate a char array of appropriate size
    napi_get_value_string_utf8(env, args[0], buf, len + 1, &len);  // get string 
    // ... 
}
```
