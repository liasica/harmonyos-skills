---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-212
title: 如何在构建打包时获取云端文件新增或更新到rawfile文件夹中
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何在构建打包时获取云端文件新增或更新到rawfile文件夹中
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:50e74a179db261ef64f68a99e7c0d220e06191f2be79e4770478f7f3fb603a88
---

## 问题现象

在代码模块resources目录下的rawfile文件夹中，某些资源文件在应用每次打包发版时都需要更新，通过云端下载下来再手动置入工程中的更新方式比较繁琐，能否通过代码或脚本解决。

## 背景知识

* DevEco Studio在编译构建的功能中，为开发者提供了扩展构建的功能。其中，Hvigor允许开发者实现自己的插件，开发者可以定义自己的构建逻辑。
* Hvigor主要提供了两种方式来开发插件：[基于hvigorfile脚本开发](../harmonyos-guides/ide-hvigor-plugin.md#section552855418188)、[基于typescript项目开发](../harmonyos-guides/ide-hvigor-plugin.md#section1825121193616)。
* 对于基于hvigorfile.ts脚本开发的方式，其优点是可实现快速开发，直接编辑工程或模块下hvigorfile.ts即可编写插件代码。而基于typescript项目开发的方式，可以通过发布达到复用和共享分发的目的。

## 解决方案

解决思路：通过hvigorfile脚本开发构建插件，在插件中执行例如bat脚本等脚本程序，将资源下载到rawfile文件夹后再完成构建打包的工作。

实现示例：

1. 首先准备一个脚本，对于Windows平台可以使用bat脚本，示例代码如下所示：

   ```bat
   @echo off
   set "download_url=https://example.com/file.zip"
   set "save_folder=./Downloads"
   set "filename=file.zip"

   :: 检查保存文件夹是否存在，如果不存在则创建
   if not exist "%save_folder%" (
   mkdir "%save_folder%"
   )

   :: 使用 PowerShell 下载文件
   powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%download_url%', '%save_folder%\%filename%')"

   echo 文件下载完成，保存路径为：'%save_folder%/%filename%'
   ```

   而类Unix平台可以使用shell脚本，示例代码如下所示：

   ```shell
   #!/bin/bash
   # 设置变量
   download_url="https://example.com/file.zip"
   save_folder="./Downloads"
   filename="file.zip"
   # 创建保存目录（如果不存在）
   mkdir -p "$save_folder"
   # 检查系统中是否有 curl 或 wget，并选择其一进行下载
   if command -v curl >/dev/null 2>&1; then
       echo "使用 curl 下载文件..."
       curl -L -o "$save_folder/$filename" "$download_url"
   elif command -v wget >/dev/null 2>&1; then
       echo "使用 wget 下载文件..."
       wget -O "$save_folder/$filename" "$download_url"
   else
       echo "错误：未找到 curl 或 wget，请安装其中一个工具。"
       exit 1
   fi
   # 检查下载是否成功
   if [ $? -eq 0 ]; then
       echo "文件下载完成，保存路径为：$(realpath "$save_folder/$filename")"
   else
       echo "下载失败！"
       exit 1
   fi
   ```

   然后将对应脚本文件放在需要更新rawfile目录文件的模块中，例如放在Entry模块的根目录，此时可以save\_folder可改为./src/main/resources/rawfile。
2. 修改Entry模块根目录中的hvigorfile.ts脚本，根据构建的环境运行不同的脚本，示例代码如下所示:

   ```ts
   import { hapTasks } from '@ohos/hvigor-ohos-plugin';
   import { execSync } from 'node:child_process';
   import util from 'node:util';

   export function downloadFilePluginFunc(str?: string): HvigorPlugin {
     return {
       pluginId: 'DownloadFilePluginID01',
       apply(pluginContext): void {
         pluginContext.registerTask({
           // 编写自定义任务
           name: 'customTask1',
           run: (taskContext) => {
             let command = '';
             const platform = process.platform;
             if (platform === 'win32') {
               command = 'downloadFile.bat';
             } else {
               command = 'sh downloadFile.sh';
             }
             const workingDirectory = __dirname;
             try {
               const output = execSync(command, { cwd: workingDirectory });
               console.info(`文件下载成功，输出: ${output.toString()}`);
             } catch(e) {
               console.info(`文件下载失败，输出: ${e.toString()}`);
             }
           },
           // 确认自定义任务插入位置
           dependencies: ['default@GenerateMetadata'],
           postDependencies: ['default@ProcessResource']
         })
       }
     }
   }

   export default {
     system: hapTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
     plugins: [downloadFilePluginFunc()] /* Custom plugin to extend the functionality of Hvigor. */
   }
   ```
3. 在未构建前，可以看到目前rawfile文件夹中没有文件：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/Rp1ZxWuHTACzXbCVqPSMjg/zh-cn_image_0000002658928503.png "点击放大")
4. 在构建打包之后，可以看到rawfile文件夹中多出来了一个文件，而且通过查看APP包的内容也能看到Entry模块打出来的Hap包的rawfile文件夹中，包含了之前下载好的文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/GLIKrEaPSVS8a3PyiKM48w/zh-cn_image_0000002628409284.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/XwHbce8XQne90GfgQVac9w/zh-cn_image_0000002658808555.png "点击放大")

   以上运行结果说明脚本执行成功，可以通过自定义构建任务获取云端文件新增或更新到rawfile文件夹中。
