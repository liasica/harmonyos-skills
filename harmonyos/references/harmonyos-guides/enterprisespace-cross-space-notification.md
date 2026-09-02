---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-cross-space-notification
title: 跨空间消息提醒
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 跨空间消息提醒
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7d9adcbf098ebbadd29e2a59b82ba9589bb5a1398aa796f1c471aa6e31c8c2ff
---

从API版本26.0.0开始，支持跨空间消息提醒的能力。

## 场景介绍

Enterprise Space Kit为应用提供跨空间消息提醒的能力，支持企业空间与个人空间之间的双向通知互通：企业应用可主动触达个人空间，个人空间的应用也能将关键信息同步至企业空间。

企业管理员可调用配置接口控制“设置 > 通知和状态栏 > 通知管理”路径下的开关，以及是否隐藏通知内容，同时还能通过查询接口实时获取当前的配置状态。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [setNotificationConfig](../harmonyos-references/enterprisespace-spacemanager.md#setnotificationconfig)(configs: [NotificationConfig](../harmonyos-references/enterprisespace-spacemanager.md#notificationconfig)[]): Promise<void> | 设置跨空间消息提醒配置。 |
| [getNotificationConfig](../harmonyos-references/enterprisespace-spacemanager.md#getnotificationconfig)(): Promise<[NotificationConfig](../harmonyos-references/enterprisespace-spacemanager.md#notificationconfig)[]> | 获取跨空间消息提醒配置。 |

## 开发步骤

1.导入跨空间消息提醒API模块相关依赖。

```typescript
import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { ErrCode } from '../../common/ErrCode';
```

2.跨空间消息提醒API接口封装。

```typescript
const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

export class NotificationConfigApi {
  static async setNotificationConfig(configs: spaceManager.NotificationConfig[]): Promise<number> {
    try {
      await spaceManager.setNotificationConfig(configs);
      hilog.info(DOMAIN, TAG, 'Succeeded in setting notification config.');
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to set notification config. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }

  static async getNotificationConfig(): Promise<spaceManager.NotificationConfig[] | undefined> {
    try {
      const configs: spaceManager.NotificationConfig[] = await spaceManager.getNotificationConfig();
      hilog.info(DOMAIN, TAG, `Succeeded in getting notification config. configs: ${JSON.stringify(configs)}`);
      return configs;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to get notification config. Code: ${err.code}, message: ${err.message}`);
      return undefined;
    }
  }
}
```

3.导入跨空间消息提醒业务实现相关依赖。

```typescript
import { router } from '@kit.ArkUI';
import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { ErrCode } from '../../common/ErrCode';
import { NotificationConfigApi } from '../api/NotificationConfigApi'
```

4.跨空间消息提醒业务相关实现。

```typescript
const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

@Entry
@Component
struct NotificationConfigPage {
  async setNotificationConfig() {
    const configs: spaceManager.NotificationConfig[] = [
      {
        workspaceId: 100, // 空间ID，由用户配置
        appIdentifier: '691867************', // 应用的唯一标识，请根据实际情况进行替换。
        notificationState: spaceManager.NotificationSwitch.ON,
        visibilityState: spaceManager.NotificationVisibilitySwitch.NOTIFICATION_VISIBLE,
        allowVisibilityChange: spaceManager.NotificationVisibilityControl.ALLOW_CHANGE,
      }
    ];
    if (await NotificationConfigApi.setNotificationConfig(configs) !== ErrCode.ERR) {
      // 处理后置逻辑
    } else {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to set notification config!');
      return;
    }
  }

  async getNotificationConfig() {
    const configs: spaceManager.NotificationConfig[] | undefined =
      await NotificationConfigApi.getNotificationConfig();
    if (configs === undefined) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to get notification config!');
      return;
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button($r('app.string.setNotificationConfig'))
          .buttonCommonStyle()
          .onClick(() => {
            this.setNotificationConfig();
          })
      }

      Row() {
        Button($r('app.string.getNotificationConfig'))
          .buttonCommonStyle()
          .onClick(() => {
            this.getNotificationConfig();
          })
      }

      Row() {
        Button($r('app.string.back'))
          .buttonCommonStyle()
          .onClick(() => {
            router.back();
          })
      }
    }
  }
}

@Extend(Button)
function buttonCommonStyle() {
  .width(200)
  .height(50)
  .backgroundColor('#6366F1')
  .fontColor('#FFFFFF')
  .fontSize(14)
  .margin({ left: 20, bottom: 5 })
}
```
