---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screen-recording
title: 录屏
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 录屏
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:39+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:189f869e7f15e861e2bdfe808eaea2ebc2d060f95704e3107f29d606a8b4056c
---

在应用开发过程中，可以使用录屏功能录制应用的运行状态，并通过录屏文件向他人展示正在开发的应用的各种功能效果。

## 使用约束

* 如果设置了锁屏密码，录屏开始前请解锁设备屏幕，并且录屏时需要保持设备的屏幕解锁状态，锁屏会导致录屏应用无法正常拉起或退出。
* 穿戴设备、模拟器不支持录屏。

## 通过DevEco Studio录屏

1. 连接真机设备，并在其中运行应用。
2. 在DevEco Studio底部切换到**Log**页签。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/GH11yaDwQAGYmhdvZiXP5A/zh-cn_image_0000002779407448.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD4466D73F48293C664E3878B62B5AA388F8AE696817415D66624EA1C10F0002 "点击放大")，即可开始录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/BsPHOXaoT9euH1OVPsAPBQ/zh-cn_image_0000002779567430.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=60FEB435FDCB658A36C1C65EB030523CF09C032AE80E95B43D85E3EA65D63A24)
4. 录屏时，需要先选择录屏文件的保存路径，开发者可使用默认路径或[设置自定义路径](ide-screen-recording.md#section89111791511)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/ghE_v79STzaapdGG5c-VnA/zh-cn_image_0000002779407454.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=B252E4BFFDEDF3F9BFCA14859A86F170805CCDE1320EFBA3146BBE6F032C5598)
5. 路径选择完毕后，点击**Start Recording**开始录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/WApOwY98SBe7uA_PQ8EA6w/zh-cn_image_0000002779407446.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=38F00F4A1E8A7345C67CB4EDBAB1DB5F221BBE76DB36B64A6F3991E4FF752405 "点击放大")
6. 录制完操作流程之后，点击**Stop Recording**结束录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/nbMvbIDcT8qetBYuSW-qlg/zh-cn_image_0000002808766999.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=91FC2E29234BC1E3CB828C25B9B445F67183FBA73D708FF471FCFCB767D76ACF "点击放大")
7. 结束录屏后，录屏文件将会保存到之前选择的路径下，可以选择调用系统播放器播放视频文件或打开文件所在的文件夹。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/CNvJ5_mDTeSN6JVIqGb-JA/zh-cn_image_0000002779407452.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E480EBC872BF9E4C96B31EB997AC1B43E70FC031386981072151E71F6B6F141 "点击放大")

## 设置录屏自定义路径

1. 点击DevEco Studio底部**Log**页签，选择**HiLog >** **Settings** **>** **Record Screen**选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/rR7oQnXRTcaaq8qBawY0Zw/zh-cn_image_0000002779567422.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=1920413B30FAEBDB1D82797E9336889277FAA3E3748D2C6B38F4D18BBBA244D3)
2. 在弹出的界面选择自定义路径，当设置好路径并勾选“Use the selected path and auto-generated file name as defaults and don't ask again”选项后，录屏时将自动使用此时设置的路径以及以录屏时的时间戳构造的文件名作为录屏文件的保存地址及文件名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/F38MC6keRjq2B6VA6DJZbA/zh-cn_image_0000002808887081.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B866E1153ABD04FF7949EE1D21FBD5465EC3DEBF383433B08F170E64715B068)

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/RZCRgOoqR_28f0had8ZawA/zh-cn_image_0000002808767007.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7131D3E0D9008231EBCAD1B17F2FA363C6B6CA01966108C343D6DF37DC558E5)

     需要再执行如下命令，指定该uri，将录屏文件复制到有下载权限的路径中（如/data/local/tmp）。

     ```bash
     hdc shell mediatool recv "file://media/Photo/2/VID_1736853237_001/test.mp4" /data/local/tmp
     ```

     命令返回值第二行即为录屏文件路径{RecordFile}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/rXiW8JU7SLOR088wSo1Qxw/zh-cn_image_0000002779567432.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=4AEE6A05031B6F8CC9A497340582AF571C73696A8F9761F07023C01935101031)
   * 如果查询结果不包含uri字段，则返回值第二行即为录屏文件路径{RecordFile}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/-Ut-ZnvrRTS79HMwxWDIYA/zh-cn_image_0000002779567428.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F476A70DB60F3FCB5F934E0EC1B18AAB7EBE19C9AAAF77371558623CCC48B01)
4. 指定上一个步骤中获取到的录屏文件路径{RecordFile}，下载录屏文件到本地。

   ```bash
   hdc file recv {RecordFile} d:\test.mp4
   ```
