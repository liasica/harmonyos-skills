---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-34
title: Hypium怎么在多台设备上并行执行测试用例
breadcrumb: FAQ > DevEco Studio > 应用测试 > Hypium怎么在多台设备上并行执行测试用例
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d053dad331e889865750b2451cb4b1bd5037ba7f7c8681824b67cb4e9a3ecbdd
---

## 问题现象

以下两种自动化测试场景，如何实现：

* 多份test.py在多台设备上测试不同的应用。
* 一份test.py脚本，同时测试多台设备。

## 背景知识

[DevEco Testing Hypium(以下简称Hypium)](../harmonyos-guides/hypium-python-guidelines.md#section16890204264419)是HarmonyOS平台的UI自动化测试框架，支持开发者使用python语言为应用编写UI自动化测试脚本，提供**控件定位能力、模拟输入功能、多设备并行操作、生成用例执行报告**等功能。

Hypium支持多设备并行执行测试用例，使用前先参考[安装向导](../harmonyos-guides/hypium-python-guidelines.md#section191615399595)完成步骤1到步骤5的安装。

## 解决方案

1. 场景一：多份test.py在多台设备上执行，新建多个main.py，通过main.py分别运行不同的test.py。
   * user\_config.xml配置并行设备的sn。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/yKso0IafQdOyPoeBdJr1HQ/zh-cn_image_0000002658928845.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=242E47EB3FB6391922A93CC057036CB9E4010A8D18FB5D4EAD662C92A7BDD2FD "点击放大")
   * 配置用例的json文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/xvwP4kpwREyX4v_QOyU0nw/zh-cn_image_0000002628409636.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=B263209389E9F72ED5FB749E4BBEFB56C6EEE86E96CA13F0C53904D9897EA9F3 "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/wGqtXCdIQSqWYhlnXtuR2g/zh-cn_image_0000002658808895.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=732C5A3B63DC18262DF0CD7CBE32506CBE519171516352DF266F2E95D07CE9DC "点击放大")
   * 新建main2.py，配置main和main2，对应不同用例和设备。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/D9IvgoA8R2KCcep-wLwO7w/zh-cn_image_0000002628569530.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=47222412056CD8BF36EAD329347665CA8154908719FFE86FC6348CA36E91612D "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/foufYBWXTy2QWVZzAhvULA/zh-cn_image_0000002658928855.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=254EC2EF12BC0641EE3E073861E22B9A5B1D45D15534667E8E6C4177F8DE6ED6 "点击放大")
   * 运行main.py和main2.py。
2. 场景二：单用例在多设备上执行。
   * 新建项目时，点击左侧的DevEco Testing Hypium，选择双设备。或者用例里使用device1、device2区分设备。（如果大于2台设备，可以继续新增，如device3）

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/FaTgiRSGTmSFi2McZMLw4w/zh-cn_image_0000002628409640.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D97003EA7C88A7386D7D5C7B995B3CCED23EE6885C79B291E4F52144D494A6C "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/cF3SC582SBSWkoc11ZXr-w/zh-cn_image_0000002658808899.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC7C20521E78834C72D34BCF2E59729E6EC60AC8A3A58F0F049D24C55FF9FCBC "点击放大")
   * 用例里面步骤分别对应不同设备（device1、device2）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/sBddAfvvSlOqIug6wvbr5A/zh-cn_image_0000002628569532.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A4271043064914893E11F8EC00F1268A3737A7655AC377D891055111377C110 "点击放大")
   * user\_config.xml配置并行设备的sn。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/xS5AF468TtGhNRdVBWBdcA/zh-cn_image_0000002658928857.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=20B6B8CC7CCC0FCE7A9BB2FAA27BFFA5752690589E19F623417FE0F6583CFB97 "点击放大")
   * 修改用例的json文件，增加设备（如果是新建项目选择双设备，默认已经配置2台设备）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/i8ctzw53SpKN8SXeCGW0_g/zh-cn_image_0000002628409642.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A8FA25F61F5E1AD41B518C65B248E3CF578F253321D068027925A951A37F168 "点击放大")
   * 配置main.py文件，指定运行设备sn号。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/cOAbRD7tSaqz0MGsPuBtvQ/zh-cn_image_0000002658808903.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=36742A0964776A4CB95B0C3E3D781E8E4FE154D84FAB3CEB02D8CE802F47E8B0 "点击放大")
   * 运行main文件。

## 常见FAQ

Q：UiViewer如何实现多设备的连接和切换？

A：UiViewer最多支持同时对两个设备进行投屏，选中想连接的设备，设备编号一个设置为dev1，另外一个设置为dev2，点击确定，即可进行两个设备的投屏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/kA_HLXqUTgOj4mjIE89b3g/zh-cn_image_0000002628569536.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=C7F2072B34F1872D39CE4D65D79A070D439D4BE2DC32147510AA81FA9A6B1C36 "点击放大")

如果要进行设备切换，点击右上角的设备切换，回到设备选择页面，重新进行选择即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/-9iATzpIQiCR6rO4WUji-Q/zh-cn_image_0000002658928861.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=83D861A4490955066AFFB4478A45669C303A6DEA49AB70E2A41C22F9D403F338 "点击放大")

Q：如何测试不同的应用。

A：Hypium测试的对象是设备，而不是指定应用。针对特定应用的测试，可以编写测试用例，通过start\_app打开指定应用，再执行对应的用例。

Q：Hypium是否支持选定模拟器进行测试？

A：支持，不管是模拟器还是真机，在user\_config.xml指定设备的sn即可。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<user_config>
    <environment>
        <!-- type: 设备连接方式,usb-hdc表示使用hdc命令控制设备(默认) -->
        <device type="usb-hdc">
            <!-- ip: 远端设备地址,ip和port为空时使用本地设备,非空时使用远端设备 -->
            <ip></ip> 
            <!-- port: 远端设备端口号 -->
            <port></port> 
            <!-- sn: 设备SN号列表,SN之间用分号";"分隔,sn字段为空时使用所有本地设备,非空时使用指定的sn设备 -->
            <sn></sn> 
        </device>
    </environment>
    <testcases>
        <!-- 指定测试用例目录，为空则默认设置为当前项目下的testcase文件夹 -->
        <dir></dir>
    </testcases>
    <resource>
        <!-- 指定资源目录，为空则默认设置为当前项目下的resource文件夹 -->
        <dir></dir>
    </resource>
    <!-- 默认为INFO，如需更详细信息可设置为DEBUG -->
    <loglevel>DEBUG</loglevel>
    <devicelog>
        <!--在测试用例结束后额外后拉取以下路径的日志到报告下-->
        <dir>/data/log/tee;/data/log/test</dir>
        <!--控制hilog日志等级，默认值为INFO-->
        <loglevel>DEBUG</loglevel>    
        <!--控制是否在拉取日志后设备端的日志，默认值为true-->
        <clear></clear>                
        <!--控制是否抓取设备日志，默认值为ON，OFF时候上述两个标签不生效-->
        <enable>ON</enable>            
    </devicelog>
</user_config>
```

Q：Hypium是否支持不输出日志？

A：框架会进行正常的日志打印，并会在测试工程的reports目录或者指定目录生成日志。但可以通过user\_config.xml把日志等级调到最高（ERROR），并把设备日志关掉，从而减少报告内容。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<user_config>
    <environment>
        <device type="usb-hdc">
            <sn></sn>
        </device>
    </environment>
    <testcases>
        <dir></dir>
    </testcases>
    <loglevel>ERROR</loglevel>
    <devicelog>OFF</devicelog>
</user_config>
```
