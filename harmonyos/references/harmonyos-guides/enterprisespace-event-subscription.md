---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-event-subscription
title: 空间事件订阅
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 空间事件订阅
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dfe6e3d212db713e037cffcde0a654c1b365e9a213d32e85fe63085a03f5daf0
---

从API版本6.0.0(20)开始，支持订阅和取消订阅空间事件的能力。

## 场景介绍

Enterprise Space Kit为应用提供订阅空间事件的能力。订阅空间切换事件后，应用将在空间切换时收到通知，并执行预设的自定义动作。同时，也提供取消订阅空间事件的能力，支持应用在特定场景下灵活管理空间事件的订阅状态。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [subscribeEvent](../harmonyos-references/enterprisespace-spacemanager.md#subscribeevent)(eventId: [EventType](../harmonyos-references/enterprisespace-spacemanager.md#eventtype)[], callback: AsyncCallback<[EventData](../harmonyos-references/enterprisespace-spacemanager.md#eventdata)>): number | 订阅空间事件，在相关事件触发时，通知应用侧。 |
| [unsubscribeEvent](../harmonyos-references/enterprisespace-spacemanager.md#unsubscribeevent)(subscribeId: number): void | 取消订阅空间事件，在相关事件触发时，不再通知应用侧。 |

## 开发步骤

1.导入空间事件订阅API模块相关依赖。

```typescript
import { AsyncCallback } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { ErrCode } from '../../common/ErrCode';
```

2.空间事件订阅API接口封装。

```typescript
const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

export class SubscribeSpaceEventApi {
  static subscribeEvent(eventIds: spaceManager.EventType[], callback: AsyncCallback<spaceManager.EventData>): number {
    try {
      const subscribeId = spaceManager.subscribeEvent(eventIds, callback);
      hilog.info(DOMAIN, TAG, `Succeeded in subscribing event. subscribeId: ${subscribeId}`);
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to subscribe event. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }

  static unsubscribeEvent(subscribeId: number): void {
    try {
      spaceManager.unsubscribeEvent(subscribeId);
      hilog.info(DOMAIN, TAG, 'Succeeded in unsubscribing event');
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to unsubscribe event. Code: ${err.code}, message: ${err.message}`);
    }
  }
}
```

3.导入空间事件订阅业务实现相关依赖。

```typescript
import { router } from '@kit.ArkUI';
import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { SubscribeSpaceEventApi } from '../api/SubscribeSpaceEventApi'
import { ErrCode } from '../../common/ErrCode';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

4.空间事件订阅业务相关实现。

```typescript
const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

@Entry
@Component
struct SubscribeSpaceEventPage {
  subscribe() {
    let eventIds: spaceManager.EventType[] = [spaceManager.EventType.EVENT_WORKSPACE_SWITCHED];
    let callBack = (error: BusinessError, data: spaceManager.EventData) => {
      if (error) {
        hilog.error(DOMAIN, TAG, `error info:${error?.code}, err message:${error?.message}`);
      } else {
        hilog.info(DOMAIN, TAG, `event: ${data.event},currentWorkSpaceId: ${data.currentWorkspaceId}`);
        // 处理事件
      }
    };
    if (SubscribeSpaceEventApi.subscribeEvent(eventIds, callBack) !== ErrCode.OK) {
      // 订阅失败处理
      hilog.error(DOMAIN, TAG, 'Failed to subscribe event!');
      return;
    }

    // 订阅成功处理
  }

  unSubscribe() {
    let subscribeId = 100; // 由订阅空间事件得到的订阅ID。
    SubscribeSpaceEventApi.unsubscribeEvent(subscribeId);
  }

  build() {
    Column() {
      Row() {
        Button($r('app.string.subscribe'))
          .buttonCommonStyle()
          .onClick(() => {
            this.subscribe();
          })
      }

      Row() {
        Button($r('app.string.unSubscribe'))
          .buttonCommonStyle()
          .onClick(() => {
            this.unSubscribe();
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
