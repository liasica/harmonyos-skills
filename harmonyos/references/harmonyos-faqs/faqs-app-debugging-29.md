---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-29
title: 应用自动签名失败，提示“calibrate the system time and sign again”
breadcrumb: FAQ > DevEco Studio > 应用调试 > 应用自动签名失败，提示“calibrate the system time and sign again”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6c9b8ffd69bbce8340d93ad162954bd8c8a5e30d4bf251ad11137d8d751177a5
---

**问题现象**

应用在进行自动签名时，签名失败，提示“The signature does not take effect or has expired. The current system time may be inaccurate. Please calibrate the system time and sign again.”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/2lKOcEg1SMiZQTeTlMd6qQ/zh-cn_image_0000002229758773.png?HW-CC-KV=V1&HW-CC-Date=20260428T003008Z&HW-CC-Expire=86400&HW-CC-Sign=24A186197A7C7D4B1BADE727BE094F4FDA5A2BBDCBDBB710F5D2D278ECEEEA80 "点击放大")

**解决措施**

出现报错是因为电脑的系统时间与北京时间不一致。请在系统设置中将时间设置为北京时间。

Windows：

1. 在开始菜单中搜索并打开“控制面板”。
2. 点击“时钟和区域”> “日期和时间”。
3. 在弹出的窗口中点击“更改日期和时间”。
4. 修改后点击“确定”保存。

macOS：

1. 在桌面点击左上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/_H3taI_rQgyl8RpwhIUuIA/zh-cn_image_0000002347874002.png?HW-CC-KV=V1&HW-CC-Date=20260428T003008Z&HW-CC-Expire=86400&HW-CC-Sign=942116DB66A47CEAD273CFAA7537D703EE1C08892778A0415100044B0600836D)菜单，选择“系统设置”。
2. 在侧边栏点击“通用”> “日期与时间”。
3. 点击时间旁边的“设置”按钮，手动输入日期和时间。

如果您使用的是公司或学校管理的设备，可能会受到MDM（移动设备管理）限制，无法更改时间设置，这种情况下需要联系公司或学校的IT管理员。
