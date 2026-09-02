---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-99
title: 编译的时候遇到“too many open files”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译的时候遇到“too many open files”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:bf49d3bae75e761460a897ad11ad7203d70a8a24ce7ce056e088e2f6c1db42f5
---

**问题描述**

mac系统项目编译报错。

```text
hvigor ERROR: EMFILE: too many open files, open '/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/ets/build-tools/ets-loader/kit_configs/@kit.ArkTS.json'
```

**解决措施**

最大连接数限制取决于系统所能打开的最大文件数（文件描述符）。在Linux中，动态端口号的默认范围是32768到65535，因此作为客户端连接同一个IP和端口号时，最多可以建立32768个连接。而在Mac系统中，默认情况下最多可以建立16384个连接。如果需要调整这些限制，可以在DevEco Studio终端执行以下命令（根据实际情况填充数字）：

```powershell
sysctl kern.maxfiles
sudo sysctl -w kern.maxfiles=20480
sudo sysctl -w kern.maxfilesperproc=18000
hvigorw --stop-daemon-all
```
