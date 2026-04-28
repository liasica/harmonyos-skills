---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/appgallery-commentmanager
title: commentManager（应用评论服务）
breadcrumb: API参考 > 应用服务 > AppGallery Kit（应用市场服务） > ArkTS API > commentManager（应用评论服务）
category: harmonyos-references
scraped_at: 2026-04-28T08:16:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e8c0d1e43470540ca21630d65ff3d682cabae078360245fe2ea1c17533820492
---

提供应用内评论能力，用户无需进入应用市场应用详情页进行评论。

说明

调用接口需捕获异常。

**起始版本：** 6.0.0(20)

## 导入模块

PhonePC/2in1Tablet

```
1. import { commentManager } from '@kit.AppGalleryKit';
```

## commentManager.showCommentDialog

PhonePC/2in1Tablet

showCommentDialog(context: common.UIExtensionContext | common.UIAbilityContext): Promise<void>

拉起应用评分弹窗。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Comment

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIExtensionContext](js-apis-inner-application-uiextensioncontext.md) | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 应用上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1021500001 | Internal system error. |
| 1021500002 | Service request failed. |
| 1021500003 | Failed to connect to AppGallery. |
| 1021500004 | Failed to write parameters. |
| 1021500005 | The app context is invalid. |
| 1021500006 | The user has not signed in to their HUAWEI ID. |
| 1021500007 | The user has already commented on the current version. |
| 1021500008 | The number of comments has reached the maximum limit. |
| 1021500009 | The user has already left a comment, and less than a year has elapsed since then. |

**示例：**

```
1. import { commentManager } from '@kit.AppGalleryKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import type { common } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Index {
9. @State message: string = 'showCommentDialog'

11. build() {
12. Row() {
13. Column() {
14. Text(this.message)
15. .fontSize(50)
16. .fontWeight(FontWeight.Bold)
17. .onClick(() => {
18. try {
19. const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
20. // 拉起应用评分弹窗
21. commentManager.showCommentDialog(uiContext).then(()=>{
22. hilog.info(0, 'TAG', "succeeded in showing commentDialog.");
23. }).catch((error: BusinessError<Object>) => {
24. hilog.error(0, 'TAG', `showCommentDialog failed, Code: ${error.code}, message: ${error.message}`);
25. });
26. } catch (error) {
27. hilog.error(0, 'TAG', `showCommentDialog failed, Code: ${error.code}, message: ${error.message}`);
28. }
29. })
30. }
31. .width('100%')
32. }
33. .height('100%')
34. }
35. }
```
