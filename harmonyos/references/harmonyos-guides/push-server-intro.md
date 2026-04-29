---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-server-intro
title: 端云调试概述
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 端云调试 > 端云调试概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:df192121b384754029518db0b59db20cc39a299ecf6f58a954a06d740dcd6080
---

[推送场景化消息](push-scenes-send.md)章节中囊括了Push Kit的所有推送场景，每个推送场景的开发可大致分为两大步骤：

1. 获取Push Token，完成端侧基于推送场景的ArkTS代码开发。
2. 向Push Kit服务侧请求，发送场景化消息。

本章则在其基础上提供了更详细的服务侧（以下简称“云侧”）开发内容，以便您在完成端侧开发后更好地进行端云联调。阅读本章节时，请确保您至少已成功[获取Push Token](push-get-token.md)。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/3J3DfsZRTLyWe70DqSalIA/zh-cn_image_0000002589245437.png?HW-CC-KV=V1&HW-CC-Date=20260429T053956Z&HW-CC-Expire=86400&HW-CC-Sign=9BC5D0811DD4293BD590CE2532A647CD507EEC6775F3079C18400AB8A827A35D)

Push Kit云侧主要业务流程如下：

1. 应用服务端向华为Push Kit云侧[推送场景化消息](push-scenes-send.md)，发送后应用服务端将收到云侧返回的响应消息。
2. Push Kit云侧将应用的场景化消息下发给应用终端，终端（Push Kit端侧）向云侧返回消息响应状态。
3. Push Kit云侧将消息响应状态回执给应用服务端。开发者可以选择[（可选）开发消息回执](push-msg-receipt.md)，以便您的服务端能收到云侧消息下发到端侧后的响应状态。未开通消息回执不会影响消息下发。
