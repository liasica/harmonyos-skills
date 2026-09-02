---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-183
title: HarmonyOS NEXT系统浏览器UA问题
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > HarmonyOS NEXT系统浏览器UA问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:215612b76d5594d693b7940d644f1ee77c52e96ce0343a7af7dd99c10c62ad04
---

## 问题现象

* 同一个的URL在其他系统中可以打开，在HarmonyOS NEXT系统中使用系统浏览器打开会报“check ip error”的错误。
* 系统浏览器打开不同网站地址获取的UA不一致。
* 在HarmonyOS NEXT系统中使用系统浏览器浏览部分网页会报错。
* 系统浏览器的UA标识默认值为包含其他平台标识。
* 扫描网页展示的二维码跳转到其他平台的APP下载地址。

## 背景知识

User-Agent（简称UA）：是一个特殊的字符串，包含设备类型、操作系统及版本等关键信息。在Web开发中，这个字符串使服务器能够识别请求的来源设备及其特性，从而根据这些信息提供定制化的内容和服务。更详细的UA介绍及自定义UA请参照[User-Agent开发指导](../harmonyos-guides/web-default-useragent.md)。

## 问题定位

在Web页面中通过navigator.userAgent获取当前浏览器或者Web组件的UA参数。打印后发现UA参数为：

```js
Mozilla/5.0 (Phone; OpenHarmony 6.0; 其他平台 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 ArkWeb/6.0.0.125 Mobile HuaweiBrowser/5.1.12.303
```

## 分析结论

1. 因为当前还有部分网站应用存在UA适配问题，为了保证用户体验，浏览器会配置部分特定页面的UA，最终导致开发者获取的UA并非是用户在浏览器中设置的UA。
2. 网站在判断当前运行环境时匹配到其他平台的标识符，将HarmonyOS系统误判为其他平台。

## 修改建议

网站判断UA的时候，把OpenHarmony字段判断放在其他平台字段之前，优先判断OpenHarmony字段。
