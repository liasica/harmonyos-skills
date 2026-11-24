---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-environment-config
title: 配置代理
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 附录 > 配置代理
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:32+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:89100870daf8e84164a730345df845946409e6ec8bbb89d77ed0db2f05839d3a
---

DevEco Studio开发环境依赖于网络环境，需要连接上网络才能确保工具的正常使用。

通常情况下，如果使用的是个人或家庭网络，是不需要配置代理信息的，部分企业网络受限的情况下，才需要配置代理信息。

## 诊断开发环境

为了您开发应用/元服务的良好体验，DevEco Studio提供了开发环境诊断的功能，帮助您识别开发环境是否完备。您可以在欢迎页面单击**Diagnose**进行诊断。如果您已经打开了工程开发界面，也可以在菜单栏单击**Help > Diagnostic Tools > Diagnose Development Environment**进行诊断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/fYfOYbQ-QC2PFhV33MpONg/zh-cn_image_0000002808886397.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=49DDF6CEA9D3D245EFBD82318A17DD0735F12D6FC147D6C203DD8417C7A55C2A)

DevEco Studio开发环境诊断项包括电脑的配置、网络的连通情况等。如果检测结果为未通过，请根据检查项的描述和修复建议进行处理。

## 配置HTTP代理

1. 在欢迎页单击**Customize > All settings… > Appearance & Behavior > System Settings > HTTP Proxy**进入HTTP Proxy设置界面。如果已经打开了工程，可以单击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Appearance & Behavior > System Settings > HTTP Proxy**进入HTTP Proxy设置界面。
   * **HTTP**配置项，配置代理服务器信息。**如果不清楚代理服务器信息，请咨询您的网络管理人员**。
     + **Host name**：代理服务器主机名或IP地址。
     + **Port number**：代理服务器对应的端口号。
     + **No proxy for**：不需要通过代理服务器访问的URL或者IP地址（地址之间用英文逗号分隔）。
   * **Proxy authentication**配置项，如果代理服务器需要通过认证鉴权才能访问，则需要配置。否则，请跳过该配置项。
     + **Login**：访问代理服务器的用户名。
     + **Password**：访问代理服务器的密码。
     + **Remember**：勾选，记住密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/TCX_jxsuQqOQzPBhbyQj1A/zh-cn_image_0000002808766319.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC6F80F8B7347A08AA0859F2430B88563330AB55562198512288824F55557420)
2. 配置完成后，单击**Check connection**，输入网络地址（如：https://developer.huawei.com），检查网络连通性。提示“Connection successful”表示代理设置成功。

## 配置NPM代理

Hvigor、ohpm在初始化时需要从npm仓库下载依赖，如果需要代理才能访问网络，请配置npm的代理。

1. 进入*C:\Users\用户名*目录，打开**.npmrc**文件。如果该目录下没有**.npmrc**文件，请新建一个。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/3BtFpvMdTymX08cv1QUg6Q/zh-cn_image_0000002808886399.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=84206EC3D9844E4B064627BAAFF5F5117B3188965BC4EB409C071449740DE8CF)
2. 修改npm仓库信息，示例如下所示：

   ```screen
   registry=https://repo.huaweicloud.com/repository/npm/
   @ohos:registry=https://repo.harmonyos.com/npm/
   ```
3. 修改代理信息，在proxy和https-proxy中，将user、password、proxyserver和port按照实际代理服务器进行修改。**如果不清楚代理服务器信息，请咨询您的网络管理人员**。示例如下所示：

   ```screen
   proxy=http://user:password@proxy.proxyserver.com:port
   https-proxy=http://user:password@proxy.proxyserver.com:port
   ```

   **说明** 

   如果password中存在特殊字符，如@、#、\*等符号，可能导致配置不生效，建议将特殊字符替换为ASCII码，并在ASCII码前加百分号%。常用符号替换为ASCII码对照表如下：

   * !：%21
   * @：%40
   * #：%23
   * $：%24
   * &：%26
   * \*：%2A
4. 将Node.js配置到环境变量中。
   * Windows环境变量设置方法：

     在系统或者用户的PATH变量中，添加Node.js安装位置的路径（默认路径为$DevEco Studio安装目录\tools\node下）。
   * macOS环境变量设置方法：

     打开终端工具，执行以下命令。

     ```screen
     export NODE_HOME=/home/xx/Downloads/node-vxx.xx.x-linux-x64  #本处路径请替换为Node.js的安装路径（默认路径为$DevEco Studio安装目录\tools\node下）
     export PATH=$NODE_HOME/bin:$PATH
     ```
5. 代理配置完成后，打开命令行工具，执行如下命令验证网络是否正常。

   ```screen
   npm info express
   ```

   执行结果如下图所示，则说明代理设置成功。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/021of0RZSeufu50rKNmvgg/zh-cn_image_0000002808766315.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8E10CCC8E39DBC7C6B6E305411491D7061F073EEDF9FAB36C2E345B7B3FE064B)

## 配置OHPM代理

若您需要配置OHPM代理信息，可通过如下步骤进入代理配置界面：

* 在欢迎页单击**Customize > All settings… > Build, Execution, Deployment > Ohpm** **> Optimize config，**进入OHPM代理设置界面。
* 在打开了工程的情况下，可以单击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Ohpm > Optimize config**，进入OHPM代理设置界面。

具体配置如下：

* **ohpm registry**：配置ohpm仓的地址信息。

  ```screen
  https://ohpm.openharmony.cn/ohpm/
  ```

* **HTTP proxy**：代理服务器信息，默认会与DevEco Studio的HTTP proxy设置项保持一致。**如果不清楚代理服务器信息，请咨询您的网络管理人员**。如果需要配置账号密码，请使用如下格式进行配置：

  ```screen
  http://user:password@proxy.proxyserver.com
  ```
* **Enable Https Proxy**：同步配置HTTPS Proxy信息。

**填写**并**勾选**以上信息后，点击**OK**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/poskj6y5RvmqkKQf7EfImQ/zh-cn_image_0000002808886401.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D160B297396F9A9DCE3209F46332A79357C4164250150C57D926AB4C9F555C4)

说明：ohpm默认校验registry仓库地址证书。如果环境检查中ohpm registry access出现'SELF\_SIGNED\_CERT\_IN\_CHAIN'或'UNABLE\_TO\_VERIFY\_LEAF\_SIGNATURE'等证书校验错误时，请查看[FAQ](../harmonyos-faqs/development-environment-faq-0005.md)解决证书校验错误问题。

在此界面配置的代理信息将写入“users/用户名/.ohpm”目录下的**.ohpmrc**文件。因此也可直接修改“users/用户名/.ohpm”目录下的**.ohpmrc**文件进行配置。

1. 进入*C:/Users/用户名*目录/.ohpm，打开**.ohpmrc**文件。如果该目录下没有**.ohpmrc**文件，请新建一个。
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
   * Windows环境变量设置方法：

     在**此电脑 > 属性 > 高级系统设置 > 高级 > 环境变量**中，在系统或者用户的PATH变量中，添加ohpm安装位置下bin文件夹的路径。默认路径为：DevEco Studio安装目录\tools\ohpm。
   * macOS环境变量设置方法：

     打开终端工具，执行以下命令。

     ```screen
     export OHPM_HOME=/home/xx/Downloads/ohpm  #本处路径请替换为ohpm的安装路径。默认路径为:/home/xx/Downloads/DevEco Studio安装目录\tools\ohpm
     export PATH=$OHPM_HOME/bin:$PATH
     ```
5. 代理配置完成后，执行如下命令验证网络是否正常。

   ```screen
   ohpm info @ohos/lottie
   ```

   执行结果如下图所示，则说明代理设置成功。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/FnSYrXbHT0ObMch1qG40yw/zh-cn_image_0000002779566740.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D67982E2090B64EAE3C9185C3AC88D5A414911B3FF4EDBB0F279F82157FF0F3)
