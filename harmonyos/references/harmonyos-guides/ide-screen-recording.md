---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screen-recording
title: 录屏
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 录屏
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b424620f64a61de04697204771473af49b3e77e686b62beafbd81ae64bcea902
---

在应用开发过程中，可以使用录屏功能录制应用的运行状态，并通过录屏文件向他人展示正在开发的应用的各种功能效果。

## 使用约束

* 如果设置了锁屏密码，录屏开始前请解锁设备屏幕，锁屏状态下录屏应用无法正常拉起。
* 如果设置了锁屏密码，录屏时请保持设备的屏幕解锁状态，若录屏过程中锁屏将导致录屏应用退出。
* 模拟器不支持录屏。

## 通过DevEco Studio录屏

1. 连接真机设备，并在其中运行应用。
2. 在DevEco Studio底部切换到**Log**页签。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/U7ut_BZ_T1qjQXMjWGId2w/zh-cn_image_0000002530753756.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=B30BE71AC4AC8A88646D1A1D45A8103E290D13EBE99A65D9E0F3B361C97D310C)，即可开始录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/ZeDU000pTDSByK__MxRWhQ/zh-cn_image_0000002561753699.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=F9AD574C6B52B1085E16A366BF01C22D73214037B8E79973129F243389C19296)
4. 录屏时，需要先选择录屏文件的保存路径，开发者可使用默认路径或[设置自定义路径](ide-screen-recording.md#section89111791511)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/8mJiJgErQxWzCLE14gy85w/zh-cn_image_0000002530753762.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=D5BF4904590A498BED32C092C81151200936F6B68C273BFD86463C734D5E5FCC)
5. 路径选择完毕后，点击**Start Recording**开始录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/7NNXWuchSMas1S8Z3FWkMQ/zh-cn_image_0000002561833673.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=D670516835F8B5952B52C1DEAB791D3310FE06F917A969DE8024D28A9583DC54 "点击放大")
6. 录制完操作流程之后，点击**Stop Recording**结束录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/q6Tbfgj2ThqsvA--kXtk0g/zh-cn_image_0000002561753689.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=8F03EF1F388CA3BEAFB65C6826B8B7017BFB57F0667E0FBD3294ED903D6D41AC "点击放大")
7. 结束录屏后，录屏文件将会保存到之前选择的路径下，可以选择调用系统播放器播放视频文件或打开文件所在的文件夹。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/t4lIOLj3RACiQvpqs3ycLA/zh-cn_image_0000002530913752.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=44C3F472FF5236166F50AD40C98C655943F64B78035BCCB2EC9D872FE9D5EA7B "点击放大")

## 设置录屏自定义路径

1. 点击DevEco Studio底部**Log**页签，选择**HiLog >** **Settings** **>** **Record Screen**选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/KCvgcnbrR6ijahZ1gkzM-w/zh-cn_image_0000002561753693.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=A8F33CB21BB555DAD2839CE4D0BD57F7E19A02D522D3354DF44951DDB361BCA5)
2. 在弹出的界面选择自定义路径，当设置好路径并勾选“Use the selected path and auto-generated file name as defaults and don't ask again”选项后，录屏时将自动使用此时设置的路径以及以录屏时的时间戳构造的文件名作为录屏文件的保存地址及文件名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/qyFmrpRKQ4uaa07i20NY_A/zh-cn_image_0000002530753752.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=BC54E3DFC40D6C330028AB7BEF600908DB9B7F9544B0B4F0D322112F01E97920)

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/y9eLWdG5QIa_bnyfM67dhg/zh-cn_image_0000002561753695.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=B2AE9519776DAA449D44CFF8780EDBB0B07BC2C23820BF6FF8716749151035BD)

     需要再执行如下命令，指定该uri，将录屏文件复制到有下载权限的路径中（如/data/local/tmp）。

     ```
     1. hdc shell mediatool recv "file://media/Photo/2/VID_1736853237_001/test.mp4" /data/local/tmp
     ```

     命令返回值第二行即为录屏文件路径{RecordFile}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/gZ_-p_q5Sbm2yy_82n7K-A/zh-cn_image_0000002530913756.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=08813510C8C9D512784031B3B572D39B3F0C06E6FA87E9DB356362600732D0EB)
   * 如果查询结果不包含uri字段，则返回值第二行即为录屏文件路径{RecordFile}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/fr8Ej_qQTf6ySAbXm63Wew/zh-cn_image_0000002530753758.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=A2633E853FE313DCE00595C54FB31579E59EB85253FCEAF9AD7C5918E6DC9D5A)
4. 指定上一个步骤中获取到的录屏文件路径{RecordFile}，下载录屏文件到本地。

   ```
   1. hdc file recv {RecordFile} d:\test.mp4
   ```
