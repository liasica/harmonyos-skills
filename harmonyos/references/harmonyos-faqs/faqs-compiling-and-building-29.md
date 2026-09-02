---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-29
title: Target AOT编译，AP文件生成失败
breadcrumb: FAQ > DevEco Studio > 编译构建 > Target AOT编译，AP文件生成失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:f8dedbe87417713490b9c0fc28b6141004eed77ff1eea0e261a2eff66a1cfd43
---

**问题现象**

Target AOT编译，AP文件生成失败，并报错提示“errno: 13”表示权限不足，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/vnT47-8QTgq-OrbRlKE4Ig/zh-cn_image_0000002654837809.png)

**解决措施**

errno: 13表示权限不足，请通过下述措施解决：

打开命令行工具，输入以下命令，关闭selinux权限管控。

```powershell
hdc shell
setenforce 0
```

以上设置重启将会失效，若设备重启请重新进行以上设置
