---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avscreencapture-faqs
title: 录屏常见问题
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(C/C++) > 录制 > 使用AVScreenCapture录屏取码流(C/C++) > 录屏常见问题
category: harmonyos-guides
scraped_at: 2026-10-31T07:32:46+08:00
doc_updated_at: 2026-10-30
content_hash: sha256:8fcad0481bef283a9b6479682b47832ee9c1afd08239d5c7557c89ac24365cfa
---

## 录屏启动报错AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT

### 问题现象

录屏设置参数或启动失败。

### 可能原因

1. 实例数量超出当前规格限制，即每种数据格式最多两个实例。
2. 未设置通话中保持录屏策略，无法启动录屏。
3. 录屏超过规格限制时，无法启动录屏。

### 解决措施

1. 在录屏过程中因为状态改变导致的录屏停止，需要在[OH\_AVScreenCapture\_SetStateCallback()](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_setstatecallback)（状态回调）中，对录屏资源进行异步释放。

   录屏会话限制策略：

   * 客户端应用数量上限4个，比如会议屏幕共享、会议投屏、后台听歌识曲、系统录屏同时存在。
   * 单应用单模式（存为文件或存为码流）可创建实例上限2个。 典型场景：在线上会议共享屏幕时，需要同步录制会议内容。
2. 从API版本20开始，如需在通话中保持录屏，可使用[OH\_AVScreenCapture\_StrategyForKeepCaptureDuringCall()](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_strategyforkeepcaptureduringcall)设置“蜂窝通话时保持录屏”策略。
3. 录屏写文件模式启动时会对视频编码参数进行规格校验。视频码率（videoBitrate）的取值范围为[1, 30000000]，单位为比特每秒（bit/s），如果超出此限制将导致启动失败，请重新检查并调整录屏配置参数。
