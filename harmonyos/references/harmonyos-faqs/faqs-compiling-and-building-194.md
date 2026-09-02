---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-194
title: 编译报错“failed with:Exit code 0xc0000043”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“failed with:Exit code 0xc0000043”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:e770ec124d1176cc9f6f225b4f4bdf29c27cc6f743e15494dcb8d86fdb266da0
---

**问题现象**

编译构建Native C++模块时，出现报错“failed with:Exit code 0xc0000043”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/L0cAsBetSTCEpteezhYKIw/zh-cn_image_0000002654798087.png)

**问题原因**

该报错是Windows系统下的一个NTSTATUS错误码，出现该报错的原因可能是使用了损坏或不完整的可执行文件，也可能是杀毒软件/防火墙拦截了ninja.exe文件的加载。

**解决措施**

1、在报错的ninja.exe文件所在目录中打开命令行工具，执行命令ninja.exe --version，若无法正常输出版本信息，可能为文件损坏或丢失，建议重新安装DevEco Studio。

2、尝试暂时关闭杀毒软件，或手动将ninja.exe文件添加到杀毒软件的白名单中，然后重新执行编译构建。
