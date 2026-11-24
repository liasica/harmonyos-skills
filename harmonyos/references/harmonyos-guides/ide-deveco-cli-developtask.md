---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-cli-developtask
title: 常用开发任务
breadcrumb: 指南 > DevEco CLI > 常用开发任务
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:52+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:bbff014d333d2a5d857800da69de8cca5b77a9266d63e3be2dec08d48c876b94
---

以开发一个音乐类型的HarmonyOS应用为例，介绍DevEco CLI常用命令。

## 开发准备

### 初始化CLI环境

输入自然语言“将devecocli的skills或mcp服务配置到opencode中”，让Agent调用鸿蒙开发相关能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/4jodC5_KTheRAvDsYAaCwQ/zh-cn_image_0000002808886619.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=A45AB72BC985F8525299AA136313F7A750C7187CB279FA884A3D21F988B1EF52 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/V1tRHy0mRRipC7bLFzDjqw/zh-cn_image_0000002779566942.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CD5F50776CFB8EB5E334DDD419839FBCC752D855FFC4C3DF8FB1CFEE2FB1831 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/T2JCbavfSyGyozqYnbvRGQ/zh-cn_image_0000002779406986.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=F6DD68CDAB11C37E89695CAF09753EE1E72C0DFF379830EB157C89D58BA7882B)

### 登录华为账号

登录华为账号，以便进行签名配置、构建或发布等需要账号权限的操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/3NO_NYRdTEKc324dHDwo6Q/zh-cn_image_0000002779566956.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2177B6A87E98A433AE37FCC5EF74CC0B1906EEF11E89BB414FE9DC73DA07CD5)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/Uo2ZtM72TDqjnE2eusSvCg/zh-cn_image_0000002808886597.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=E71A654185B934E16151041CC29F9FD925D4D2D7EFF58F90DCCB44364AE03FBA)

### 查询文档

搜索并查看鸿蒙开发文档，了解指定组件或API的用法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/wdWVLmunQimwfJMjbC97bA/zh-cn_image_0000002779566962.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=1842343D36698BEA697F53B699B68E6BB1A3A1898D6C97EBF850479EC61F0EBE)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/0oBkhTZ4TVmXtcNqdbiafw/zh-cn_image_0000002808886631.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=260D5EE02A63B069F9A7E5A460581162F1511E0DCB2288142DD1322EE2F3B9BD)

## 创建项目

### 创建音乐应用工程

创建一个音乐类型的应用工程，自动生成基础目录结构和示例代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/9j6BChH2QVqfsHFn7VyN_w/zh-cn_image_0000002808886611.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=55E1F68932C8AEA5AFD5B63CB146C0D1C2DE4A392FD6ABC731F5076EC2890A4B)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/CdEgACbaRZ-_Vq6j6haNrQ/zh-cn_image_0000002779566964.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=E6312424B62B21CDABDA1F8C213BA2AC7A8FE45673011162A3CA5D9DC49612DC)

### 配置签名

配置调试签名，使应用可以安装到真机或模拟器上进行调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/7TmAjIA9QyKOVsIfSoYFDQ/zh-cn_image_0000002808766517.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C4703353E4469884918C72CA9197FA5BF8035C044DEE2963D1C788D642929A3)

## 生成代码

### 编写播放器核心功能

编写音乐播放器的核心功能代码，并在编写代码过程中自动查看相关API的用法，对生成的功能代码进行检查。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/Mvu6odwRSOeAm_OXAlDeBw/zh-cn_image_0000002779566950.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2CDD2D36E7EB1A8C97C7B60891E75DE2A1ED4263F461E3690AB7F954DC88CDA)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/t0j6CMGhQAajOH4Gp0lOww/zh-cn_image_0000002808886599.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=9AD81A4469D747BA3D292FEA1541634A5ADC264699D4568BF08C5FE1A72BD401)

### 检查代码规范

检查代码是否符合ArkTS编码规范，并给出改进建议。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/Z7y-RWcaRuWdnS8rzK8ruA/zh-cn_image_0000002808766535.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D362D6A1F90A55677B94C7593A0050224D60AF8295C609AFCAFED7AD6C0730F)

### 检查兼容性

检查项目在目标设备上的兼容性，排查潜在的兼容问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/1XaUHyZ8RrqLZaJ2x7Uyag/zh-cn_image_0000002779406984.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=89AE00D40D7E1AAB4F8C9855F769CCA6EF4A5E972282F8FDC6D81662FC94D7A8)

## 构建与运行

### 调试构建

执行调试构建，将应用安装到设备或模拟器上进行调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/rec9nD06RkuUaPZ4LDHviA/zh-cn_image_0000002808886603.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED914C0AA8B2E194A7F8AEF366FA3BA1FDFF5D242EBF3DD7B14453C7E244FFC6)

### 清理构建产物

清理构建产生的中间文件和产物，释放磁盘空间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/_8vLRLcFTM6jtzzM2Vlh_Q/zh-cn_image_0000002808766539.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=0BC362C5069E4DC7334E62410BBE7124DE33BBC39407FA2AAF5975B81A1224D1)

## 热重载开发

将主题色改为亮色，通过热重载在不重启应用的情况下验证UI改动生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/JYvPvJooQXe4Tkkx3hNAKA/zh-cn_image_0000002808766523.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=29DD9F1BBC2D50DA47D64D961CBAC34A9E3FECA447C668A61177423D45BA4164)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/vBR-x4RgTlWzkto3Pn83iA/zh-cn_image_0000002779406974.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=29B0226537D100434B14593D7190D6C7EE0CC3FB6D18C81596E5A73E37882F5C)

## 模拟器测试

### 镜像管理

查询适用于当前工程的模拟器镜像。Agent读取工程的API配置，调用DevEco CLI的镜像查询能力，检查手机镜像的系统版本和下载状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/orlwZq5OQMilhVSSccboZQ/zh-cn_image_0000002808886621.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=FEAB80481F0A6CC4E66C4F7F3C6173950C6715F80BBE406C0DAEFEE1184E643C)

Agent选择本地已下载的HarmonyOS 7.0手机镜像，供后续创建测试实例使用。需要其他版本时，可以继续获取所需镜像。

### 创建专用测试模拟器

为音乐应用创建专用测试模拟器。确定名称后，Agent调用 DevEco CLI的实例创建能力，再查询实例列表，确认MusicApp\_Phone已创建成功。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/JkWMqqBiR7SulbjmOK8XAA/zh-cn_image_0000002808766537.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=37A7DDBB156180F93E4AA4EFF15608AD004CE7F09CB31C451DA161A91F8F607C)

### 启动模拟器

启动测试实例。Agent调用 DevEco CLI启动模拟器，并查询运行状态和连接信息，为后续部署应用确定目标设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/2BKoJ1VlTau7e_r7MTOIPg/zh-cn_image_0000002779566952.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=58310D93B2D7434D81D199D06511B44A2E413289198277D496A69B053C3AA0FF)

启动完成后，模拟器显示系统界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/I_Ve7CipQL2mWWnSlwfTjw/zh-cn_image_0000002808766531.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB6BD13D560866307764895418C6D937E2F9B8103B1F998E112E5F2EC1050CD9 "点击放大")

### 在模拟器上调试运行应用

将音乐应用运行到已启动的模拟器。Agent结合工程模块和目标设备，调用DevEco CLI完成调试构建、安装和启动，并根据返回结果反馈部署状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/qhlyTqnCTgeK9lhgMxCt1w/zh-cn_image_0000002779566968.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B608C012722858DD53830ABE54EAF11F250EF26156FB2DB85D24DC783E2AB5F "点击放大")

应用启动后，可在模拟器上查看首页的推荐歌单和歌曲列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/l36R4HMlRGuy296cecxR3Q/zh-cn_image_0000002779566954.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FFDFD94A2977E6951FFB26ACDD10B92932384364ED5E644A4065DC7FD518408 "点击放大")

### 调整模拟器音量

在测试过程中，调整模拟器音量。Agent调用DevEco CLI的模拟器控制能力，将音量操作应用到当前测试实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/JDAUk4X9TqGnTAgYj7A3sw/zh-cn_image_0000002779406982.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=C88E4FBE62E0289DBDAA381C79DF9432476D590E6AE6491FCEF9DEA6FD2729C8 "点击放大")

结合系统音量面板，观察播放器页面和应用首页的显示效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/uSAQmaw0Qi2pC63IobKkvg/zh-cn_image_0000002808766529.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=58D513AA333C72BC17A25116028EA7DEADD739EB9784523A06AC74495B9CEBEE "点击放大")

## 调试与日志

### 查看设备日志

获取测试设备最近的日志。Agent调用DevEco CLI的日志采集能力，读取最近100行内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/1dq-G302RTS5sCpUlYf1wQ/zh-cn_image_0000002779406960.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=F38615A8999B5CAAA1D3BA3DC32C6098B40FBE922492251ECA3C2C18324CF569)

当返回内容主要为系统应用日志时，可以进一步限定应用范围，继续筛选。

### 音乐应用专项日志

只查看当前音乐应用的日志。Agent根据工程包名调用DevEco CLI的应用日志筛选能力，提取应用启动和页面加载等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/hc5wXVCSRKSfIR7-Rd1eow/zh-cn_image_0000002808766547.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4505CC323123F24D66AE3FEF46682A05C594E28C30E0FC5523123D4BF4324A2)

Agent将生命周期日志解释为应用创建、窗口创建、进入前台和页面加载完成，帮助判断启动过程。需要进一步分析播放行为时，可以按播放器的业务标记筛选相关事件。

### 实时日志跟踪

持续跟踪应用日志，同时操作播放、暂停和切歌。Agent使用DevEco CLI的实时日志能力采集运行信息，将新产生的日志与界面操作对应起来。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/6PB2G8ZFS1inIFMTihDdxw/zh-cn_image_0000002779406976.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CE29255E8552D2ADC11BE25567F251B4601315028A021478C1798B7C06D75C8)

### 查看历史日志

查询指定时间段内的应用日志，例如当前时刻10分钟前至5分钟前这段时间。Agent 将时间范围转换为日志查询条件，调用DevEco CLI获取对应记录，并解释该时段发生的操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/erIhAzuhTwqHRxKUC4aW3g/zh-cn_image_0000002779406964.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=BDC999552E2D2EDD186EF6928712671F68893A79C9161129673E1DF2043CE798)

查询结果包含应用创建、进入前台和页面加载记录，可用于回溯启动过程，或与异常发生的时间进行对照。

### 分析崩溃日志

在测试代码中加入越界访问，点击“下一首”触发崩溃，用于演示故障定位流程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/4n6-ExfLS-mRp42G2PsJMQ/zh-cn_image_0000002808886617.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=459B104C65EA865C956C2A2382A7D6EEC48A4A4DD9AEC153B7FC117872B91D46)

应用崩溃后，分析原因。Agent调用DevEco CLI获取崩溃日志，提取异常类型和调用栈，再读取对应源码进行定位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/zctNuwdqS4adJbioyYaKVw/zh-cn_image_0000002779566940.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=2EA34565B2C18802523363DF392DE7C89C75719B008DF0F3669954ED2A08D7FF)

Agent定位到“下一首”逻辑中的歌单越界访问：读取不存在的歌曲后继续访问其名称，引发异常。根据这一结果，可以继续移除演示故障代码、检查歌单边界，并通过DevEco CLI重新构建运行，按相同操作复验。

## Skills（可选）

### 列举可用Skills

查询HarmonyOS应用开发可用的技能。Agent调用DevEco CLI的技能查询能力，获取skill列表，并按ArkUI开发、崩溃分析、多设备适配等用途进行整理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/XernJNO-TDWN6hjgSELe3g/zh-cn_image_0000002779566944.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=019A17306A4B83168FBCE5BEF557A9FB3FB319A6C5AFE0D26A4E12C67B320608)

### 查找所需Skills

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/98LmTlaNSOKhjm57omAQKw/zh-cn_image_0000002779406966.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=08C35A27BFDF5B753373BC3E72D87AA6EB3B3875F065E788C51CE9823FC124A4)

Agent结合各项技能的描述，选择多设备适配入口，以及折叠状态、窗口尺寸、屏幕方向和交互方式相关技能，并说明选择理由。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/V3rt_m06RXOJblorlkHC5w/zh-cn_image_0000002808766525.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=82AF40E0E1A073DBE5A0C6E033979B4B7D3275F53779DF833F4C74CE87914D55)

### 安装Skills

将选定skill安装到当前工程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/eqGWKPXLSV6yYNz8Mu4uug/zh-cn_image_0000002779406962.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B6DF30400DBEC25C8B965DF3D97C150DBAD8C94F4BA899CAC4B6B6FE21898E9)Agent调用DevEco CLI的skill安装能力，完成五项技能的安装，并反馈安装结果。Agent可加载对应技能，依据其中的指导开展适配开发。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/o6y7-C8XSmG2oKUZjzbGwQ/zh-cn_image_0000002808886605.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=D4E894A25C73CC919D5C3EC9F0BFAF1E1CAE17027F5959AC3D83B0D38BD9E8E6)

## 应用发布前检查

### 兼容性检查

检查当前代码的系统版本兼容性。Agent先调用 DevEco CLI查询可用的检查版本，再结合工程配置确定源版本和目标版本，执行工程扫描。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/e2a7v8dCTUGiVdKuPNfn7A/zh-cn_image_0000002779406972.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B7CDFA1B64CE4D48491684A6BDA9799063A916AEB48377E49B3EACFF5CDFA74)

DevEco CLI返回API变更及代码位置，Agent据此整理接口定义、视觉布局和接口行为等方面的影响，指出需要关注的调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/5v6300YHQi-P9rHQQDQQoA/zh-cn_image_0000002808886609.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=6CE99705A818FE820B0CBA4DA433B58D811FBE67AA8EEE237D2EA7D7900CABB0)

### 签名检查

检查工程签名配置和材料，确认是否满足构建及发布要求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/oNxpcOLuTcWMvYjkE-el7w/zh-cn_image_0000002779566946.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=F2101FEB81C3B434C1097BF108136DCD4108F819C6A72054B520622BBD8E2D76)

Agent读取工程配置，检查构建产品与签名配置的关联，再核对证书、密钥库、profile、应用包名和有效期，汇总检查结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/FN97TbAZS1yccQk6k26nfw/zh-cn_image_0000002808766533.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=6DA785A9CBCFC629F7953E7664B24E94693E54B11E8988F184F9B55564B868B9)

### 发布构建

执行发布构建。Agent根据工程配置调用DevEco CLI的release构建能力，检查构建结果，并查找生成的应用包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/HfGLjQJxSeeqNQAOQbm7lw/zh-cn_image_0000002808766541.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=D60E032DD20FDA6D536BD74FB7DC2A34EFF9511D9E79FA34A70E46190A31EF2F)

构建完成后，Agent汇总已签名和未签名产物的位置，便于继续测试或准备交付。
