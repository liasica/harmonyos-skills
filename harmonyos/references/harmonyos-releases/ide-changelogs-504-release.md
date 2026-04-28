---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/ide-changelogs-504-release
title: 变更说明
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.4(16) > DevEco Studio > 变更说明
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:29+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:c5b9ae1863efc96622765c7c108eaddd143c0ba1e3e94cfcbe2ad8a48afdb51e
---

## DevEco Studio连接设备时更改设备日志输出等级为INFO

升级到DevEco Studio 5.0.4 Release（5.0.11.100）及以上版本，通过DevEco Studio连接设备时，设备日志输出等级为INFO。

**变更影响**

如果设备日志输出等级不是INFO，在连接DevEco Studio后会被更改为INFO，设备会输出INFO及以上级别的日志。断开DevEco Studio后，设备日志输出等级仍为INFO。

重启设备后，设备的日志等级请参考[hilog查看和设置日志级别](../harmonyos-guides/hilog.md#查看和设置日志级别)。

**适配指导**

连接DevEco Studio时，可通过以下命令自定义设备日志输出等级。

```
1. hdc shell hilog -b <loglevel>
```
