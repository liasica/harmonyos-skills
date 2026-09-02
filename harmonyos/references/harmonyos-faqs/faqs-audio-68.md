---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-68
title: OHAudio播放音频出现卡顿问题
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > OHAudio播放音频出现卡顿问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:460826d6c7983ee2d7c113dc66f625032b0478eb19555e023b7019c6ebaa2324
---

## 问题现象

OHAudio播放音频出现卡顿，如何定位？

## 背景知识

* [OHAudio](../harmonyos-guides/using-ohaudio-for-playback.md)是系统在API version 10中引入的一套C API，此API在设计上实现归一，同时支持普通音频通路和低时延通路。仅支持PCM格式，适用于依赖Native层实现音频输出功能的场景。
* [HiProfiler](../harmonyos-guides/hiprofiler.md)调优组件旨在为开发者提供一系列调优能力，可以用来帮助分析内存、性能等问题。

## 问题定位

此类问题可通过抓取trace数据，分析问题出现时音频数据回调是否正常。

1. 抓取trace数据。
   * 先执行hdc shell进入命令行。
   * 粘贴如下Bash脚本执行，并同时复现问题，开始抓30秒trace数据。也可以参考[命令行说明](../harmonyos-guides/hiprofiler.md#命令行说明)，或使用[DevEco Studio](../harmonyos-guides/ide-software-install.md)和[Smartperf](https://gitcode.com/openharmony/developtools_smartperf_host/releases)网页抓取。
   * 执行命令将trace文件保存到本地hdc file recv /data/local/tmp/hiprofiler\_data.htrace ./hiprofiler\_data.htrace。

   ```bash
   hiprofiler_cmd \
     -c - \
     -o /data/local/tmp/hiprofiler_data.htrace \
     -t 30 \
     -s \
     -k \
   <<CONFIG
    request_id: 1
    session_config {
     buffers {
      pages: 16384
     }
    }
    plugin_configs {
     plugin_name: "ftrace-plugin"
     sample_interval: 1000
     config_data {
      ftrace_events: "sched/sched_switch"
      ftrace_events: "power/suspend_resume"
      ftrace_events: "sched/sched_wakeup"
      ftrace_events: "sched/sched_wakeup_new"
      ftrace_events: "sched/sched_waking"
      ftrace_events: "sched/sched_process_exit"
      ftrace_events: "sched/sched_process_free"
      ftrace_events: "task/task_newtask"
      ftrace_events: "task/task_rename"
      ftrace_events: "power/cpu_frequency"
      ftrace_events: "power/cpu_idle"
      hitrace_categories: "ability"
      hitrace_categories: "ace"
      hitrace_categories: "app"
      hitrace_categories: "ark"
      hitrace_categories: "binder"
      hitrace_categories: "disk"
      hitrace_categories: "freq"
      hitrace_categories: "graphic"
      hitrace_categories: "idle"
      hitrace_categories: "irq"
      hitrace_categories: "memreclaim"
      hitrace_categories: "mmc"
      hitrace_categories: "multimodalinput"
      hitrace_categories: "notification"
      hitrace_categories: "ohos"
      hitrace_categories: "pagecache"
      hitrace_categories: "rpc"
      hitrace_categories: "sched"
      hitrace_categories: "sync"
      hitrace_categories: "window"
      hitrace_categories: "workq"
      hitrace_categories: "zaudio"
      hitrace_categories: "zcamera"
      hitrace_categories: "zimage"
      hitrace_categories: "zmedia"
      buffer_size_kb: 204800
      flush_interval_ms: 1000
      flush_threshold_kb: 4096
      parse_ksyms: true
      clock: "boot"
      trace_period_ms: 200
      debug_on: false
     }
    }
   CONFIG
   ```
2. 使用[DevEco Profiler调优工具](../harmonyos-guides/ide-profiler.md)或[Smartperf](https://gitcode.com/openharmony/developtools_smartperf_host/releases)网页中打开trace文件分析。
   * 查看应用进程下的音频输出回调线程OS\_AudioWriteCB，其中RendererInClientInner::OnWriteData是应用送数据给系统的回调处理函数，trace中发现此回调函数处理耗时都小于1ms，没有明显堵塞问题，运行正常。
   * 查看RendererInClientInClient线程，会打印应用送给系统的数据大小，发现有几次为0的数据，这不是正常现象。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/1WIAqJmeTtaKgPHaQvoWug/zh-cn_image_0000002664157965.png "点击放大")

## 分析结论

应用送给系统的音频数据中，有为0的静音数据，播放后会有卡顿现象。

## 修改建议

应用侧需要排查[OH\_AudioRenderer\_OnWriteDataCallback](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiorenderer_onwritedatacallback)回调函数中写入静音数据的问题。在无法填满回调所需长度数据的情况下，建议返回AUDIO\_DATA\_CALLBACK\_RESULT\_INVALID，系统不会处理该段音频数据。
