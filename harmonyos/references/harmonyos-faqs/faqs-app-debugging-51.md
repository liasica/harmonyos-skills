---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-51
title: 如何解决调试启动时，一直卡在Waiting for application to come online notification的问题
breadcrumb: FAQ > DevEco Studio > 应用调试 > 如何解决调试启动时，一直卡在Waiting for application to come online notification的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:bb7e8600a3993679b44f94c33b754fd4a739ce09958147c1383aa37690fb49b0
---

这种情况可能是由以下条件触发的：

* 调试侧拿到的还是旧的进程pid

  首先，使用hdc shell进入设备，然后执行ps命令查找包名（bundleName）对应的进程数。如果有两个进程，说明属于此种场景。命令如下：

  ```
  1. > hdc shell
  2. ps -ef|grep bundleName
  ```

  **解决方案**

  卸载应用，然后重新启动调试。如果问题仍然存在，请重启设备并启动调试。
* 应用没拉起来

  首先，执行hdc track-jpid命令检查应用是否已启动。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/-RMtvbo8TPeNiIgQOQLPDQ/zh-cn_image_0000002194158768.png?HW-CC-KV=V1&HW-CC-Date=20260428T003006Z&HW-CC-Expire=86400&HW-CC-Sign=AF99F5A71D7E084E2FCBEAC30DD9D291769CC0DFCB3740954E8BCF19C2F05822)

  如果列表中没有对应的应用进程，开发者可以通过以下步骤检查应用是否存在：首先，使用hdc shell连接到设备，然后执行ps -ef | grep bundleName命令。

  如果应用不存在，说明应用未启动。如果应用存在但未出现在hdc track-jpid列表中，说明应用未注册。

  应用可能为release版本。使用hdc shell bm dump -n bundleName > aa.txt查看debug值是否为true。如果debug值为false，则设备上的应用为release版本。建议清理工程并重新进行debug打包。如果问题仍然存在，说明应用未成功覆盖安装。请首先判断当前需要调试的应用是否为预置应用。如果是预置应用，建议进行OTA升级。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/IR70HDBVRk6E9GxrJFnhcA/zh-cn_image_0000002229604145.png?HW-CC-KV=V1&HW-CC-Date=20260428T003006Z&HW-CC-Expire=86400&HW-CC-Sign=B4212473A652C595CB2F4DEC3C1BDE256EBAD5C5E1E582ABC62555D8784091B6 "点击放大")

  **build mode：**None/debug打出的包均为debug包
* hvigor 版本不配套

  如果不配套，请使用配套版本。新建一个模板工程，检查hvigor目录下的hvigor-config.json5文件中的版本号，确保与当前版本配套。
