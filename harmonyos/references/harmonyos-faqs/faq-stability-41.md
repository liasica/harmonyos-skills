---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-41
title: 未开启NFC情况下跳转NFC功能页面，应用闪退重启
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 未开启NFC情况下跳转NFC功能页面，应用闪退重启
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:fbbfdbc633d540e2c75fb2c5181a8488a0d30153c5846392b25b5e2f08222d76
---

## 问题现象

NFC关闭情况下，点击跳转到应用NFC功能页面，随后立刻闪退重启。

## 背景知识

* [3100201 NFC服务读写Tag错误](../harmonyos-references/errorcode-nfc.md#section3100201-nfc服务读写tag错误)：异常信息Tag running state is abnormal in service，NFC服务执行Tag业务逻辑遇到错误。
* 关于NFC标签通信相关内容，可见[NFC标签读写开发指南](../harmonyos-guides/nfc-tag-access-guide.md)。

## 问题定位

1. 从faultlogger目录下获取到应用的JsCrash故障日志，故障原因是自定义错误类Error，故障信息为Tag running state is abnormal in service，NFC服务执行Tag业务逻辑遇到错误。堆栈中有具体到应用代码，栈顶函数为tagOn，由此可知，应用在调用[tag.on()](../harmonyos-references/js-apis-nfctag.md#tagonreadermode11)接口时NFC未开启，导致该异常产生。

   ```shell
   Reason:Error
   Error name:Error
   Error message:Tag running state is abnormal in service.
   Error code:
   Stacktrace:
   Cannot get SourceMap info, dump raw stack:
       at tagOn (entry|entry|1.0.0|src/main/ets/d/d1/e1.ts:0:1)
       at startReadCardWithHandler (entry|entry|1.0.0|src/main/ets/d/d1/e1.ts:0:1)
       at aboutToAppear (entry|entry|1.0.0|src/main/ets/pages/recharge/NFCRechargePage.ts:0:1)
       at anonymous (entry|entry|1.0.0|src/main/ets/pages/recharge/RechargeCenterPage.ts:0:1)
   ```
2. 排查[tag.on()](../harmonyos-references/js-apis-nfctag.md#tagonreadermode11)接口调用前，是否判断NFC可用，或者发生异常时，是否及时捕获处理。

## 分析结论

应用在NFC未开启的情况下调用[tag.on()](../harmonyos-references/js-apis-nfctag.md#tagonreadermode11)接口，导致异常闪退。

## 修改建议

在使用NFC相关能力时，应该先校验设备是否支持，以及状态是否开启。或者在出现异常时捕获处理，提醒用户开启NFC。

```ts
import { hilog } from '@kit.PerformanceAnalysisKit';
import { nfcController, tag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { bundleManager } from '@kit.AbilityKit';

let discTech : number[] = [tag.NFC_A]; // 用前台ability时所需要的技术代替
let elementName : bundleManager.ElementName = {
  bundleName: 'com.example.commondemofordfx',
  abilityName: 'EntryAbility'
};

function readerModeCb(err : BusinessError, tagInfo : tag.TagInfo) {
  if (!err) {
    console.log('offCallback: tag found tagInfo = ', JSON.stringify(tagInfo));
  } else {
    console.error('offCallback err: ' + err.message);
    return;
  }
  // taginfo的其他操作
}

@Entry
@Component
struct CheckNFCAbilityPage {
  @State nfcSupport: boolean = false;
  @State nfcOpen: boolean = false;
  @State nfcRunFailMsg: string = '未运行';

  aboutToAppear(): void {
    this.checkNfcCapability();
    this.checkNfcOpen();
  }

  // 检查设备是否支持NFC能力
  checkNfcCapability() {
    if (!canIUse('SystemCapability.Communication.NFC.Core')) {
      hilog.error(0x0000, 'testTag', 'nfc unavailable.');
      return;
    }
    this.nfcSupport = true;
  }

  // 检查Nfc是否开启
  checkNfcOpen() {
    if (!nfcController.isNfcOpen()) {
      hilog.error(0x0000, 'testTag', 'nfc disabled.');
      return;
    }
    this.nfcOpen = true;
  }

  NfcRun() {
    try {
      tag.on('readerMode', elementName, discTech, readerModeCb);
      this.nfcRunFailMsg = '运行成功';
    } catch (e) {
      hilog.error(0x0000, 'testTag',`tag.on error: ${(e as BusinessError).message}`);
      this.nfcRunFailMsg = `失败信息：${(e as BusinessError).message}`;
      // 异常处理，例如提示弹窗。
    }
  }

  build() {
    Column({ space: 20 }) {
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
      if (!this.nfcOpen) {
        // 设备不支持NFC的情况
        Text('NFC功能未开启')
          .fontSize(20)
          .fontColor(Color.Red)
      } else {
        Text('NFC功能已开启')
          .fontSize(20)
          .fontColor(Color.Red)
      }
      Button('重新检查NFC')
        .onClick(() => {
          this.checkNfcCapability();
          this.checkNfcOpen();
        })
      Button('点击运行NFC')
        .onClick(() => {
          this.NfcRun();
        })
      Text(this.nfcRunFailMsg).fontSize(20)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
