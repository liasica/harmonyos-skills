---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-1
title: 通过命令行或终端可以正常发布，在Git Bash上发布时提示错误：私钥路径中的私钥内容错误
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 通过命令行或终端可以正常发布，在Git Bash上发布时提示错误：私钥路径中的私钥内容错误
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:eea8dfaae267fc91fea74187222763d1ec0c03218c573f95d99c3fdebb4db710
---

**问题现象**

通过命令行或终端可以正常发布，但在Git Bash上发布时出现错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/pPd-jEweQsOpGHTNyxCfHQ/zh-cn_image_0000002194158912.png?HW-CC-KV=V1&HW-CC-Date=20260428T003020Z&HW-CC-Expire=86400&HW-CC-Sign=F732DC0D2E41562D1024C09A1F0029E16343EFC1596A9198C9A3F441837A1138 "点击放大")

**解决措施**

方法一：从Git官网下载并安装最新版本的Git，使用该版本自带的Git Bash终端进行操作。

方法二：在当前Git安装目录下的etc目录中新增git-bash.config文件，文件中添加一行MSYS=enable\_pcon配置。重新打开Git Bash终端，运行ohpm publish命令即可。
