---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-video-rom
title: 视频场景ROM低功耗建议
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 视频场景ROM低功耗建议
category: best-practices
scraped_at: 2026-10-29T08:03:23+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:9dead32b6b4b9ad2110cc730bb80c50ecdfb90cc74b409c0f51d3bf93046c931
---

## 建议

视频和小视频在线播放时，不建议将片源全部下载到ROM中。下载到ROM的功耗比仅加载到DDR中高100mA以上。因此，应避免将片源全部下载到ROM。

## 开发步骤

推荐使用异步接口fileIo.write()将数据写入ROM。该函数返回number，其中number为实际写入的数据长度（单位：字节）。通过统计该返回值的累计值，可获得应用在一段时间内写入ROM的文件总大小。建议结合定时器或速率控制逻辑，确保视频和小视频在线播放场景下，文件下载速率不超过20MB/min，以降低ROM写入带来的额外功耗。

```screen
let filePath: string = pathDir + "/test.txt";
let file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let str: string = "hello, world";
// Use asynchronous methods to write files to the ROM
fileIo.write(file.fd, str).then((writeLen: number) => {
  hilog.info(0x0000, 'FileIo', 'write data to file succeed and size is:' + writeLen);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'FileIo', 'write data to file failed with error message: ' + err.message + ', error code: ' + err.code);
}).finally(() => {
  fileIo.closeSync(file);
});
```

## 调测验证

通过查看storage\_info节点的信息，如下所示：Total Host Write Data表示整机下载文件的总大小（单位为100MB）。建议文件下载的总速率不超过20MB/min。以视频播放10分钟为例，测试前后的Total Host Write Data节点差值应小于或等于2，符合要求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/gYGzSjlNTMSLG-pKbNt9hQ/zh-cn_image_0000002229337325.png "点击放大")
