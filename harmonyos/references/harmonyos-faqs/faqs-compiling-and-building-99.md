---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-99
title: 编译的时候遇到“too many open files”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译的时候遇到“too many open files”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:08268cd1d1ccf3f3c7e4e2f38932e6ed452c78354d5c787e92ad6b3314c9ecb4
---

**问题描述**

mac系统项目编译报错。

```
1. hvigor ERROR: EMFILE: too many open files, open '/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/ets/build-tools/ets-loader/kit_configs/@kit.ArkTS.json'
```

**解决措施**

最大连接数限制取决于系统所能打开的最大文件数（文件描述符）。在Linux中，动态端口号的默认范围是32768到65535，因此作为客户端连接同一个IP和端口号时，最多可以建立32768个连接。而在Mac系统中，默认情况下最多可以建立16384个连接。如果需要调整这些限制，可以在DevEco Studio终端执行以下命令（根据实际情况填充数字）：

```
1. sysctl kern.maxfiles
2. sudo sysctl -w kern.maxfiles=20480
3. sudo sysctl -w kern.maxfilesperproc=18000
4. hvigorw --stop-daemon-all
```
