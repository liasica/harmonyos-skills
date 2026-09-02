---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-43
title: 如何解决连接手机时，提示：“hdc server port 8710 has been used”的问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何解决连接手机时，提示：“hdc server port 8710 has been used”的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:d33e824d0841b9661a3328c286efc53d8db4211dcf5e0fdcc03a60a73483fcc9
---

* 方式一：结束掉占用该端口的应用。
  1. 运行cmd命令行工具，输入“netstat -ano | findstr 端口号”，查询占用端口号的进程PID。
  2. 打开任务管理器，选择详细信息页签，查看此PID对应的应用。
  3. 结束掉对应应用后，重启DevEco Studio。
* 方式二：为hdc端口号设置其他的环境变量。
  1. Windows环境变量设置方法：

     在电脑的“属性” -> “高级系统设置” -> “高级” -> “环境变量”中添加hdc端口。变量名为 OHOS\_HDC\_SERVER\_PORT，变量值可设置为任意未被占用的端口。
  2. Mac环境变量设置方法：

     a.打开终端工具，执行echo $SHELL命令，根据输出结果分别执行不同命令:

     如果输出结果为 /bin/bash，则执行 vi ~/.bash\_profile 命令，打开 .bash\_profile 文件。

     如果输出结果为 /bin/zsh，则执行 vi ~/.zshrc 命令，打开 .zshrc 文件。

     b.单击字母“i”以进入Insert模式。

     c.输入以下内容，将OHOS\_HDC\_SERVER\_PORT端口信息添加到PATH路径中。

     ```powershell
     OHOS_HDC_SERVER_PORT=端口号
     launchctl setenv OHOS_HDC_SERVER_PORT $OHOS_HDC_SERVER_PORT
     export OHOS_HDC_SERVER_PORT
     ```

     d.编辑完成后，单击Esc键退出编辑模式，然后输入:wq并单击Enter键保存。

     e.执行以下命令，使配置的环境变量生效：

     如果步骤1打开的是 .bash\_profile 文件，执行 source ~/.bash\_profile 命令。

     如果步骤1中打开的是`.zshrc`文件，执行 source ~/.zshrc 命令。

     f.环境变量配置完成后，关闭并重启DevEco Studio。
