---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screen-recording
title: 录屏
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 录屏
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d0bfe45c483d8105592ecf44c0ffbfc627aef15e059ba599ccbf4ccf440831dd
---

在应用开发过程中，可以使用录屏功能录制应用的运行状态，并通过录屏文件向他人展示正在开发的应用的各种功能效果。

## 使用约束

* 如果设置了锁屏密码，录屏开始前请解锁设备屏幕，并且录屏时需要保持设备的屏幕解锁状态，锁屏会导致录屏应用无法正常拉起或退出。
* 穿戴设备、模拟器不支持录屏。

## 通过DevEco Studio录屏

1. 连接真机设备，并在其中运行应用。
2. 在DevEco Studio底部切换到**Log**页签。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/NnlP6JovRWCmkH-Toe74PA/zh-cn_image_0000002779407448.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F3F937DE40B9679C3AB6CFA46AE25279B461B872E93AE11616F51FA984461C2 "点击放大")，即可开始录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/ej5IIg_XRBmmkuzDU5htXA/zh-cn_image_0000002779567430.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=6ED4864C6D926661ABDE82929BBB3434C7305A79D00BC14008AF84440F36401B)
4. 录屏时，需要先选择录屏文件的保存路径，开发者可使用默认路径或[设置自定义路径](ide-screen-recording.md#section89111791511)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/EpQL638pQxqI-p7h8qEQjg/zh-cn_image_0000002779407454.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=164F9D8E687F20F8E3CD24EFB4113C415D2354E638D430A164837760A7685492)
5. 路径选择完毕后，点击**Start Recording**开始录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/zGVdaIEBSGa9voJgl0HxtA/zh-cn_image_0000002779407446.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC1C0EC44F68C0410B34C604AB78510E6F641FDD52B0B08BDD820F2443C32609 "点击放大")
6. 录制完操作流程之后，点击**Stop Recording**结束录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/9SzTkNFPRPOjChgjEFkk8g/zh-cn_image_0000002808766999.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB16B7BB666108EA7C98D1230DFE72BA47A6D1EBB20238BCCEF8328A0F774286 "点击放大")
7. 结束录屏后，录屏文件将会保存到之前选择的路径下，可以选择调用系统播放器播放视频文件或打开文件所在的文件夹。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/phHrQPMjQGC_MEwS7qR7Cw/zh-cn_image_0000002779407452.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC50BFFF951482E5165DFD981C79B3BF44C287E977F515378533E51C81AFC182 "点击放大")

## 设置录屏自定义路径

1. 点击DevEco Studio底部**Log**页签，选择**HiLog >** **Settings** **>** **Record Screen**选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/tkDupdePRoGiBalPehtGjw/zh-cn_image_0000002779567422.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=8315A4F30676E8BC88BDE2F73AEDA6A8E09838B8C2B2079064734822D9765A7B)
2. 在弹出的界面选择自定义路径，当设置好路径并勾选“Use the selected path and auto-generated file name as defaults and don't ask again”选项后，录屏时将自动使用此时设置的路径以及以录屏时的时间戳构造的文件名作为录屏文件的保存地址及文件名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/D_3P2Tc8Q8aiYNc0WnHUew/zh-cn_image_0000002808887081.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC0F993F16EE9A5849D144C714139E34DE196FBA7A2EA46C6472A7FFF65BABEB)

## 通过命令行方式录屏

hdc是可以用于调试的命令行工具，通过该工具可以实现录屏功能。更多关于命令行工具hdc的说明请参见[hdc工具使用指导](hdc.md)。

1. 启动录屏。

   ```bash
   hdc shell aa start -b com.huawei.hmos.screenrecorder -a com.huawei.hmos.screenrecorder.ServiceExtAbility --ps "CustomizedFileName" "test.mp4"   // 指定录屏文件名称为test.mp4
   ```
2. 停止录屏。

   ```bash
   hdc shell aa start -b com.huawei.hmos.screenrecorder -a com.huawei.hmos.screenrecorder.ServiceExtAbility
   ```
3. 获取录屏文件位置，记录为{RecordFile}。

   ```bash
   hdc shell mediatool query test.mp4 -u
   ```

   * 如果查询的结果中包含uri字段，则返回值第三行对应的录屏文件路径不允许直接下载。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/Rwe78GFrTPixOtl-GpGarQ/zh-cn_image_0000002808767007.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=C17AFB697E73D7056EBCB24AA8648801F0EAB9852B55891D1DDFAC9080EDFFA3)

     需要再执行如下命令，指定该uri，将录屏文件复制到有下载权限的路径中（如/data/local/tmp）。

     ```bash
     hdc shell mediatool recv "file://media/Photo/2/VID_1736853237_001/test.mp4" /data/local/tmp
     ```

     命令返回值第二行即为录屏文件路径{RecordFile}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/obqN2qBxTWqT_c6TrRP9SQ/zh-cn_image_0000002779567432.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=916E36734FAE81B6F0DA19E3143A07E58AA0C16DDBEA1539E4B26B1DBA4691AE)
   * 如果查询结果不包含uri字段，则返回值第二行即为录屏文件路径{RecordFile}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/PFVRVNlWTm2ijTkyVkTS2w/zh-cn_image_0000002779567428.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=E920D5477C3AE64F24E713741A459A98BFF570F716771A9EC82C3E567F31292F)
4. 指定上一个步骤中获取到的录屏文件路径{RecordFile}，下载录屏文件到本地。

   ```bash
   hdc file recv {RecordFile} d:\test.mp4
   ```
