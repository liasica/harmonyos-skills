---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-29
title: Target AOT编译，AP文件生成失败
breadcrumb: FAQ > DevEco Studio > 编译构建 > Target AOT编译，AP文件生成失败
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:235ee16b5f337fd297dcf380ae2eaab3ac67761192ef036b6bb23a2124d1c819
---

**问题现象**

Target AOT编译，AP文件生成失败，并报错提示“errno: 13”表示权限不足，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/3ul8yOwKTPmnADzlG-5CNw/zh-cn_image_0000002229758617.png?HW-CC-KV=V1&HW-CC-Date=20260428T002912Z&HW-CC-Expire=86400&HW-CC-Sign=95BD6E97C55F1DF1B012AF0B04BD999E5D93B354D546F05294BFA6038AF60123)

**解决措施**

errno: 13表示权限不足，请通过下述措施解决：

打开命令行工具，输入以下命令，关闭selinux权限管控。

```
1. hdc shell
2. setenforce 0
```

以上设置重启将会失效，若设备重启请重新进行以上设置
