---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-63
title: hilog日志导致应用性能异常怎么定位优化
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > hilog日志导致应用性能异常怎么定位优化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d2f3c07bedeb2afe5e3bda6c2dee26f7fa26e7b180e127a8f6b382f10c991dec
---

如果发现hilog导致应用性能异常，一般有三个原因：

**原因一**

循环打印日志，导致进程检测到日志打印耗时变长。

**解决方法**

查看日志是否有循环打印场景，删除循环打印日志。

**原因二**

日志打印参数初始化耗时长。

例如存在日志接口入参调用函数代码: hilog.debug(0xd010, 'testTag', 'map info: %{public}s', mapToJson(this.paramsMap)), 这行日志打印代码中，需要先执行mapToJson(this.paramsMap)获取日志参数字符串，此函数可能有耗时操作，从而使hilog.debug接口耗时变长。

**解决方法**

如果确认日志打印中参数初始化为耗时函数，可以在日志打印前先使用hilog.isLoggable判断当前打印是否符合日志级别要求，例如：

```typescript
if (hilog.isLoggable(0xd010, 'testTag', hilog.LogLevel.DEBUG)) {
  hilog.debug(0xd010, 'testTag', 'map info: %{public}s', mapToJson(this.paramsMap))
}
```

**原因三**

OH\_LOG\_SetCallback接口传入的回调函数存在耗时操作，导致日志打印接口耗时变长。

**解决方法**

优化OH\_LOG\_SetCallback接口传入的回调函数的实现解决耗时变长问题。
