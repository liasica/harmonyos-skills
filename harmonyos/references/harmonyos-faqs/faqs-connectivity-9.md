---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-9
title: 不支持NFC的设备使用NFC功能时应用闪退
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 不支持NFC的设备使用NFC功能时应用闪退
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:18+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:5cc9ad255539d6a7d128f71c4222e4086cb48afcc7115c7f0df93eccb88c3cb3
---

## 问题现象

不支持NFC的设备上使用NFC功能时，应用发生闪退。

## 背景知识

* JsCrash异常根据不同的异常场景，在Reason字段进行了分类，分为Error、TypeError、SyntaxError、ReferenceError、RangeError等错误类型。参考文档[JS Crash（进程崩溃）检测](../harmonyos-guides/jscrash-guidelines.md)。
* JsCrash日志规格说明可以参考[日志规格](../harmonyos-guides/jscrash-guidelines.md#日志规格)。
* [tag.unregisterForegroundDispatch](../harmonyos-references/js-apis-nfctag.md#tagunregisterforegrounddispatch10)接口的作用是取消注册对NFC Tag读卡事件的监听，退出前台应用优先分发。

## 问题定位

1. 从faultlogger目录下获取到应用的JsCrash故障日志，故障原因是TypeError，故障信息为Cannot read property xxx of undefined（xxx为NFC相关属性或方法，如unregisterForegroundDispatch、NFC\_A等），无法调用未定义的属性和方法。

   ```txt
   Reason:TypeError
   Error name:TypeError
   Error message:Cannot read property unregisterForegroundDispatch of undefined
   Stacktrace:
   Cannot get SourceMap info, dump raw stack:
       at unRegister (phone|phone|1.0.0|src/main/ets/utils/NFCUtil.ts:52:1)
       at onWebPageAboutToDisappear (phone|phone|1.0.0|src/main/ets/scenes/webview/jshandler/JsMsgNFCHandler.ts:110:1)
       at anonymous (phone|phone|1.0.0|src/main/ets/scenes/webview/jshandler/JsManager.ts:130:1)
       at webPageDestroyEventDispatch (phone|phone|1.0.0|src/main/ets/scenes/webview/jshandler/JsManager.ts:130:1)
       at webPageAboutToDisappear (phone|phone|1.0.0|src/main/ets/scenes/webview/jshandler/JsProxy.ts:34:1)
       at aboutToDisappear (phone|phone|1.0.0|src/main/ets/scenes/webview/pages/WebViewPage.ts:211:1)
   ```
2. 不支持NFC硬件的设备上系统不会加载tag模块，通过import { tag } from '@kit.ConnectivityKit'导入的tag对象为undefined。代码中直接访问tag的属性或方法时（如调用tag.unregisterForegroundDispatch或在类属性初始化器中访问tag.NFC\_A），触发TypeError未被捕获，导致应用崩溃。

## 分析结论

不支持NFC的设备上系统不加载tag模块，import导入的tag对象为undefined，访问tag的属性或方法时触发TypeError未被捕获，应用崩溃。

## 修改建议

使用canIUse("SystemCapability.Communication.NFC.Core")判断设备是否支持NFC能力，详情可见[NFC标签读写开发指南](../atomic-guides/atomic-nfc-tag-access-guide.md)。

```ts
@Entry
@Component
struct CheckNFCAbilityPage {
  @State nfcSupport: boolean = false;

  aboutToAppear(): void {
    this.checkNfcCapability();
  }

  // 检查设备是否支持NFC能力
  checkNfcCapability() {
    if (canIUse('SystemCapability.Communication.NFC.Core')) {
      this.nfcSupport = true;
      console.info('该设备支持NFC功能');
    } else {
      this.nfcSupport = false;
      console.info('该设备不支持NFC功能');
    }
  }

  build() {
    Column() {
      if (!this.nfcSupport) {
        // 设备不支持NFC的情况
        Text('当前设备不支持NFC功能')
          .fontSize(20)
          .fontColor(Color.Red)
      } else {
        Text('当前设备支持NFC功能')
          .fontSize(20)
          .fontColor(Color.Red)
      }
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
