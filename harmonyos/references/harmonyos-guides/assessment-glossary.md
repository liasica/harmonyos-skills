---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/assessment-glossary
title: Automatic Scene Configuration Kit术语
breadcrumb: 指南 > 系统 > 基础功能 > Automatic Scene Configuration Kit（场景配置服务） > Automatic Scene Configuration Kit术语
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:47+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:29a061fe574c424cc9c5940a89e44839a9690c9c975fc616b5e0e978d6090270
---

本文介绍Automatic Scene Configuration Kit相关术语。

## A

### allowedApps；应用白名单

评估配置中用于指定评估期间允许运行的应用包名集合。不在白名单内的应用在评估期间无法运行。

### Assessment Mode；评估模式

开始评估后，系统对部分系统能力进行限制的运行状态，用于防止用户作弊或泄露评估内容。评估模式经用户在确认弹窗中确认后进入，通过结束评估或评估被中断退出。

### AssessmentConfig；评估配置

调用begin接口时传入的配置信息，包含评估最大时长duration与应用白名单allowedApps两个字段。

### AssessmentErrorCode；评估错误码

表示评估操作结果与评估中断原因的枚举，成员包括OK、USER\_CANCEL、TIMEOUT、SYSTEM\_ERROR、ENV\_ANOMALY。

### AssessmentInterruptInfo；评估中断信息

评估被中断时通过onInterrupted回调传入的信息，包含中断原因码code与中断原因的详细描述message。

## D

### duration；评估最大时长

评估配置中用于指定本次评估最长持续时间的字段，单位为毫秒，取值存在上限。取值为0时按默认时长处理，默认时长与上限一致。达到评估最大时长后评估被中断，中断原因码为TIMEOUT。

## I

### IAssessmentCallback；评估回调

调用begin接口时注册的回调接口，用于接收评估过程事件，包含评估开始的onBegin、评估中断的onInterrupted与评估结束的onEnd三个方法。
