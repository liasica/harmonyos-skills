---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-pc-phones-mutually
title: 手机与PC/2in1、手机与Tablet间相互分享
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与PC/2in1碰一碰分享 > 手机与PC/2in1、手机与Tablet间相互分享
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:33+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:1bdb0b902f7acaed30008fe0b7757ace2e3213233add2f65c96250a9ea726102
---

Phone与PC/2in1设备间相互分享，可参考：[手机间内容分享](knock-share-between-phones-content.md)。

从6.1.0(23)版本开始，Phone与Tablet设备间相互分享，可参考：[手机间内容分享](knock-share-between-phones-content.md)。

## 获取轻碰坐标

从26.0.0版本开始，手机与PC/2in1、手机与Tablet设备触发轻碰事件时，在PC/2in1或Tablet设备侧可从回调事件中获取轻碰的位置（基于屏幕左上角为初始点的坐标信息），通过轻碰的位置不同，实现不同的业务逻辑。例如向文档指定位置插入图片，或者获取窗口中指定的图片等。

```typescript
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { harmonyShare, systemShare } from '@kit.ShareKit';
import { fileUri } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Component
export default struct KnockShareScreen {
  @State knockShareScreenX: number | undefined = undefined;
  @State knockShareScreenY: number | undefined = undefined;
  @State dataReceiveScreenX: number | undefined = undefined;
  @State dataReceiveScreenY: number | undefined = undefined;

  aboutToAppear(): void {
    this.knockShareListening();
  }

  private knockShareListening() {
    harmonyShare.on('knockShare', this.knockShareCallback);

    let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
      windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
      capabilities: [{ // 设置接收端支持的数据类型及数量
        utd: utd.UniformDataType.IMAGE,
        maxSupportedCount: 1
      }]
    }
    harmonyShare.on('dataReceive', capabilityRegistry, this.dataReceiveCallback);
  }

  private knockShareCallback = (sharableTarget: harmonyShare.SharableTarget) => {
    let uiContext: UIContext = this.getUIContext();
    let contextFaker: Context = uiContext.getHostContext() as Context;
    let filePath = contextFaker.filesDir + '/exampleKnock1.jpg'; // 仅为示例 请替换正确的文件路径
    let shareData: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.JPEG,
      uri: fileUri.getUriFromPath(filePath),
      thumbnailUri: fileUri.getUriFromPath(filePath)
    });
    let sharableTargetInfo = sharableTarget.getInfo(); // 通过getInfo方法获取屏幕信息
    this.knockShareScreenX = sharableTargetInfo.coordinate?.screenX;
    this.knockShareScreenY = sharableTargetInfo.coordinate?.screenY;
    sharableTarget.share(shareData);
  }

  private dataReceiveCallback = (receivableTarget: harmonyShare.ReceivableTarget) => {
    let uiContext: UIContext = this.getUIContext();
    let context = uiContext.getHostContext() as common.UIAbilityContext;
    let sandboxUri = fileUri.getUriFromPath(context.filesDir);
    let receivableTargetInfo = receivableTarget.getInfo(); // 通过getInfo方法获取屏幕信息
    this.dataReceiveScreenX = receivableTargetInfo.coordinate?.screenX;
    this.dataReceiveScreenY = receivableTargetInfo.coordinate?.screenY;
    receivableTarget.receive(sandboxUri, {
      onDataReceived: (sharedData: systemShare.SharedData) => {
        // do something.
      },
      onResult: (resultCode: harmonyShare.ShareResultCode) => {
        if (resultCode === harmonyShare.ShareResultCode.SHARE_SUCCESS) {
          // do something.
        }
      }
    });
  }

  build() {
  }
}
```
