---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-device-file-explorer
title: 访问设备文件
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 访问设备文件
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b68590747627629a5514bd472453abac68ed17cea5c780e75a6a39e7c2472486
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
* 应用沙箱视图不支持模拟器设备。
* 应用需为debug应用才可使用沙箱视图查看文件结构、对应用沙箱内的文件/文件夹进行新建、删除、上传或下载操作。

## 操作步骤

1. 在菜单栏单击**View > Tool Windows > Device File Browser**，打开Device File Browser。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/OaLUKsMfQ62LZJEiRdkKkQ/zh-cn_image_0000002808766447.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC1A116CE3873D28091D22A63C68F58C5930062E1E803E0E734F37B754761BDE)
2. 从下拉列表中选择设备（设备需已连接）。
3. 选择设备后，显示文件/文件夹列表，可进行以下操作：
   1. 右键单击目录或文件，进行新建/删除操作。
   2. 右键单击**Save As**将选定的文件或目录下载到PC上，右键单击**Upload**将PC上的文件上传到设备指定目录。

      如果需要查看数据库文件，可以通过该方式将数据库文件（路径举例：data > app > el2 > 100 > database >项目名称 > entry > rdb > 数据库文件）下载到PC上，再通过其他工具进行可视化查看。

      **说明** 

      从DevEco Studio 6.0.0 Beta2版本开始，支持使用快捷键**Ctrl或Shift+鼠标左键**（macOS为**Command或Shift+鼠标左键**），选中多个文件/目录下载到本地计算机；从DevEco Studio 6.0.2 Beta1版本开始，支持使用快捷键选中多个文件/目录删除。
   3. 在搜索框中输入关键字，可以对目录和文件进行搜索。
   4. 双击某个文件可在DevEco Studio中将其打开。打开文件会默认下载文件到临时目录（%USER%\AppData\Local\Huawei\DevEcoStudio{版本号}\device-file-browser\{设备名称}\{设备上的文件路径}），关闭文件后，临时文件将被删除。
   5. 如果通过命令行方式上传文件到设备后，需要右键对应文件夹，选择**Synchronize**后才可以在Device File Browser窗口中显示该文件。

## 可访问目录

Device File Browser可访问的文件夹有五种类型：[应用沙箱目录](app-sandbox-directory.md)、一般暂存区目录、日志目录、设备公共目录、媒体库目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/ilcinlrPTtO8QFYsrBH4Ng/zh-cn_image_0000002808886525.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CB8101DD66B8801B7EFA8F6850658A66416458EC82145494E516FE6FBD93757)

### 应用沙箱目录

此目录用于存放应用自身相关的数据、资源文件等，有两种访问方式。

* **普通文件视图**

  普通文件视图将按照设备的真实物理路径显示当前设备上的文件结构。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/8ObuJ_T2RqmMVQ1M8_TCLg/zh-cn_image_0000002808886535.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=A317C08EACAB7D560B146234D0C640E4E749B3D747A3EFE729D4F9D36F0D154B)

  应用沙箱在设备上的物理路径位于/data/app/{el1，el2}/100/{base，database}/{packageName}路径下。

  在普通文件视图下，el1目录下的文件仅具备查看文件目录结构的权限，无法执行新建、删除、上传或下载操作；与el1相比，el2目录下的文件允许下载，但其他操作仍无权限执行。

* **应用沙箱视图**

  应用沙箱视图会展示所有debug类型的应用，按照应用的沙箱文件路径显示应用的沙箱文件结构。

  从DevEco Studio 6.1.0 Beta1版本开始，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/D5SBQmpOQwCPYJPQ8OTi6g/zh-cn_image_0000002779406902.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=B510EC4E90BAD44B483F50E6B082C3CF9B309121245A6720646DCB56363BE7A0)即可过滤出当前工程对应的沙箱目录。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/bzpTwt9wRLy_B5BN5bTR2w/zh-cn_image_0000002808886533.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE15BEEB5394EE49DC1C0A5A5DFFD7890CCEA5E09A6A7EE3C2B5E893C5F8DCAC)

  API 15以下的版本，当需要以沙箱视图查看应用的文件结构时，需在module.json5文件内配置ohos.permission.INTERNET开启网络权限，卸载并重新安装应用。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/4eHjJL2XS-SDU7lpQJiQjw/zh-cn_image_0000002779406904.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6BF147713BD2C2143F821C9BC4D2BFF1D381EB55CCEC5E5084CDBF566E515E8)

  对应于物理路径，沙箱路径为/data/storage/{el1，el2}/{base，database}。

  在应用沙箱视图下，el1和el2目录下的文件均支持新建、删除、上传、下载操作。

  从DevEco Studio 6.0.1 Release版本开始，新增云空间目录/data/storage/el2/cloud，具体使用方式请参考[端云文件协同](cloud-sync-file-overview.md)。

### 一般暂存区目录

一般暂存区目录位于/data/local/tmp/路径下，支持新建、删除、上传、下载操作，在DevEco Studio进行调试、测试等操作时，将在此目录下生成相关的文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/7N7qsQ3hQC6I3gEUMw1x0g/zh-cn_image_0000002779566862.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=EECF7E588ABE610FF19F02E5E803F341846DF8D401D098B0024869E6A170A1C4)

### 日志目录

应用运行时的日志通过HiLog工具实时输出，此工具的输出缓存区一般为256K，超出大小的历史日志将会以压缩包的形式保存在/data/log/hilog/路径下。

当需要查看历史日志时，需要将此目录下的压缩包文件和数据字典压缩包文件hilog\_dict.XXX.zip下载到本地计算机，然后使用[hilogtool工具](hilog-tool.md)解析出对应的日志原文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/HWkZavWjRcyK1200CC-qlg/zh-cn_image_0000002808766457.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=50112E50E483F3C689BD6AD8DC49F41B15717F91E3D7147CE76A17A6A7F25B1D)

### 公共目录

用户的桌面、文档、下载等公共目录位于/storage/media/100/local/files/Docs路径下，支持删除、上传、下载操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/jinaC-NtRHiHd-pb65i_Tw/zh-cn_image_0000002808886543.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=541573A8C6580552E89D4723C951818F64A8A8AB3527E408592C1523B34E7012)

### 媒体库目录

从API 22开始，新增媒体库目录/mnt/data/100/media\_fuse/Photo，原有的/storage/media/100/local/files/Photo目录变为一个链接，点击后跳转到/mnt/data/100/media\_fuse/Photo，支持通过该目录上传、下载、删除图片、视频文件。

**说明** 

Wearable设备不支持媒体库目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/23O0RKBfQ9-qwTj1sAA57w/zh-cn_image_0000002779566876.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=6074C226972DA5AE56C923B0A209A5A31730D572B890B0D721B2358BF39D9912)

## 特殊目录

设备上存在两个特殊的目录：faultlog目录和图库目录，这两个目录有下载权限，但没有查看权限，Device File Browser中无法显示这两个目录，但其下的文件可以通过hdc命令查看并导出。

### faultlog目录

当应用崩溃时，会在/data/log/faultlog/faultlogger路径下生成相关的崩溃日志，可通过以下方式查询并下载日志。

1. 执行命令，查询此路径下的崩溃日志文件列表。
   * 设备版本低于5.1.0.54时，执行以下命令。

     ```bash
     hdc shell hidumper -s 1201 -a "-p Faultlogger"
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/rvz_4b_vSR-xe3rQVJ9-gg/zh-cn_image_0000002808886529.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E2ADD86DE23BF27F06954127E35DAB3F2454284BF4E4333E997F5EFBC70F758)
   * 设备版本为5.1.0.54及以上时，崩溃日志文件名时间戳新增了毫秒级信息，执行以下命令。

     ```bash
     hdc shell hidumper -s 1201 -a "-p Faultlogger %s -LogSuffixWithMs"
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/XrOTp1fASLWlhssoDZF2jQ/zh-cn_image_0000002808886541.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C8D07D2DB0B837C1F8196F71D49C329CAE168737A6602132F5F13CD51F0AEBE)
2. 执行命令，查看指定的崩溃日志文件的内容。

   ```bash
   hdc shell hidumper -s 1201 -a "-p Faultlogger -f {filename}"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/ounvd3UyReShGybxOILwAg/zh-cn_image_0000002808766453.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9192B349FDD0235127936FD96249D5F5F90CA7985A581B065F9F5D5C26F45CD)
3. 执行命令，将文件保存到本地计算机指定的路径下。

   ```bash
   hdc file recv /data/log/faultlog/faultlogger/{filename} {path}
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/LC_qedGRR4Oq7X2RKxj4ew/zh-cn_image_0000002808766445.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D2395F6FD53BB875FE37021E6CD5679F1D059BD4804329C3F9DAA7FB4C2CE1E)

### 图库目录

图库目录中保存了录屏工具、照相机等系统应用生成的图片、视频文件，可通过以下方式将文件下载到本地计算机。

1. 在图库中查看文件名及后缀，例如a.mp4。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Nj2jnPyHR7Spzg5cXXMniA/zh-cn_image_0000002808886531.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=88704C5AA7A8D85062D50BB4AD195E73BDC373F4D4F3BC75D3EA8031610FC097)
2. 查询文件路径，记录为{FilePath}。

   ```bash
   hdc shell mediatool query a.mp4 -u
   ```

   * 如果查询的结果中包含uri字段，则返回值第三行对应的文件路径不允许直接下载。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/ianauAqiTsWWQZGHoqyYxw/zh-cn_image_0000002808766461.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0A7F2E18A1C2143AEAB170B498EC6ED518291D32990D0E2267F366F44B0099A)

     需要再执行如下命令，指定该uri，将文件复制到有下载权限的路径中（如/data/local/tmp）。

     ```bash
     hdc shell mediatool recv file://media/Photo/2/VID_1744944984_000/a.mp4 /data/local/tmp
     ```

     命令返回值第二行即为文件路径{FilePath}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/P8u9V6tRT_-DGRCqWgkjXw/zh-cn_image_0000002808886527.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=F17284B9347DD58E7E74DDB341A4295F8DF627795DE1CD6D55F6A874A66C030B)
   * 如果查询结果不包含uri字段，则返回值第二行即为文件路径{FilePath}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/xYIOOmPdRPmC3fGVjW8ibQ/zh-cn_image_0000002808766451.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=7AE534F6F9D71D7AF17A5B99997EAC2028CC11D54ABDE6D62B570765B58644A5)
3. 指定上一个步骤中获取到的文件路径{FilePath}，下载文件到本地。

   ```bash
   hdc file recv {FilePath} .\
   ```

## 命令行方式访问应用沙箱

可以通过命令行的方式访问debug应用的[沙箱目录](app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系)。

* 从API 15开始，支持通过hdc工具访问debug应用的沙箱目录，推荐开发者使用此种方式。更多关于命令行工具hdc的说明请参见[hdc工具使用指导](hdc.md)。
  1. 在设备侧启动应用。

     ```bash
     $ hdc shell aa start -a {abilityName} -b {bundleName}
     start ability successfully.
     ```

     + abilityName：应用的ability名称。
     + bundleName：调试应用包名。
  2. 通过命令访问应用沙箱目录，创建目录文件，删除指定目录下的文件。

     ```bash
     $ hdc shell -b {bundleName} ls -lZ -A "./data/storage/el2/base"          // 查看应用沙箱下/el2/base目录文件（返回文件全部信息）
     $ hdc shell -b {bundleName} ls -A "./data/storage/el2/base"          // 查看应用沙箱下/el2/base目录文件（仅返回文件名）
     $ hdc shell -b {bundleName} mkdir -p "./data/storage/el2/base/test"     // 在应用沙箱下/el2/base目录下创建test目录
     $ hdc shell -b {bundleName} rm -r "./data/storage/el2/base/test.txt"  // 在应用沙箱下/el2/base目录下删除test.txt文件
     $ hdc shell -b {bundleName} rm -r "./data/storage/el2/base/test"      // 在应用沙箱下/el2/base目录下删除test目录
     ```
  3. 通过命令往应用沙箱目录中发送文件，从沙箱目录中下载文件到本地计算机。

     ```bash
     $ hdc file send -b {bundleName} "D:\test.txt" "./data/storage/el2/base"    // 发送文件到设备沙箱目录/el2/base
     $ hdc file recv -b {bundleName} "./data/storage/el2/base/test.txt" D:\  // 从设备沙箱目录/el2/base下载文件到本地计算机
     ```
* API 22及以下的版本，支持以下方式访问debug应用的沙箱目录。从API 23开始，此方式无法使用，请通过上文的hdc工具进行访问。
  1. 在工程主模块下的module.json5文件下增加网络权限。

     ```json5
     "requestPermissions": [
       {"name":  "ohos.permission.INTERNET"}
     ]
     ```
  2. 在设备侧(hdc shell)启动应用的bftpd服务，并查询端口号是否启动成功。

     ```bash
     $ aa process -b {bundleName} -a {abilityName} -p "/system/bin/bftpd -D -p {port}"  -S
     start native process successfully.
     $ ps -ef | grep bftpd
     20020143     12254   613 0 11:52:53 ?     00:00:00 bftpd -D -p 9021   // 对应端口号的bftpd服务启动成功
     shell        13035 11901 10 11:54:44 ?    00:00:00 grep bftpd
     ```

     + bundleName：调试应用包名。
     + abilityName：应用的ability名称。
     + port：可用端口号。
  3. 通过命令访问应用沙箱目录，创建目录文件，删除指定目录下的文件。

     ```bash
     $ ftpget -p {port} -P guest -u anonymous localhost -l /data/storage/el2/base           // 查看应用沙箱下/el2/base目录文件（返回文件全部信息）
     $ ftpget -p {port} -P guest -u anonymous localhost -L /data/storage/el2/base           // 查看应用沙箱下/el2/base目录文件（仅返回文件名）
     $ ftpget -p {port} -P guest -u anonymous localhost -M /data/storage/el2/base/test      // 在应用沙箱下/el2/base目录下创建test目录
     $ ftpget -p {port} -P guest -u anonymous localhost -d /data/storage/el2/base/test.txt  // 在应用沙箱下/el2/base目录下删除test.txt文件
     $ ftpget -p {port} -P guest -u anonymous localhost -D /data/storage/el2/base/test      // 在应用沙箱下/el2/base目录下删除test目录（仅支持删除空目录）
     ```
  4. 通过命令往应用沙箱目录中发送文件，从沙箱目录中下载文件到本地。(/data/local/tmp/作为中转目录)

     ```bash
     $ hdc file send test.txt /data/local/tmp/test.txt    // 先发送文件到设备data/local/tmp目录
     $ ftpget -p {port} -P guest -u anonymous localhost -s /data/local/tmp/test.txt /data/storage/el2/base/test.txt  // 再推送到应用沙箱目录
     $ ftpget -p {port} -P guest -u anonymous localhost -g /data/local/tmp/test.txt /data/storage/el2/base/test.txt  // 先下载到设备的data/local/tmp目录
     $ hdc file recv /data/local/tmp/test.txt test.txt  // 再从设备中获取
     ```

## 常见问题

沙箱视图下，打开沙箱文件夹时报错：[Fail][E003001] Invalid bundle name。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/En18O9cIQJmIO5F-c2Qz6g/zh-cn_image_0000002808766449.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=77318E44941E9F2C0882D4EBF391A48D0873B7825CEC66D38ED10AC3120109E8)

可能是以下原因：

1. 应用不是debug应用，无法查看沙箱文件。
2. 应用安装后，未运行过或重启了设备，导致应用沙箱暂未挂载。此场景下先手动运行一遍应用，然后在报错目录右键点击**Synchronize**即可打开目录。
