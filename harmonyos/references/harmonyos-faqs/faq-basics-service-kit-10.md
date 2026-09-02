---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-10
title: 如何获取系统版本号
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何获取系统版本号
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0cfe69f0efdd26dfb31e17335ea2731e2cddc9d22f800c051e5986988235a43e
---

可通过[@ohos.deviceInfo (设备信息)](../harmonyos-references/js-apis-device-info.md)模块，查询设备信息。

示例如下：

```typescript
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
