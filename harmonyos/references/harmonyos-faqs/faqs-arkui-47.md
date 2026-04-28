---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-47
title: 自定义字体的注册方式是什么，如何从资源存放路径中取出字体资源
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 自定义字体的注册方式是什么，如何从资源存放路径中取出字体资源
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:225c385dac45941f083eb71a233a0f5db20bfc48057885e89aedeba254512a93
---

在工程中存放自定义字体资源文件，通过代码中的registerFont接口注册这些字体，然后在文本组件中使用fontFamily属性引用。

推荐使用 $rawfile 方式引用自定义字体资源，资源应放置在 resources/rawfile 目录下。

获取字体资源可参考如下代码：

```
1. this.getUIContext().getFont().registerFont({
2. familyName: 'Gealova',
3. familySrc: $rawfile('font/gealova.otf')
4. })
```

[FontResources.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/FontResources.ets#L12-L15)

**参考链接**

[@ohos.font (注册自定义字体)](../harmonyos-references/js-apis-font.md)
