---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-environment-config
title: 配置OHPM代理
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 附录 > 配置OHPM代理
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:21+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:f71a34b9f023d18ddde2ce273fa587ed740c4f7a7fe541a18a5f793d7a67967c
---

鸿蒙电脑DevEco Studio开发环境依赖于网络环境，需要连接上网络才能确保工具的正常使用。一般来说，如果使用的是个人或家庭网络，是不需要配置代理信息的，部分企业网络受限的情况下，才需要配置代理信息。可通过如下步骤进入代理配置。

1. 进入OHPM代理设置界面。
   * 在打开了工程的情况下，单击界面右上角**设置> 扩展 > Ohpm > 优化配置**。
   * 在欢迎页单击打开一个空目录或空文件，单击界面右上角**设置> 扩展 > Ohpm > 优化配置**。
2. 配置OHPM设置。
   * **OHPM仓库**：配置ohpm仓的地址信息。

     ```screen
     https://ohpm.openharmony.cn/ohpm/
     ```
   * **HTTP代理**：代理服务器信息。其中，**主机名**为代理服务器主机名或IP地址如下，**端口号**为代理服务器对应的端口号。如果需要配置账号密码，请使用如下格式进行配置：

     ```screen
     http://user:password@proxy.proxyserver.com
     ```
   * **启用HTTPS代理**：同步配置HTTPS代理信息。

   填写并勾选以上信息后，点击确认。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/JRaJhxqiS76DSE4_7GQdmA/zh-cn_image_0000002779728697.png "点击放大")
3. 代理配置完成后，点击底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/JSZW2AYKTPOBilo9BRYKsQ/zh-cn_image_0000002750169522.png)终端图标，可执行如下命令验证代理是否配置成功。执行结果如下图所示，则说明代理设置成功。

   ```screen
   ohpm info @ohos/lottie
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/qwv3KAGuTDWVOqm7AbVxQg/zh-cn_image_0000002750009636.png "点击放大")

**说明** 

ohpm默认校验registry仓库地址证书。如果环境检查中ohpm registry access出现'SELF\_SIGNED\_CERT\_IN\_CHAIN'或'UNABLE\_TO\_VERIFY\_LEAF\_SIGNATURE'等证书校验错误时，请查看[FAQ-问题现象2](../harmonyos-faqs/faqs-development-environment-10.md)解决证书校验错误问题。

在此界面配置的代理信息将写入“/storage/Users/currentUser/.ohpm”目录下的**.ohpmrc**文件。

1. 进入/storage/Users/currentUser/.ohpm，打开**.ohpmrc**文件。

   **说明** 

   在文件配置前，若此路径下无.ohpmrc文件，完成OHPM代理设置后会自动生成；若此路径下存在.ohpmrc文件，完成OHPM代理设置后会生成新.ohpmrc文件，原文件以备份形式存在。
2. 修改ohpm仓库信息，示例如下所示：

   ```screen
   registry=https://ohpm.openharmony.cn/ohpm/
   ```
3. 修改ohpm代理信息，在http\_proxy和https\_proxy中，将user、password、proxyserver和port按照实际代理服务器进行修改。示例如下所示：

   ```screen
   http_proxy=http://user:password@proxy.proxyserver.com:port
   https_proxy=http://user:password@proxy.proxyserver.com:port
   ```

   **说明** 

   如果password中存在特殊字符，如@、#、\*等符号，可能导致配置不生效，建议将特殊字符替换为ASCII码，并在ASCII码前加百分号%。常用符号替换为ASCII码对照表如下：

   * !：%21
   * @：%40
   * #：%23
   * $：%24
   * &：%26
   * \*：%2A
4. 将ohpm配置到环境变量中。
   * 在**此电脑 > 属性 > 高级系统设置 > 高级 > 环境变量**中，在系统或者用户的PATH变量中，添加ohpm安装位置下bin文件夹的路径。默认路径为：DevEco Studio安装目录\tools\ohpm。
5. 代理配置完成后，下载并打开[命令行工具](ide-hmos-command-line-tools.md)，执行如下命令验证网络是否正常。

   ```screen
   ohpm info @ohos/lottie
   ```

   执行结果如下图所示，则说明代理设置成功。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/zHStuRq6S0Cz8mWySF3EKA/zh-cn_image_0000002779608545.png)
