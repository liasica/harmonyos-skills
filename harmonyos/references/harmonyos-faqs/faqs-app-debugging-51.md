---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-51
title: 如何解决调试启动时，一直卡在Waiting for application to come online notification的问题
breadcrumb: FAQ > DevEco Studio > 应用调试 > 如何解决调试启动时，一直卡在Waiting for application to come online notification的问题
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:24+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b2073afa106f00d7e6ec3d894ce66b23640448738dc3a3088ca68199aa65c8bf
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/-RMtvbo8TPeNiIgQOQLPDQ/zh-cn_image_0000002194158768.png?HW-CC-KV=V1&HW-CC-Date=20260429T062123Z&HW-CC-Expire=86400&HW-CC-Sign=53726DD899DA4DC82A015E85C6A7E09011C7AAC531E4649D18DE39D6298DB8C8)

  如果列表中没有对应的应用进程，开发者可以通过以下步骤检查应用是否存在：首先，使用hdc shell连接到设备，然后执行ps -ef | grep bundleName命令。

  如果应用不存在，说明应用未启动。如果应用存在但未出现在hdc track-jpid列表中，说明应用未注册。

  应用可能为release版本。使用hdc shell bm dump -n bundleName > aa.txt查看debug值是否为true。如果debug值为false，则设备上的应用为release版本。建议清理工程并重新进行debug打包。如果问题仍然存在，说明应用未成功覆盖安装。请首先判断当前需要调试的应用是否为预置应用。如果是预置应用，建议进行OTA升级。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/IR70HDBVRk6E9GxrJFnhcA/zh-cn_image_0000002229604145.png?HW-CC-KV=V1&HW-CC-Date=20260429T062123Z&HW-CC-Expire=86400&HW-CC-Sign=AA6DDD17ABCD1E0E0FE5CAFAFA16E0B8ABDC9E0888C21D92C5105AEC7818B74B "点击放大")

  **build mode：**None/debug打出的包均为debug包
* hvigor 版本不配套

  如果不配套，请使用配套版本。新建一个模板工程，检查hvigor目录下的hvigor-config.json5文件中的版本号，确保与当前版本配套。
