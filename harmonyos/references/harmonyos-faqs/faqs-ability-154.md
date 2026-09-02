---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-154
title: 如何解决使用getBundleInfoForSelf接口获取appinfo中permissions信息为空的问题
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何解决使用getBundleInfoForSelf接口获取appinfo中permissions信息为空的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:57a247c8c87e413d6e7b0c10208f2eab812f1285ba18688d6d99c021e89e4350
---

## 问题现象

在开发应用时，需要获取应用包申请权限信息，系统提供了bundleManager.getBundleInfoForSelf接口去获取应用包权限信息，但接口返回后获取的appinfo信息中permissions为空值，是什么原因？

```ts
let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION;
bundleManager.getBundleInfoForSelf(this.bundleFlags).then((data) => {
  let permissions = JSON.stringify(data.reqPermissionDetails);
  hilog.info(0x0000, 'test', `permissions: ${permissions}`);
})
```

## 背景知识

应用包信息，可以通过[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取自身的应用包信息，其中参数[BundleFlag](../harmonyos-references/js-apis-bundlemanager.md#bundleflag)指定所返回的[BundleInfo](../harmonyos-references/js-apis-bundlemanager-bundleinfo.md)中所包含的信息。

## 问题定位

1. 调用bundleManager.getBundleInfoForSelf接口获取应用包信息需要传入bundleFlags参数，根据传入的bundleFlags参数不同，获取的appinfo信息不同，检查bundleFlags参数是否设置正确。
2. bundleFlags参数设置可以参考[BundleFlag](../harmonyos-references/js-apis-bundlemanager.md#bundleflag)。
3. 获取应用包申请权限信息需要添加包信息标志GET\_BUNDLE\_INFO\_WITH\_REQUESTED\_PERMISSION，未添加此标志值则无法获取应用包申请权限信息。

## 分析结论

由于未添加包信息标志GET\_BUNDLE\_INFO\_WITH\_REQUESTED\_PERMISSION，导致无法获取包申请权限信息。

## 修改建议

添加包信息标志GET\_BUNDLE\_INFO\_WITH\_REQUESTED\_PERMISSION，以获取包申请权限信息。

```ts
import { bundleManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct GetBundleInfo {
  getInfo() {
    let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
    bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION;
    bundleManager.getBundleInfoForSelf(bundleFlags).then((data) => {
      let permissions = JSON.stringify(data.reqPermissionDetails);
      hilog.info(0x0000, 'TAG', 'permissions:' + permissions);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'TAG', err.message);
    });
  }

  build() {
    Column() {
      Button('点击获取包申请权限信息')
        .fontSize(30)
        .onClick(() => {
          this.getInfo();
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

## 总结

部分API接口会根据传入的参数不同而返回不同的结果，在使用此类API接口时需要注意传入参数的准确性，从而正确的获取所需要的数据。
