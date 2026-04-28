---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-9
title: 如何实现相机关闭
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何实现相机关闭
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e15407ac8fab169fe6ea555b710af331bdc66c32813b88c3e579ee773bbce8a0
---

实现相机关闭的参考代码如下：

```
1. // Stop the current session
2. photoSession.stop();

4. // Release camera input stream
5. cameraInput.close();

7. // Release preview output stream
8. previewOutput.release();

10. // Release the photo output stream
11. photoOutput.release();

13. // Release session
14. photoSession.release();

16. // Session left blank
17. photoSession = undefined;
```

[CloseSession.txt](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/CloseSession.txt#L7-L23)

**参考链接**

[拍照实践(ArkTS)](../harmonyos-guides/camera-shooting-case.md)
