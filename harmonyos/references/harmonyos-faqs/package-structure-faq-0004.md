---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/package-structure-faq-0004
title: 应用包信息查询与免安装配置常见问题
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 常见问题 > 应用包信息查询与免安装配置常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:17+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:b5534b5d819eb2c8f4861a343c5f370f753b8fd60b73dfb4f3e87ceecbb8d794
---

**Q：如何查询应用包的名称、供应商、版本号、版本文本、安装时间、更新时间描述信息？**

**A**：首先，通过 bundleManager.getBundleInfoForSelf() 接口获取应用包的名称、供应商、版本号、版本文本、安装时间和更新时间。具体可参考示例代码：

```ts
import { bundleManager } from '@kit.AbilityKit';

// Apply to obtain BundleInfo and applicationInfo
let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION;

try {
  bundleManager.getBundleInfoForSelf(bundleFlags, (err, data) => {
    // Get the bundle name of the application itself
    const bundleName = data.name;
    // Get the version number of the application（versionCode）
    const versionCode = data.versionCode;
    // Get the version name of the application（versionName）
    const versionName = data.versionName;

    if (err) {
      console.error(`getBundleInfoForSelf failed: ${err.message}`);
    } else {
      console.info(`get bundleName successfully: ${bundleName}`);
      console.info(`get versionCode successfully: ${versionCode}`);
      console.info(`get versionName successfully: ${versionName}`);
      console.info(`getBundleInfoForSelf successfully: ${JSON.stringify(data)}`);
    }
  });
} catch (err) {
  console.error(`getBundleInfoForSelf failed: ${JSON.stringify(err)}`);
}
```

参考链接：[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself-1)。

**Q：应用免安装的限制、字段解释以及如何自测？**

**A**：应用免安装的限制、字段解释以及自测方式如下：

* 免安装限制：免安装HAP的总大小限制为10M。10M是指所有HAP的总大小。如果App内有多个HAP，所有HAP的总大小不能超过10M。分包时，每个文件的大小不能超过2M。
* DeliveryWithInstall：配置应用的可选安装功能。具体场景是在应用市场下载安装时，是否跟随应用一起安装。Entry模块的该字段允许设置为false。配置为true的HAP包也会计算在免安装的10M限制内。
* InstallationFree：标识当前Module是否支持免安装特性。如果应用的Entry类型Module的该字段配置为true，Feature类型Module的该字段也必须配置为true。
* 自测：开发者需编写一个服务中心，模拟处理免安装请求。

参考链接：[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)。
