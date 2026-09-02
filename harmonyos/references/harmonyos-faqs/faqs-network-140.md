---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-140
title: 如何使用WireShark分析网络请求各阶段的TcpDump日志
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何使用WireShark分析网络请求各阶段的TcpDump日志
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:89df8d0a6fbd06a5f3d5224b6150404e059e8b76b2baec1220f7859b2ad7a151
---

## 问题现象

在网络问题定位定界过程中，如何高效使用WireShark工具分析TcpDump包？

## 背景知识

分析HarmonyOS系统的网络相关问题，最重要的工具就是用于呈现及解析网络报文的WireShark，其通过可视化的界面以时间为线索，以报文为粒度完整地呈现了本通信节点与其他内/外部节点的所有通信细节。通过WireShark工具打开网络抓包文件后，我们将看到海量的数据报文，WireShark为了使用者分析的便利，提供了多种不同背景色的提示信息（在WireShark中叫作“专家信息”），而这些提示信息需要有足够的协议基础和充分的实践积累，才能够熟练掌握和应用。本文将对在WireShark中经常出现的八类提示信息进行解释与分析，便于使用WireShark进行网络问题分析的人员快速掌握其中的关键部分，以支撑HarmonyOS系统问题的定位与解决。

## 解决方案

1. WireShark网络报文提示信息的基础：WireShark在解析和呈现网络抓包文件中的报文信息时，会额外提供“专家信息”，这些信息是WireShark根据报文所属的连接结合上下文综合分析的结果。如下图所示的报文，除了解析报文的对应协议字段外，“[]”中的部分即为WireShark通过分析提供的“专家信息”，同时由于这些信息对于使用者分析网络问题比较重要，因此，整个报文的底色被特别显示为黑色或者红色以提示使用者。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/qYWbjLpNSZ6Xcry0l8ev4A/zh-cn_image_0000002628611266.png "点击放大")

   分析TcpDump包时，如果我们需要整体分析一个网络抓包文件的所有专家信息，可以通过WireShark中的菜单：分析->专家信息来获取，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/O7XhMuFPQk2AVnskAiytAA/zh-cn_image_0000002658850529.png "点击放大")
2. 专家信息：专家信息从严重程度上分有Error/Warning/Note/Chat这些常见级别，Error/Warning级别属于WireShark认为较严重的问题，需要使用者关注，Note/Chat级别属于在网络通信过程中重要的关键信息，但并不意味是问题，需要使用者进行分析甄别。从整体来看，对于专家信息，需要注意2点：
   * 专家信息来源于WireShark自身的协议分析组件，其基于网络报文的字段信息分析，但并非网络报文携带的字段信息，亦不在网络上传输，同时不同版本的WireShark甚至可能专家信息的结果也不相同。
   * 专家信息仅为参考，并非100%正确，通过WireShark专家信息的协助，再基于人的专家经验最终才能得到正确的分析结论。
3. 常见WireShark网络报文提示的分析案例：
   1. **专家信息TCP Previous segment not captured**。
      * 级别：Warning，这并非是一个正常的现象，但是一类最常见的专家信息。
      * 发生的原因：由TCP报文序号的不连续性导致，也就是说此处可能发生了TCP报文的丢包或者乱序。
      * 分析：以下图为例，观察67200行的发包，TCP报文序号为3352，报文长度为0字节，即下一个报文的连续序号应为3352，但是下一个报文序号（67201行）实际为3431，中间缺少一段TCP数据（序号区间3352~3430），因此专家信息上报“TCP Previous segment not captured”，注意，此处WireShark专家信息的描述较保守，其含义为“TCP（连续的）报文未能捕获”，因为此处导致不连续的原因可能很多，包括丢包/乱序/未从连接起始阶段抓包等原因，但是最常见的原因还是报文丢失和乱序。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/KGzqNZoTTjasKMmCJzcs8A/zh-cn_image_0000002628771158.png "点击放大")
   2. **专家信息TCP Out-Of-Order**。
      * 级别：Warning，这并非一个正常的现象，是一类最常见的专家信息。
      * 发生的原因：由TCP报文的不连续性导致，此处收到报文发生了乱序。
      * 分析：如下图所示，观察67201行的发包，TCP报文序号为3431，而在67202行收到的报文，其TCP报文序号为3352<3431，当发生后面TCP报文的序号小于前面TCP报文的序号时，专家信息会提示“TCP Out-Of-Order”，由此可以看到，当发生报文乱序的时候，往往会触发两个告警信息：
      1. 报文序号之间不连续导致“TCP Previous segment not captured”。
      2. 乱序报文到达导致的“TCP Out-Of-Order”，而如果仅发生了报文丢包，则只会出现第1个告警信息。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/vejQOwWiRfCtB9T4xj4cTg/zh-cn_image_0000002658970481.png "点击放大")
   3. **专家信息TCP Dup Ack**。
      * 级别：Note，这是一类最常见的专家信息。
      * 发生的原因：重复的Ack，标识通信节点曾经收到过TCP报文，并发送了对应序号的Ack，但是由于各种原因（如报文不连续），又重复发送了相同的序号的Ack。
      * 分析：如下图所示，观察67195行的发包，其TCP的Ack序号为3352，而在67204行，其又发送了Ack序号为3352的报文，导致专家信息会提示“TCP Dup Ack”，其中“#1”标识当前是第一次发生重复Ack序号3352的情况，如果后续继续重复发送Ack序号3352的情况，其就会标识成“#2”“#3”等等。之所以关注Dup Ack的次数，原因在于TCP的快速重传机制，经典的TCP快速重传设计为当发生3次Dup Ack就会触发快速重传，因此可以用于判断报文重传的状态。此外，Dup Ack本身不会导致网络传输的性能衰减，部分Dup Ack也可能是协议特意为之，因此Dup Ack未被归入Warning级别。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/sd7-s6CzQWaSQXCHPs_kQw/zh-cn_image_0000002628611268.png "点击放大")
   4. **专家信息TCP Fast Retransmission**。
      * 级别：Note，这是一类最常见的专家信息。
      * 发生的原因：TCP快速重传，WireShark通过分析认定该报文属于快速重传的报文，注意此处的分析属于推测，因此最底层的描述有个“suspect”描述，原因是，对于底层抓包来说，一个重传报文是否属于快速重传是没法100%确定的，只有TCP协议栈本身才能够确定。
      * 分析：当看到该提示，可以认为当前网络上发生过丢包，但是很快就通过重传恢复了，因此，从网络性能角度来讲，对于网络传输速率的影响是较小的。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/aELhYx78SluyldrnjWe2Vg/zh-cn_image_0000002658850531.png "点击放大")
   5. **专家信息TCP Retransmission**。
      * 级别：Note，这是一类最常见的专家信息。
      * 发生的原因：TCP超时重传，WireShark通过分析认定该报文属于超时重传的报文，注意此处的分析属于WireShark推测，因此最底层的描述有个“suspect”描述，原因是对于底层抓包来说，一个重传报文是否属于超时重传是没法100%确定的，WireShark仅仅是通过丢包的时间和发生重传的时间间隔来进行逻辑推理，是否是TCP超时逻辑触发重传，只有TCP协议栈本身才能够确定。
      * 分析：超时重传是TCP重传中的兜底策略，在快速重传等方案未能恢复丢包的情况下，通过超时重传来保障丢包的恢复，如果超时重传也失效，会导致TCP连接的断链，因此一般超时重传比其他的重传会造成更大的性能影响，在频繁超时重传的情况下，网络的传输性能将会有较大的衰减。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/y5odKkdBTm6UpxFWVl2r5Q/zh-cn_image_0000002628771160.png "点击放大")
   6. **专家信息TCP RST**。
      * 级别：Warning，该信息提醒用户连接发生异常。
      * 发生的原因：TCP连接接收或者发送了RST报文，该报文一般意味着连接的关闭，而且该关闭方式并非采用优雅关闭，而是采用了强制关闭。因此，WireShark会将该报文高亮提示用户当前连接发生了断链，且断链并非正常关闭。该信息也往往是造成上层业务视频播放卡顿、页面加载白块等的原因。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/biQag0tYTsWoJBljUxz5Mw/zh-cn_image_0000002658970483.png "点击放大")
   7. **专家信息Destination Unreachable**。
      * 级别：Note，该信息提醒用户之前发送的报文未能按预期抵达对应的目标地址。
      * 发生的原因：网络发送的TCP/UDP报文携带了目标IP地址和目标端口，当报文在中间设备转发时没有路由抵达目标IP地址，则中间设备会返回当前的ICMP error报文，并携带IP地址不可达信息，当报文到达目标IP地址但是没有对应的目标端口监听接收，则目标设备会返回当前的ICMP error报文，并携带端口不可达（port unreachable）信息，该问题往往导致报文未按预期到达对端。
      * 分析：该错误属于发生在网络层，因此会导致连接的异常，若发生在建链时会导致连接建立失败，若发生在数据传输时，会导致数据无法到达对端。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/1M6FZ8lzS16xXMob5KDC4g/zh-cn_image_0000002628611270.png "点击放大")
   8. **专家信息TCP Acked unseen segment**。
      * 级别：Warning，该信息提醒用户TCP Ack报文Ack了“未发送”的报文。
      * 发生的原因：该信息一般发生在抓包的起始位置，当一次抓包从一次连接的中间部分开始，则可能未完整的抓取到存在关联的报文（如发送的报文和对应Ack的报文），此时就会导致WireShark认为当前的Ack报文Ack了不存在的报文或者“未发送的报文”，从WireShark的分析解析即可以看出，其提示这一般发生在抓包文件的开始部分，在这种情况下，可以认为是一种正常的情况。
      * 分析：除了上述的最常见情况外，另一种情况是发生了抓包丢失的情况，但该情况较少见。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/rTPZGx9vT2C1HoNj6WgGAg/zh-cn_image_0000002658850533.png "点击放大")

## 总结

WireShark是一款强大的网络分析软件，其不仅显示抓取的网络报文的结构化信息，同时也提供了一定的协议分析能力提示网络可能存在的问题，能够提升用户网络异常分析的效率，掌握这些WireShark提示信息的发生原理将为我们解决网络问题提供有效支撑。
