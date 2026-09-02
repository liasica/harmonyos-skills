---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-remote-compile-practice
title: 内存优化：远程编译实践
breadcrumb: 指南 > 构建应用 > 提升构建效率 > 实践说明 > 内存优化：远程编译实践
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:27+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:19216ba273a1a16258edfc68e78f825d9858b39d322ef4788b65d137f4f2cc2d
---

## 概述

远程编译是一种将构建任务从本地机器迁移至远程服务端执行的开发优化方案，适用于项目规模较大、本地内存不足以支撑完整编译的场景。通过远程编译，可将内存压力转移至性能更强的服务器，保证本地开发的流畅性。

## 工作流程

本地通过rsync服务将代码和构建信息同步至远程服务器，服务端完成编译构建后，再将构建产物同步回本地。客户端轮询监控构建状态，等待构建完成。

整个过程中，实际编译工作由服务端承担，本地仅负责发起构建和接收结果，无需保留完整的编译中间产物，从而有效释放本地内存资源。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/8HGcddBtT_mamsOhUFlkRQ/zh-cn_image_0000002731382087.png "点击放大")

## 使用示例

此示例通过rsync+Hvigor插件+Python脚本实现远程编译，仅供参考，开发者也可以通过其他方式实现远程编译。

在使用本文提供的能力之前，开发者需要具备rsync和Python开发的基础知识。

### 客户端配置

客户端位于开发机器，负责将代码和构建信息同步至远程服务器。以下文件需开发者手动创建，存放路径不限，可根据实际情况放置于任意目录。

1. 创建config.json文件，用于指定rsync同步命令、监控文件路径等参数，示例如下。开发者也可以根据实际情况更改以下参数名或新增其他参数。

   ```json5
   // 示例中仅提供主要的字段说明，其他字段可参考示例代码，需要将路径、IP等替换为实际的内容
   {
     "rsyncType": "client",   // 标识当前为客户端配置
     "monitor": {
       "trigger_file": "/path/to/client/trigger.json"  // 构建信息文件路径，客户端监控此文件中的构建状态变化，本文以trigger.json为例
     },
     "rsyncCommand": "rsync -rltvz --no-o --no-g --timeout=90000 --exclude-from=/path/to/client/exclude.txt /path/to/project rsync://user@server_ip:873/basetest",  // 将本地源码同步至远程服务器的rsync命令
     "origin": {
       "base_dir": "/path/to/project" // 项目路径
     },
     "output": {
       "host": "server_ip"  // 服务端IP
     }
   }
   ```
2. 如果部分文件/目录不需要同步到服务端，可通过rsync命令的--exclude-from参数进行忽略。例如以上示例在exclude.txt中指定忽略的文件/目录。

   ```txt
   // 根据实际情况填写
   .git/
   .idea/
   node_modules/
   oh_modules/
   **/build
   **/build/**
   **/.hvigor/**
   .appanalyzer
   ```
3. 新建rsyncd.conf，用于启动本地rsync服务，示例如下。

   ```txt
   // rsyncd.conf配置并非固定不变，此示例仅供当前远程编译参考使用，根据实际环境修改参数取值
   use chroot = false
   strict modes = false
   hosts allow = *
   log file = rsyncd.log
   pid file = rsyncd.pid
   port = 873
   uid = your_user
   gid = your_group
   [basetest]
   path = /path/to/project/parent
   read only = false
   [client]
   path = /path/to/client/config
   read only = no
   ```
4. 下载[示例代码](ide-remote-compile-practice.md#section12699149191818)中的remote-plugin.ts，并将代码中的configPath、filePath、oldFilePath替换为实际的路径。

   remote-plugin.ts负责创建、读写构建信息文件（即config.json文件的trigger\_file参数对应的文件，本文是trigger.json）和轮询监控构建状态。构建信息文件中会记录构建命令、构建状态等信息，开发者也可以记录其他信息。

   **说明** 

   此示例使用process.argv解析构建参数生成构建命令，需要开发者[将本地守护进程关闭](ide-hvigor-daemon.md#section16318421606)，才能正确读取到参数；或可以直接将构建命令写在插件中调用即可，获取构建命令的方式不限，可根据实际情况处理。

   在工程级hvigorfile.ts中导入remote-plugin.ts。

   ```ts
   import { appTasks } from '@ohos/hvigor-ohos-plugin';
   import { remoteBuildPlugin } from '/path/to/remote-plugin';  // 修改为实际的路径

   export default {
     system: appTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
     plugins: [
       remoteBuildPlugin()
     ]       /* Custom plugin to extend the functionality of Hvigor. */
   }
   ```
5. 新建客户端Python脚本，可参考示例代码中的client/rsync\_client.py，负责读写构建信息文件、轮询监控构建状态、同步代码和构建信息至远程，主要功能说明如下。

   ```txt
   # 配置加载
   load_client2_config()        # 解析config.json，提取配置
   build_remote_spec()          # 构造rsync目标地址

   # JSON操作
   read_json() / write_json()   # 读取/写入JSON文件
   update_trigger_status()      # 更新trigger.json状态

   # 锁管理
   acquire_lock() / release_lock()  # 基于.lock文件的互斥锁，防止并发构建

   # 代码同步
   sync_to_remote()             # rsync同步代码到服务端

   # 文件监控
   monitor_trigger_file()       # 监控trigger.json变化（watchdog或轮询fallback）
   to_cygdrive_path()           # Windows路径转换为cygdrive格式

   # 错误处理
   write_console_file()         # 写入错误日志到console.file

   # 程序入口
   main()                       # 程序入口，启动监控循环
   ```
6. 启动客户端rsync服务和Python脚本。

### 服务端配置

1. 创建config.json文件，用于指定rsync同步命令、监控文件路径等参数，示例如下。开发者也可以根据实际情况更改以下参数名或新增其他参数。

   ```json5
   // 示例中仅提供主要的字段说明，其他字段可参考示例代码，需要将路径、IP等替换为实际的内容
   {
     "rsyncType": "server",   // 标识当前为服务端配置
     "monitor": {
       "trigger_file": "/path/to/server/trigger.json"  // 构建信息文件路径，服务端监控此文件中的构建状态变化，本文以trigger.json为例
     },
     "rsyncCommand": "rsync -rltvz --no-o --no-g --timeout=9000 --exclude-from=/path/to/server/exclude.txt /path/to/project rsync://user@client_ip:873/basetest",  // 将服务端构建产物、日志等同步至客户端的rsync命令
     "build": {
       "base_path": "/path/to/project"  // 项目路径
     },
     "output": {
       "host": "client_ip",  // 服务端IP
     }
   }
   ```
2. 如果部分文件/目录不需要同步到客户端，可通过rsync命令的--exclude-from参数进行忽略。例如以上示例在exclude.txt中指定忽略的文件/目录。

   ```txt
   // 请根据实际情况填写
   .git/
   .idea/
   *.iml
   node_modules/
   oh_modules/
   *.log
   ```
3. 新建rsyncd.conf，用于启动服务端rsync服务，示例如下。

   ```txt
   // rsyncd.conf配置并非固定不变，此示例仅供当前远程编译参考使用，根据实际环境修改参数取值
   syslog facility = 0
   log file = /path/to/server/log/rsyncd.log
   uid = your_user
   gid = your_group
   use chroot = no
   port = 873
   strict modes = false
   timeout = 60000
   # 模块配置
   [basetest]
   path = /path/to/project/parent
   read only = no
   [server]
   path = /path/to/server/config
   read only = no
   ```
4. 新建服务端Python脚本，可参考示例代码中的server/rsync\_server.py，负责读写构建信息文件、轮询监控构建状态、执行构建任务、同步构建产物和构建信息至客户端，主要功能说明如下。

   ```txt
   # 配置加载
   load_server2_config()        # 解析config.json，提取配置
   build_remote_spec()          # 构造rsync目标地址

   # JSON操作
   read_json() / write_json()   # 读取/写入JSON文件
   update_trigger_status()      # 更新trigger.json状态

   # 锁管理
   acquire_lock() / release_lock()  # 基于.lock文件的互斥锁，防止并发构建

   # 构建执行
   execute_node_build()         # 执行构建命令，支持超时控制
   terminate_process_tree()     # 终止构建进程树

   # 产物同步
   sync_to_remote()             # rsync同步产物到客户端

   # 文件监控
   monitor_trigger_file()       # 监控trigger.json变化（watchdog或轮询fallback）
   to_cygdrive_path()           # Windows路径转换为cygdrive格式

   # 错误处理
   write_console_file()         # 写入错误日志到console.file

   # 程序入口
   main()                       # 程序入口，启动监控循环
   ```
5. 启动服务端rsync服务和Python脚本。

### 启动构建

启动rsync服务和Python脚本后，在本地启动构建，即可自动转移到远端服务器进行构建。查看日志信息如下说明远程编译启动成功。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/fvtBgzTVTWinZzTd5q0-jw/zh-cn_image_0000002731542061.png)

### 示例代码

* [远程编译](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/RemoteBuild)
