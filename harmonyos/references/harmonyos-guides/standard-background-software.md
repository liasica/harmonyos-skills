---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/standard-background-software
title: 后台软件资源使用
breadcrumb: 指南 > 应用体验建议 > 应用功耗体验建议 > 后台场景 > 后台软件资源使用
category: harmonyos-guides
scraped_at: 2026-09-30T07:35:45+08:00
doc_updated_at: 2026-09-29
content_hash: sha256:7a4a27ec18c4a506b211c55f501ea0a7d30815bcb1240dceffef1789349fb332
---

## 后台上传下载合理使用

|  |  |
| --- | --- |
| 描述 | 应用需要上传下载时，应使用系统上传下载服务，不要申请长时任务。 |
| 类型 | 规则 |
| 适用设备 | 手机、平板 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [后台上传下载合理使用](../best-practices/bpta-reasonable-request-use.md) |

## 后台音频播放合理使用

|  |  |
| --- | --- |
| 描述 | 申请音频播放长时任务的应用退到后台后，请勿存在“不写入音频数据”或者“写入静音数据”等恶意行为。 |
| 类型 | 规则 |
| 适用设备 | 手机、平板、智能穿戴、轻量级智能穿戴 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [后台音频播放合理使用](../best-practices/bpta-reasonable-audio-playback-use.md) |

## 后台定位导航服务合理使用

|  |  |
| --- | --- |
| 描述 | 申请定位长时任务的应用在导航时应设置正确的应用场景。 |
| 类型 | 规则 |
| 适用设备 | 手机、平板、智能穿戴、轻量级智能穿戴 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [后台定位导航服务合理使用](../best-practices/bpta-reasonable-position-navigation-use.md) |

## 后台系统资源合理使用

|  |  |
| --- | --- |
| 描述 | 无长时任务的应用退后台，应将对应资源释放，不得直接或者间接持阻止系统休眠的锁。 |
| 类型 | 规则 |
| 适用设备 | 手机、平板、智能穿戴、轻量级智能穿戴 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [后台系统资源合理使用](../best-practices/bpta-reasonable-system-use.md) |
