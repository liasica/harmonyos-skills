---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-between-phones-group
title: 邀请组队
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与手机碰一碰分享 > 邀请组队
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:21+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:ce5aa56c67004b8f62bf79ea3fa4222386c4f5f105b2ca9b78f39c1aedc2bcf0
---

## 注册碰一碰事件

在组队房间邀请界面注册碰一碰事件。

**图1** 横屏应用示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/_Q_27x6LQgW_8tU-LUR5fw/zh-cn_image_0000002742124365.png)

**图2** 竖屏应用示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/N3UQWjZcSMuZyWV3iu2QoQ/zh-cn_image_0000002712245458.png)

## 注册单向分享能力

通过碰一碰分享邀请好友加入组队房间，若双方都同时在组队房间内互相邀请，无法相互加入对方的组队房间。

针对以上场景，Share Kit提供单向仅发送能力。参考：[SendCapabilityRegistry](../harmonyos-references/share-harmony-share.md#sendcapabilityregistry)的sendOnly属性。

若碰一碰的双方都设置单向仅发送，则终止本次分享并提示用户"请任意一方退出当前应用后再试"；反之，均可分享成功。

```typescript
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';
import { fileUri } from '@kit.CoreFileKit';

@Component
export default struct Index {
  aboutToAppear(): void {
    let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
      windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
      sendOnly: true // 声明仅支持单向发送 若对端也同样声明仅支持单向发送 则双向分享时会失败
    }
    harmonyShare.on('knockShare', capabilityRegistry, (sharableTarget: harmonyShare.SharableTarget) => {
      let uiContext: UIContext = this.getUIContext();
      let contextFaker: Context = uiContext.getHostContext() as Context;
      let filePath = contextFaker.filesDir + '/exampleKnock1.jpg'; // 仅为示例 请替换正确的文件路径
      let shareData: systemShare.SharedData = new systemShare.SharedData({
        utd: utd.UniformDataType.HYPERLINK,
        content: 'https://sharekitdemo.drcn.agconnect.link/ZB3p',
        // 根据title,description,thumbnailUri会生成不同的卡片模板。
        thumbnailUri: fileUri.getUriFromPath(filePath),
        title: '碰一碰分享卡片标题',
        description: '碰一碰分享卡片描述'
      });
      sharableTarget.share(shareData);
    });
  }

  aboutToDisappear(): void {
    let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
      windowId: 999 // 此值仅为示例 实际使用时请替换正确的windowId
    }
    // 解除碰一碰分享'knockShare'监听事件
    harmonyShare.off('knockShare', capabilityRegistry);
  }

  build() {
  }
}
```

## 设置组队邀请预览

预览图设置参考：[设置分享预览](knock-share-between-phones-content.md#设置分享预览)。

## 处理组队链接

当目标应用被分享拉起时，可以通过[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)回调中获取传入的want参数。其中want.uri字段为邀请组队的链接，通过链接上携带的参数信息，处理组队邀请的业务逻辑。

示例代码：

```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage): Promise<void> {
    try {
      windowStage.loadContent('pages/Index');
    } catch (error) {
      console.error(`onWindowStageCreate error. Code: ${error?.code}, message: ${error?.message}`);
    }
  }

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    console.info('EntryAbility onCreate invoked. uri: ', want.uri);
    // to do things.
  }

  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    console.info('EntryAbility onNewWant invoked. uri: ', want.uri);
    // to do things.
  }
}
```

## 异常场景终止分享

当碰一碰分享回调触发时，发生异常场景导致无法继续分享，可终止本次分享。

参考：[异常场景终止分享](knock-share-between-phones-content.md#异常场景需终止分享)。
