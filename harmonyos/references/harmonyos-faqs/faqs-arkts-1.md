---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-1
title: 将rawfile中json格式的字符串转换成对应的object对象后，调用实例方法后程序崩溃
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 将rawfile中json格式的字符串转换成对应的object对象后，调用实例方法后程序崩溃
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1c68b9cf2b79586382f3b6f7d0fc1b07a33e5bbf92e9320788f4a858800ce2e7
---

**问题现象**

系统将直接报告错误：“jscrash happened in xxxxxxxxx”，崩溃日志中的错误信息为：“Error message: Unexpected Object in JSON”。

**问题原因**

通过JSON解析字符串得到的对象原型为Object，其原型链中没有自有的实例方法，因此无法调用。

**解决措施**

如需调用该方法，可采用以下两种方式：

1. 在解析后的对象上添加对应的原型，即转换为对应的实例对象。

   JSON.parse方法会将function转换为字符串，直接调用会导致不可调用的错误，从而引发崩溃。为了继续使用这些函数，通常的方法是使用eval函数将字符串转换为函数，但ArkTS限制了eval函数的使用，因此这种方法不可行。解决方案是使用class-transformer的plainToClass方法。
2. 将实例方法改为静态方法，通过类名调用。
