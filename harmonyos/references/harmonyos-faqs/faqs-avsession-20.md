---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-20
title: 创建AVSession出错，错误码6600101
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 创建AVSession出错，错误码6600101
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:902f8fe705171d0eab6f51c37a73470fe067a6301cd64d77825c799f6777379f
---

## 问题现象

在销毁上一次成功创建的AVSession后创建新的AVSession时，偶尔会出现新AVSession创建失败。报错信息为：CreateSession failed，错误码为6600101。

## 背景知识

[AVSession](../harmonyos-references/arkts-apis-avsession-avsession.md)是系统提供的音视频管控服务，用于统一管理系统中所有音视频行为，构建音视频统一展示和控制能力。

## 问题定位

1. 根据问题现象中的场景和错误码，确定是创建AVSession时出错，原因是[会话服务端异常](../harmonyos-references/errorcode-avsession.md#section6600101-会话服务端异常)。
2. 参考[createAVSession](../harmonyos-references/arkts-apis-avsession-f.md#avsessioncreateavsession10)（创建AVSession），一个Ability只能存在一个AVSession，重复创建会失败，错误码为6600101。推测是重复创建导致错误。
3. 在确保当前AVSession销毁完毕后再创建新的AVSession，创建AVSession成功。
4. 确定是重复创建AVSession导致错误。

## 分析结论

一个Ability中只能存在一个AVSession，重复创建会失败。在创建AVSession时，必须确保此时Ability内没有已创建的AVSession存在。

## 修改建议

销毁媒体会话的[destroy](../harmonyos-references/arkts-apis-avsession-avsession.md#destroy10)是异步接口，需要确保销毁流程完毕后，才能创建新的AVSession。

```ts
import { avSession } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  private session?: avSession.AVSession = undefined;

  build() {
    Column() {
      Button('Create Session')
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          if (this.session !== undefined) {
            this.session.destroy()
              .then(async () => {
                try {
                  this.session = await avSession.createAVSession(context, 'SESSION_NAME', 'audio');
                  console.info(`create session successfully`);
                } catch (err) {
                  console.error(`failed to create session, error=${JSON.stringify(err)}`);
                }
              })
              .catch((err: BusinessError) => {
                console.error(`failed to destroy session, error=${JSON.stringify(err)}`);
              });
          } else {
            try {
              this.session = await avSession.createAVSession(context, 'SESSION_NAME', 'audio');
            } catch (err) {
              console.error(`failed to create session, error=${JSON.stringify(err)}`);
            }
          }
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```
