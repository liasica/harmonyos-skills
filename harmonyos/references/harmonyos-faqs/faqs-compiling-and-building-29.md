---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-29
title: Target AOT编译，AP文件生成失败
breadcrumb: FAQ > DevEco Studio > 编译构建 > Target AOT编译，AP文件生成失败
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a9cafa09a6ceb615d93603048ca9cc7f9d3fa9f3e303b72e18675f397a9e92b9
---

**问题现象**

Target AOT编译，AP文件生成失败，并报错提示“errno: 13”表示权限不足，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/3ul8yOwKTPmnADzlG-5CNw/zh-cn_image_0000002229758617.png?HW-CC-KV=V1&HW-CC-Date=20260429T062025Z&HW-CC-Expire=86400&HW-CC-Sign=FFA0B75BAAD2CFC86397F7FFC23455E57B1C4DAF666E07DD30CB40F53345E231)

**解决措施**

errno: 13表示权限不足，请通过下述措施解决：

打开命令行工具，输入以下命令，关闭selinux权限管控。

```
1. hdc shell
2. setenforce 0
```

以上设置重启将会失效，若设备重启请重新进行以上设置
