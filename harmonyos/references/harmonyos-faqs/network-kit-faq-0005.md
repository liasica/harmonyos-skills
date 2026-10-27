---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/network-kit-faq-0005
title: HTTP抓包调试常见问题
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 常见问题 > HTTP抓包调试常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:13+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:858ad3b672de217188e70ae2f1305c6914b17d3bb3c608786f14ac130594466a
---

**Q：为了数据传输安全，其他平台端都做了对应的防抓包措施，可以避免用户通过抓包工具窃取一些相关信息，HarmonyOS应用应该如何做到防抓包呢？**

**A**：HarmonyOS应用的防抓包策略是HTTPS协议+证书校验+取消代理。

1. HTTP升级成HTTPS：确保所有的网络请求都通过HTTPS协议进行，HTTPS是HTTP和SSL/TLS安全协议的结合，它提供了加密、数字证书认证、数据完整性三方面的保护。抓包工具即使拦截到数据包，也只能看到密文，无法直接解析。
2. 证书校验：常规HTTPS是单向认证（服务端向客户端证明身份），抓包工具通过伪造根证书让客户端信任，从而解密HTTPS数据。双向认证让客户端也向服务端证明身份，只有携带合法客户端证书的请求，服务端才会处理。详细步骤：
   * 服务端生成CA根证书，并基于根证书生成客户端证书（公钥+私钥，如p12/pem格式）。
   * HarmonyOS应用客户端将客户端证书内置到应用中，参考[配置信任应用管理的CA证书](../best-practices/bpta-network-ca-security.md#section05271716102218)；同时配置[不信任用户安装的CA证书](../best-practices/bpta-network-ca-security.md#section11935814273)。
   * 服务端配置TLS双向认证，要求客户端握手时必须携带合法客户端证书，否则直接断开连接；
   * 证书定期更新，避免证书泄露，若泄露立即吊销并更换。

3. 取消代理：检测客户端是否开启了HTTP/HTTPS代理，抓包工具几乎都需要通过代理拦截请求，对于有HTTPS请求和RCP请求可通过取消代理实现。
   * Network Kit：[使用HTTP访问网络](../harmonyos-guides/http-request.md)通过配置usingProxy:false实现，示例代码可参考[发起HTTP数据请求](../harmonyos-guides/http-request.md#发起http数据请求)。
   * Remote Communication Kit：[定制代理](../harmonyos-guides/remote-communication-customproxyconfig.md)通过配置proxy:'no-proxy'实现，示例代码可参考[使用样例](../harmonyos-guides/remote-communication-customproxyconfig.md#section16684193015209)。

**Q：SSL证书即将过期的情况下，使用axios发起网络请求如何防抓包？**

**A**：防抓包需要SSL证书，所以需要及时更新SSL证书，避免证书到期导致无法抓包。

**Q：如何禁止使用网络代理工具（如Fiddler、Charles）对应用进行抓包，从而获取HTTPS协议的网络请求返回的明文信息？**

**A**：配置不信任用户安装的CA证书，创建src/main/resources/base/profile/network\_config.json配置文件并进行配置，如下设置（参考文档：[配置不信任用户安装的CA证书](../best-practices/bpta-network-ca-security.md#section11935814273)）：{"trust-current-user-ca": false}。

**Q：HarmonyOS Next手机上抓取tcpdump包（网络数据包）有可用的推荐工具吗？**

**A**：操作步骤如下：

1. 下载并安装Wireshark软件；电脑开启热点，手机连接电脑热点，保证手机的请求转发到电脑；通过ipconfig命令查看对应的网络接口，示例中网络对应的本地连接10如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Lcghn037TRitoo1i_VvZ8w/zh-cn_image_0000002802160281.png "点击放大")
2. 根据当前手机连接的局域网设置捕获的网络接口；具体设置的路径为捕获-选项-勾选具体的网络接口，例如本次选择的是本地连接10；

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/DYtGTx6MQvS-SdTHVRnmRw/zh-cn_image_0000002802080199.png "点击放大")
3. 点击开始捕获分组。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/UUJb4CdGRo2bbAy5HbJlKg/zh-cn_image_0000002802080201.png "点击放大")
4. 操作App复现问题，可以查看Wireshark的包列表区和包内容细节区。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/wtrYChBGQ7W7G6SXnyCyEA/zh-cn_image_0000002772720454.png "点击放大")
5. 保存生成的tcpdump包文件；具体路径为文件-保存（另存为），即可生成后缀名为pcapng的文件。

**Q：HarmonyOS PC上如何在本机抓取所有网卡（包括虚拟网卡）的数据包？**

**A**：量产版PC上，普通三方应用目前不能在本机对所有网卡做pcap/混杂模式抓包，尤其是虚拟网卡和loopback。当前公开SDK没有提供给普通应用的pcap抓包接口，相关权限属于system\_basic级别且不可由普通应用在[module.json5](../harmonyos-guides/module-configuration-file.md)中声明申请，当前设备范围也不包含2in1设备。

根据不同的分析目标，可选择以下替代方案：

方案一：只分析自己应用的HTTP/HTTPS流量。

让应用显式走Charles、Fiddler或mitmproxy等代理，测试证书仅用于调试包。若有证书锁定或QUIC，需要在调试配置中处理。

方案二：分析设备对外流量。

让PC的流量经过可控路由器、热点或网关，在出口侧镜像或抓包。此方案能覆盖经过出口的流量，但仍抓不到本机loopback和内部虚拟网卡间流量。

方案三：分析自己应用的非HTTP协议流量。

在应用网络层增加收发日志或埋点，或在服务端抓包。

方案四：系统授权环境抓包。

只有系统应用、工程机或工程镜像并获得厂商授权时，才适合使用libpcap/tcpdump对所有接口抓取。普通开发者签名无法获取这类权限。

**Q：如何使用Charles工具抓包？**

**A**：

**说明** 

1. 配置环境时，在Charles弹出的窗口中选择Allow，以确保与手机连接。
2. 不支持安装crt格式证书，需转换为pem格式。
3. 上传下载@ohos.request模块接口均不支持Charles抓包。

Charles是一款网络调试和分析代理工具，可用于拦截和查看设备与服务器之间的通信。它支持监视应用程序的网络流量、修改请求和响应，以及模拟不同网络条件。主要功能包括：

* 截取http和https网络封包。
* 支持重发网络请求，方便后端调试。
* 支持修改网络请求参数。
* 支持网络请求的截获并动态修改。
* 支持模拟慢速网络。

使用时，需设置应用的请求通过Charles客户端代理转发至服务器，以便在Charles客户端进行抓包。启动Charles后，它会自动与浏览器设置为代理，无需额外配置。通过浏览器发送网络请求时，Charles将直接抓取请求和响应信息。

Charles抓包不仅可以抓取电脑端的HTTP请求，还能抓取App的HTTP请求。手机抓包需要在电脑端配置，并确保手机和电脑在同一网络下，完成。对于HTTPS协议的报文，需安装SSL证书后才能抓取，具体步骤包括与。

Charles具体使用步骤如下：

1. 安装Charles。
2. 设备代理设置：
   1. 查看Charles的IP地址，通常与PC主机的IP地址相同。
      * Charles的IP地址查看方式：点击Help -> Local IP Address查看。
      * 电脑IP地址查看方式：打开"运行"（快捷键：win+R键或者在任务栏的"搜索"按钮中查找并点击"运行"），输入"cmd"后进入命令行窗口，在命令行窗口中输入"ipconfig"命令查看IP。
   2. 设置Charles的调试端口号。
      * 点击"Proxy" -> SSL Proxy Settings -> 在Include栏下点击"Add" -> 添加":"，即Host输入"*"，Port输入"*"，再添加"*:443"，即Host输入"*"，Port输入"443" -> 点击"确定"。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/HmHYOFeVT_WhBz5-H-2DJQ/zh-cn_image_0000002772883276.png "点击放大")
      * 点击"Proxy" -> Proxy Settings -> 设置"HTTP Proxy"下的Port（即Charles监听的端口，默认为8888）-> 勾选"Enable transparent HTTP proxying" -> 最后点击"OK"。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/MIQiOD92TdSYgF0o6ssisg/zh-cn_image_0000002802083027.png "点击放大")
   3. 手机与PC连接同一局域网，Wi-Fi设置为手动代理，服务器主机名和端口为Charles的IP地址和监听端口。

      点击需要连接的Wi-Fi进入密码输入页面。在输入密码前，点击"代理"，选择"手动"，设置"代理的服务器主机名"为Charles的IP地址，"服务器端口"为Charles监听的端口，即设置为8888。最后输入密码，连接Wi-Fi。
3. Charles证书下载。
   1. 安装Charles根证书到PC信任目录。

      点击顶部菜单栏"Help" -> 选择"SSL Proxying" -> 点击"Install Charles Root Certificate" -> 点击"安装证书" -> 设置存储位置（可选择当前用户或本地计算机）后，点击"下一步" -> 选择"将所有证书都放入下列存储" -> 点击"浏览" -> 设置证书存储路径为"受信任的根证书颁发机构"。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/EmhcapogRpqoy8Q0mcmIqA/zh-cn_image_0000002772723318.png "点击放大")
   2. 导入系统根证书到手机。

      方式一：点击 Charles 顶部菜单栏"Help" -> 选择"SSL Proxying" -> 点击"Install Charles Root Certificate on a Mobile Device or Remote Browser" -> 在手机的自带浏览器中访问 <http://chls.pro/ssl> -> 点击"立即下载"，将证书下载至手机内存中。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/sgyiHXnASOyAH3VdsHJOSg/zh-cn_image_0000002802163133.png)

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/LoSDvF4bRLiDNbmM3B6vng/zh-cn_image_0000002772883280.png "点击放大")

      方式二：在PC端，点击"Help"->点击"SSL Proxying"->选择"Save Charles Root Certificate..."，将证书保存到本地，格式为pem。将手机连接到电脑，通过DevEco将刚保存的pem文件上传到手机中（鼠标右键点击目标文件夹，选择"Upload..."，然后选择刚保存的pem文件），即可进行后续的证书安装步骤。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/tX7Lr5cvTJ-ojYraC9M6ug/zh-cn_image_0000002802083033.png "点击放大")
4. 证书安装。

   证书在手机上的安装步骤如下：

   在手机端点击"设置" -> 隐私和安全 -> 下滑点击"高级" -> 选择"证书与凭据" -> 进入证书安装选项 -> 选择"从存储设备安装" -> 点击"CA证书" -> 点击"继续" -> 选择"浏览" -> 找到下载的证书位置 -> 点击证书 -> 弹出"安装证书成功"的提示，则安装成功。

   | 选择【从存储设备安装】 | 点击【CA证书】 |
   | --- | --- |
   |  |  |
5. 过滤网络请求。

   需要对网络请求进行过滤，只监控指定目录服务器上发送的请求。对于这种需求，有两种方法：

   1. 在主界面中部点击Ctrl+F打开搜索栏，填入过滤关键字。例如监听www.charlesproxy.com，填入或勾选信息后点击Find。
   2. 在Charles的菜单栏中选择"Proxy" -> "Recording Settings" -> 选择"Include"栏 -> 点击"Add"添加一个项目 -> 按需填入需要监控的协议，重新监听即可只截取目标网站。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/d7qrVXGATfya-TM7X1o_2A/zh-cn_image_0000002772883286.png "点击放大")

**Q：使用模拟器发起HTTPS请求时如何安装数字证书？**

**A**：安装网站服务器的数字证书的方式如下：

1. 将证书拖拽上传至模拟器，可在文件管理的"我的手机">"下载"目录下查看上传的文件。
2. 安装证书的方式如下：
   * 点击设置 > WLAN >![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/RDAdFhkxQ82a_vlu4rC-Qw/zh-cn_image_0000002802162319.png)> 安装证书 > CA证书，选择pem格式证书进行安装。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/FlQnGsBbTtGWUAHCbA4EHg/zh-cn_image_0000002802083035.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/56BaMNlQScy1fQ10uYePjA/zh-cn_image_0000002772723326.png "点击放大")
   * 在本机命令行窗口中使用以下命令打开证书管理。

     ```shell
     hdc shell aa start -a MainAbility -b com.ohos.certmanager
     ```

     选择从存储设备安装，安装pem格式的证书。
