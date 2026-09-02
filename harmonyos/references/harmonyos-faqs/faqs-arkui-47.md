---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-47
title: 自定义字体的注册方式是什么，如何从资源存放路径中取出字体资源
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 自定义字体的注册方式是什么，如何从资源存放路径中取出字体资源
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:13a64c584d46f39e5b7a53d8724ad8bcd2fd8420b2f165ad4a2b8111bd96b6a7
---

在工程中存放自定义字体资源文件，通过代码中的registerFont接口注册这些字体，然后在文本组件中使用fontFamily属性引用。

推荐使用 $rawfile 方式引用自定义字体资源，资源应放置在 resources/rawfile 目录下。

获取字体资源可参考如下代码：

```typescript
this.getUIContext().getFont().registerFont({
  familyName: 'Gealova',
  familySrc: $rawfile('font/gealova.otf')
})
```

**参考链接**

[@ohos.font (注册自定义字体)](../harmonyos-references/js-apis-font.md)
