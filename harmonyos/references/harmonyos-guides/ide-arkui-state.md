---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-state
title: 查看ArkUI状态变量
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > 查看ArkUI状态变量
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:23dda103c410dc3c96bac9186d75c2db12eb84e27af380999a355d63269133e7
---

从DevEco Studio 6.0.2 Beta1版本开始，支持在调试时查看ArkUI状态变量的实时变化情况。

在调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/TXAaW8QfTPWyzu7vEoy3cg/zh-cn_image_0000002808766215.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=9749A45431437F8374CC38EC4A43331325025449CFA4417A79BDE9E1BE8429C3)，勾选**ArkUI State**，打开ArkUI状态变量面板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/Jom3UjE1QQa6RP-ca8QG-g/zh-cn_image_0000002808886299.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=4241EEB63DDD3D6EB27C8A6CE5F4F904FAED772AE7D7AE8D072B33F44851D68D)

状态变量面板分为总览（Summary）和当前值（Current Value）两个子面板：

* 总览面板显示了当前应用运行时，状态变量更新的总体情况，包含了状态变量的名称、更新次数、装饰器类型、所属组件、所属类、当前值。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/dkvntiuxTk67kS56HwEFAQ/zh-cn_image_0000002808766221.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=812B9159842D2F1866CE3EFAD19CF8BD208075256C1D3B1A3EC5FF2C0892D225)
* 当前值面板记录了状态变量实时变化的数据，包含了状态变量的更新时间、名称、所属组件、所属类、装饰器类型、当前值、影响的组件数量。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Jg5-RynbSnWsDWTi8Y8fPg/zh-cn_image_0000002808886295.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=654852CA019162EFD5134E5F1363DBF1E643CE297B5C75A3BABA5921AFE842B4)当点击右侧的箭头时，新弹出的面板将显示当前选中状态变量影响的组件列表，包含影响组件的组件名、组件ID、是否为自定义组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/Bh7uma_FTcmhAe-w_5Kh_g/zh-cn_image_0000002808886297.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=176067CD46340076FB57198ADE96BB5E3007919C39DFF450DB188FEDB6029D80)

**说明** 

* 打开状态变量面板后才会开始监听状态变量的更新，因此，无法查看面板打开前状态变量的更新情况。
* 同一次调试过程中，关闭状态变量面板不会清空之前的数据，当前值面板最多展示1000条数据，超过限制后，仅展示最新的1000条数据。
