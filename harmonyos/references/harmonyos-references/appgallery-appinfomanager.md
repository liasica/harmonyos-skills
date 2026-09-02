---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/appgallery-appinfomanager
title: appInfoManager（应用元数据管理服务）
breadcrumb: API参考 > 应用服务 > AppGallery Kit（应用市场服务） > ArkTS API > appInfoManager（应用元数据管理服务）
category: harmonyos-references
scraped_at: 2026-09-02T15:02:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a416745731f9cd586dd7be27fb003bad471a98e9c5b378a290d32bcccb70a48f
---

提供查询动态图标信息、选择动态图标、禁用动态图标功能。

**说明** 

调用接口需捕获异常。

**起始版本：** 5.0.3(15)

## 导入模块

```typescript
import { appInfoManager } from '@kit.AppGalleryKit';
```

## DynamicIconInfo

动态图标信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.AppInfoManager

**起始版本：** 5.0.3(15)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iconUrl | string | 是 | 否 | 动态图标链接。 |
| iconId | string | 是 | 否 | 动态图标ID。 |
| enabled | boolean | 是 | 否 | 该动态图标是否正在使用中。true表示当前正在使用中，false表示当前未使用。 |

## appInfoManager.queryDynamicIcons

queryDynamicIcons(): Promise<DynamicIconInfo[]>

查询动态图标信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.AppInfoManager

**起始版本：** 5.0.3(15)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DynamicIconInfo](appgallery-appinfomanager.md#dynamiciconinfo)[]> | Promise对象，返回动态图标信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-appgallery.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006800001 | The specified service extension connect failed. |
| 1006800009 | System internal error. |
| 1006800010 | No dynamic icon data. |

**示例：**

```typescript
import { appInfoManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = 'dynamicIconManager';

@Entry
@Component
@Preview
struct DynamicIconPage {

  scroller: Scroller = new Scroller();
  @State dynamicIconInfos: appInfoManager.DynamicIconInfo[] = [];
  @State message: string = '';

  private queryDynamicIcon() {
    try {
      hilog.info(0, TAG, `queryDynamicIcon start.`);
      // 查询动态图标信息,返回动态图标信息
      appInfoManager.queryDynamicIcons().then((iconInfos: appInfoManager.DynamicIconInfo[]) => {
        hilog.info(0, TAG, `queryDynamicIcons success. iconInfos: ${JSON.stringify(iconInfos)}`);
        this.dynamicIconInfos = iconInfos;
        this.message = JSON.stringify(iconInfos);
      }).catch((error: BusinessError) => {
        this.message = `queryDynamicIcon failed: ${JSON.stringify(error)}`;
        hilog.error(0, TAG,
          `queryDynamicIcons failed, code: ${error.code}, exception message: ${error.message}`);
      })
    } catch (error) {
      this.message = `queryDynamicIcon exception: ${JSON.stringify(error)}`;
      hilog.error(0, TAG,
        `queryDynamicIcons exception, code: ${error.code}, exception message: ${error.message}`);
    }
  }

  build() {
    Scroll(this.scroller) {
      Column() {
        Row() {
          Button("queryDynamicIcons").onClick(() => {
            this.queryDynamicIcon();
          }).margin({ top: 4, bottom: 4 })
        }
      }
    }
  }
}
```

## appInfoManager.selectDynamicIcon

selectDynamicIcon(iconId: string): Promise<void>

选择动态图标。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.AppInfoManager

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| iconId | string | 是 | 动态图标ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-appgallery.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006800009 | System internal error. |
| 1006800011 | Select dynamic icon failed. |
| 1006800013 | Failed to switch to the custom icon because a custom theme icon is currently in use.  适用版本：6.0.0(20)+ |

**示例：**

```typescript
import { appInfoManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let iconId: string = 'iconId';
  appInfoManager.selectDynamicIcon(iconId).then(() => {
      hilog.info(0, 'TAG', "Succeeded in selecting dynamic icon");
  }).catch((error: BusinessError) => {
    hilog.error(0, 'TAG', "selectDynamicIcon failed, code: " + error.code + ", exception message: " + error.message);
  });
} catch (error) {
  hilog.error(0, 'TAG', "selectDynamicIcon exception code: " + error.code + ", exception message: " + error.message);
}
```

## appInfoManager.disableDynamicIcon

disableDynamicIcon(): Promise<void>

禁用动态图标，恢复默认图标。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.AppInfoManager

**起始版本：** 5.0.3(15)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-appgallery.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006800009 | System internal error. |
| 1006800012 | Disable dynamic icon failed. |

**示例：**

```typescript
import { appInfoManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appInfoManager.disableDynamicIcon().then(() => {
      hilog.info(0, 'TAG', "Succeeded in disabling dynamic icon");
  }).catch((error: BusinessError) => {
    hilog.error(0, 'TAG', "disableDynamicIcon failed, code: " + error.code + ", exception message: " + error.message);
  });
} catch (error) {
  hilog.error(0, 'TAG', "disableDynamicIcon exception code: " + error.code + ", exception message: " + error.message);
}
```
