---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-package
title: @system.package (应用管理)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 已停止维护的接口 > @system.package (应用管理)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:289f90d253ad2864ad0534ebc470898a9ec42f759065d38ee3f05626133a6b7a
---

说明

* 从API version 9开始不再维护，推荐使用该模块[@ohos.bundle.bundleManager](js-apis-bundlemanager.md)。
* 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import Package from '@system.package';
```

## package.hasInstalled(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 3开始支持，从API version 9开始废弃，建议使用[getBundleInfo](js-apis-bundlemanager.md#bundlemanagergetbundleinfo14)替代。

hasInstalled(options: CheckPackageHasInstalledOptions): void

查询指定应用是否存在，或者原生应用是否安装。

**系统能力：** SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CheckPackageHasInstalledOptions](js-apis-system-package.md#checkpackagehasinstalledoptions) | 是 | 选项参数。 |

**示例：**

```
1. import Package from '@system.package';

3. @Entry
4. @Component
5. struct MainPage {
6. hasInstalled() {
7. Package.hasInstalled({
8. bundleName: 'com.example.bundlename',
9. success: (data) => {
10. console.log('package has installed: ' + data);
11. },
12. fail: (msg:string, code) => {
13. console.log('query package fail, code: ' + code + ', data: ' + msg);
14. },
15. });
16. }
17. build() {
18. }
19. }
```

## CheckPackageHasInstalledResponse

PhonePC/2in1TabletTVWearable

说明

从API version 3开始支持，从API version 9开始废弃。

指示应用包是否已安装。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | boolean | 是 | 指示应用是否已安装。 |

## CheckPackageHasInstalledOptions

PhonePC/2in1TabletTVWearable

说明

从API version 3开始支持，从API version 9开始废弃。

查询包是否已安装时的选项。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 应用Bundle名称。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |
