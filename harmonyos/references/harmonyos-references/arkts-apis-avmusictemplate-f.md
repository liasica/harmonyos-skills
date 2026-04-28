---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avmusictemplate-f
title: Functions
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avMusicTemplate (音频模板) > Functions
category: harmonyos-references
scraped_at: 2026-04-28T08:12:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b6a8686f7c586f975602b0bcea0ff65b28735ceb48a96da7f2a7d583561e2ad6
---

说明

* 本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块仅适用于API version 23及以上版本的Car设备。

## 导入模块

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';
```

## avMusicTemplate.createAVMusicTemplate

createAVMusicTemplate(accessType: AVMusicTemplateType): AVMusicTemplate

创建音频模板，返回音频模板实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accessType | [AVMusicTemplateType](arkts-apis-avmusictemplate-e.md#avmusictemplatetype) | 是 | 音频模板枚举类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AVMusicTemplate](arkts-apis-avmusictemplate-avmusictemplate.md) | 音频模板对象，可用于获取会话ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function createAVMusicTemplate can not work correctly due to limited device capabilities. |
| 35000001 | Failed to create the AVMusicTemplate. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private static sInstance: TemplateManager;

7. private constructor() {
8. }

10. /**
11. * 获取模板控制器实例。
12. *
13. * @returns 模板控制器实例。
14. */
15. public static getInstance(): TemplateManager {
16. if (!TemplateManager.sInstance) {
17. TemplateManager.sInstance = new TemplateManager();
18. }
19. return TemplateManager.sInstance;
20. };

22. /**
23. * 创建音频模板。
24. */
25. public createTemplate() {
26. if (this.template) {
27. console.warn('createTemplate: template not undefined');
28. return
29. }
30. try {
31. this.template = avMusicTemplate.createAVMusicTemplate(avMusicTemplate.AVMusicTemplateType.DEFAULT);
32. console.info('Succeeded in creating template.');
33. } catch (e) {
34. console.error(`createTemplate, errCode: ${e?.code}`);
35. }
36. }
37. }
```
