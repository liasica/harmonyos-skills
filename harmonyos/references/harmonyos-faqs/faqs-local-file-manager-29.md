---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-29
title: fileIo.open读取应用沙盒路径失败
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > fileIo.open读取应用沙盒路径失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-18
content_hash: sha256:114b2291477bfe00d18a75e3fa8dc310e8e03311de9ba9f0fa129dd1db8ea955
---

**问题现象**

获取到demo中的歌曲path，将其转换为uri发送给另一个app。通过context获取应用文件的应用沙箱路径后，将其传入fileIo.open时发现报错。

**解决措施**

uid是系统中用于[应用沙箱](../harmonyos-guides/access-token-overview.md#应用沙箱)隔离的唯一标识符，它分配给每个应用进程，确保应用在运行时相互隔离（如文件系统，内存空间等），可以通过[getOsAccountLocalId接口](../harmonyos-references/js-apis-osaccount.md#getosaccountlocalid9)获取。

进行文件共享时， 获取当前应用的uid，使用fileIo.chown修改文件属主，将uid更改为应用的。
