---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-pc-phones-sandbox
title: 分享内容直达应用界面
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与PC/2in1碰一碰分享 > 分享内容直达应用界面
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:33+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:d03c913e877c7b57443fe5b3da43c1fe8ebbb169f8837dba74a33aa619484b6b
---

从6.0.0(20)版本开始，沙箱接收能力支持PC/2in1设备；从6.1.0(23)版本开始，新增支持Tablet设备。

PC/2in1、Tablet设备创新交互方案：支持手机轻贴屏幕即可将单/多文件快速传输至PC/2in1或Tablet设备应用沙箱，传输完成后通知目标应用接收文件列表，实现无缝预览与编辑。

沙箱接收仅支持文件类型的数据，应用需指定支持接收的文件类型和最大数量。

* 若类型不匹配，则跳过已注册的沙箱接口能力，采用华为分享默认逻辑接收文件数据。参考：[目标设备接收分享数据一步直达体验](share-access-one-step.md)。
* 若数量不匹配，则通过系统弹窗提示用户异常。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { uniformTypeDescriptor as utd } from '@kit.ArkData';
   import { systemShare, harmonyShare } from '@kit.ShareKit';
   import { common } from '@kit.AbilityKit';
   ```
2. 进入可接收数据的窗口，注册沙箱接收事件。

   ```typescript
   aboutToAppear(): void {
     let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
       windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
       capabilities: [{ // 设置接收端支持的数据类型及数量
         utd: utd.UniformDataType.IMAGE,
         maxSupportedCount: 1
       }]
     }
     // 注册沙箱接收'dataReceive'监听事件
     harmonyShare.on('dataReceive', capabilityRegistry, (receivableTarget: harmonyShare.ReceivableTarget) => {
       let uiContext: UIContext = this.getUIContext();
       let context = uiContext.getHostContext() as common.UIAbilityContext;
       receivableTarget.receive(context.filesDir, { // 此路径仅为示例 使用时请替换实际路径
         onDataReceived: (sharedData: systemShare.SharedData) => {
           let sharedRecords = sharedData.getRecords();
           sharedRecords.forEach((record: systemShare.SharedRecord) => {
             // 处理分享数据
           });
         },
         onResult(resultCode: harmonyShare.ShareResultCode) {
           if (resultCode === harmonyShare.ShareResultCode.SHARE_SUCCESS) {
             // To do things.
           }
         }
       });
     });
   }
   ```
3. 关闭可接收数据的窗口，取消沙箱接收事件。

   ```typescript
   aboutToDisappear(): void {
     let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
       windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
       capabilities: [{
         utd: utd.UniformDataType.IMAGE,
         maxSupportedCount: 1
       }]
     }
     // 取消沙箱接收'dataReceive'监听事件
     harmonyShare.off('dataReceive', capabilityRegistry);
   }
   ```

## 拒绝本次沙箱接收

当本次沙箱接收回调触发时，如果应用因为业务实现需要拒绝本次接收时，可使用[ReceivableTarget.reject()](../harmonyos-references/share-harmony-share.md#reject-1)方法拒绝本次接收。

```typescript
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { harmonyShare } from '@kit.ShareKit';

@Component
export default struct Index {
  aboutToAppear(): void {
    let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
      windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
      capabilities: [{
        utd: utd.UniformDataType.IMAGE,
        maxSupportedCount: 1
      }]
    }
    // 注册沙箱接收'dataReceive'监听事件
    harmonyShare.on('dataReceive', capabilityRegistry, (receivableTarget: harmonyShare.ReceivableTarget) => {
      receivableTarget.reject(harmonyShare.ReceivableErrorCode.NO_RECEIVABLE_ERROR);
    });
  }

  aboutToDisappear(): void {
    let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
      windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
      capabilities: [{
        utd: utd.UniformDataType.IMAGE,
        maxSupportedCount: 1
      }]
    }
    // 取消沙箱接收'dataReceive'监听事件
    harmonyShare.off('dataReceive', capabilityRegistry);
  }

  build() {
  }
}
```
