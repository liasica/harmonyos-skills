---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/distributed-fs-overview
title: 分布式文件系统概述
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 分布式文件系统 > 分布式文件系统概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:19+08:00
doc_updated_at: 2026-03-30
content_hash: sha256:6c612ce65cf2bad415da4e73549556da4b86a60a09b0655438fc6009cc9e8408
---

分布式文件系统（hmdfs，HarmonyOS Distributed File System）提供跨设备的文件访问能力，适用于以下场景：

* 两台设备组网，用户可以利用一台设备上的编辑软件编辑另外一台设备上的文档。
* 平板保存的音乐，车载系统直接可见并可播放。
* 户外拍摄的照片，回家打开平板直接访问原设备拍摄的照片。

hmdfs在分布式软总线动态组网的基础上，为网络上各个设备节点提供一个全局一致的访问视图，支持开发者通过基础文件系统的接口进行读写访问，具有高性能、低延时等优点。

## 分布式文件系统架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/8nZt96M6StmMOzkJnCOjEQ/zh-cn_image_0000002583438325.png?HW-CC-KV=V1&HW-CC-Date=20260427T234118Z&HW-CC-Expire=86400&HW-CC-Sign=8E7455B28FD3BB400652A96D69990BA4550D89837B93D98F7266939B5E59355D)

* distributedfile\_daemon：主要负责设备上线监听、通过软总线建立链路，并根据分布式的设备安全等级执行不同的数据流转策略。
* hmdfs：实现在内核的网络文件系统，包括缓存管理、文件访问、元数据管理和冲突管理等。

  注意

  [/data/storage/el2/distributedfiles/](app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系) 目录下面的文件不能随意删除，详细注意事项请参考[跨设备文件共享和访问](file-access-across-devices.md)。

  + 缓存管理
    - 设备分布式组网后，hmdfs提供文件的互访能力，但不会主动进行文件数据传输和拷贝。如果应用需要将数据保存到本地，需主动拷贝。
    - hmdfs保证Close-to-Open的一致性，即一端写关闭后，另外一端可以读取到最新数据，不保证文件内容的实时一致性。
    - 数据在远端写入，但是由于网络原因未及时回刷，文件系统会在下次网络接入时回刷本地，但是如果远端已修改则无法回刷。
  + 文件访问
    - 文件访问接口与本地一致（[ohos.file.fs](../harmonyos-references/js-apis-file-fs.md)）。
    - 如果文件在本地，则堆叠访问本地文件系统。
    - 如果文件在其他设备，则同步网络访问远端设备文件。

      说明

      symlink：不支持。
  + 元数据管理
    - 分布式组网下，文件一端创建、删除、修改，另一端可以“立即”查看到最新文件，查看速度取决于网络情况。
    - 远端设备离线后，该设备数据将不再在本端设备呈现。但由于设备离线的感知具有延迟，可能会造成部分消息4s超时，因此开发者需要考虑接口的网络超时或一些文件虽然可以看到，但实际设备可能已离线的场景。
  + 冲突处理
    - 若存在本地文件与远端文件命名相同的情况，会导致冲突，远端同步到本端的文件会被自动重命名，本地文件命名保持不变。
    - 远端多个设备冲突，以接入本设备ID为顺序，显示设备ID小的同名文件，其他文件被依次重命名。
    - 如果组网场景，目录树下已经有远端文件，创建同名文件，提示文件已存在。
    - 冲突文件显示\_conflict\_dev后依次加id，id从1自动递增。
    - 同名目录之间仅融合不存在冲突，文件和远端目录同名冲突，远端目录后缀加\_remote\_directory。
