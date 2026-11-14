---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-data-migration-faqs
title: 常见问题与异常处理
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 常见问题与异常处理
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:17+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:ccf7daebc3476cbd12243175389e831358534c809de2e46c8ac3b4012caef4dd
---

## 应用数据迁移暂停

**问题现象1**

在数据加载界面，应用数据迁移暂停。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/u0jjR_aJTG6Ff3_77RprwA/zh-cn_image_0000002817426599.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=358999C8C646B0F2F0B0C4024B09565DB438A6C2835D1062E72E93C8654431F9)

**可能原因**

应用数据迁移的过程中需要使用到网络，当前终端设备网络不可用，导致数据迁移暂停。

**解决方法**

单击“稍后连接WLAN加载”按钮，进入桌面后连接网络，终端设备网络可用后，恢复应用数据迁移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/B_RUr-xsRCehvxjD-9AtXw/zh-cn_image_0000002788467180.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC139A63A14B3DBC67520CAB8CCBA243A274C6ED78549E8F043B469D2ADC337F)

**问题现象2**

进入桌面之后，若应用数据迁移还未结束，可通过通知栏进入应用加载界面查看加载进度

在应用加载界面，应用数据迁移暂停。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/tcG3-OeLRsekg3On8I8JdQ/zh-cn_image_0000002817506669.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=866399BF02693F043766B254E77845A6EEAD48AEC4CA09C48AD5628551080273)

**可能原因**

应用数据迁移的过程中需要使用到网络，当前终端设备网络不可用，导致数据迁移暂停。

**解决方法**

单击“稍后连接WLAN加载”按钮，进入桌面后连接网络，终端设备网络可用后，恢复应用数据迁移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/hqjhlYNBRWeeEHNga868PA/zh-cn_image_0000002788307238.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6A564085A5AAA722E9EE2157A544450EDA0005B36C324A9C4B9D37C5D83DC1F)

## 应用数据迁移执行十五分钟后失败

**问题现象**

应用数据迁移执行十五分钟后显示失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/GM_yCQSER-6ZUC-SdhFFZA/zh-cn_image_0000002817506667.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=85D02B7651597F456E19D97A304BB9F35E29F0C623B8ADC3399EE6AC70953AF1)

**可能原因**

单个应用数据迁移执行超过十五分钟，超过设定的单个应用最长数据迁移时间，任务执行失败。

**解决方法**

请优化应用BackupExtensionAbility的代码实现，在十五分钟内完成应用数据迁移。

**说明** 

已接入“数据迁移框架”的应用完成数据迁移后，才可以被消费者使用。尽可能快的完成应用数据迁移，可以带给消费者更好的体验。

## 启动迁移按钮无法点击

**问题现象**

在迁移调试界面，输入应用包名后启动迁移按钮无法点亮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/015gN_C_RHWnPv1vRLuUXg/zh-cn_image_0000002817426601.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=D77E481CD1A5C16FCBA62D3F6D664E50BC515A15E978C07C241AB6876118A2E7)

**可能原因**

迁移调试工具版本过低（版本号低于6.0.0.190）。

**解决方法**

请参考[开发者自验证](adaptation-process.md#开发者自验证)下“迁移调试”工具获取方式，申请最新版迁移调试工具。
