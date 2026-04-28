---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-delivery-report
title: （可选）推送报告
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 端云调试 > （可选）推送报告
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:551402ad6c381f75a185ed6d590a6d4f6943dd39d8e2beb73f0c08e505469637
---

登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，点击“开发与服务”，在项目列表中找到您的项目，通过“增长 > 推送服务 > 推送报告”，您可以在“推送报告”中查看推送消息详情和推送用户详情。

说明

推送报告数据不是实时数据，当天生成的数据在控制台次日才能查看到。

## 推送消息详情

您可以查看推送消息的详情，场景化消息的统计图和对应表格，同时可以按照通道维度进行查看，有“通过AGC控制台”、“通过API方式”和“全部通道”；也可以按照消息类型维度进行查看。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/L2bJ9JNMSbSBP_1bWY5Rvw/zh-cn_image_0000002583439183.png?HW-CC-KV=V1&HW-CC-Date=20260427T235032Z&HW-CC-Expire=86400&HW-CC-Sign=651EAB42BA389C7158F8375911D72508CB4E9530D363165AD38FDD49274B50D9)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/GhkWXgo6Rj-tUZP_-RIzlQ/zh-cn_image_0000002552959138.png?HW-CC-KV=V1&HW-CC-Date=20260427T235032Z&HW-CC-Expire=86400&HW-CC-Sign=0EA3EF549EC761AF3F6E35418FA268B8CE8E10F40AA4F0C0EFB1E716B0515388)

点击自定义后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/Gi0zl-jeSxekoagDD_pikA/zh-cn_image_0000002583479139.png?HW-CC-KV=V1&HW-CC-Date=20260427T235032Z&HW-CC-Expire=86400&HW-CC-Sign=FDB860A0824E81135BECDA2306DB28F2F09782FE61853E3C1C9315318382F92E)，可自定义推送消息报表展示的表格列，默认展示的表格列有：日期、消息类型、请求量、发送量、到达量、显示量、点击量、到达率（%）、点击率（%）、沉默设备丢弃、应用被卸载、无效TOKEN、通知关闭。全选可展示全部表格列，重置则恢复默认表格列。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/TTihD-SqTE-5EovmOPbgJA/zh-cn_image_0000002552799490.png?HW-CC-KV=V1&HW-CC-Date=20260427T235032Z&HW-CC-Expire=86400&HW-CC-Sign=13C160FCA732A4B9518039A2C5564D41E737A180AC1EB61F9D6B5ECE00F22297)

报表数据条目说明：

* 请求量：该推送任务预计覆盖的设备数量。
* 发送量：在请求量的基础上剔除不符合下发条件的消息数量，实际下发的消息数量。
* 到达量：扣除未触达量后实际到达的数量。
* 显示量：消息展示在通知栏的数量。
* 点击量：用户点击推送消息的数量。
* 到达率（%）：到达量/发送量。
* 点击率（%）：点击量/显示量。
* 沉默设备丢弃：终端设备超过30天没有联网的数量。
* 频控丢弃量：向单个设备发送消息超出上限，超出部分被丢弃的数量。
* 应用被卸载：用户已经卸载该应用并且没有重新安装的数量。
* 无效TOKEN：消息从云端发送到终端设备过程中，由于Token无效不展示的数量。
* 通知关闭：用户关闭了应用的消息通知权限的数量。
* 消息覆盖：待发送消息被覆盖的数量。针对待发送消息，只保留最新一条，其余待发送消息会被覆盖不下发。
* 其他原因：其他不满足触达条件的情况，如推送链接无法正常访问等。
* 过期量：目标设备离线，在消息有效期内设备未上线导致消息过期的数量。
* 缓存量：目标设备离线，消息仍在有效期内的数量。
* 未触达量：消息未到达终端设备的数量。

说明

不符合下发条件的消息数量包括：沉默设备丢弃、频控丢弃量、应用被卸载、无效TOKEN、通知关闭、消息覆盖、其他原因、过期量、缓存量。

## 推送用户详情

您可以查看推送用户的详情，根据时间维度查看活跃用户、新增用户和总用户的统计数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/ua3030NsRfqZXsE75CCaow/zh-cn_image_0000002583439185.png?HW-CC-KV=V1&HW-CC-Date=20260427T235032Z&HW-CC-Expire=86400&HW-CC-Sign=4BF9ED9A1E2B1B4FA27817C48A4C0CF8F3B853BDE7A69CDFABFECCED5588684C)

报表数据条目说明：

* 当天活跃用户数：当天设备与Push服务端建立连接的用户数量。
* 当天新增用户数：当天新安装的用户数量。不统计重复卸载安装应用场景。
* 30日活跃用户数：查询日往前30日内设备与Push服务端建立连接的用户数量。
* 总用户数：已安装的总用户数量。
