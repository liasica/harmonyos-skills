---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-23
title: 播放新的音频时不会打断正在播放的音频
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 播放新的音频时不会打断正在播放的音频
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:21+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:cdbc8af333be366207d3d170a60067162b1a2315afece28f78b9e4e725520801
---

## 问题现象

播放音频A然后播放音频B，此时音频A和音频B可以同时播放。

## 背景知识

* 音频流：音频流是指音频系统中一个具备音频格式和音频使用场景信息的独立音频数据处理单元。可以表示播放，也可以表示录制，并且具备独立音量调节和音频设备路由切换能力。对于播放流，其类型由StreamUsage决定；对于录制流，其类型由SourceType决定。
  + 音频流类型在音量控制、音频焦点管理、输入/输出设备选择等方面有决定性影响。
  + 应用需要根据自身的业务场景和实际需求，[为音频选择合适的流类型](../harmonyos-guides/using-right-sourcetype-for-recording.md)。
* 音频焦点策略：当音频流申请或释放音频焦点时，系统依据音频焦点策略，对所有音频流（包括播放和录制）实施焦点管理，决定哪些音频流可正常运行，哪些需被打断或执行其他操作。
  + 系统预设的默认音频焦点策略，主要依据音频流类型（即播放流的[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)和录制流的[SourceType](../harmonyos-references/arkts-apis-audio-e.md#sourcetype8)）及音频流启动的顺序进行决策。
  + 若默认的音频焦点策略无法满足特定场景的需求，应用程序可利用[音频会话（AudioSession）](../harmonyos-guides/audio-playback-concurrency.md#音频焦点策略)，调整本应用音频流所采用的音频焦点策略。

## 问题定位

### 场景一

查看应用使用的[音频流类型](../harmonyos-guides/using-right-streamusage-for-playback.md)是否是可以同时播放的音频流，参考[音频焦点调整](../harmonyos-guides/using-right-sourcetype-for-recording.md#音频焦点调整)中常见的音频流类型影响音频焦点的表现，导航（Navigation）和音乐（Music）、音乐（Music）和游戏音频（Game）都不会打断正在播放的音频。

### 场景二

查看应用是否是自定义的音频焦点策略，有没有对音频并发模式做处理。

## 分析结论

### 场景一

使用了错误的音频流。例如导航类音频流可以和其他音频流同时播放，就会导致音频无法打断的现象。

### 场景二

使用自定义的音频焦点策略时，未对此情况做特殊处理。

## 修改建议

### 场景一

根据业务场景使用合适的音频流。

### 场景二

在自定义音频焦点策略中对音频并发时做特殊处理，具体可参考：[处理音频焦点示例](../harmonyos-guides/audio-playback-concurrency.md#典型场景)。
