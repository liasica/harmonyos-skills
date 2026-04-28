---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-device-file-explorer
title: 访问设备文件
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 访问设备文件
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4fb8240f0603aa85ee3c84a347d9c25009144891ab93bf05f1fffa7411d10f4f
---

开发者可以使用Device File Browser，在DevEco Studio上如PC端操作一样，对设备文件进行新建、删除、上传、下载等操作，而无需使用命令行，提升开发效率，当前支持普通文件视图与应用沙箱视图两种模式。

## 使用场景

* 查看设备上的文件列表及基本信息。
* 在设备上搜索文件及文件夹。
* 在设备上新建、删除文件。
* 从PC本地上传文件到设备上，从设备上下载文件到PC本地。

## 使用约束

* 已通过USB或Wi-Fi连接设备。
* 不支持访问无权限目录，新建、删除、上传、下载文件受设备权限约束。
* 不支持文件拖拽。
* 不支持文件修改。如需对文件进行修改，需下载至PC，在本地修改后再上传至设备。
* 不支持上传文件或文件夹的快捷方式。
* 应用沙箱视图不支持模拟器设备。
* 应用需为debug应用才可使用沙箱视图查看文件结构、对应用沙箱内的文件/文件夹进行新建、删除、上传或下载操作。

## 操作步骤

1. 在菜单栏单击**View > Tool Windows > Device File Browser**，打开Device File Browser。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/vzJc7IgOSPyP_2rhwXaNkQ/zh-cn_image_0000002530913150.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=AF0604376F3FA85C8797FA6D32E7E297EBE91C75F517E490E5EC32C1A9ADD8C8)
2. 从下拉列表中选择设备（设备需已连接）。
3. 选择设备后，显示文件/文件夹列表，可进行以下操作：
   1. 右键单击目录或文件，进行新建/删除操作。
   2. 右键单击**Save As**将选定的文件或目录下载到PC上，右键单击**Upload**将PC上的文件上传到设备指定目录。

      如果需要查看数据库文件，可以通过该方式将数据库文件（路径举例：data > app > el2 > 100 > database >项目名称 > entry > rdb > 数据库文件）下载到PC上，再通过其他工具进行可视化查看。

      说明

      从DevEco Studio 6.0.0 Beta2版本开始，支持使用快捷键**Ctrl或Shift+鼠标左键**（macOS为**Command或Shift+鼠标左键**），选中多个文件或目录下载到本地计算机。
   3. 焦点在Device File Browser框中，输入字母可以快速进行搜索。
   4. 双击某个文件可在DevEco Studio中将其打开。打开文件会默认下载文件到临时目录（%USER%\AppData\Local\Huawei\DevEcoStudio{版本号}\device-file-browser\{设备名称}\{设备上的文件路径}），关闭文件后，临时文件将被删除。
   5. 如果通过命令行方式上传文件到设备后，需要右键对应文件夹，选择**Synchronize**后才可以在Device File Browser窗口中显示该文件。

## 可访问目录

Device File Browser可访问的文件夹有五种类型：[应用沙箱目录](app-sandbox-directory.md)、一般暂存区目录、日志目录、设备公共目录、媒体库目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/uLIIND3hRGOy75H6tK8nyA/zh-cn_image_0000002530913138.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=414D6190E28CABF0743DC6676D2EA4500BB2D17850033213EC235E0847C41A65)

### 应用沙箱目录

此目录用于存放应用自身相关的数据、资源文件等，有两种访问方式。

* **普通文件视图**

  普通文件视图将按照设备的真实物理路径显示当前设备上的文件结构。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/thzZ9lPPRYODtXJRZRLrWQ/zh-cn_image_0000002561833091.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=FFC82B21EE40CD1B6DB43E7448F3FFEED98A57835CDC6D5A917C5B1D3A38F1C0)

  应用沙箱在设备上的物理路径位于/data/app/{el1，el2}/100/{base，database}/{packageName}路径下。

  在普通文件视图下，el1目录下的文件仅具备查看文件目录结构的权限，无法执行新建、删除、上传或下载操作；与el1相比，el2目录下的文件允许下载，但其他操作仍无权限执行。

* **应用沙箱视图**

  应用沙箱视图会展示所有debug类型的应用，按照应用的沙箱文件路径显示应用的沙箱文件结构。

  从DevEco Studio 6.1.0 Beta1版本开始，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/BBA0iyP9QgOkuH43TkyAkw/zh-cn_image_0000002561833111.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=11D1D61683131487C6210883F4208421CD0777B982791532477D9B00029FFC8D)即可过滤出当前工程对应的沙箱目录。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/ICN0orXFS6O0r5sy3YJCyQ/zh-cn_image_0000002561833087.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=BFEE52217C6C489918706BFECADDEAB5E7982D95BEB95D62EF3339979187643F)

  API 15以下的版本，当需要以沙箱视图查看应用的文件结构时，需在module.json5文件内配置ohos.permission.INTERNET开启网络权限，卸载并重新安装应用。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/aK085iOVSZixSuEJWE68SA/zh-cn_image_0000002561833115.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=EC4BA85354DDC5C6EB44C26DB2A0D7EA4B47700F387AC1FAB9EBFB965FD71FE4)

  对应于物理路径，沙箱路径为/data/storage/{el1，el2}/{base，database}。

  在应用沙箱视图下，el1和el2目录下的文件均支持新建、删除、上传、下载操作。

  从DevEco Studio 6.0.1 Release版本开始，新增云空间目录/data/storage/el2/cloud，具体使用方式请参考[端云文件协同](cloud-sync-file-overview.md)。

### 一般暂存区目录

一般暂存区目录位于/data/local/tmp/路径下，支持新建、删除、上传、下载操作，在DevEco Studio进行调试、测试等操作时，将在此目录下生成相关的文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/UzTiQaroQAG7IYImE6xmPg/zh-cn_image_0000002530913140.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=3547E3704C7555287F482B46486E1F3DF5CE920800AB50E8A47EB1A2F1190B64)

### 日志目录

应用运行时的日志通过HiLog工具实时输出，此工具的输出缓存区一般为256K，超出大小的历史日志将会以压缩包的形式保存在/data/log/hilog/路径下。

当需要查看历史日志时，需要将此目录下的压缩包文件和数据字典压缩包文件hilog\_dict.XXX.zip下载到本地计算机，然后使用[hilogtool工具](hilog-tool.md)解析出对应的日志原文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/s75kJa0NSuiSfxFFrEWxOA/zh-cn_image_0000002561833097.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=547AD05D14E8179010060A8DB2803403EE89763703D94A9D86A648BD539CE898)

### 公共目录

用户的桌面、文档、下载等公共目录位于/storage/media/100/local/files/Docs路径下，支持删除、上传、下载操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/aNDi5b1GTRK9TwCM2rhiKQ/zh-cn_image_0000002530753196.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=A4462711477B992307591734E95C630FF3EFD87C0C63F0A57C97374D7E4ADF08)

### 媒体库目录

从API 22开始，新增媒体库目录/mnt/data/100/media\_fuse/Photo，原有的/storage/media/100/local/files/Photo目录变为一个链接，点击后跳转到/mnt/data/100/media\_fuse/Photo，支持通过该目录上传、下载、删除图片、视频文件。

说明

Wearable设备不支持媒体库目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/yNHlBTyASZCaUoxs5yc7XQ/zh-cn_image_0000002530753182.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=9A036400A2C8E9C9B295493C305CBFAEC84511E6B11ED3CFB1AF90942E6A3B4E)

## 特殊目录

设备上存在两个特殊的目录：faultlog目录和图库目录，这两个目录有下载权限，但没有查看权限，Device File Browser中无法显示这两个目录，但其下的文件可以通过hdc命令查看并导出。

### faultlog目录

当应用崩溃时，会在/data/log/faultlog/faultlogger路径下生成相关的崩溃日志，可通过以下方式查询并下载日志。

1. 执行命令，查询此路径下的崩溃日志文件列表。
   * 设备版本低于5.1.0.54时，执行以下命令。

     ```
     1. hdc shell hidumper -s 1201 -a "-p Faultlogger"
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/6OxrcL2BTeSh4Kk4snRLSQ/zh-cn_image_0000002530913152.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=DD84112160ECD442CA3E809C85A2230D0BD1BA16C1982441E328C2EE6BA08591)
   * 设备版本为5.1.0.54及以上时，崩溃日志文件名时间戳新增了毫秒级信息，执行以下命令。

     ```
     1. hdc shell hidumper -s 1201 -a "-p Faultlogger %s -LogSuffixWithMs"
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/Pva-lcpxTNGpmobIrbgJrg/zh-cn_image_0000002530913178.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=E264DABB2303172B9C1285AB945BD633257E5758C704CD8CD87741114F1FB853)
2. 执行命令，查看指定的崩溃日志文件的内容。

   ```
   1. hdc shell hidumper -s 1201 -a "-p Faultlogger -f {filename}"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/NVgROVhbT4CNi14TtyowXA/zh-cn_image_0000002530913164.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=B73CBC9130C677ED461C1B4C26DCC0C6016D426241A395E9C29E9B97D05A1BC9)
3. 执行命令，将文件保存到本地计算机指定的路径下。

   ```
   1. hdc file recv /data/log/faultlog/faultlogger/{filename} {path}
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/x_JxH9J7RVKrr_TNlQGMCw/zh-cn_image_0000002530913142.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=CD4AF6227FE0B2A85B71CBB7FFB36FCE3E979194EA2D1A6188386997A29F8EDB)

### 图库目录

图库目录中保存了录屏工具、照相机等系统应用生成的图片、视频文件，可通过以下方式将文件下载到本地计算机。

1. 在图库中查看文件名及后缀，例如a.mp4。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/L1f4Xm2-SkqQ8MA-o4fJjw/zh-cn_image_0000002561753101.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=BFD692D6127C7CA167EA4513A18C0E4FB9E50D3C37D3235ADE65FC69CF04AF9E)
2. 查询文件路径，记录为{FilePath}。

   ```
   1. hdc shell mediatool query a.mp4 -u
   ```

   * 如果查询的结果中包含uri字段，则返回值第三行对应的文件路径不允许直接下载。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/qG-Eai0RQlqYd1w9-kCwMw/zh-cn_image_0000002530913182.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=543C0931F10CC989B2168826B08E6FEFC14079891113A362C013B88D4CC7539A)

     需要再执行如下命令，指定该uri，将文件复制到有下载权限的路径中（如/data/local/tmp）。

     ```
     1. hdc shell mediatool recv file://media/Photo/2/VID_1744944984_000/a.mp4 /data/local/tmp
     ```

     命令返回值第二行即为文件路径{FilePath}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/zkipzqKmQsKF5_0lHP0Ckg/zh-cn_image_0000002561833071.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=5BFACE51FB5ED43682F936F671A7D5D14E044BBC043247F90157B4A980546A08)
   * 如果查询结果不包含uri字段，则返回值第二行即为文件路径{FilePath}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/795tyGlGR6asIBEzsc3xTw/zh-cn_image_0000002561753103.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=7F5E80FD7E3FA92D234449D4824614DC230BB17781B8C2B92A24AE3ED3DCF4C6)
3. 指定上一个步骤中获取到的文件路径{FilePath}，下载文件到本地。

   ```
   1. hdc file recv {FilePath} .\
   ```

## 命令行方式访问应用沙箱

可以通过命令行的方式访问debug应用的[沙箱目录](app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系)。

* 从API 15开始，支持通过hdc工具访问debug应用的沙箱目录，推荐开发者使用此种方式。更多关于命令行工具hdc的说明请参见[hdc工具使用指导](hdc.md)。
  1. 在设备侧启动应用。

     ```
     1. $ hdc shell aa start -a {abilityName} -b {bundleName}
     2. start ability successfully.
     ```

     + abilityName：应用的ability名称。
     + bundleName：调试应用包名。
  2. 通过命令访问应用沙箱目录，创建目录文件，删除指定目录下的文件。

     ```
     1. $ hdc shell -b {bundleName} ls -lZ -A "./data/storage/el2/base"          // 查看应用沙箱下/el2/base目录文件（返回文件全部信息）
     2. $ hdc shell -b {bundleName} ls -A "./data/storage/el2/base"          // 查看应用沙箱下/el2/base目录文件（仅返回文件名）
     3. $ hdc shell -b {bundleName} mkdir -p "./data/storage/el2/base/test"     // 在应用沙箱下/el2/base目录下创建test目录
     4. $ hdc shell -b {bundleName} rm -r "./data/storage/el2/base/test.txt"  // 在应用沙箱下/el2/base目录下删除test.txt文件
     5. $ hdc shell -b {bundleName} rm -r "./data/storage/el2/base/test"      // 在应用沙箱下/el2/base目录下删除test目录
     ```
  3. 通过命令往应用沙箱目录中发送文件，从沙箱目录中下载文件到本地计算机。

     ```
     1. $ hdc file send -b {bundleName} "D:\test.txt" "./data/storage/el2/base"    // 发送文件到设备沙箱目录/el2/base
     2. $ hdc file recv -b {bundleName} "./data/storage/el2/base/test.txt" D:\  // 从设备沙箱目录/el2/base下载文件到本地计算机
     ```
* API 15以下的版本，通过以下方式访问debug应用的沙箱目录。
  1. 在工程主模块下的module.json5文件下增加网络权限。

     ```
     1. "requestPermissions": [
     2. {"name":  "ohos.permission.INTERNET"}
     3. ]
     ```
  2. 在设备侧(hdc shell)启动应用的bftpd服务，并查询端口号是否启动成功。

     ```
     1. $ aa process -b {bundleName} -a {abilityName} -p "/system/bin/bftpd -D -p {port}"  -S
     2. start native process successfully.
     3. $ ps -ef | grep bftpd
     4. 20020143     12254   613 0 11:52:53 ?     00:00:00 bftpd -D -p 9021   // 对应端口号的bftpd服务启动成功
     5. shell        13035 11901 10 11:54:44 ?    00:00:00 grep bftpd
     ```

     + bundleName：调试应用包名。
     + abilityName：应用的ability名称。
     + port：可用端口号。
  3. 通过命令访问应用沙箱目录，创建目录文件，删除指定目录下的文件。

     ```
     1. $ ftpget -p {port} -P guest -u anonymous localhost -l /data/storage/el2/base           // 查看应用沙箱下/el2/base目录文件（返回文件全部信息）
     2. $ ftpget -p {port} -P guest -u anonymous localhost -L /data/storage/el2/base           // 查看应用沙箱下/el2/base目录文件（仅返回文件名）
     3. $ ftpget -p {port} -P guest -u anonymous localhost -M /data/storage/el2/base/test      // 在应用沙箱下/el2/base目录下创建test目录
     4. $ ftpget -p {port} -P guest -u anonymous localhost -d /data/storage/el2/base/test.txt  // 在应用沙箱下/el2/base目录下删除test.txt文件
     5. $ ftpget -p {port} -P guest -u anonymous localhost -D /data/storage/el2/base/test      // 在应用沙箱下/el2/base目录下删除test目录（仅支持删除空目录）
     ```
  4. 通过命令往应用沙箱目录中发送文件，从沙箱目录中下载文件到本地。(/data/local/tmp/作为中转目录)

     ```
     1. $ hdc file send test.txt /data/local/tmp/test.txt    // 先发送文件到设备data/local/tmp目录
     2. $ ftpget -p {port} -P guest -u anonymous localhost -s /data/local/tmp/test.txt /data/storage/el2/base/test.txt  // 再推送到应用沙箱目录
     3. $ ftpget -p {port} -P guest -u anonymous localhost -g /data/local/tmp/test.txt /data/storage/el2/base/test.txt  // 先下载到设备的data/local/tmp目录
     4. $ hdc file recv /data/local/tmp/test.txt test.txt  // 再从设备中获取
     ```

## 常见问题

沙箱视图下，打开沙箱文件夹时报错：[Fail][E003001] Invalid bundle name。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/vAPXkqPBT8ymbj9k0k6-xg/zh-cn_image_0000002530913154.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=15BA12B491C181C024989BB216A690AEAEF8A4DD2DB35398AF1A10D43EFA0E0A)

可能是以下原因：

1. 应用不是debug应用，无法查看沙箱文件。
2. 应用安装后，未运行过或重启了设备，导致应用沙箱暂未挂载。此场景下先手动运行一遍应用，然后在报错目录右键点击**Synchronize**即可打开目录。
