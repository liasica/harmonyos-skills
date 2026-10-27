---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0021
title: Target AOT编译AP文件生成失败问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > Target AOT编译AP文件生成失败问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:51+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:5fec20735e39f97fd464c639ad379cc7daa654f7453d27364336c59c27a8b539
---

**Q：Target AOT编译，AP文件生成失败，并报错提示“errno: 13”表示权限不足，如下图所示。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/8hd-8NGhSTWud1nA_YpuFA/zh-cn_image_0000002772702484.png "点击放大")

**A**：errno: 13表示权限不足，请通过下述措施解决：

打开命令行工具，输入以下命令，关闭selinux权限管控。

```shell
hdc shell
setenforce 0
```

以上设置重启将会失效，若设备重启请重新进行以上设置。
