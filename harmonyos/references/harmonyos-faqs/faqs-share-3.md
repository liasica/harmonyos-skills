---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-share-3
title: 如何获取到其他应用分享的内容
breadcrumb: FAQ > 应用服务开发 > 内容分享服务（Share Kit） > 如何获取到其他应用分享的内容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:8098ef87a006b2bdc131d03ccadf6cf5da2aa3b30d43e9c6d49aaa2f8ed26497
---

## 问题现象

在“entry/src/main/ets/entryability/EntryAbility”文件中onForeground生命周期方法使用systemShare.getSharedData方法无法获取到其他应用分享的内容。

问题代码示例参考如下：

```screen
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { systemShare } from '@kit.ShareKit';

const DOMAIN = 0x0000;

let  storageWant:Want|undefined = undefined
export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    storageWant = want;
  }
  // ...
  onForeground(): void {
    // Ability has brought to foreground
    systemShare.getSharedData(storageWant)
      .then((data: systemShare.SharedData) => {
        data.getRecords().forEach((record: systemShare.SharedRecord) => {
          // 处理分享数据
          console.info('getSharedData utd 分享')
        });
      })
      .catch((error: BusinessError) => {
        console.error(`Failed to getSharedData. Code: ${error.code}, message: ${error.message}`);
      });
  }
}
```

## 背景知识

[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)：当已经启动的UIAbility实例再次被拉起时，系统会触发该回调。

[onForeground](../harmonyos-guides/uiability-lifecycle.md#onforeground)：在UIAbility切换至前台时且UIAbility的UI可见之前，系统触发onForeground回调。

## 解决方案

onNewWant和onForeground都具备从后台转前台触发的特性。但是onForeground没有返回最新的want，而onNewWant方法能够获取新的want，这个want里有其他应用分享的内容。示例如下：

```screen
onNewWant(want: Want) {
  systemShare.getSharedData(want)
    .then((data: systemShare.SharedData) => {
      data.getRecords().forEach(() => {
        // 处理分享数据
        this.context.eventHub.emit("ShareContent", { msg: "应用进入前台" });
      });
    })
    .catch((error: BusinessError) => {
      console.error(`Failed to getSharedData. Code: ${error.code}, message: ${error.message}`);
    });
}
```

另外，目标应用可通过解析分享过来的数据中的[SharedRecord](../harmonyos-references/share-system-share.md#sharedrecord)里的UTD的值判断分享的文件夹或具体的文件类型。

类型匹配参考：[UTD预置列表](../harmonyos-guides/uniform-data-type-list.md)。文件夹名或文件名可以通过title字段获取。以便在界面展示分享内容的基本信息。
