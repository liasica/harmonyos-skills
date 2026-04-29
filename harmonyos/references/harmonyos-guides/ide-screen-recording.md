---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screen-recording
title: 录屏
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 录屏
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1d4d113ea166ff0fa1a1cdeb865cfe694615cb8c31407990233bc6a83c6af06a
---

在应用开发过程中，可以使用录屏功能录制应用的运行状态，并通过录屏文件向他人展示正在开发的应用的各种功能效果。

## 使用约束

* 如果设置了锁屏密码，录屏开始前请解锁设备屏幕，锁屏状态下录屏应用无法正常拉起。
* 如果设置了锁屏密码，录屏时请保持设备的屏幕解锁状态，若录屏过程中锁屏将导致录屏应用退出。
* 模拟器不支持录屏。

## 通过DevEco Studio录屏

1. 连接真机设备，并在其中运行应用。
2. 在DevEco Studio底部切换到**Log**页签。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/pKb6AmW5RwKzlfu0WQayfA/zh-cn_image_0000002530753756.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=862EDF259B8190F79FA8A2B907134951EB7C6FD1453F76242D0AB619C3B2AF71)，即可开始录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/0spYck97Tye2RY_o8claSA/zh-cn_image_0000002561753699.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=D06E4ABB957062D7C031D368ED48591D52E8ADA2E3D41DE24FC5FAE3832BDAA7)
4. 录屏时，需要先选择录屏文件的保存路径，开发者可使用默认路径或[设置自定义路径](ide-screen-recording.md#section89111791511)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/1WYnTcC3QH23RfdgvJKPQQ/zh-cn_image_0000002530753762.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=855445EC198B7E7B7F1CFB9E25001D6E436A48034FFB09CED8DFFAFC5BED063E)
5. 路径选择完毕后，点击**Start Recording**开始录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/mhH_3sfdRs2Es09IWBny8g/zh-cn_image_0000002561833673.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=CE707CB760FD82BD38E41F7DB6E796A94FD4FBD9204A3DC24DE9C349757B3ED0 "点击放大")
6. 录制完操作流程之后，点击**Stop Recording**结束录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/OQx7Jh_ORAmLzYZI64D88w/zh-cn_image_0000002561753689.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=2E2BC604FD60FB4C6F7A2D40BC855B250274841DC08ACD13F7DE473E5BE257C1 "点击放大")
7. 结束录屏后，录屏文件将会保存到之前选择的路径下，可以选择调用系统播放器播放视频文件或打开文件所在的文件夹。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/mjdgoX0VQOuyzbYREaLrfw/zh-cn_image_0000002530913752.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=945574D472B1B8069DD8C87EE5C07725211F2777BB03DFE62C5E36A4191D594D "点击放大")

## 设置录屏自定义路径

1. 点击DevEco Studio底部**Log**页签，选择**HiLog >** **Settings** **>** **Record Screen**选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/FCKLVm3wS4WG9_2fgHR5Ug/zh-cn_image_0000002561753693.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=A1D461E846438FBDFF36381D17D22CDB749A94DD89D3A4DBD52782E7730D1DBF)
2. 在弹出的界面选择自定义路径，当设置好路径并勾选“Use the selected path and auto-generated file name as defaults and don't ask again”选项后，录屏时将自动使用此时设置的路径以及以录屏时的时间戳构造的文件名作为录屏文件的保存地址及文件名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/P6AbxweCSPC-DYVVNLOicg/zh-cn_image_0000002530753752.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=6294DB5BE1433B80D5B32F04E12D6BD03617651894E043CA1DD29EC37956CC88)

## 通过命令行方式录屏

hdc是可以用于调试的命令行工具，通过该工具可以实现录屏功能。更多关于命令行工具hdc的说明请参见[hdc工具使用指导](hdc.md)。

1. 启动录屏。

   ```
   1. hdc shell aa start -b com.huawei.hmos.screenrecorder -a com.huawei.hmos.screenrecorder.ServiceExtAbility --ps "CustomizedFileName" "test.mp4"   // 指定录屏文件名称为test.mp4
   ```
2. 停止录屏。

   ```
   1. hdc shell aa start -b com.huawei.hmos.screenrecorder -a com.huawei.hmos.screenrecorder.ServiceExtAbility
   ```
3. 获取录屏文件位置，记录为{RecordFile}。

   ```
   1. hdc shell mediatool query test.mp4 -u
   ```

   * 如果查询的结果中包含uri字段，则返回值第三行对应的录屏文件路径不允许直接下载。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/3uQ2T5loTkS9892e6jd-Xg/zh-cn_image_0000002561753695.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=2AB4D48AB1F85140D6867DBDBB7D1D527954863359464B88F816548C875212C1)

     需要再执行如下命令，指定该uri，将录屏文件复制到有下载权限的路径中（如/data/local/tmp）。

     ```
     1. hdc shell mediatool recv "file://media/Photo/2/VID_1736853237_001/test.mp4" /data/local/tmp
     ```

     命令返回值第二行即为录屏文件路径{RecordFile}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/9sKx54_QQ4-EF8bqJ4Ee2Q/zh-cn_image_0000002530913756.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=79764503F2EFFACDDA25DC562E59C8F82700B3D2BC29DDA6B1BEBC4BC0926C6A)
   * 如果查询结果不包含uri字段，则返回值第二行即为录屏文件路径{RecordFile}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/z1E7Pk-uQqKjzmuUgDJI-w/zh-cn_image_0000002530753758.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=65D0927B61C9E953F1ED9E8121D7B6CCC93676D1C0A573C894925572705BC306)
4. 指定上一个步骤中获取到的录屏文件路径{RecordFile}，下载录屏文件到本地。

   ```
   1. hdc file recv {RecordFile} d:\test.mp4
   ```
