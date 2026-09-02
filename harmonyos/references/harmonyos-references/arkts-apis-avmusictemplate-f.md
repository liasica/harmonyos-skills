---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avmusictemplate-f
title: Functions
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avMusicTemplate (音频模板) > Functions
category: harmonyos-references
scraped_at: 2026-09-02T15:02:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d0a6ace426cacc1e210777d4af8cd809c5986091406eec7e5199bdfc66280e0d
---

**说明** 

* 本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块仅适用于API version 23及以上版本的Car设备。

## 导入模块

```ts
import { avMusicTemplate } from '@kit.AVSessionKit';
```

## avMusicTemplate.createAVMusicTemplate

createAVMusicTemplate(accessType: AVMusicTemplateType): AVMusicTemplate

创建音频模板，返回音频模板实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accessType | [AVMusicTemplateType](arkts-apis-avmusictemplate-e.md#avmusictemplatetype) | 是 | 音频模板类型。 |

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

```ts
import { avMusicTemplate } from '@kit.AVSessionKit';

export class TemplateManager {
  private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
  private static instance: TemplateManager;

  private constructor() {
  }

  /**
   * 获取模板管理器实例。
   *
   * @returns 模板管理器实例。
   */
  public static getInstance(): TemplateManager {
    if (!TemplateManager.instance) {
      TemplateManager.instance = new TemplateManager();
    }
    return TemplateManager.instance;
  };

  /**
   * 创建音频模板。
   */
  public createTemplate() {
    if (this.template) {
      console.warn('createTemplate: template already exists');
      return;
    }
    try {
      this.template = avMusicTemplate.createAVMusicTemplate(avMusicTemplate.AVMusicTemplateType.DEFAULT);
      console.info('Succeeded in creating template.');
    } catch (e) {
      console.error(`createTemplate, errCode: ${e?.code}`);
    }
  }
}
```
