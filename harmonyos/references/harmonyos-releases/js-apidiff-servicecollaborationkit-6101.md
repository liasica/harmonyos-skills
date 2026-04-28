---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-servicecollaborationkit-6101
title: Service Collaboration Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Service Collaboration Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b5006cc5306d639fcc5b17af14b6aa68e2c0614ee2eea9b4e5ffedb463e0e79c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：@Builder  declare function createCollaborationServiceMenuItems(businessFilter: Array<CollaborationServiceFilter>, canReceiveMaxCount: number, deviceTypeFilter: Array<CollaborationDeviceFilterType>): void;  差异内容：@Builder  declare function createCollaborationServiceMenuItems(businessFilter: Array<CollaborationServiceFilter>, canReceiveMaxCount: number, deviceTypeFilter: Array<CollaborationDeviceFilterType>): void; | api/@hms.collaboration.service.d.ets |
| 新增API | NA | 类名：global；  API声明：declare enum CollaborationDeviceFilterType  差异内容：declare enum CollaborationDeviceFilterType | api/@hms.collaboration.service.d.ets |
| 新增API | NA | 类名：CollaborationDeviceFilterType；  API声明：PHONE = 1  差异内容：PHONE = 1 | api/@hms.collaboration.service.d.ets |
| 新增API | NA | 类名：CollaborationDeviceFilterType；  API声明：TABLET = 2  差异内容：TABLET = 2 | api/@hms.collaboration.service.d.ets |
| 新增API | NA | 类名：CollaborationDeviceFilterType；  API声明：PC\_2IN1 = 3  差异内容：PC\_2IN1 = 3 | api/@hms.collaboration.service.d.ets |
