---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/standard-background-hardware
title: 后台硬件资源使用
breadcrumb: 指南 > 应用体验建议 > 应用功耗体验建议 > 后台场景 > 后台硬件资源使用
category: harmonyos-guides
scraped_at: 2026-04-28T07:58:03+08:00
doc_updated_at: 2026-01-19
content_hash: sha256:549b49cb9be4c91123a27026ffc4a5112ac066ada316bc5089927a9d1ca3bbcf
---

## 后台进程CPU负载约束（长时任务）

|  |  |
| --- | --- |
| 描述 | 应用或元服务后台CPU运行：后台进程持续10分钟CPU使用率不得高于80%。 |
| 类型 | 规则 |
| 适用设备 | 手机、折叠屏、平板 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [长时任务后台进程CPU使用率约束](../best-practices/bpta-controlling-background-process-cpu.md) |

## 后台进程CPU使用率约束（短时任务）

|  |  |
| --- | --- |
| 描述 | 应用或元服务后台CPU运行：后台进程任务期间CPU使用率不得高于80%。 |
| 类型 | 规则 |
| 适用设备 | 手机、折叠屏、平板 |
| 应用形态适用性 | 鸿蒙应用 |
| 说明 | [短时任务后台进程CPU使用率约束](../best-practices/bpta-controlling-background-process-cpu.md) |

## 蓝牙资源合理使用

|  |  |
| --- | --- |
| 描述 | 无长时任务的应用退到后台不允许有蓝牙扫描。 |
| 类型 | 规则 |
| 适用设备 | 手机、折叠屏、平板 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [蓝牙资源合理使用](../best-practices/bpta-reasonable-bluetooth-use.md) |

## 网络资源合理使用

|  |  |
| --- | --- |
| 描述 | 无长时任务的应用退到后台主动断开socket连接，包含TCP和UDP连接。 |
| 类型 | 规则 |
| 适用设备 | 手机、折叠屏、平板 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [网络资源合理使用](../best-practices/bpta-reasonable-network-use.md) |

## 麦克风或者扬声器合理使用

|  |  |
| --- | --- |
| 描述 | 无长时任务的应用退到后台不得使用麦克风或扬声器。 |
| 类型 | 规则 |
| 适用设备 | 手机、折叠屏、平板 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [音频资源合理使用](../best-practices/bpta-reasonable-audio-use.md) |

## GPS资源合理使用

|  |  |
| --- | --- |
| 描述 | 无长时任务的应用退后台不得使用定位服务。 |
| 类型 | 规则 |
| 适用设备 | 手机、折叠屏、平板 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [GPS资源合理使用](../best-practices/bpta-reasonable-gps-use.md) |

## 传感器资源合理使用

|  |  |
| --- | --- |
| 描述 | 应用退后台不得使用传感器，前台使用时根据业务尽量使用once()接口监听结果。 |
| 类型 | 规则 |
| 适用设备 | 手机、折叠屏、平板 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [传感器资源合理使用](../best-practices/bpta-reasonable-sensor-use.md) |
