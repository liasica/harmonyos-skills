---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audiovivid-intro
title: Audio Vivid能力介绍
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > Audio Vivid能力 > Audio Vivid能力介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:dff51ac76d84d3dcba3a4cc1eeba6066cd6a0dc101aa77f360523f0d521745f4
---

Audio Vivid（菁彩三维声）是全球首个基于AI技术的音频编解码标准，由世界超高清视频产业联盟（UWA联盟）与数字音视频编解码技术标准工作组（AVS）联合制定，共同发布。包含音频PCM数据以及元数据的音频格式，相比传统立体声音源，Audio Vivid包含音频内容源的元数据信息，能够还原物理和感知世界中的真实听感，打造极致的沉浸式听觉体验。

HarmonyOS打造全链路高清空间音频系统，包含Audio Vivid编解码、空间音频渲染算法等关键能力，并在各类终端产品逐步构建全场景空间音频特性，从传统立体声升级到三维声，获得更好的音质、更沉浸的空间感。

HarmonyOS支持播放Audio Vivid格式音源，并在耳机实现双耳空间音频渲染重放，在手机、平板、PC等支持外放空间音频渲染重放。系统的空间音频渲染能力无感接入，不需要做特定适配。

搭配HarmonyOS高清空间音频渲染能力，将音乐中的人声和各种乐器声作为独立的声音对象，重新定义各种声音对象的位置、移动轨迹和声音大小、远近等要素，实现声音在听众四周及上方全面萦绕，实现更佳的空间音频沉浸式体验，获得影院、音乐厅等的临场感与艺术体验。佩戴支持头动跟踪的耳机收听空间音频，还能实现动态头动跟踪，让声音围绕听众重新定位，还原逼真的临场感。

以下主要介绍使用HarmonyOS进行Audio Vivid格式音源的端到端播放的流程。

Audio Vivid端到端播放包括调用系统编解码能力进行[解封装](audiovivid-avdemuxer.md)、[解码](audiovivid-audiodecoder.md)，以及调用系统播放能力进行[渲染播放](audiovivid-audiorenderer.md)两个部分。
