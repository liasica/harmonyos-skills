---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-9
title: 如何在命令行使用ohpm
breadcrumb: FAQ > DevEco Studio > 环境准备 > 如何在命令行使用ohpm
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:550e18d00599e4f7f89cdcfc5d589b1ed771d650d547d40de046a6370524bf5f
---

注意

安装node.js 18.x及以上版本，并配置环境变量。

ohpm 默认解压路径为：DevEco Studio 中默认安装位置：<DevEco Studio 安装目录>\tools\ohpm；命令行工具中默认安装位置：<Command Line Tools 安装目录>/command-line-tools/ohpm。

**问题现象****1**

安装ohpm后，如果在命令行中无法直接使用ohpm，请检查环境变量配置是否正确。

**解决措施****1**

1. 在Windows系统中，右键点击“此电脑”选择“属性”，进入“高级系统设置”，点击“环境变量”，在“系统变量”中找到“Path”，点击“编辑”，添加ohpm工具包解压后的bin目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/HwMjfs5VSmqqzis_Z16eMw/zh-cn_image_0000002229604141.png?HW-CC-KV=V1&HW-CC-Date=20260429T062004Z&HW-CC-Expire=86400&HW-CC-Sign=C2B573C143AFE43B1F681615CC3B55B193204BD872A897A966C69AE51518A267 "点击放大")
2. 添加变量后，重开命令行窗口，执行ohpm -v查看ohpm版本号，终端输出版本号信息（如1.0.0）即为成功。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/oCw5BvUJQyGgiEXBSHZDOQ/zh-cn_image_0000002194318368.png?HW-CC-KV=V1&HW-CC-Date=20260429T062004Z&HW-CC-Expire=86400&HW-CC-Sign=58125772344AAC84570889FADA459A643562C249990BC7F1241B4346606674ED)

**问题现象2**

在Linux/Mac系统中，安装ohpm后，不能在命令行中使用ohpm。

**解决措施2**

编辑配置文件，将ohpm工具包解压目录中的bin目录路径添加到PATH环境变量中（以 Mac 系统的 Zsh 命令行为例）。

1. 打开终端并编辑 ~/.zshrc 文件。

   ```
   1. vi ~/.zshrc
   ```
2. 在文件末尾添加以下行，将软件的bin目录添加到PATH环境变量中（例如：/home/tctAdmin/ohpm/bin）：

   ```
   1. export PATH="/home/tctAdmin/ohpm/bin:$PATH"
   ```
3. 保存 ~/.zshrc 文件并退出编辑器。
4. 使用以下命令使更改生效，或者关闭并重新打开命令行窗口。

   ```
   1. source ~/.zshrc
   ```
5. 执行ohpm -v查看 ohpm 版本号，命令行输出版本号（如 1.0.0）表示成功。

   ```
   1. ohpm -v
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/06r0HA0GTvSBAi1FHEw0Og/zh-cn_image_0000002194318372.png?HW-CC-KV=V1&HW-CC-Date=20260429T062004Z&HW-CC-Expire=86400&HW-CC-Sign=76A0408E6D44EEF13B7C5BAF29B3467B3F750F84A71A0EE479C2DFB5497798A1)
