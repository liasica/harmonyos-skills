---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-video-rom
title: 视频场景ROM低功耗建议
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 视频场景ROM低功耗建议
category: best-practices
scraped_at: 2026-04-28T08:22:41+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:0434337d2025d74915260be0726836f502d6f9ea355b6ebd2d4d9a1aad1b0f17
---

## 建议

视频和小视频在线播放时，不建议将片源全部下载到ROM中。下载到ROM的功耗比仅加载到DDR中高100mA以上。因此，应避免将片源全部下载到ROM。

## 开发步骤

推荐使用异步接口fileIo.write()写文件到ROM，函数的返回值number为实际写入的数据长度（单位：字节）。统计返回值的累计值，该累计值表示应用在一段时间内写入ROM的文件总大小。为确保视频和小视频在线播放时，文件下载速率不超过20MB/min。

```
1. let filePath: string = pathDir + "/test.txt";
2. let file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
3. let str: string = "hello, world";
4. // Use asynchronous methods to write files to the ROM
5. fileIo.write(file.fd, str).then((writeLen: number) => {
6. hilog.info(0x0000, 'Sample', 'write data to file succeed and size is:' + writeLen);
7. }).catch((err: BusinessError) => {
8. hilog.error(0x0000, 'Sample', 'write data to file failed with error message: ' + err.message + ', error code: ' + err.code);
9. }).finally(() => {
10. fileIo.closeSync(file);
11. });
```

[VideoScenesROMRule.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/RationalUseOfFrontEndResources/entry/src/main/ets/pages/VideoScenesROMRule.ets#L26-L36)

## 调测验证

通过查看storage\_info节点的信息，如下所示：Total Host Write Data表示整机下载文件的总大小（单位为100MB）。建议文件下载的总速率不超过20MB/min。以视频播放10分钟为例，测试前后的Total Host Write Data节点差值应小于或等于2，符合要求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/RI_cXgyzQrWTip5ZY-PzGw/zh-cn_image_0000002229337325.png?HW-CC-KV=V1&HW-CC-Date=20260428T002240Z&HW-CC-Expire=86400&HW-CC-Sign=759732C55D943711685739DDEDF2FE93A8469F94B9D301D38A4A970FC81EA560 "点击放大")
