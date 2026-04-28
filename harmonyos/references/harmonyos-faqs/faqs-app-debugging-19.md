---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-19
title: 运行时提示“Hdc server port XXXX has been used”
breadcrumb: FAQ > DevEco Studio > 应用调试 > 运行时提示“Hdc server port XXXX has been used”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:574bf9ba924d2d3bee42f4f94a21de4ab2c140d6faae054531ccb8ed7b70c47d
---

**问题现象**

在设备中运行HAP时，提示“Hdc server port XXXX已被使用。请配置环境变量‘OHOS\_HDC\_SERVER\_PORT’并重启DevEco Studio。”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/00fk2zPiQtqGNpvP2XtuWw/zh-cn_image_0000002229758497.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=1493AD2B4164B7CEE7ED4707D2C421E3DDB3254190F361854DE1F51E02E270DD)

**解决措施**

HDC的默认端口8710导致服务无法启动。解决方法如下：

方式一：结束掉占用该端口的应用。

1. 运行CMD命令行工具，输入“netstat -ano | findstr *端口号*”，查询占用端口号的进程PID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/nuAKMheFS8-JJOho4VdDRQ/zh-cn_image_0000002194158624.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=CC8C86370782FB3AEFD6C0E121361C5F632BBD9E28B49E49188A154544F16A1C)
2. 打开任务管理器，选择详细信息页，查看PID对应的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/mDw2htStSGCf99Wp_eNzYg/zh-cn_image_0000002194318240.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=67E02B935D773FFEA297BE657EAFA9DEBB095072F1EFA6CC4859A72C55A7FBBC)
3. 结束掉对应应用后，重启DevEco Studio。

方式二：为HDC端口号设置其他的环境变量。

* Windows环境变量设置方法：

  在**此电脑 > 属性 > 高级系统设置 > 高级 > 环境变量**中，添加变量名OHOS\_HDC\_SERVER\_PORT，变量值设置为任意未占用的端口，例如7035。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/XrpLSW3ERyC3hg-06zeQiw/zh-cn_image_0000002194318236.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=C381E8E4118A20378308DDFC4C87542E496E57C796935C2BBCF8AC4AF601FD02)

  环境变量配置完成后，关闭并重启DevEco Studio。
* macOS环境变量设置方法：
  1. 打开终端，执行以下命令，根据输出结果执行不同命令。

     ```
     1. echo $SHELL
     ```

     + 如果输出结果为/bin/bash，则执行以下命令以打开.bash\_profile文件。

       ```
       1. vi ~/.bash_profile
       ```
     + 如果输出结果为/bin/zsh，则执行以下命令以打开.zshrc文件。

       ```
       1. vi ~/.zshrc
       ```
  2. 按字母“i”，进入**Insert**模式。
  3. 输入以下内容，添加OHOS\_HDC\_SERVER\_PORT端口信息。

     ```
     1. OHOS_HDC_SERVER_PORT=7035
     2. launchctl setenv OHOS_HDC_SERVER_PORT $OHOS_HDC_SERVER_PORT
     3. export OHOS_HDC_SERVER_PORT
     ```
  4. 编辑完成后，单击**Esc**键退出编辑模式，然后输入“:wq”并单击**Enter**键保存。
  5. 执行以下命令，使环境变量生效。
     + 如果[步骤1](faqs-app-debugging-19.md#zh-cn_topic_0000001166752005_li1264071053012)打开的是.bash\_profile文件，请执行如下命令：

       ```
       1. source ~/.bash_profile
       ```
     + 如果[步骤1](faqs-app-debugging-19.md#zh-cn_topic_0000001166752005_li1264071053012)打开的是.zshrc文件，请执行如下命令：

       ```
       1. source ~/.zshrc
       ```
  6. 环境变量配置完成后，关闭并重启DevEco Studio。

方式三：如果查询端口未被占用，检查端口是否被防火墙拦截。如果被拦截，放行端口，然后重启DevEco Studio重新尝试。
