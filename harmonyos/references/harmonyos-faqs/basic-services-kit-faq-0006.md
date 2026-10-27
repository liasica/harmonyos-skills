---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/basic-services-kit-faq-0006
title: 设备版本号获取常见问题
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 常见问题 > 设备版本号获取常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:19+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:42956c5145d3f7665c91827f83c6f80de46cd7a0394d60564672235865b137fe
---

**Q：如何获取系统版本号？**

**A**：可通过[@ohos.deviceInfo (设备信息)](../harmonyos-references/js-apis-device-info.md)模块，查询设备信息。与版本相关的字段有三个，含义各不相同：

* displayVersion：产品版本，示例：ALN-AL00 5.0.0.1(XXX)。
* osFullName：系统版本，版本格式 OpenHarmony-x.x.x.x（即本题所指"系统版本号"）。
* versionId：版本 ID，由 deviceType、manufacture、brand、productSeries、osFullName、productModel、softwareModel、sdkApiVersion、incrementalVersion、buildType 拼接组成，并非单独的版本号。

如需版本号中各段数值，官方建议直接使用 majorVersion、seniorVersion、featureVersion、buildVersion，不建议自行解析 osFullName；如需发行版（HarmonyOS）系统版本号，可用 distributionOSVersion（起始 API version 10，格式 x.x.x，示例：5.0.0）。

示例如下：

```ts
import { deviceInfo } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let displayVersionInfo: string = deviceInfo.displayVersion; // product version
let osFullNameInfo: string = deviceInfo.osFullName; // system version
let versionIdInfo: string = deviceInfo.versionId; // version ID

@Entry
@Component
struct GetSysVersion {
  build() {
    Row() {
      Column() {
        Button('get device info')
          .onClick(() => {
            hilog.info(0x000, 'displayVersion TAG', `displayVersion:${displayVersionInfo}`);
            hilog.info(0x000, 'osFullName TAG', `osFullName:${osFullNameInfo}`);
            hilog.info(0x000, 'versionId TAG', `versionId:${versionIdInfo}`);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

**说明** 

示例结果通过 hilog 输出，运行后可在 DevEco Studio 的日志窗口查看，或执行 hdc shell hilog 并按 displayVersion TAG、osFullName TAG、versionId TAG 过滤查看。

**Q：如何获取设备支持的API的版本号？**

**A**：可以通过设备信息模块deviceInfo查询，常见的版本号获取方式如下：

* 系统软件API版本：deviceInfo.sdkApiVersion（number，示例：12）。
* 首个版本系统软件API版本：deviceInfo.firstApiVersion（number，示例：3）。
* 发行版系统API版本：deviceInfo.distributionOSApiVersion（number，起始 API version 10）。注意其返回值为数值编码而非点分版本号，取值 = X\*10000 + Y\*100 + Z，以 50001 为基数递增，例如 API version 6.1.1(24) 对应返回 60101；从 API version 26.0.0 起，系统 API 版本格式为 sdkApiVersion.sdkMinorApiVersion.sdkPatchApiVersion。

参考链接：[@ohos.deviceInfo (设备信息)](../harmonyos-references/js-apis-device-info.md)。
