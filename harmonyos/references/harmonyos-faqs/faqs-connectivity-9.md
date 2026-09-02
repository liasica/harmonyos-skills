---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-9
title: 平板应用使用NFC功能时闪退
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 平板应用使用NFC功能时闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ba3e3eee54918d736cc00e575b763b9ac9b59decea4f53c6b38d0c358af67c04
---

## 问题现象

平板上的应用使用NFC功能时，发生闪退。

## 背景知识

* JsCrash异常根据不同的异常场景，在Reason字段进行了分类，分为Error、TypeError、SyntaxError、ReferenceError、RangeError等错误类型。参考文档[JS Crash（进程崩溃）检测](../harmonyos-guides/jscrash-guidelines.md)。
* JsCrash日志规格说明可以参考[日志规格](../harmonyos-guides/jscrash-guidelines.md#日志规格)。
* [tag.unregisterForegroundDispatch](../harmonyos-references/js-apis-nfctag.md#tagunregisterforegrounddispatch10)接口的作用是取消注册对NFC Tag读卡事件的监听，退出前台应用优先分发。

## 问题定位

1. 从faultlogger目录下获取到应用的JsCrash故障日志，故障原因是TypeError，故障信息为Cannot read property unregisterForegroundDispatch of undefined，无法调用未定义的属性和方法。

   ```shell
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
2. 从堆栈中观察到栈顶为NFCUtil，未定义的属性和方法是unregisterForegroundDispatch，是[@ohos.nfc.tag (标准NFC-Tag)](../harmonyos-references/js-apis-nfctag.md)的接口，平板不支持此领域的接口，设备的系统不存在相关SDK，这会导致在调用时出现undefined错误。

## 分析结论

平板不支持NFC相关能力，导致接口调用时出现undefined错误。

## 修改建议

使用canIUse("SystemCapability.Communication.NFC.Tag")判断设备是否支持NFC能力，详情可见[NFC标签读写开发指南](../atomic-guides/atomic-nfc-tag-access-guide.md)。

```ts
@Entry
@Component
struct CheckNFCAbilityPage {
  @State nfcSupport: boolean = false;

  aboutToAppear(): void {
    this.checkNfcCapability();
  }

  // 检查设备硬件能力
  checkNfcCapability() {
    if (canIUse('SystemCapability.Communication.NFC.Core')) {
      this.nfcSupport = true;
      console.log('该设备支持NFC功能');
    } else {
      this.nfcSupport = false;
      console.log('该设备不支持NFC功能');
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
