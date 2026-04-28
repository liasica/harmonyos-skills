---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-29
title: fileIo.open读取应用沙盒路径失败
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > fileIo.open读取应用沙盒路径失败
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:28+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:6dc2c8c0f08b1658330080f28927b16a5928b4e306a4710ce42e9e208dd4a54b
---

**问题现象**

获取到demo中的歌曲path，将其转换为uri发送给另一个app。通过context获取应用文件的应用沙箱路径后，将其传入fileIo.open时发现报错。

**解决措施**

进行文件共享时， 获取当前应用的uid/gid，使用fileIo.chown修改文件属主，将uid和gid更改为应用的。
