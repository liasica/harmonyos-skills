---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screen-recording
title: 录屏
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 录屏
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:1d3b5587ba883f4425cf9d57057380819897bd931868b4aee670b3480a20dbd1
---

在应用开发过程中，可以使用录屏功能录制应用的运行状态，并通过录屏文件向他人展示正在开发的应用的各种功能效果。

## 使用约束

* 如果设置了锁屏密码，录屏开始前请解锁设备屏幕，并且录屏时需要保持设备的屏幕解锁状态，锁屏会导致录屏应用无法正常拉起或退出。
* 穿戴设备、模拟器不支持录屏。

## 通过DevEco Studio录屏

1. 连接真机设备，并在其中运行应用。
2. 在DevEco Studio底部切换到**Log**页签。
3. 点击左侧工具栏中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/JmUZTIMDSLiIYiZ-XVSyng/zh-cn_image_0000002779407448.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=063CA26CB43AB93E09241ACD6694470138E7F76C4E2B4DD8D4CB77AA0316EF0C "点击放大")，即可开始录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/APvqjxQ2SDy6KiIwQE8UUw/zh-cn_image_0000002779567430.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E4B59FB0E197BBDC0CB81B6B27407CA2B41AD00738CDE803500F7F14F1EC9CF)
4. 录屏时，需要先选择录屏文件的保存路径，开发者可使用默认路径或[设置自定义路径](ide-screen-recording.md#section89111791511)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/DuuI4104TbOQj9dmJW1y8Q/zh-cn_image_0000002779407454.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=20BD57701BA81C258D2F81E3BC0EE9E097C61826827ED5F3690C13B5FEA92031)
5. 路径选择完毕后，点击**Start Recording**开始录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/wZnSgq8vRkWM9WcJGmFoFg/zh-cn_image_0000002779407446.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B64BEE02BCDD82CE07CEF3D054191D2C08106A9CE5F542B103A4875495F9CF4 "点击放大")
6. 录制完操作流程之后，点击**Stop Recording**结束录屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/sLO1wvevSzqWyLQei-wt5Q/zh-cn_image_0000002808766999.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=22FE92BFE33721E00312BC0FFE89ADCF8E043AA8B081E3B4BAB66EB3FB1AF4E2 "点击放大")
7. 结束录屏后，录屏文件将会保存到之前选择的路径下，可以选择调用系统播放器播放视频文件或打开文件所在的文件夹。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/0hHeM5z3QXuAxwoyI-LI1Q/zh-cn_image_0000002779407452.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=EEC503DA09037F36F5F0175F5D5F370E6B27B1F002A1E8C46C85E656C7961188 "点击放大")

## 设置录屏自定义路径

1. 点击DevEco Studio底部**Log**页签，选择**HiLog >** **Settings** **>** **Record Screen**选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/ExD5UVGgQJOb9rsC9znW4A/zh-cn_image_0000002779567422.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=835013BFDF8BA1D3CBD70D8542D6DB3D397C40CE2BF05FCE1B78352820A26544)
2. 在弹出的界面选择自定义路径，当设置好路径并勾选“Use the selected path and auto-generated file name as defaults and don't ask again”选项后，录屏时将自动使用此时设置的路径以及以录屏时的时间戳构造的文件名作为录屏文件的保存地址及文件名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/uQsHvA4BTEm1FiprJU0pUA/zh-cn_image_0000002808887081.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=1AD72BFE06508521CDCDAF08260720BF4FF1AAF9C66D1749B1CA2240FE6BF827)

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/Dqi8HDD-R-2FKjUEyrLF3Q/zh-cn_image_0000002808767007.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D250F243D2349A36A60E16B1A3F86490D879BC6CD3D092D4BF0781DEBE4F5CA)

     需要再执行如下命令，指定该uri，将录屏文件复制到有下载权限的路径中（如/data/local/tmp）。

     ```bash
     hdc shell mediatool recv "file://media/Photo/2/VID_1736853237_001/test.mp4" /data/local/tmp
     ```

     命令返回值第二行即为录屏文件路径{RecordFile}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/WzSbPigkRoO2didpQG2n3w/zh-cn_image_0000002779567432.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=67ED923D02553E1A07B32A3B62C8C541F99C4C484EDE3F79EEFA96236CC2E0D2)
   * 如果查询结果不包含uri字段，则返回值第二行即为录屏文件路径{RecordFile}。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/q544Rxe5QBSuQEmFceIzrw/zh-cn_image_0000002779567428.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=241EBF065A46862DDFCDBB88BACE172A40FA76B9C0B7337E6A8EF8F33BBE4FC5)
4. 指定上一个步骤中获取到的录屏文件路径{RecordFile}，下载录屏文件到本地。

   ```bash
   hdc file recv {RecordFile} d:\test.mp4
   ```
