---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-169
title: 如何判断应用是否为系统应用
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何判断应用是否为系统应用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2b33568f3ffd7860a108e69e038dfe3153f761a492ed70a6d45fe34f398ac29d
---

## 问题现象

需要对当前应用打开其他应用行为做限制时，希望不限制打开系统应用行为。如何根据包名判断应用是否为系统应用呢？

## 解决方案

* 通过[getBundleInfo()](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfo14)接口查询应用信息：（需要[ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED](../harmonyos-guides/permissions-for-enterprise-apps.md#ohospermissionget_bundle_info_privileged)权限）

  该接口的bundleFlags参数传入GET\_BUNDLE\_INFO\_WITH\_APPLICATION可以获取返回的[BundleInfo](../harmonyos-references/js-apis-bundlemanager-bundleinfo.md#bundleinfo-1)中的[ApplicationInfo](../harmonyos-references/js-apis-bundlemanager-applicationinfo.md#applicationinfo-1)，其中systemApp字段标识应用是否为系统应用，取值为true表示系统应用，取值为false表示非系统应用。

  **注意**：调用该接口需要[ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED](../harmonyos-guides/permissions-for-enterprise-apps.md#ohospermissionget_bundle_info_privileged)权限，该权限为系统级别权限，API 7-13该权限仅向系统应用开放；从API 14开始，开放范围从系统应用变更为企业普通应用。

  关键代码如下：

  ```ts
  import { bundleManager } from '@kit.AbilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct IsSystemApp {
    build() {
      Column({ space: 10 }) {
        Button('华为钱包是系统应用吗')
          .onClick(() => {
            let bundleName = 'com.huawei.hmos.wallet'; // 应用包名
            let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION; // 用于获取包含appInfo的bundleInfo
            let userId = 100;
            try {
              bundleManager.getBundleInfo(bundleName, bundleFlags, userId, (err, data) => {
                if (err) {
                  console.error(`getBundleInfo failed: ${err.message}`);
                } else {
                  console.info(`getBundleInfo successfully, isSystemApp: ${data.appInfo.systemApp}`);
                }
              });
            } catch (err) {
              let message = (err as BusinessError).message;
              console.error(`getBundleInfo failed: ${message}`);
            }
          });
      }
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%');
    }
  }
  ```
* 通过[hdc shell bm dump -n bundleName](../harmonyos-guides/bm-tool.md#查询应用信息命令dump)命令查询指定Bundle名称的详细信息：

  根据此命令返回的applicationInfo中的isSystemApp字段判断是否为系统应用，isSystemApp为true，则为系统应用。
