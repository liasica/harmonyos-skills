---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/app-debugging-faq-0013
title: HDC调试端口占用问题排查
breadcrumb: FAQ > DevEco Studio > 应用调试 > 常见问题 > HDC调试端口占用问题排查
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:c33ba0944d20ff7f96212ace9b8513f7c55d512f80070b1cfab840d4e4d2fac1
---

**Q：在设备中运行HAP时，提示"Hdc server port XXXX已被使用。请配置环境变量'OHOS\_HDC\_SERVER\_PORT'并重启DevEco Studio。"**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/zI5ZJamDTHGfPFeECKyD9Q/zh-cn_image_0000002802394017.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D3651F3F23E5F40C6223A687CB25FB41D850AFF6A8849034C894CB68F13DFC2)

**A**：HDC的默认端口8710导致服务无法启动。解决方法如下：

方式一：结束掉占用该端口的应用。

1. 运行CMD命令行工具，输入"netstat -ano | findstr *端口号*"，查询占用端口号的进程PID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/qjqmQQJVR_GT8uLBNrRP6Q/zh-cn_image_0000002802394019.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=B26EA6B57128E8D1536F7E709EAF65196BAC859A7A384DC06D7FB31A07D637D3 "点击放大")
2. 打开任务管理器，选择详细信息页，查看PID对应的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/8AJAbyvfTfyhhWPzW8JPIg/zh-cn_image_0000002773154174.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D2E6CB6764523D34A13FE1249A9263AD8843008B012EEA6037642F36E125947 "点击放大")
3. 结束掉对应应用后，重启DevEco Studio。

方式二：为HDC端口号设置其他的环境变量。

* Windows环境变量设置方法：

  在**此电脑 > 属性 > 高级系统设置 > 高级 > 环境变量**中，添加变量名OHOS\_HDC\_SERVER\_PORT，变量值设置为任意未占用的端口，例如7035。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/s_XjcosWQkSll3FnY_GXiQ/zh-cn_image_0000002802353941.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=D08502DD6601B7E1E27899C36D77C8AA357B17B8420DF3F564D10CB751C5DC49)

  环境变量配置完成后，关闭并重启DevEco Studio。
* macOS环境变量设置方法：
  1. 打开终端，执行以下命令，根据输出结果执行不同命令。

     ```shell
     echo $SHELL
     ```

     如果输出结果为/bin/bash，则执行以下命令以打开.bash\_profile文件。

     ```shell
     vi ~/.bash_profile
     ```

     如果输出结果为/bin/zsh，则执行以下命令以打开.zshrc文件。

     ```shell
     vi ~/.zshrc
     ```
  2. 按字母"i"，进入**Insert**模式。
  3. 输入以下内容，添加OHOS\_HDC\_SERVER\_PORT端口信息。

     ```shell
     OHOS_HDC_SERVER_PORT=7035
     launchctl setenv OHOS_HDC_SERVER_PORT $OHOS_HDC_SERVER_PORT
     export OHOS_HDC_SERVER_PORT
     ```
  4. 编辑完成后，单击**Esc**键退出编辑模式，然后输入":wq"并单击**Enter**键保存。
  5. 执行以下命令，使环境变量生效。

     如果步骤1打开的是.bash\_profile文件，请执行如下命令：

     ```shell
     source ~/.bash_profile
     ```

     如果步骤1打开的是.zshrc文件，请执行如下命令：

     ```shell
     source ~/.zshrc
     ```
  6. 环境变量配置完成后，关闭并重启DevEco Studio。

方式三：如果查询端口未被占用，检查端口是否被防火墙拦截。如果被拦截，放行端口，然后重启DevEco Studio重新尝试。
