---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-14
title: el1与el2文件之间的区别
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > el1与el2文件之间的区别
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2f83a78d9f64083173449178f74473bf82e8f01032693055ad86da2f03b455ef
---

三级目录el1/和el2/：代表不同文件加密类型。

el1（设备级加密区）：设备开机后可访问的数据区。

el2（用户级加密区）：设备开机后，需解锁对应用户的锁屏界面（包括密码、指纹、人脸等认证方式；若未设置锁屏则无需解锁）至少一次，才能访问加密数据区。

应用若无特殊需求，应将数据存放在el2加密目录下，以保障数据安全。对于需要在用户解锁前访问的文件，如时钟、闹铃、壁纸等，应将这些文件存放在设备级加密区（el1）。

具体关于应用沙箱路径的内容可以参考[应用沙箱路径](../harmonyos-guides/app-sandbox-directory.md#应用沙箱目录与应用沙箱路径)。
