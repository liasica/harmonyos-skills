---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-options
title: 命令
breadcrumb: 指南 > AI Coding > DevEco Code > 命令
category: harmonyos-guides
scraped_at: 2026-09-15T07:03:56+08:00
doc_updated_at: 2026-09-14
content_hash: sha256:39203d8739b6eca64f7abff64e1488d3124fda24028aba84893969aaf84bba4b
---

## collect

从0.2.0版本开始，当DevEco Code出现异常（如卡顿、报错、崩溃等）时，支持通过该命令触发日志上传弹框，在弹框中勾选需要上传的日志文件，以便定位和修复工具问题。

DevEco Code日志默认存储路径为：

* Windows：C:\Users\用户名\.local\share\deveco\log
* macOS：~/.local/share/deveco/log

**命令格式：**

```txt
/collect
```

**说明** 

若应用非正常退出（如卡顿闪退等），当应用再次启动时会自动弹出上传日志弹框。

执行/privacy命令，选择**disable crash detect**输入回车，可关闭自动触发上传日志功能。
