---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-16
title: ArkTS侧传入的string转换成std::string类型时报错
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > ArkTS侧传入的string转换成std::string类型时报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3113cff43517d053fbe9e4372aba01d451f7574b88d6b1525574e49034a93d95
---

## 问题现象

业务需要在ets中调用C++的方法，其中的一个参数是std::string类型，但是将ArkTS传进来string类型的参数转为std::string类型时，类型强转报错。

错误代码如下：

```
char *faceDetectModelDirChar;
napi_get_value_string_utf8(env, args[0], faceDetectModelDirChar, 0, &length);
// 将char*转为std::string类型
std::string faceDetectModelDir = faceDetectModelDirChar;
```

## 背景知识

[使用Node-API接口创建和获取string值](../harmonyos-guides/use-napi-about-string.md#napi_get_value_string_utf8)：将ArkTS的字符类型的数据转换为utf8编码的字符。

## 问题定位

对比官网指导文档和错误代码，发现错误代码中将获取字符串长度和字符串内容放在同一次调用中，和官方指导中先获取字符串长度，再获取字符串内容不一致。

## 分析结论

错误代码对Node-API的接口使用不正确，napi\_get\_value\_string\_utf8需要先获取字符串长度后再获取字符串内容给指定对象。

## 修改建议

参照指导文档修改：

1. 先调用napi\_get\_value\_string\_utf8获取字符串的长度；
2. 分配字符串的存储空间，需要包含'\0'占用的空间；
3. 再次调用napi\_get\_value\_string\_utf8获取字符串的内容；
4. 最后将字符串转换为std::string类型。
