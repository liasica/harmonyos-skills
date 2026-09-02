---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-59
title: 上传视频超时失败
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 上传视频超时失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d04412effa3460d21d13cd36f57a5d3951d1abd05fc1394857020ff24e2cefbf
---

## 问题现象

应用内上传长视频，提示超时，无法成功上传。

## 背景知识

应用内上传文件，通常使用request.uploadFile或者request.agent，其中使用request.agent方式时，可以通过[Task](../harmonyos-references/js-apis-request.md#requestagenttask10)对象的[Config](../harmonyos-references/js-apis-request.md#requestagentconfig10)设置超时时间。

## 问题定位

1. 查看hilog日志，应用从开始点击上传，到页面提示上传超时，中间耗时1分钟。

   ```shell
   10-10 15:27:42.114   21357-21357   C01C50/com.hm.example/Requestkit  com.hm.example    I     [js_task.cpp 167] End create seq 28, tid 64355709
   10-10 15:27:42.114   21357-21357   C01C50/com.hm.example/Requestkit  com.hm.example    I     [request_event.cpp 172] End task 64355709 on progress seq 29
   10-10 15:27:43.268   21357-21357   C01C50/com.hm.example/Requestkit  com.hm.example    I     [js_notify_data_listener.cpp 214] Notify progress tid 64355709
   10-10 15:28:42.125   21357-21357   C0390D/com.hm.example/AceOverlay  com.hm.example    I     [(100000:100000:scope)] begin to close custom dialog.
   ```
2. 在代码中搜索upload关键词，发现uploadToCloud方法入参中的超时参数传入的是60\*1000。
3. 尝试上传时长较短、文件体积较小的视频，确保在上传耗时不超过1分钟的情况下可以成功上传。

## 分析结论

由于应用将视频上传的超时时间设置为1分钟，在上传时长较长、文件体积较大的视频时，容易触发超时，从而导致上传失败。

## 修改建议

建议应用优化上传超时场景下的错误提示，或对视频文件的大小或时长进行限制，以降低上传耗时并避免超时失败。
