---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-18
title: 通过resourceManager.getStringResource接口获取HSP资源文件报“Resource id invalid”错误
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 通过resourceManager.getStringResource接口获取HSP资源文件报“Resource id invalid”错误
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b3b348d1d9bad9a5f6c434e4d0c6ecad2d339cd27323c3b2aa9da2c076885e1a
---

**问题现象**

通过this.resourceManager.getStringResource($r('app.string.PlayCount').id)获取HSP资源文件时出现错误。

错误消息：资源ID无效。

错误代码：9001001

SourceCode：returnResource = this.context.resourceManager.getStringSync(id)。

**可能原因**

传入的id值不存在，未创建相应的context。

**解决措施**

根据模块名创建上下文Context，然后使用getStringByNameSync方法获取指定资源名称对应的字符串。具体示例代码如下：

```
1. import { common, application } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { JSON } from '@kit.ArkTS';

5. @Entry
6. @Component
7. struct Index {
8. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

10. build() {
11. Column() {
12. Button()
13. .onClick(() => {
14. // Create a context based on the module name
15. let moduleName: string = 'library';
16. application.createModuleContext(this.context, moduleName)
17. .then((data: common.Context) => {
18. console.info(`CreateModuleContext success, data: ${JSON.stringify(data)}`);
19. if (data !== null) {
20. this.getUIContext().getPromptAction().showToast({
21. message: ('get Context success')
22. });
23. }

25. // Then run getStringByNameSync to obtain the string corresponding to the specified resource name
26. try {
27. let str = data.resourceManager.getStringByNameSync('shared_desc');
28. console.info(`getStringByNameSync, data: ${JSON.stringify(str)}`);
29. } catch (error) {
30. let code = (error as BusinessError).code;
31. let message = (error as BusinessError).message;
32. console.error(`getStringByNameSync failed, error code: ${code}, message: ${message}.`);
33. }
34. })
35. .catch((err: BusinessError) => {
36. console.error(`CreateModuleContext failed, err code:${err.code}, err msg: ${err.message}`);
37. });
38. })
39. }
40. }
41. }
```

[ErrorInObtainingHSPFile.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/PackageStructureKit/entry/src/main/ets/pages/ErrorInObtainingHSPFile.ets#L21-L61)

**参考链接**

[应用上下文Context](../harmonyos-guides/application-context-stage.md)、[获取本应用中其他module的context](../harmonyos-guides/application-context-stage.md#获取本应用中其他module的context模块级别的上下文)、[getStringByNameSync](../harmonyos-references/js-apis-resource-manager.md#getstringbynamesync9)
