---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/stability-kit-troubleshooting-0005
title: AVPlayer内存泄漏导致应用闪退问题定位
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 故障排查 > AVPlayer内存泄漏导致应用闪退问题定位
category: harmonyos-faqs
scraped_at: 2026-10-15T07:13:29+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:91ddc8426e72a3ab06c3bbf2c7e99a343e585af36f6c8fb66288b288b28ba9c7
---

## 问题现象

media\_service线程泄漏，导致应用闪退。

## 定位过程

1. 在hilog日志中搜索关键字"PlayerServer"，查看应用是否同时存在多个AVPlayer实例。

   ```txt
   04-01 19:36:29.316  1423  3302 I C02B22/media_service/MediaUtils: [a92abccfbd4ca04 115721d 0](GetClientBundleName(), 99): bundle name is 应用包名 uid is 20020226
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: [a92abccfbd4ca04 115721d 0]{WriteInfo():81} ------------------PlayerServer------------------
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: -----Instance #0: pid = 3439 uid = 20020017-----
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: -----Instance #1: pid = 7524 uid = 20020196-----
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: -----Instance #2: pid = 53380 uid = 20020226-----
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: -----Instance #3: pid = 53380 uid = 20020226-----
   04-01 19:36:29.317  1423  3302 I P02B2B/media_service/MediaServerManager: -----Instance #4: pid = 53380 uid = 20020226-----
   ```
2. 从当前日志可以看出，当前应用存在68个AVPlayer实例，排查应用是否创建AVPlayer后没有调用release释放AVPlayer实例。

   ```txt
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

   ```txt
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
