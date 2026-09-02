---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-1
title: 通过命令行或终端可以正常发布，在Git Bash上发布时提示错误：私钥路径中的私钥内容错误
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 通过命令行或终端可以正常发布，在Git Bash上发布时提示错误：私钥路径中的私钥内容错误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:957b0a3ddff79fab1b4d29042ea944f899764b5581c8800dd77ea179d5c4c0c8
---

**问题现象**

通过命令行或终端可以正常发布，但在Git Bash上发布时出现错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/n8toceyoQimDvCGxsjrvlg/zh-cn_image_0000002624638734.png "点击放大")

**解决措施**

方法一：从Git官网下载并安装最新版本的Git，使用该版本自带的Git Bash终端进行操作。

方法二：在当前Git安装目录下的etc目录中新增git-bash.config文件，文件中添加一行MSYS=enable\_pcon配置。重新打开Git Bash终端，运行ohpm publish命令即可。
