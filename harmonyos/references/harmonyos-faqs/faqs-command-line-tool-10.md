---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-10
title: ohpm publish在本地Git bash环境下一直报错“the content of private key in the key_path error”
breadcrumb: FAQ > DevEco Studio > 命令行工具 > ohpm publish在本地Git bash环境下一直报错“the content of private key in the key_path error”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d6ba53dd9c25ac7b201bb2f94be911dc0af8112fdd5243c530747a25bf9a664d
---

**问题描述**

在本地Git Bash环境下使用ohpm publish命令时，一直报错“the content of private key in the key\_path error”。但在DevEco Studio中不会出现此问题，DevEco Studio会提示输入密码。当前使用的ohpm版本为1.5，环境变量已配置。

**原因分析**

使用ohpm publish命令上传包时，如果使用SSH证书密码认证，程序需要通过TTY流读取用户输入的密码。如果Git安装的版本过低，其携带的Git Bash会导致TTY流丢失，从而引发该错误。

**解决方案**

1、从Git官网下载并安装最新版本的Git，使用该版本附带的Git Bash终端进行操作。

2、在当前Git安装目录下的etc目录中新增git-bash.config文件，并在文件中添加一行MSYS=enable\_pcon配置。重新打开Git Bash终端，运行ohpm publish命令即可。
