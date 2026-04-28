---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-14
title: 如何获取当前应用程序缓存目录
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何获取当前应用程序缓存目录
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:783f8103f9ee9d9c69e783510ecd63e3e9e14a10596c6b164ce65047951bf9c3
---

使用Context.cacheDir获取应用程序的缓存目录。代码示例如下：

```
1. import { common } from '@kit.AbilityKit';

3. @Entry
4. @Component
5. export struct GetCacheDirectoryView {
6. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. @State cachePath: string = '';

9. build() {
10. Column() {
11. Text(this.cachePath)
12. .margin({ bottom: 24 })
13. Button() {
14. Text('Get the application cache directory address')
15. }
16. .onClick(() => {
17. const applicationContext = this.context.getApplicationContext();
18. // Get the application file path
19. const cacheDir = applicationContext.cacheDir;
20. this.cachePath = cacheDir + '/test.txt';
21. })
22. .width(300)
23. .height(50)
24. }
25. .justifyContent(FlexAlign.Center)
26. .width('100%')
27. .height('100%')
28. }
29. }
```

[GetCacheDirectoryView.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/GetCacheDirectoryView.ets#L21-L49)

**参考链接**

[获取应用文件路径](../harmonyos-guides/application-context-stage.md#获取应用文件路径)
