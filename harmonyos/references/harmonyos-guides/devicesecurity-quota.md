---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-quota
title: 服务配额
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 服务配额
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2a078be3ee16a2e72cb48e3940a6cdd098dc17d492a67fd62060deb7ac12898a
---

| 功能 | 配额说明 |
| --- | --- |
| 应用设备状态检测（DeviceVerify） | API限额：默认情况下，每个应用每天最多可以调用10万次的DeviceVerify Rest接口请求。  如果应用需要修改服务配额，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请修改配额。  - 问题分类：选择HarmonyOS NEXT/系统/Device Security Kit。  - 问题描述：填写申请原因、申请应用、配额大小以及使用场景。  我们会在5个工作日内回复申请结果，请留意电话和邮箱消息。 |
| 安全检测（SafetyDetect） | - 系统完整性检测API：每个应用在每个设备上每天最多可以调用1万次、每分钟最多调用5次。  - URL检测API：每个应用在每个设备上每天最多可以调用1万次。  - 系统完整性增强检测API：每个应用在每个设备上每天最多可以调用1万次、每分钟最多调用5次。 |
| 业务风险检测（BusinessRiskIntelligentDetection） | - 涉诈剧本检测API：每个应用在每个设备上每天最多可以调用10次。  - 模拟点击检测API：每30秒最多可以调用10次，每个应用在每个设备上每天最多可以调用20次。  - 模拟点击增强检测API：每30秒最多可以调用10次，每个应用在每个设备上每天最多可以调用20次。 |
| 安全审计（SecurityAudit） | - 订阅通知类事件场景：每个应用在每个设备上最多创建2个通知类事件客户端，单个设备上最多创建16个通知类事件客户端。  - 订阅阻断类事件场景：每个应用在每个设备上最多创建2个阻断类事件客户端，单个设备上最多创建16个阻断类事件客户端。 |
