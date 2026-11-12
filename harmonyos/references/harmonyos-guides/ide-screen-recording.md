---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screen-recording
title: 录屏
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 录屏
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d6d4bc819a400f886a1ac1cd2bfbb17f55d746264270f63376d0ce0debb25b66
---

在应用开发过程中，可以使用录屏功能录制应用的运行状态，并通过录屏文件向他人展示正在开发的应用的各种功能效果。

## 使用约束

* 如果设置了锁屏密码，录屏开始前请解锁设备屏幕，并且录屏时需要保持设备的屏幕解锁状态，锁屏会导致录屏应用无法正常拉起或退出。
* 穿戴设备、模拟器不支持录屏。

## 通过DevEco Studio录屏

1. 连接真机设备，并在其中运行应用。
2. 在DevEco Studio底部切换到**Log**页签。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/P6s-D5WUSkaVKhP-DRzqSg/zh-cn_image_0000002779407448.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A5FA014082128A87BC28AA3D4D729B5F24FA0951E3E7FDAF6B4C662E8BE7DFE8 "点击放大")，即可开始录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/4Jfu8WAMT-KR1wqVhUJ6CQ/zh-cn_image_0000002779567430.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A5BF56E56561D0E6B385F9D04C5B9E3C4E56F2D1DAC4E26465230BF8E4E4FCEF)
4. 录屏时，需要先选择录屏文件的保存路径，开发者可使用默认路径或[设置自定义路径](ide-screen-recording.md#section89111791511)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/q5-oCMGPRLK61fcYLwqNZg/zh-cn_image_0000002779407454.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C2DF3F79560B190BAA756DAE8A92DE2A01165E63A2A90DE7C80B7C06D20EF41)
5. 路径选择完毕后，点击**Start Recording**开始录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/rbCoLC95TseWT-mZFGnq2w/zh-cn_image_0000002779407446.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=AEDE414F8BD832401AA17C0BFF025C4068F6DA2F55B58A3F3C51EB789A370809 "点击放大")
6. 录制完操作流程之后，点击**Stop Recording**结束录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/BtHKuJqgSHiRXNOqj0rjpg/zh-cn_image_0000002808766999.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E72AA9065E9BFE2136A51D7C236BDE9161213C3DEAA75957B42729193A34BE3A "点击放大")
7. 结束录屏后，录屏文件将会保存到之前选择的路径下，可以选择调用系统播放器播放视频文件或打开文件所在的文件夹。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/bVoHwbc0Q-Gm3t70yWJNgg/zh-cn_image_0000002779407452.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=ACA28E4AB7D4FF2AED7DB32FE9013F4A2E944780F5C450F7FB2B50124469B987 "点击放大")

## 设置录屏自定义路径

1. 点击DevEco Studio底部**Log**页签，选择**HiLog >** **Settings** **>** **Record Screen**选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/sz8KCrHfRcShvFgiecfwew/zh-cn_image_0000002779567422.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=62F99CC1D01A46436C4052D332049EDA4BF98370A71BAF162F91A641910D9162)
2. 在弹出的界面选择自定义路径，当设置好路径并勾选“Use the selected path and auto-generated file name as defaults and don't ask again”选项后，录屏时将自动使用此时设置的路径以及以录屏时的时间戳构造的文件名作为录屏文件的保存地址及文件名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/0OYzhRGRSYyaa9cpYhRd-A/zh-cn_image_0000002808887081.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6B2E98FA040053B62034806B5CE5BD0DE11CE6A6A37C8CB9D262243A4E12C9C)

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/o7GmGU5WQqisLitdeuIlSw/zh-cn_image_0000002808767007.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5F321D33EA47DE4070B66A05BA07DCDF6CB89E6FE6F69C5E6AD312D6F8EA4F3)

     需要再执行如下命令，指定该uri，将录屏文件复制到有下载权限的路径中（如/data/local/tmp）。

     ```bash
     hdc shell mediatool recv "file://media/Photo/2/VID_1736853237_001/test.mp4" /data/local/tmp
     ```

     命令返回值第二行即为录屏文件路径{RecordFile}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/T0cxH3tyQqaEIxy0n9-lIw/zh-cn_image_0000002779567432.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=88C3C00B312449F6A52C0D0B798C32D02AEA0307160619D609F2CFA223607554)
   * 如果查询结果不包含uri字段，则返回值第二行即为录屏文件路径{RecordFile}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/yxy7cu5yR8a3I5zsCVlt0Q/zh-cn_image_0000002779567428.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=777241458BC379359E897D89AD7BBFB52767FEF6DFD2336376B374ECA8B290DC)
4. 指定上一个步骤中获取到的录屏文件路径{RecordFile}，下载录屏文件到本地。

   ```bash
   hdc file recv {RecordFile} d:\test.mp4
   ```
