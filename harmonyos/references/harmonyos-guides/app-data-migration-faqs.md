---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-data-migration-faqs
title: 常见问题与异常处理
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 常见问题与异常处理
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:55+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:f16a4dc889d3f163773e650241109a4c8e123b7c6d40665328a2e05021e9e7fa
---

## 应用数据迁移暂停

**问题现象1**

在数据加载界面，应用数据迁移暂停。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/wCAioYWnTZuxjaNDlZ0uWQ/zh-cn_image_0000002791725536.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD7FA808CD61983D60F24F55DD3DF4C3BFA72D63759A0E9C741A76663911DC64)

**可能原因**

应用数据迁移的过程中需要使用到网络，当前终端设备网络不可用，导致数据迁移暂停。

**解决方法**

单击“稍后连接WLAN加载”按钮，进入桌面后连接网络，终端设备网络可用后，恢复应用数据迁移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/cg0XDDFkS7qoyg7UrhNBGQ/zh-cn_image_0000002791565564.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7C1628932D7570386C99D3E49251113C21ED963960EE7063B10A2393130080A)

**问题现象2**

进入桌面之后，若应用数据迁移还未结束，可通过通知栏进入应用加载界面查看加载进度

在应用加载界面，应用数据迁移暂停。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/zvJk-utKR2GtiU5Wv0mORw/zh-cn_image_0000002820525517.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B3BF8EAC44CD2A61A62FADAE4B16697FBBCB7614A8AC2282E679B4B6E5ECB7C)

**可能原因**

应用数据迁移的过程中需要使用到网络，当前终端设备网络不可用，导致数据迁移暂停。

**解决方法**

单击“稍后连接WLAN加载”按钮，进入桌面后连接网络，终端设备网络可用后，恢复应用数据迁移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/pvBeKuKSRbSKzkPs2YMNsA/zh-cn_image_0000002820405517.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4A693B2558B88524BEBA1D9911E90FCF9174C2BCB8D12C54B133E05EAC5C7DD)

## 应用数据迁移执行十五分钟后失败

**问题现象**

应用数据迁移执行十五分钟后显示失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/2RYK9W8lTXWJA3wC6Dy20g/zh-cn_image_0000002820525515.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A9D1051A5D2158663CC10812627F43CA8313CF1685818D8F324041A9F3F177D)

**可能原因**

单个应用数据迁移执行超过十五分钟，超过设定的单个应用最长数据迁移时间，任务执行失败。

**解决方法**

请优化应用BackupExtensionAbility的代码实现，在十五分钟内完成应用数据迁移。

**说明** 

已接入“数据迁移框架”的应用完成数据迁移后，才可以被消费者使用。尽可能快的完成应用数据迁移，可以带给消费者更好的体验。

## 启动迁移按钮无法点击

**问题现象**

在迁移调试界面，输入应用包名后启动迁移按钮无法点亮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/PuhgNy6nSKGcMs1IQw0VdQ/zh-cn_image_0000002791725538.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB44E14647F568760F89A6241BFE7F2F481F37EA816149D7A8E7E829CE764D71)

**可能原因**

迁移调试工具版本过低（版本号低于6.0.0.190）。

**解决方法**

请参考[开发者自验证](adaptation-process.md#开发者自验证)下“迁移调试”工具获取方式，申请最新版迁移调试工具。
