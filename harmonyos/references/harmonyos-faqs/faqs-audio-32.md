---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-32
title: 安全键盘输入法中断音乐播放如何解决
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 安全键盘输入法中断音乐播放如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:9e1bbcd4fd7599ca75131a2b209709964cd7d4f9ef91e82de2d4ffcbfd0a1ed0
---

## 问题现象

在一些银行等金融类软件中，一般会使用安全键盘输入法进行输入账号密码等隐私信息，但会出现在输入信息时会中断音乐播放的问题。

使用安全输入法输入前，音乐正常播放；使用安全输入法输入时，音乐播放暂停。

## 背景知识

[IME Kit](../harmonyos-guides/ime-kit-intro.md)：负责建立编辑框所在应用与输入法应用之间的通信通道，确保两者可以共同协作提供文本输入功能，也为系统应用提供管理输入法应用的能力。

## 问题定位

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/z0Jj_MZ7Roer2PVU_LdJmw/zh-cn_image_0000002639837502.png "点击放大")

打开被中断的音乐播放器，可以看到提示“允许同时播放提示”，音频焦点被抢占。安全键盘启用时（如银行/支付场景），系统会强制获取音频焦点，导致音乐被暂停。

通过问题复现步骤，发现该问题只在某些特定应用中内置安全键盘出现该问题，目前可以发现设置了“允许和其他应用同时播放”就不会打断音乐播放，效果正常。

## 分析结论

音乐播放器的音频焦点被安全输入法的输入时音频抢占。

## 修改建议

对于输入法音效打断音乐播放的情形，建议应用使用音频会话管理（[AudioSessionManager](../harmonyos-guides/audio-session-management.md)）提供的接口，通过AudioSession主动管理应用内音频流的焦点，对输入法音效采用音频并发策略。

补充说明，若需在输入法中使用语音转文字功能并屏蔽媒体声音，可设置CONCURRENCY\_PAUSE\_OTHERS并发模式来暂停其他音频。使用完毕后需要停用AudioSession。
