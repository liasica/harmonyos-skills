---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/ide-changelogs-504-release
title: 变更说明
breadcrumb: 版本说明 > 更多版本 > 历史版本 > 5.0.4(16) > DevEco Studio > 变更说明
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:23+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:df3b3ac05b4092ec83c924b8b5faeefcae17772a9855ababc9eeb550c6fe6bdf
---

## DevEco Studio连接设备时更改设备日志输出等级为INFO

升级到DevEco Studio 5.0.4 Release（5.0.11.100）及以上版本，通过DevEco Studio连接设备时，设备日志输出等级为INFO。

**变更影响**

如果设备日志输出等级不是INFO，在连接DevEco Studio后会被更改为INFO，设备会输出INFO及以上级别的日志。断开DevEco Studio后，设备日志输出等级仍为INFO。

重启设备后，设备的日志等级请参考[hilog查看和设置日志级别](../harmonyos-guides/hilog.md#查看和设置日志级别)。

**适配指导**

连接DevEco Studio时，可通过以下命令自定义设备日志输出等级。

```screen
hdc shell hilog -b <loglevel>
```
