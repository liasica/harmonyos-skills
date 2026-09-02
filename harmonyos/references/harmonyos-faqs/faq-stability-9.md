---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-9
title: 媒体服务线程泄漏导致应用闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 媒体服务线程泄漏导致应用闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f0f5f9682668d907cc1af5d5ba03b93afdd32f51a40602cd3c3cff54c943fc70
---

## 问题现象

media\_service线程泄漏，导致应用闪退。

## 背景知识

* 线程泄漏：60s一次遍历进程，获取进程的总线程数，超过阈值（700个）时抓取详细线程名信息，同步上报泄漏。
* [AVPlayer](../harmonyos-guides/media-kit-intro.md#avplayer)主要工作是将Audio/Video媒体资源（比如mp4/mp3/mkv/mpeg-ts等）转码为可供渲染的图像和可听见的音频模拟信号，并通过输出设备进行播放。播放的全流程包含：创建AVPlayer，设置播放资源，设置播放参数（音量/倍速/焦点模式），播放控制（播放/暂停/跳转/停止），重置，销毁资源。

## 问题定位

1. 在hilog日志中搜索关键字"PlayerServer"，查看应用是否同时存在多个AVPlayer实例。

   ```screen
   04-01 19:36:29.316  1423  3302 I C02B22/media_service/MediaUtils: [a92abccfbd4ca04 115721d 0](GetClientBundleName(), 99): bundle name is 应用包名 uid is 20020226
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: [a92abccfbd4ca04 115721d 0]{WriteInfo():81} ------------------PlayerServer------------------
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: -----Instance #0: pid = 3439 uid = 20020017-----
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: -----Instance #1: pid = 7524 uid = 20020196-----
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: -----Instance #2: pid = 53380 uid = 20020226-----
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: -----Instance #3: pid = 53380 uid = 20020226-----
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: -----Instance #4: pid = 53380 uid = 20020226-----
   ```
2. 从当前日志可以看出，当前应用存在68个AVPlayer实例，排查应用是否创建AVPlayer后没有调用release释放AVPlayer实例。

   ```screen
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: -----Instance #64: pid = 53380 uid = 20020226-----
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: -----Instance #65: pid = 53380 uid = 20020226-----
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: -----Instance #66: pid = 53380 uid = 20020226-----
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: -----Instance #67: pid = 53380 uid = 20020226-----
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: -----Instance #68: pid = 53380 uid = 20020226-----
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: -----Insta
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: [a92abccfbd4ca04 115721d 0]{WriteInfo():81} ------------------RecorderServer------------------
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: [a92abccfbd4ca04 115721d 0]{WriteInfo():81} ------------------CodecServer------------------
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: [a92abccfbd4ca04 115721d 0]{WriteInfo():81} ------------------AVMetaServer------------------
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: [a92abccfbd4ca04 115721d 0]{WriteInfo():81} ------------------TranscoderServer------------------
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: [a92abccfbd4ca04 115721d 0]{WriteInfo():81} ------------------ScreenCaptureServer------------------
   ```
3. 根据应用打印的日志信息，搜索关键字"AVPlayer state"，从日志中可以看出，应用没有调用release释放AVPlayer实例。

   ```screen
   04-01 19:36:37.171 53380 53380 I A03D00/com.hx.example/JSAPP: [a92abecfc5273c4 0 0]AVPlayer state initialized called.
   04-01 19:36:37.193 53380 53380 I A03D00/com.hx.example/JSAPP: AVPlayer state prepared called.
   04-01 19:36:37.256 53380 53380 I A03D00/com.hx.example/JSAPP: AVPlayer state playing called.
   04-01 19:36:38.152 53380 53380 I A03D00/com.hx.example/JSAPP: AVPlayer state initialized called.
   04-01 19:36:38.172 53380 53380 I A03D00/com.hx.example/JSAPP: AVPlayer state prepared called.
   04-01 19:36:38.193 53380 53380 I A03D00/com.hx.example/JSAPP: AVPlayer state playing called.
   04-01 19:36:38.297 53380 53380 I A03D00/com.hx.example/JSAPP: AVPlayer state stopped called.
   04-01 19:36:38.303 53380 53380 I A03D00/com.hx.example/JSAPP: AVPlayer state idle called.
   04-01 19:36:39.337 53380 53380 I A03D00/com.hx.example/JSAPP: AVPlayer state initialized called.
   04-01 19:36:39.350 53380 53380 I A03D00/com.hx.example/JSAPP: AVPlayer state prepared called.
   04-01 19:36:39.368 53380 53380 I A03D00/com.hx.example/JSAPP: AVPlayer state playing called.
   04-01 19:36:39.435 53380 53380 I A03D00/com.hx.example/JSAPP: AVPlayer state stopped called.
   04-01 19:36:39.441 53380 53380 I A03D00/com.hx.example/JSAPP: AVPlayer state idle called.
   04-01 19:36:40.524 53380 53380 I A03D00/com.hx.example/JSAPP: AVPlayer state stopped called.
   04-01 19:36:40.528 53380 53380 I A03D00/com.hx.example/JSAPP: AVPlayer state idle called.
   ```

## 分析结论

应用创建AVPlayer实例未释放，导致线程泄漏。

## 修改建议

当客户端暂时不使用播放器时，调用release回收内存资源，做好资源利用，代码参考[release](../harmonyos-references/arkts-apis-media-avplayer.md#release9-1)接口文档中的示例。
