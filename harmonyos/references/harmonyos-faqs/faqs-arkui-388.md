---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-388
title: 使用Router跳转导致闪退，可能是什么原因，如何排查
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 使用Router跳转导致闪退，可能是什么原因，如何排查
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3e2278eb82137ee2a7d465606b7868fc654dde2290c99c74ff85e1c5145260b6
---

**场景一**: 循环依赖导致闪退

**问题现象**

使用ohos.router (页面路由）跳转，有HAR1包里A页面和HAR2中的B页面，A和B相互跳转，会因为相互引用崩溃。

**可能原因**

使用router路由跳转时，由于HAR包相互引用，造成循环依赖，会出现闪退。

**解决措施**

在设计时尽量通过依赖管理避免循环依赖，建议通过Navigation实现页面路由管理或者HMRouter进行路由管理，临时方案可采用lazy的方式避免循环依赖。

**场景二**: 未找到UIContext上下文

**问题现象**

router的pushUrl出现闪退，报错信息为：Error message: lnternal error.UI execution context not found. Error code: 100001．。

**可能原因**

在使用router进行跳转时，如果路由跳转在上下文不明确的地方使用，如Native调用的回调函数或者其他类似场景，会出现闪退现象。

**解决措施**

建议router的使用切换为UIContext中的使用方案。

```
1. this.getUIContext().getRouter().pushUrl({
2. url: 'login/UserNameLoginPage'
3. }, () => {
4. this.getUIContext().getRouter().clear();
5. })
```

[UseRouterJumpAndCrash.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/abce1db5a4cf676fd100dbd3a0acd02f5bb30358/ArkUI/entry/src/main/ets/pages/UseRouterJumpAndCrash.ets#L13-L17)

**场景三**: 混淆用法错误

**问题现象**

使用router.replace()，在debug模式下运行正常，release模式下闪退。

**可能原因**

首先排查混淆用法是否正确，正例：

```
1. -enable-property-obfuscation
2. -enable-toplevel-obfuscation
3. -enable-filename-obfuscation
4. -enable-export-obfuscation
5. -keep
6. ./src/main/ets/startup/\*\*
```

[obfuscation-rules.txt](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/abce1db5a4cf676fd100dbd3a0acd02f5bb30358/ArkUI/entry/obfuscation-rules.txt#L21-L26)

* 检查配置文件build-profile.json5中的"enable"字段是否为 true。
* 确定子module的Build方式。
* 排查文件中这个属性所在的类是否export或者import。
* 排查是否keep的是.har包中的属性。

**分析结论**

子场景一：使用-keep filepath形式不会影响-enable-filename-obfuscation功能，文件名仍会被混淆。

子场景二：-keep的是.har包中的属性，但是-keep不能保留.har文件。

**修改建议**

子场景一：用-keep-file-name的形式配置混淆，支持使用名称类通配符。

子场景二：用-keep保留oh\_modules文件夹下对应的har包来避免混淆：在obfuscation-rules.txt文件里配置，用-keep ./oh\_modules/har-name。

关于混淆的用法可以参考：[ArkGuard混淆常见问题](../harmonyos-guides/source-obfuscation-questions.md)。
