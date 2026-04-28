---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-3
title: 运行应用时提示“appid **** is not in white list, to skip”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 预加载 > 运行应用时提示“appid **** is not in white list, to skip”
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e41ab6cfb135f0bb88aac5a2653a8713ae6a94321163b2e80a4ad953733bfbfc
---

**问题现象**

运行应用时提示“appid \*\*\*\* is not in white list, to skip”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/GTI-pudQTb-AaZHjYaFyTw/zh-cn_image_0000002583438927.png?HW-CC-KV=V1&HW-CC-Date=20260427T234850Z&HW-CC-Expire=86400&HW-CC-Sign=63F9B9902FEA1FEDD7B052D705EED71C87E0F25B16E24345F08BA6767136616C)

**解决措施**

出现此错误，是因为手机白名单中未包含当前应用。可按照如下步骤排查和解决：

1. 确认云侧是否已开通云函数和预加载服务。须确保已成功开通。
2. 确认日志中提示的APP ID前缀与云侧创建应用的实际APP ID是否一致。若两者不一致，可能使用了错误的签名方式。请更改为[关联注册应用进行自动签名](ide-signing.md#section20943184413328)或者[手动签名](ide-signing.md#section297715173233)方式。
3. 手机端进入“设置->系统->日期和时间”，关闭“自动设置”开关，将“日期”往后加1天，然后卸载应用重新安装，应用会自动更新白名单。
